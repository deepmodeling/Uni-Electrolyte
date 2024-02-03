

import numpy as np
import pandas
from rdkit import Chem
from rdkit.Chem import AllChem

import os
import shutil
os.environ['CUBLAS_WORKSPACE_CONFIG'] = ':4096:8'
os.environ['NCCL_SOCKET_IFNAME']='lo'
os.environ['CUDA_VISIBLE_DEVICES']='0'

# from model import GraphFormer
from model import GraphFormer,Embedding_extractor
#from IPython import embed
from data import GraphDataModule, get_dataset
from argparse import ArgumentParser
#from pprint import pprint
import pytorch_lightning as pl
from pytorch_lightning.callbacks import ModelCheckpoint, LearningRateMonitor
import os,sys
from pytorch_lightning.plugins import DDPPlugin
from entry import predict_epoch_end
import torch.nn as nn
import pandas as pd
import torch
import torch.utils.data
from torch.utils.data import Dataset,Subset
from pytorch_lightning.callbacks.early_stopping import EarlyStopping
from pytorch_lightning.loggers.tensorboard import TensorBoardLogger
import datetime
from sklearn.model_selection import KFold
now = datetime.datetime.now() 

class Rem():
    def __init__(self,args):
        # ------------
        # args
        # ------------ #'--accelerator', 'ddp'
        self.args=args
        self.args.plugins = DDPPlugin(find_unused_parameters=True)
        self.args.max_steps = self.args.tot_updates + 1

        if not self.args.test and not self.args.validate:
            print(self.args)
        pl.seed_everything(self.args.seed)


        # ------------
        # training
        # ------------
        # metric = 'valid_' + get_dataset(dm.dataset_name)['metric']
        dirpath = self.args.default_root_dir + f'/lightning_logs/checkpoints'
        # self.checkpoint_callback = ModelCheckpoint(
        #     dirpath=dirpath,
        #     save_top_k=1,
        #     save_last=True,
        #     every_n_train_steps=10,
        #     monitor='batch_train_loss',
        #     mode='min',
        #     # every_n_epochs = 2,
        # )

        if not self.args.test and not self.args.validate and os.path.exists(dirpath + '/last.ckpt'):
            self.args.resume_from_checkpoint = dirpath + '/last.ckpt'
            print('args.resume_from_checkpoint', self.args.resume_from_checkpoint)


    def predict_repr(self, smiles_list):
        # ------------
        # data
        # ------------
        self.trainer = pl.Trainer.from_argparse_args(self.args)
        self.trainer.callbacks.append(self.checkpoint_callback)
        self.trainer.callbacks.append(LearningRateMonitor(logging_interval='step'))

        os.system("mkdir -p data/%s/raw/"%(self.args.dataset_name))
        os.system("mkdir -p results/%s/"%(self.args.dataset_name))
        os.system("rm data/%s/raw/*"%self.args.dataset_name)
        os.system("rm data/%s/processed/*" % self.args.dataset_name)
        os.system("rm results/%s/*" % self.args.dataset_name)
        #import pdb
        #pdb.set_trace()
        with open("data/%s/raw/%s"%(self.args.dataset_name,self.args.input_file),"w") as fp:
            print("smiles", file=fp)
            for smiles in smiles_list:
                print(smiles,file=fp)
        dm = GraphDataModule.from_argparse_args(self.args, input_file=self.args.input_file)
        try:
            self.model
        except:
            self.model = Embedding_extractor(self.args)
        else:
            pass
        #self.model = Embedding_extractor(self.args)

        if not self.args.test and not self.args.validate:
            pass#print(self.model)
        #print('total params:', sum(p.numel() for p in self.model.parameters()))



        result = self.trainer.predict(self.model, datamodule=dm)
        return predict_epoch_end(self.args, result)


    def inference(self):
        # ------------
        # data
        # ------------

        # dataloader
        from torch.utils.data import DataLoader
        from functools import partial
        from collator import collator
        from custom_dataset import EmbeddingDataset
        if len(self.args.loaded_target_list)!=0:  #inference 不用读入数据文件的预测值
            raise Exception

        predict_input_csv_file_name=self.args.predict_input_csv_file_path.split("/")[-1]
        if not  os.path.exists("data"):
            os.mkdir("data")

        if  os.path.exists("data/%s" % (self.args.predict_dataset_name)):
            if self.args.predict_dataset_name == "" or  self.args.predict_dataset_name  is None:
                raise Exception
            os.system("rm -rf data/%s" % (self.args.predict_dataset_name))       #os.rmdir("data/%s" % (self.args.predict_dataset_name))
        os.mkdir("data/%s" % (self.args.predict_dataset_name))
        os.mkdir("data/%s/raw" % (self.args.predict_dataset_name))
        shutil.copy(self.args.predict_input_csv_file_path,
                    "data/%s/raw/%s" % (self.args.predict_dataset_name,predict_input_csv_file_name))

        predict_input_df=pandas.read_csv("data/%s/raw/%s" % (self.args.predict_dataset_name,predict_input_csv_file_name))
        self.args.loaded_target_list=[self.args.predicted_target]
        if self.args.predicted_target not in predict_input_df.keys(): #不加上一个假的真实值的话，collator会报错
            predict_input_df[self.args.predicted_target]=0
            predict_input_df.to_csv("data/%s/raw/%s" % (self.args.predict_dataset_name,predict_input_csv_file_name))

        if self.args.dataset_name is not None:
            raise Exception
        self.args.dataset_name = self.args.predict_dataset_name #model.py 中没有args.dataset_name 会报错

        predict_test_dataset = \
        get_dataset(dataset_name=self.args.predict_dataset_name, input_file=predict_input_csv_file_name,
                    loaded_target_list=self.args.loaded_target_list,ID_name=self.args.ID_name)["dataset"]
        predict_dataloader = DataLoader(
            predict_test_dataset,
            batch_size=self.args.batch_size,
            shuffle=False,
            num_workers=self.args.num_workers,
            pin_memory=True,
            persistent_workers=True,
            collate_fn=partial(collator, max_node=9999, multi_hop_max_dist=5,
                               rel_pos_max=1024, predicted_target=self.args.predicted_target),
        )
        print('len(predict_dataloader)', len(predict_dataloader))
        self.model = Embedding_extractor(self.args)

        if self.args.inference!=True:
            raise Exception
        if self.args.predicted_target=="be" :
            self.model=Embedding_extractor.load_from_checkpoint(
            "/root/Uni-Electrolyte/scoring_model/g2gt/src/lightning_logs/rem_electrolyte_train_1_CHO_47371_uninf_20230706_be_20230714175816/version_0/checkpoints/epoch=387-epoch=epoch_val_loss=0.133.ckpt",
               args=self.args)
        elif self.args.predicted_target=="log_vs" :
            self.model=Embedding_extractor.load_from_checkpoint(
            "/root/Uni-Electrolyte/scoring_model/g2gt/src/lightning_logs/rem_electrolyte_train_1_CHO_47371_uninf_20230706_log_vs_20230714180801/version_0/checkpoints/epoch=238-epoch=epoch_val_loss=0.163.ckpt",
               args=self.args)
        elif self.args.predicted_target=="log_dcs" :
            self.model=Embedding_extractor.load_from_checkpoint(
            "/root/Uni-Electrolyte/scoring_model/g2gt/src/lightning_logs/rem_electrolyte_train_1_CHO_47371_uninf_20230706_log_dcs_20230715131757/version_0/checkpoints/epoch=201-epoch=epoch_val_loss=0.155.ckpt",
               args=self.args)
        elif self.args.predicted_target=="HOMO" :
            self.model=Embedding_extractor.load_from_checkpoint(
            "/root/Uni-Electrolyte/scoring_model/g2gt/src/lightning_logs/rem_electrolyte_train_1_CHO_47371_uninf_20230706_HOMO_20230714180947/version_0/checkpoints/epoch=760-epoch=epoch_val_loss=0.145.ckpt",
               args=self.args)
        elif self.args.predicted_target=="LUMO" :
            self.model=Embedding_extractor.load_from_checkpoint(
            "/root/Uni-Electrolyte/scoring_model/g2gt/src/lightning_logs/rem_electrolyte_train_1_CHO_47371_uninf_20230706_LUMO_20230714180955/version_0/checkpoints/epoch=608-epoch=epoch_val_loss=0.211.ckpt",
               args=self.args)
        else:
            raise Exception

        trainer = pl.Trainer(
            logger=TensorBoardLogger("lightning_logs", name=self.args.log_name),
            max_epochs=self.args.epoch,
            devices=1,
            accelerator="auto",
            callbacks=[
                # EarlyStopping(monitor="epoch_val_loss", mode="min",patience=50,verbose=True),
                LearningRateMonitor(logging_interval='step'),
                ModelCheckpoint(filename='{epoch}-{epoch_val_loss:.3f}', save_top_k=3, save_last=True,
                                monitor="epoch_val_loss", mode='min', verbose=True, auto_insert_metric_name=True),
            ],
            # limit_train_batches=20,
            # log_every_n_steps=10
        )

        if self.args.predict_output_csv_file_path is None:
            raise Exception

        trainer.predict(model=self.model, dataloaders=predict_dataloader)
        #trainer.test(model=self.model, dataloaders=predict_dataloader)




    def generate_scaffolds(self,
                           dataset,
                           log_every_n: int = 1000) :
        """Returns all scaffolds from the dataset.

        Parameters
        ----------
        dataset: Dataset
            Dataset to be split.
        log_every_n: int, optional (default 1000)
            Controls the logger by dictating how often logger outputs
            will be produced.

        Returns
        -------
        scaffold_sets: List[List[int]]
            List of indices of each scaffold in the dataset.
        """

        def _generate_scaffold(smiles: str, include_chirality: bool = False) -> str:
            """Compute the Bemis-Murcko scaffold for a SMILES string.

            Bemis-Murcko scaffolds are described in DOI: 10.1021/jm9602928.
            They are essentially that part of the molecule consisting of
            rings and the linker atoms between them.

            Paramters
            ---------
            smiles: str
                SMILES
            include_chirality: bool, default False
                Whether to include chirality in scaffolds or not.

            Returns
            -------
            str
                The MurckScaffold SMILES from the original SMILES

            References
            ----------
            .. [1] Bemis, Guy W., and Mark A. Murcko. "The properties of known drugs.
                1. Molecular frameworks." Journal of medicinal chemistry 39.15 (1996): 2887-2893.

            Note
            ----
            This function requires RDKit to be installed.
            """
            try:
                from rdkit import Chem
                from rdkit.Chem.Scaffolds.MurckoScaffold import MurckoScaffoldSmiles
            except ModuleNotFoundError:
                raise ImportError("This function requires RDKit to be installed.")

            mol = Chem.MolFromSmiles(smiles)
            scaffold = MurckoScaffoldSmiles(mol=mol, includeChirality=include_chirality)
            return scaffold

        scaffolds = {}
        data_len = len(dataset)

        for ind, tmp_data in enumerate(dataset):

            scaffold = _generate_scaffold(tmp_data.smiles)
            if scaffold not in scaffolds:
                scaffolds[scaffold] = [ind]
            else:
                scaffolds[scaffold].append(ind)

        # Sort from largest to smallest scaffold sets
        scaffolds = {key: sorted(value) for key, value in scaffolds.items()}
        scaffold_sets = [
            scaffold_set
            for (scaffold,
                 scaffold_set) in sorted(scaffolds.items(),
                                         key=lambda x: (len(x[1]), x[1][0]),
                                         reverse=True)
        ]
        index_list=[]
        for scaffold_set in scaffold_sets:
            index_list+=scaffold_set
        return index_list
    def train(self):
        # ------------
        # data
        # ------------

        #dataloader
        from torch.utils.data import DataLoader
        from functools import partial
        from collator import collator
        from custom_dataset import EmbeddingDataset

   
        if not os.path.exists("data/%s"%(self.args.dataset_name)):
  
            os.mkdir("data/%s"%(self.args.dataset_name))
            os.mkdir("data/%s/raw"%(self.args.dataset_name))
            shutil.copy("/data/%s"%(self.args.input_filename),"data/%s/raw/%s"%(self.args.dataset_name,self.args.input_filename))
        all_train_dataset=get_dataset(dataset_name=self.args.dataset_name,input_file=self.args.input_filename,loaded_target_list=self.args.loaded_target_list,ID_name=self.args.ID_name)["dataset"]
        
        # use 20% of training data for validation
        train_set_size = int(len(all_train_dataset) * 0.9)
        valid_set_size = len(all_train_dataset) - train_set_size



        if not os.path.exists("data/%s"%(self.args.iid_test_dataset_name)):
            os.mkdir("data/%s"%(self.args.iid_test_dataset_name))
            os.mkdir("data/%s/raw"%(self.args.iid_test_dataset_name))
            shutil.copy("/data/%s"%(self.args.iid_test_input_filename),"data/%s/raw/%s"%(self.args.iid_test_dataset_name,self.args.iid_test_input_filename))
        
        iid_test_dataset=get_dataset(dataset_name=self.args.iid_test_dataset_name,input_file=self.args.iid_test_input_filename,loaded_target_list=self.args.loaded_target_list,ID_name=self.args.ID_name)["dataset"]
        iid_test_dataloader = DataLoader(
            iid_test_dataset,
            batch_size=self.args.batch_size,
            shuffle=False,
            num_workers=self.args.num_workers,
            pin_memory=True,
            persistent_workers=True,
            collate_fn=partial(collator, max_node=9999, multi_hop_max_dist=5,
                               rel_pos_max=1024,predicted_target=self.args.predicted_target),
        )
        print('len(iid_test_dataloader)', len(iid_test_dataloader))
        

        if not os.path.exists("data/%s"%(self.args.ood_test_dataset_name)):
            os.mkdir("data/%s"%(self.args.ood_test_dataset_name))
            os.mkdir("data/%s/raw"%(self.args.ood_test_dataset_name))
            shutil.copy("/data/%s"%(self.args.ood_test_input_filename),"data/%s/raw/%s"%(self.args.ood_test_dataset_name,self.args.ood_test_input_filename))
        
        ood_test_dataset=get_dataset(dataset_name=self.args.ood_test_dataset_name,input_file=self.args.ood_test_input_filename,loaded_target_list=self.args.loaded_target_list,ID_name=self.args.ID_name)["dataset"]
        ood_test_dataloader = DataLoader(
            ood_test_dataset,
            batch_size=self.args.batch_size,
            shuffle=False,
            num_workers=self.args.num_workers,
            pin_memory=True,
            persistent_workers=True,
            collate_fn=partial(collator, max_node=9999, multi_hop_max_dist=5,
                               rel_pos_max=1024,predicted_target=self.args.predicted_target),
        )
        print('len(ood_test_dataloader)', len(ood_test_dataloader))

        fold_num = 5
        trainer = pl.Trainer(
            logger=TensorBoardLogger("lightning_logs", name=self.args.log_name),
            max_epochs=self.args.epoch,
            devices=1,
            accelerator="auto",
            callbacks=[
                # EarlyStopping(monitor="epoch_val_loss", mode="min",patience=50,verbose=True),
                LearningRateMonitor(logging_interval='step'),
                ModelCheckpoint(filename='{epoch}-{epoch_val_loss:.3f}', save_top_k=3, save_last=True,
                                monitor="epoch_val_loss", mode='min', verbose=True, auto_insert_metric_name=True),
                ModelCheckpoint(filename='best', save_top_k=1,
                                monitor="epoch_val_loss", mode='min', verbose=True),
            ],
            # limit_train_batches=20,
            # log_every_n_steps=10
        )

        test_outputs_iid_csv_path_list = []
        test_outputs_ood_csv_path_list = []
        #self.model = Embedding_extractor(self.args)
        #self.model.save_checkpoint("lightning_logs/%s/origin_model.ckpt" % (self.args.log_name))
        #ori_log_name=self.args.log_name
        for fold_idx in range(fold_num):
            print("--------------model%s-----------------------" % (fold_idx))
            #self.args.log_name=ori_log_name+"_" + fold

            self.model = Embedding_extractor(self.args)
            # split the train set into two
            seed_int=self.args.seed+fold_idx*100
            seed = torch.Generator().manual_seed(seed_int)
            train_dataset, valid_dataset = torch.utils.data.random_split(all_train_dataset, [train_set_size, valid_set_size],
                                                              generator=seed)
            # # import pdb
            # # pdb.set_trace()
            # scaffold_rerank_index_list = self.generate_scaffolds(all_train_dataset)
            # # 创建交叉验证分割器
            # # 计算每个子列表的长度
            # chunk_size = len(scaffold_rerank_index_list) // fold_num
            # # 使用列表切片将列表分成5个子列表
            # sublists = [scaffold_rerank_index_list[i:i + chunk_size] for i in
            #             range(0, len(scaffold_rerank_index_list), chunk_size)]
            # val_indices = sublists[fold_idx]
            # train_indices = []
            # for idx, sublist in enumerate(sublists):
            #     if idx == fold_idx:
            #         continue
            #     train_indices += sublist
            # train_dataset=Subset(all_train_dataset, train_indices)
            # valid_dataset=Subset(all_train_dataset, val_indices)
            train_dataloader=DataLoader(
             train_dataset,
             batch_size=self.args.batch_size,
             shuffle=False,
             num_workers=self.args.num_workers,
             pin_memory=True,
             persistent_workers=True,
             collate_fn=partial(collator, max_node=9999,
                                multi_hop_max_dist=5,
                                rel_pos_max=1024,
                                predicted_target=self.args.predicted_target), )

            print('len(train_dataloader)', len(train_dataloader))

            valid_dataloader = DataLoader(
                valid_dataset,
                batch_size=self.args.batch_size,
                shuffle=False,
                num_workers=self.args.num_workers,
                pin_memory=True,
                persistent_workers=True,
                collate_fn=partial(collator, max_node=9999, multi_hop_max_dist=5,
                                   rel_pos_max=1024, predicted_target=self.args.predicted_target), )
            print('len(valid_dataloader)', len(valid_dataloader))

            trainer = pl.Trainer(
                logger=TensorBoardLogger("lightning_logs", name=self.args.log_name),
                max_epochs=self.args.epoch,
                devices=1,
                accelerator="auto",
                callbacks=[
                    # EarlyStopping(monitor="epoch_val_loss", mode="min",patience=50,verbose=True),
                    LearningRateMonitor(logging_interval='step'),
                    ModelCheckpoint(filename='{epoch}-{epoch_val_loss:.3f}', save_top_k=3, save_last=True,
                                    monitor="epoch_val_loss", mode='min', verbose=True, auto_insert_metric_name=True),
                    ModelCheckpoint(filename='best', save_top_k=1,
                                    monitor="epoch_val_loss", mode='min', verbose=True),
                ],
                # limit_train_batches=20,
                # log_every_n_steps=10
            )
            trainer.fit(model=self.model, train_dataloaders=train_dataloader, val_dataloaders=valid_dataloader )
            model_path="lightning_logs/%s/version_0/checkpoints/best.ckpt" % (self.args.log_name)


            self.model.test_outputs_csv_path = "lightning_logs/%s/test_output_iid_%s.csv" % (self.args.log_name, fold_idx)
            trainer.test(model=self.model, dataloaders=iid_test_dataloader,ckpt_path=model_path)
            test_outputs_iid_csv_path_list.append(self.model.test_outputs_csv_path)

            self.model.test_outputs_csv_path = "lightning_logs/%s/test_output_ood_%s.csv" % (self.args.log_name,fold_idx)
            trainer.test(model=self.model, dataloaders=ood_test_dataloader,ckpt_path=model_path)
            test_outputs_ood_csv_path_list.append(self.model.test_outputs_csv_path)
            del trainer

        output_process_merge_csv(test_outputs_iid_csv_path_list, self.args.log_name, "iid")
        output_process_merge_csv(test_outputs_ood_csv_path_list, self.args.log_name, "ood")

def output_process_merge_csv(test_outputs_csv_path_list, log_name,tag):
    test_output_df = pd.read_csv(test_outputs_csv_path_list[0])
    for fold in range(len(test_outputs_csv_path_list)):
        if fold == 0:
            continue
        test_output_df_tmp = pd.read_csv(test_outputs_csv_path_list[fold])
        test_output_df_tmp = test_output_df_tmp.rename(columns={'y_pred': 'y_pred2'})[["ID", "y_pred2"]]
        test_output_df = pd.merge(test_output_df, test_output_df_tmp, on="ID")
        test_output_df["y_pred"] = test_output_df["y_pred2"] + test_output_df["y_pred"]
        del test_output_df["y_pred2"]
    test_output_df["y_pred"] /= len(test_outputs_csv_path_list)
    test_output_df.to_csv("./lightning_logs/%s/merged_test_result_%s.csv" % (log_name,tag))


    mae_loss_fn = nn.L1Loss(reduction="mean")
    y_pred = torch.tensor(test_output_df["y_pred"])
    y_true = torch.tensor(test_output_df["y_true"])
    mae = mae_loss_fn(y_pred, y_true)
    de_log_mae = mae_loss_fn(torch.pow(10, y_pred), torch.pow(10, y_true))
    de_log_ratio = torch.mean(torch.abs(torch.pow(10, y_pred) / torch.pow(10, y_true) - 1))

    print('%s:mae %s'% (tag,mae))
    print("%s:de_log_mae %s"%(tag, de_log_mae))
    print("%s:de_log_ratio %s"%(tag, de_log_ratio))

    with open("./lightning_logs/%s/merging_%s.log" % (log_name,tag), "w") as fp:
        print('%s:mae %s'%(tag, mae), file=fp)
        print("%s:de_log_mae %s"%(tag, de_log_mae), file=fp)
        print("%s:de_log_ratio %s"%( tag,de_log_ratio), file=fp)


#
#
#
# def main_repr():
#     """
#     pipeline task on nb-server
#     :param
#     --input_file: a csv format file path, which must contain a column called smiles
#     --input_file: a csv format file path, which contains a smiles column which corresponds
#     to input where possible, and a vector column
#
#     :return:
#     """
#     parser = ArgumentParser()
#     parser = pl.Trainer.add_argparse_args(parser)
#     parser = GraphFormer.add_model_specific_args(parser)
#     parser = GraphDataModule.add_argparse_args(parser)
#     parser.add_argument('--input_filepath', type=str)
#     parser.add_argument('--output_filepath',type=str)
#     args = parser.parse_args()
#     input_dataframe=pd.read_csv(args.input_filepath)
#     input_smiles_list=[]
#     sys.argv=sys.argv[:1]
#     for smiles in input_dataframe["SMILES"]:
#         try:
#             smiles_out=AllChem.MolToSmiles(AllChem.MolFromSmiles(smiles))
#             if smiles_out is None:
#                 raise Exception
#         except:
#             continue
#         input_smiles_list.append(smiles_out)
#
#     rem = Rem()
#     rr=rem.predict_repr(input_smiles_list)
#
#     smiles_out_list=[]
#     vector_list=[]
#     for smiles in rr:
#         smiles_out_list.append(smiles)
#         vector_list.append(rr[smiles][0])
#     out_dict={"SMILES":smiles_out_list,"vector":vector_list}
#     out_df=pd.DataFrame(data=out_dict)
#     out_df.to_csv(args.output_filepath,index=False)
#     import pickle
#     with open("%s.pkl"%(args.output_filepath),"wb") as pkl_fp:
#         pickle.dump(out_dict,pkl_fp)
#


def main():
    """
    """

    sys.argv += ['--num_workers', '11', '--seed', '0','--epoch' ,"1" ,  '--batch_size',
                 '512', '--gpus', '1', '--ffn_dim', '2048', '--hidden_dim',
                 '768', '--dropout_rate', '0.1', '--intput_dropout_rate', '0.1', '--attention_dropout_rate', '0.1',
                 '--n_layer',
                 '8', '--peak_lr', '2.5e-4', '--end_lr', '1e-6', '--head_size', '24', '--weight_decay', '0.00',
                 '--edge_type',   
                 'one_hop', '--warmup_updates', '1000', '--tot_updates', '10000', '--default_root_dir', '/root/Uni-Electrolyte/scoring_model/g2gt/src/',
                 '--progress_bar_refresh_rate', '1']

    parser = ArgumentParser()
    parser = pl.Trainer.add_argparse_args(parser)
    parser = GraphFormer.add_model_specific_args(parser)
    parser = GraphDataModule.add_argparse_args(parser)
    parser.add_argument('--pooling', default='attention', type=str)
    parser.add_argument('--downstream_ffn_dim', default=768, type=int)
    parser.add_argument('--downstream_dropout', default=0, type=float)
    #parser.add_argument('--dataset_name', type=str) #这句话不被加上也有dataset_name参数
    parser.add_argument('--input_filename', type=str)
    parser.add_argument("--sigmoid_inf",type=float)
    parser.add_argument("--sigmoid_sup",type=float)
    parser.add_argument("--epoch",type=int)
    parser.add_argument("--iid_test_dataset_name",type=str )
    parser.add_argument("--iid_test_input_filename",type=str )
    parser.add_argument("--ood_test_dataset_name",type=str)
    parser.add_argument("--ood_test_input_filename",type=str)
    parser.add_argument("--freeze",action="store_true")
    parser.add_argument("--log_name_prefix",type=str)
    parser.add_argument("--predicted_target",type=str)
    parser.add_argument("--loaded_target_list",type=str,help="target keys needed for loaded with ',' as split sign" )
    parser.add_argument("--inference",action="store_true")
    parser.add_argument("--ID_name", type=str)
    parser.add_argument("--predict_output_csv_file_path",type=str)
    parser.add_argument("--predict_input_csv_file_path", type=str)
    parser.add_argument("--predict_dataset_name", type=str)

    args = parser.parse_args() 
    
    if  args.loaded_target_list is None:

        args.loaded_target_list=[]
    else:
        args.loaded_target_list=args.loaded_target_list.split(",")

    args.log_name="%s_%s_%s"%(args.log_name_prefix,args.predicted_target,now.strftime("%Y%m%d%H%M%S"))
   
    rem=Rem(args)

    if args.inference==True:
        rem.inference()
    else:
        rem.train()


if __name__=="__main__":
    #rem=Rem()

    #rr=rem.predict(["O=C(CCNC(=O)C1CCC1)NC[C@]12CCC[C@H]1N(CC1CCC1)CC2"])
    #print(rr["O=C(CCNC(=O)C1CCC1)NC[C@]12CCC[C@H]1N(CC1CCC1)CC2"])
    # import pdb
    # pdb.set_trace()
    # print()

    main()

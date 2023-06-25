import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem

import os
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
import pandas as pd

class Rem():
    def __init__(self,dataset_name="qsar"):
        # ------------
        # args
        # ------------ #'--accelerator', 'ddp'
        sys.argv += ['--input_file', 'qsar.csv', '--output_file', 'qsar', '--num_workers', '1', '--seed', '0','--batch_size',
                     '1', '--dataset_name', dataset_name, '--gpus', '1', '--ffn_dim', '2048','--hidden_dim',
                     '768', '--dropout_rate', '0.1', '--intput_dropout_rate', '0.1', '--attention_dropout_rate', '0.1','--n_layer',
                     '8', '--peak_lr', '2.5e-4', '--end_lr', '1e-6', '--head_size', '24', '--weight_decay', '0.00','--edge_type',
                     'one_hop', '--warmup_updates', '1000', '--tot_updates', '500000', '--default_root_dir','./',
                     '--progress_bar_refresh_rate', '1']

        parser = ArgumentParser()
        parser = pl.Trainer.add_argparse_args(parser)
        parser = GraphFormer.add_model_specific_args(parser)
        parser = GraphDataModule.add_argparse_args(parser)
        parser.add_argument('--pooling', default='attention', type=str)
        parser.add_argument('--downstream_ffn_dim', default=768, type=int)
        parser.add_argument('--downstream_dropout', default=0, type=float)
        parser.add_argument('--input_file', default='', type=str)
        parser.add_argument('--output_file', default='out', type=str)

        self.args = parser.parse_args()
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
        self.checkpoint_callback = ModelCheckpoint(
            dirpath=dirpath,
            save_top_k=1,
            save_last=True,
            every_n_train_steps=10,
            monitor='rmse/validation',
            mode='min',
            # every_n_epochs = 2,
        )

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

    def train(self,root,input_file):
        # ------------
        # data
        # ------------

        #dataloader
        from torch.utils.data import DataLoader
        from functools import partial
        from collator import collator
        from custom_dataset import EmbeddingDataset

        train_dataset=EmbeddingDataset(root=root, input_file=input_file),
        train_loader = DataLoader(
            train_dataset,
            batch_size=1,
            shuffle=False,
            num_workers=0,
            pin_memory=True,
            persistent_workers=True,
            collate_fn=partial(collator, max_node=9999, multi_hop_max_dist=5,
                               rel_pos_max=1024),
        )
        print('len(test_dataloader)', len(train_loader))
        self.model = Embedding_extractor(self.args)

        self.trainer = pl.Trainer.from_argparse_args(self.args)
        self.trainer.callbacks.append(self.checkpoint_callback)
        self.trainer.callbacks.append(LearningRateMonitor(logging_interval='step'))
        trainer = pl.Trainer(limit_train_batches=100, max_epochs=1)
        trainer.fit(model=self.model, train_dataloaders=train_loader)








def main_finetune():
    """
    """
    parser = ArgumentParser()
    parser.add_argument('--input_rootpath', type=str)
    parser.add_argument('--input_filename', type=str)
    args = parser.parse_args()

    rem=Rem()
    rem.train(root=args.input_rootpath,
              input_file=args.input_filename)


def main_repr():
    """
    pipeline task on nb-server
    :param
    --input_file: a csv format file path, which must contain a column called smiles
    --input_file: a csv format file path, which contains a smiles column which corresponds
    to input where possible, and a vector column

    :return:
    """
    parser = ArgumentParser()
    parser = pl.Trainer.add_argparse_args(parser)
    parser = GraphFormer.add_model_specific_args(parser)
    parser = GraphDataModule.add_argparse_args(parser)
    parser.add_argument('--input_filepath', type=str)
    parser.add_argument('--output_filepath',type=str)
    args = parser.parse_args()
    input_dataframe=pd.read_csv(args.input_filepath)
    input_smiles_list=[]
    sys.argv=sys.argv[:1]
    for smiles in input_dataframe["SMILES"]:
        try:
            smiles_out=AllChem.MolToSmiles(AllChem.MolFromSmiles(smiles))
            if smiles_out is None:
                raise Exception
        except:
            continue
        input_smiles_list.append(smiles_out)

    rem = Rem()
    rr=rem.predict_repr(input_smiles_list)

    smiles_out_list=[]
    vector_list=[]
    for smiles in rr:
        smiles_out_list.append(smiles)
        vector_list.append(rr[smiles][0])
    out_dict={"SMILES":smiles_out_list,"vector":vector_list}
    out_df=pd.DataFrame(data=out_dict)
    out_df.to_csv(args.output_filepath,index=False)
    import pickle
    with open("%s.pkl"%(args.output_filepath),"wb") as pkl_fp:
        pickle.dump(out_dict,pkl_fp)


if __name__=="__main__":
    #rem=Rem()

    #rr=rem.predict(["O=C(CCNC(=O)C1CCC1)NC[C@]12CCC[C@H]1N(CC1CCC1)CC2"])
    #print(rr["O=C(CCNC(=O)C1CCC1)NC[C@]12CCC[C@H]1N(CC1CCC1)CC2"])
    # import pdb
    # pdb.set_trace()
    # print()

    main_finetune()

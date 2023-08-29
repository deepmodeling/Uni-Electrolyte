

import numpy as np
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
import pandas as pd
import torch
import torch.utils.data as data
from pytorch_lightning.callbacks.early_stopping import EarlyStopping
from pytorch_lightning.loggers.tensorboard import TensorBoardLogger
import datetime
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

    def train(self):
        # ------------
        # data
        # ------------

        #dataloader
        from torch.utils.data import DataLoader
        from functools import partial
        from collator import collator
        from custom_dataset import EmbeddingDataset

   
        all_dataset=get_dataset(dataset_name=self.args.dataset_name,input_file=self.args.input_filename,loaded_target_list=self.args.loaded_target_list)["dataset"]

        #get split from ogb loading mode
        from ogb.lsc import PCQM4Mv2Dataset
        dataset = PCQM4Mv2Dataset(root=self.args.dataset_name, only_smiles=True)
        split_dict = dataset.get_idx_split()
        train_idx = split_dict['train']  # numpy array storing indices of training molecules
        valid_idx = split_dict['valid']  # numpy array storing indices of validation molecules
        testdev_idx = split_dict['test-dev']  # numpy array storing indices of test-dev molecules
        testchallenge_idx = split_dict['test-challenge']  # numpy array storing indices of test-challenge molecules

        train_dataset=all_dataset[train_idx]
        valid_dataset=all_dataset[valid_idx]
        testdev_dataset=all_dataset[testdev_idx]
        testchallenge_dataset=all_dataset[testchallenge_idx]
        
        train_dataloader = DataLoader(
            train_dataset,
            batch_size=self.args.batch_size,
            shuffle=False,
            num_workers=self.args.num_workers,
            pin_memory=True,
            persistent_workers=True,
            collate_fn=partial(collator, max_node=9999, multi_hop_max_dist=5,
                               rel_pos_max=1024,predicted_target=self.args.predicted_target),)
        print('len(train_dataloader)', len(train_dataloader))

        valid_dataloader = DataLoader(
            valid_dataset,
            batch_size=self.args.batch_size,
            shuffle=False,
            num_workers=self.args.num_workers,
            pin_memory=True,
            persistent_workers=True,
            collate_fn=partial(collator, max_node=9999, multi_hop_max_dist=5,
                                rel_pos_max=1024,predicted_target=self.args.predicted_target),)
        print('len(valid_dataloader)', len(valid_dataloader))

        testdev_dataloader = DataLoader(
            testdev_dataset,
            batch_size=self.args.batch_size,
            shuffle=False,
            num_workers=self.args.num_workers,
            pin_memory=True,
            persistent_workers=True,
            collate_fn=partial(collator, max_node=9999, multi_hop_max_dist=5,
                               rel_pos_max=1024,predicted_target=self.args.predicted_target),
        )
        print('len(testdev_dataloader)', len(testdev_dataloader))
        

        testchallenge_dataloader = DataLoader(
            testchallenge_dataset,
            batch_size=self.args.batch_size,
            shuffle=False,
            num_workers=self.args.num_workers,
            pin_memory=True,
            persistent_workers=True,
            collate_fn=partial(collator, max_node=9999, multi_hop_max_dist=5,
                               rel_pos_max=1024,predicted_target=self.args.predicted_target),
        )
        print('len(testchallenge_dataloader)', len(testchallenge_dataloader))
        
      

        self.model = Embedding_extractor(self.args)
      
        # self.model=Embedding_extractor.load_from_checkpoint(
        #     "lightning_logs/version_0/checkpoints/epoch=156-step=10989.ckpt",
        #     args=self.args)
        # self.model=Embedding_extractor.load_from_checkpoint(
        #     "/data/rem/src/lightning_logs/cyc_no_freeze_no_decline_head_token_pooling_HOMO_20230706124935/version_0/checkpoints/epoch=582-epoch=epoch_val_loss=0.182.ckpt",
        #     args=self.args)
        # self.model=Embedding_extractor.load_from_checkpoint(
        #     "/data/rem/src/lightning_logs/cyc_no_freeze_no_decline_head_token_pooling_LUMO_20230706131306/version_0/checkpoints/epoch=907-epoch=epoch_val_loss=0.232.ckpt",
        #     args=self.args)
        # self.model=Embedding_extractor.load_from_checkpoint(
        #        "/data/rem/src/lightning_logs/cyc_no_freeze_no_decline_head_token_pooling_20230704183633/version_0/checkpoints/epoch=599-epoch=epoch_val_loss=0.164.ckpt",
        #        args=self.args)
        #self.model=Embedding_extractor.load_from_checkpoint(
        #     "/data/rem/src/lightning_logs/rem_electrolyte_train_1_CHO_47371_uninf_20230706_log_dcs_20230715131757/version_0/checkpoints/epoch=201-epoch=epoch_val_loss=0.155.ckpt",
        #        args=self.args)
        #self.model=Embedding_extractor.load_from_checkpoint(
        #"/data/rem/src/lightning_logs/rem_electrolyte_train_1_CHO_47371_uninf_20230706_log_vs_20230714180801/version_0/checkpoints/epoch=238-epoch=epoch_val_loss=0.163.ckpt",
        #        args=self.args)
        
        trainer = pl.Trainer( 
            logger= TensorBoardLogger("lightning_logs", name=self.args.log_name),
            max_epochs=self.args.epoch,
            devices=1,
            accelerator="auto",
            callbacks=[
                #EarlyStopping(monitor="epoch_val_loss", mode="min",patience=50,verbose=True),
                LearningRateMonitor(logging_interval='step'),
                ModelCheckpoint(filename='{epoch}-{epoch_val_loss:.3f}',save_top_k=3,save_last=True,monitor="epoch_val_loss",mode='min',verbose=True,auto_insert_metric_name=True),
            ],
            #limit_train_batches=20,
            #log_every_n_steps=10
            )
        trainer.fit(model=self.model, train_dataloaders=train_dataloader,val_dataloaders=valid_dataloader,)
        
        trainer.test(model=self.model, dataloaders=testdev_dataset)
        #trainer.test(model=self.model, dataloaders=testchallenge_dataloader)

        










def main_finetune():
    """
    """

    sys.argv += ['--num_workers', '11', '--seed', '0','--epoch' ,"1000" ,  '--batch_size', 
                 '512', '--gpus', '1', '--ffn_dim', '2048', '--hidden_dim',
                 '768', '--dropout_rate', '0.1', '--intput_dropout_rate', '0.1', '--attention_dropout_rate', '0.1',
                 '--n_layer',
                 '8', '--peak_lr', '2.5e-4', '--end_lr', '1e-6', '--head_size', '24', '--weight_decay', '0.00',
                 '--edge_type',   
                 'one_hop', '--warmup_updates', '1000', '--tot_updates', '10000', '--default_root_dir', './',
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
    parser.add_argument("--freeze",action="store_true")
    parser.add_argument("--log_name_prefix",type=str)
    parser.add_argument("--predicted_target",type=str)
    parser.add_argument("--loaded_target_list",type=str,help="target keys needed for loaded with ',' as split sign" )

    args = parser.parse_args() 
    args.loaded_target_list=args.loaded_target_list.split(",")
    args.log_name="%s_%s_%s"%(args.log_name_prefix,args.predicted_target,now.strftime("%Y%m%d%H%M%S"))
   
    rem=Rem(args)
    rem.train()


if __name__=="__main__":
    #rem=Rem()

    #rr=rem.predict(["O=C(CCNC(=O)C1CCC1)NC[C@]12CCC[C@H]1N(CC1CCC1)CC2"])
    #print(rr["O=C(CCNC(=O)C1CCC1)NC[C@]12CCC[C@H]1N(CC1CCC1)CC2"])
    # import pdb
    # pdb.set_trace()
    # print()

    main_finetune()

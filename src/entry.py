# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import torch
# torch.use_deterministic_algorithms(True)
import os
os.environ['CUBLAS_WORKSPACE_CONFIG'] = ':4096:8'

# from model import GraphFormer
from model import GraphFormer,Embedding_extractor

from IPython import embed
from data import GraphDataModule, get_dataset
from argparse import ArgumentParser
from pprint import pprint
import pytorch_lightning as pl
from pytorch_lightning.callbacks import ModelCheckpoint, LearningRateMonitor
import os,sys
import pickle

# from pytorch_lightning.plugins import DDPPlugin

def cli_main():
    # ------------
    # args
    # ------------
    sys.argv+= ['--input_file', 'qsar.csv', '--output_file', 'qsar', '--num_workers', '5', '--seed', '0', '--batch_size',
                '1', '--dataset_name', 'qsar', '--gpus', '1', '--accelerator', 'ddp', '--ffn_dim', '2048', '--hidden_dim',
                '768', '--dropout_rate', '0.1', '--intput_dropout_rate', '0.1', '--attention_dropout_rate', '0.1', '--n_layer',
                '8', '--peak_lr', '2.5e-4', '--end_lr', '1e-6', '--head_size', '24', '--weight_decay', '0.00', '--edge_type',
                'one_hop', '--warmup_updates', '1000', '--tot_updates', '500000', '--default_root_dir', './',
                '--progress_bar_refresh_rate', '1']

    parser = ArgumentParser()
    parser = pl.Trainer.add_argparse_args(parser)
    parser = GraphFormer.add_model_specific_args(parser)
    parser = GraphDataModule.add_argparse_args(parser)
    parser.add_argument('--pooling',default='attention',type=str)
    parser.add_argument('--downstream_ffn_dim',default=768,type=int)
    parser.add_argument('--downstream_dropout',default=0,type=float)
    parser.add_argument('--input_file',default='',type=str)
    parser.add_argument('--output_file',default='out',type=str)

    args = parser.parse_args()
    args.plugins = DDPPlugin(find_unused_parameters=True)
    args.max_steps = args.tot_updates + 1
    
    if not args.test and not args.validate:
        print(args)
    pl.seed_everything(args.seed)

    # ------------
    # data
    # ------------


    # with open("data/%s/raw/%s" % (args.dataset_name,args.input_file), "w") as fp:
    #     for smiles in ["[CH]1c2ccccc2CSc2ccccc21"]:
    #         print(smiles, file=fp)
    dm = GraphDataModule.from_argparse_args(args,input_file=args.input_file)

    model = Embedding_extractor(args)
    

    if not args.test and not args.validate:
        print(model)
    print('total params:', sum(p.numel() for p in model.parameters()))

    # ------------
    # training
    # ------------
    metric = 'valid_' + get_dataset(dm.dataset_name)['metric']
    dirpath = args.default_root_dir + f'/lightning_logs/checkpoints'
    checkpoint_callback = ModelCheckpoint(
        dirpath=dirpath,
        save_top_k =1,
        save_last=True,
        every_n_train_steps=10,
        monitor='rmse/validation',
        mode ='min',
        #every_n_epochs = 2,
    )

    if not args.test and not args.validate and os.path.exists(dirpath + '/last.ckpt'):
        args.resume_from_checkpoint = dirpath + '/last.ckpt'
        print('args.resume_from_checkpoint', args.resume_from_checkpoint)

    trainer = pl.Trainer.from_argparse_args(args)
    trainer.callbacks.append(checkpoint_callback)
    trainer.callbacks.append(LearningRateMonitor(logging_interval='step'))


 
    result = trainer.predict_repr(model, datamodule=dm)
    predict_epoch_end(args,result)
    
def predict_epoch_end(args, test_step_outputs):
    srcpath = args.default_root_dir+"/data/"+args.dataset_name
    outpath = args.default_root_dir

    out_dic = {}
    i=0
    print("?")
    src_smiles=open(srcpath+"/processed/smiles.txt")
    smiles_list = []
    for line in src_smiles:
        smiles_list.append(line.strip())
    path =outpath+"/results/"+args.dataset_name+"/"
    if not os.path.exists(path):
        os.mkdir(path)

    filename = path+args.output_file
    while os.path.exists(filename+"%s" % i):
        i += 1
            
    outfile = open(f"{filename}{i}","wb")

    for i in test_step_outputs:
        idx = i['idx']
        out_dic[smiles_list[idx]] = i['pred']
    pickle.dump(out_dic,outfile)
    outfile.close()
    return out_dic

if __name__ == '__main__':
    cli_main()

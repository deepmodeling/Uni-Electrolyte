import os

import torch
from uni_electrolyte.evaluator.dataset import thuEMol
from uni_electrolyte.evaluator.inference import pyG_inference_without_label
from uni_electrolyte.evaluator.model.spatial import LEFTNet
from uni_electrolyte.evaluator.trainer import pyG_trainer
from torch_geometric.data import DataLoader


targets = ['binding_e', 'dielectric_constant', 'viscosity', 'homo', 'lumo']
target = targets[0]

model = LEFTNet(
    num_layers=6,
    hidden_channels=192,
    num_radial=96,
    cutoff=8
)


####################################################################################################################
device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device("cpu")
trainer = pyG_trainer()
####################################################################################################################
ckpt = torch.load(r'./input/valid_checkpoint.pt')
model.load_state_dict(ckpt['model_state_dict'])
model.to(device=device)
####################################################################################################################
dataset = thuEMol(root='./input/data/iid_test', load_target_list=targets)
dataset.data.y = dataset.data[target]
split_idx = dataset.get_idx_split(len(dataset.data.y), train_size=1, valid_size=1, seed=42)
train_dataset, valid_dataset, test_dataset = dataset[split_idx['train']], dataset[split_idx['valid']], dataset[
    split_idx['test']]
print('train, validaion, test:', len(train_dataset), len(valid_dataset), len(test_dataset))
####################################################################################################################
evaluation = pyG_inference_without_label(dump_info_path=r'./output/inference_without_label_test', property=target)
info = trainer.val(model=model, data_loader=DataLoader(test_dataset, 50, shuffle=False),
                   energy_and_force=False, p=0, evaluation=evaluation, device=device)
####################################################################################################################

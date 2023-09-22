import os

import torch
from uni_electrolyte.evaluator.dataset import pyG_thuEMol
from uni_electrolyte.evaluator.inference import pyG_inference_test, pyG_inference_train, pyG_inference_without_label
from uni_electrolyte.evaluator.model.spatial import ComENet
from uni_electrolyte.evaluator.trainer import pyG_trainer
from torch_geometric.data import DataLoader


targets = ['binding_e', 'dielectric_constant', 'viscosity', 'homo', 'lumo']
target = targets[0]

model = ComENet()

data_path = r'./input/data'
####################################################################################################################
device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device("cpu")

dataset = pyG_thuEMol(root=os.path.join(data_path, 'train'))
dataset.data.y = dataset.data[target]
split_idx = dataset.get_idx_split(len(dataset.data.y), train_size=33540, valid_size=3353, seed=42)
train_dataset, valid_dataset, test_dataset = dataset[split_idx['train']], dataset[split_idx['valid']], dataset[
    split_idx['test']]
print('train, validaion, test:', len(train_dataset), len(valid_dataset), len(test_dataset))

loss_func = torch.nn.MSELoss()
evaluation = pyG_inference_train()

trainer = pyG_trainer()
trainer.runCLR(device=device, train_dataset=train_dataset, valid_dataset=valid_dataset,
               model=model, loss_func=loss_func, evaluation=evaluation,
               batch_size=100, val_batch_size=100, epochs=2,
               save_dir='./output/run_info',
               log_dir='./output/run_info',
               optimizer_args={'max_lr': 5e-4,
                               'base_lr': 1e-5,
                               'step_size_up': 10,
                               'step_size_down': 40,
                               'mode': "exp_range"})

####################################################################################################################
ckpt = torch.load('./output/run_info/valid_checkpoint.pt')
model.load_state_dict(ckpt['model_state_dict'])
model.to(device=device)
####################################################################################################################
dataset = pyG_thuEMol(root=os.path.join(data_path, 'ood_test'))
dataset.data.y = dataset.data[target]
split_idx = dataset.get_idx_split(len(dataset.data.y), train_size=1, valid_size=1, seed=42)
train_dataset, valid_dataset, test_dataset = dataset[split_idx['train']], dataset[split_idx['valid']], dataset[
    split_idx['test']]
print('train, validaion, test:', len(train_dataset), len(valid_dataset), len(test_dataset))
####################################################################################################################
evaluation = pyG_inference_test(dump_info_path=r'./output/test_info', info_file_flag='ood_test', property=target)
_ = trainer.val(model=model, data_loader=DataLoader(test_dataset, 50, shuffle=False),
                   energy_and_force=False, p=0, evaluation=evaluation, device=device)
####################################################################################################################
dataset = pyG_thuEMol(root=os.path.join(data_path, 'iid_test'))
dataset.data.y = dataset.data[target]
split_idx = dataset.get_idx_split(len(dataset.data.y), train_size=1, valid_size=1, seed=42)
train_dataset, valid_dataset, test_dataset = dataset[split_idx['train']], dataset[split_idx['valid']], dataset[
    split_idx['test']]
print('train, validaion, test:', len(train_dataset), len(valid_dataset), len(test_dataset))
####################################################################################################################
evaluation = pyG_inference_test(dump_info_path=r'./output/test_info', info_file_flag='iid_test', property=target)
_ = trainer.val(model=model, data_loader=DataLoader(test_dataset, 50, shuffle=False),
                   energy_and_force=False, p=0, evaluation=evaluation, device=device)
####################################################################################################################

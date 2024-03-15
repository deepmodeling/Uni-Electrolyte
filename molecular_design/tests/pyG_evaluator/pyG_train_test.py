import os

import torch
from torch.utils.data import ConcatDataset
#export PYTHONPATH=$PYTHONPATH:/root/yinshiqiu/Uni-Electrolyte/molecular_design:/root/yinshiqiu/Uni-Electrolyte/molecular_design/uni_electrolyte/evaluator/model/spatial   to search the uni_electrolyte package
from uni_electrolyte.evaluator.dataset import thuEMol,g2g_thuEMol
from uni_electrolyte.evaluator.inference import pyG_inference_test, pyG_inference_train, pyG_inference_without_label

from uni_electrolyte.evaluator.trainer import pyG_trainer
from torch_geometric.data import DataLoader
from uni_electrolyte.evaluator.model.spatial import OA_REACTDIFF_LEFTNet,LEFTNet
device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device("cpu")

targets = ['binding_e', 'dielectric_constant', 'viscosity', 'homo', 'lumo']
target = targets[1]
# model = LEFTNet(
#     num_layers=6,
#     hidden_channels=128,
#     # hidden_channels=256,
#     num_radial=96,
#     cutoff=8
# )
# import pdb
# pdb.set_trace()
model=OA_REACTDIFF_LEFTNet(device)
model = model.to(device)
# import pdb
# pdb.set_trace()

data_root_path="202312_data"
data_path = f'{data_root_path}/input/'
####################################################################################################################

ood_test_dataset=g2g_thuEMol(root=os.path.join(data_path, 'ood_test'), load_target_list=targets)
ood_test_dataset.data.y = ood_test_dataset.data[target]
_train_dataset = g2g_thuEMol(root=os.path.join(data_path, 'train'), load_target_list=targets)
_train_dataset.data.y = _train_dataset.data[target]
all_train_dataset = ConcatDataset([ood_test_dataset, _train_dataset])

train_size=int(0.9*len(all_train_dataset))
valid_size=len(all_train_dataset)-train_size
split_idx = all_train_dataset.get_idx_split(len(all_train_dataset), train_size=train_size, valid_size=valid_size, seed=42)
# split_idx = dataset.get_idx_split(len(dataset.data.y), train_size=100, valid_size=100, seed=42)
train_dataset, valid_dataset, = all_train_dataset[split_idx['train']], all_train_dataset[split_idx['valid']]
print('train, validaion, test:', len(train_dataset), len(valid_dataset))

loss_func = torch.nn.MSELoss()
evaluation = pyG_inference_train()

trainer = pyG_trainer()

trainer.runCLR(device=device, train_dataset=train_dataset, valid_dataset=valid_dataset,
               model=model, loss_func=loss_func, evaluation=evaluation,
               batch_size=200, val_batch_size=200, epochs=2,
               save_dir='./output/run_info',
               log_dir='./output/run_info',
                optimizer_args={'max_lr': 5e-4,
                                'base_lr': 1e-5,
                                'step_size_up': 10,
                                'step_size_down': 40,
                                'mode': "exp_range"},
                )
####################################################################################################################
ckpt = torch.load('./output/run_info/valid_checkpoint.pt')
model.load_state_dict(ckpt['model_state_dict'])
model.to(device=device)
####################################################################################################################
iid_test_dataset = g2g_thuEMol(root=os.path.join(data_path, 'iid_test'), load_target_list=targets)
iid_test_dataset.data.y = iid_test_dataset.data[target]
# split_idx = dataset.get_idx_split(len(dataset.data.y), train_size=0, valid_size=0, seed=42)
# test_dataset = dataset[split_idx['test']]
# print('Dataset size:', len(test_dataset))
####################################################################################################################
evaluation = pyG_inference_test(dump_info_path=r'./output/test_info/iid_test', info_file_flag=target, property=target)
_ = trainer.val(model=model, data_loader=DataLoader(iid_test_dataset, 50, shuffle=False),
                   energy_and_force=False, p=0, evaluation=evaluation, device=device)
# ####################################################################################################################
# dataset = g2g_thuEMol(root=os.path.join(data_path, 'ood_test'), load_target_list=targets)
# dataset.data.y = dataset.data[target]
# test_dataset=dataset
# # split_idx = dataset.get_idx_split(len(dataset.data.y), train_size=0, valid_size=0, seed=42)
# # test_dataset = dataset[split_idx['test']]
# # print('Dataset size:', len(test_dataset))
# ####################################################################################################################
# evaluation = pyG_inference_test(dump_info_path=r'./output/test_info/ood_test', info_file_flag=target, property=target)
# _ = trainer.val(model=model, data_loader=DataLoader(test_dataset, 50, shuffle=False),
#                    energy_and_force=False, p=0, evaluation=evaluation, device=device)
#

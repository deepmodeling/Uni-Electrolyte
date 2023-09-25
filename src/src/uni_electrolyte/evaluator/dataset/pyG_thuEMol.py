# A torch-geometric data format to properly incorporate Thu-ChenXiang electrolyte database.
# Part of this code are borrowed from dive-into-graph project,
# see https://github.com/divelab/DIG/blob/dig-stable/dig/threedgraph/dataset/PygQM93D.py

import os.path as osp
import numpy as np
from tqdm import tqdm
import torch
from sklearn.utils import shuffle

from torch_geometric.data import InMemoryDataset, download_url
from torch_geometric.data import Data, DataLoader


# the original target prediction class
# need to be adjusted for new multiple-targets prediction task
class thuEMol(InMemoryDataset):
    def __init__(self, root='dataset/', transform=None, pre_transform=None, pre_filter=None, load_target_list: list=None):
        self.load_target_list = load_target_list

        super(thuEMol, self).__init__(root, transform, pre_transform, pre_filter)

        self.data, self.slices = torch.load(self.processed_paths[0])

    @property
    def raw_file_names(self):
        return 'thuEMol.npz'

    @property
    def processed_file_names(self):
        return 'thuEMol_pre.pt'

    def download(self):
        print('Please contact Tsinghua University.')
        pass

    def process(self):

        data = np.load(osp.join(self.raw_dir, self.raw_file_names))

        R = data['R']
        Z = data['Z']
        N = data['N']
        split = np.cumsum(N)
        R_qm9 = np.split(R, split)
        Z_qm9 = np.split(Z, split)
        target = {}
        for name in self.load_target_list:
            target[name] = np.expand_dims(data[name], axis=-1)

        data_list = []
        for i in tqdm(range(len(N))):
            R_i = torch.tensor(R_qm9[i], dtype=torch.float32)
            z_i = torch.tensor(Z_qm9[i], dtype=torch.int64)
            y_i = [torch.tensor(target[name][i], dtype=torch.float32) for name in self.load_target_list]
            y_dict = dict(zip(self.load_target_list, y_i))
            data = Data(pos=R_i, z=z_i, y=y_i[0], **y_dict)
            data_list.append(data)

        if self.pre_filter is not None:
            data_list = [data for data in data_list if self.pre_filter(data)]
        if self.pre_transform is not None:
            data_list = [self.pre_transform(data) for data in data_list]

        data, slices = self.collate(data_list)

        print('Saving...')
        torch.save((data, slices), self.processed_paths[0])

    def get_idx_split(self, data_size, train_size, valid_size, seed):
        ids = shuffle(range(data_size), random_state=seed)
        train_idx, val_idx, test_idx = torch.tensor(ids[:train_size]), torch.tensor(
            ids[train_size:train_size + valid_size]), torch.tensor(ids[train_size + valid_size:])
        split_dict = {'train': train_idx, 'valid': val_idx, 'test': test_idx}
        return split_dict
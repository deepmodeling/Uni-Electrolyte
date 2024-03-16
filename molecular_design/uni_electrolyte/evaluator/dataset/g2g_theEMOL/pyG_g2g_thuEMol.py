# A torch-geometric data format to properly incorporate Thu-ChenXiang electrolyte database.
# Part of this code are borrowed from dive-into-graph project,
# see https://github.com/divelab/DIG/blob/dig-stable/dig/threedgraph/dataset/PygQM93D.py

import os.path as osp
import numpy as np
from tqdm import tqdm
import torch
from sklearn.utils import shuffle
from rdkit.Chem import AllChem
from torch_geometric.data import InMemoryDataset, download_url
from torch_geometric.data import Data, DataLoader
from uni_electrolyte.evaluator.model.spatial.oa_reactdiff.utils.xyz2mol import xyz2mol

# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.


from rdkit import Chem
import rdkit.Chem.AllChem as AllChem
import joblib
import math
from scipy.spatial.distance import cdist
import torch
import numpy as np
from .custom_dataset import mol2graph,preprocess_item


# the original target prediction class
# need to be adjusted for new multiple-targets prediction task
class g2g_thuEMol(InMemoryDataset):
    def __init__(self, root='dataset/', transform=None, pre_transform=None, pre_filter=None, load_target_list: list=None, use_pbc: bool=False):
        self.load_target_list = load_target_list
        self.use_pbc = use_pbc
        self.error_nums = 0


        super(g2g_thuEMol, self).__init__(root, transform, pre_transform, pre_filter)
        fp = open(osp.join(self.processed_dir, "error_data"), "w")
        fp.close()
        self.data, self.slices = torch.load(self.processed_paths[0])


    @property
    def raw_file_names(self):
        return 'thuEMol.npz'

    @property
    def processed_file_names(self):
        return 'g2g_thuEMol_pre.pt'

    def download(self):
        print('Please contact Tsinghua University.')
        pass


    def process(self):

        old_data = np.load(osp.join(self.raw_dir, self.raw_file_names))

        R = old_data['R']
        Z = old_data['Z']
        N = old_data['N']
        split = np.cumsum(N)
        R_qm9 = np.split(R, split)
        Z_qm9 = np.split(Z, split)
        target = {}
        for name in self.load_target_list:
            target[name] = np.expand_dims(old_data[name], axis=-1)

        data_list = []
        for i in tqdm(range(len(N))):
            R_i = torch.tensor(R_qm9[i], dtype=torch.float32)
            z_i = torch.tensor(Z_qm9[i], dtype=torch.int64)
            y_i = [torch.tensor(target[name][i], dtype=torch.float32) for name in self.load_target_list]
            y_dict = dict(zip(self.load_target_list, y_i))
            data = Data(pos=R_i, z=z_i, y=y_i[0], **y_dict)

            #add SMILES/bond info
            try:
                mols=xyz2mol(atoms=z_i.tolist(),coordinates=R_i.tolist())
            except:
                self.error_nums += 1
                print(osp.join(self.raw_dir, self.raw_file_names),
                      "molecule %s xyz2mol error nums:%s" % (i, self.error_nums))
                with open(osp.join(self.processed_dir, "error_data"), "a") as fp:
                    print("mol index :%s atom_nums:%s" % (i, len(z_i)), file=fp)
                continue
            if type(mols)!=list:
                self.error_nums += 1
                print(osp.join(self.raw_dir, self.raw_file_names),
                      "molecule %s xyz2mol error nums:%s" % (i, self.error_nums))
                with open(osp.join(self.processed_dir, "error_data"), "a") as fp:
                    print("mol index :%s atom_nums:%s" % (i, len(z_i)), file=fp)
                continue
            if len(mols)!=1:
                self.error_nums += 1
                print(osp.join(self.raw_dir, self.raw_file_names),
                      "molecule %s xyz2mol error nums:%s" % (i, self.error_nums))
                with open(osp.join(self.processed_dir, "error_data"), "a") as fp:
                    print("mol index :%s atom_nums:%s" % (i, len(z_i)), file=fp)
                continue
            mol=mols[0]
            tmp_mol=AllChem.RemoveAllHs(mol)
            xyz2smiles=AllChem.MolToSmiles(tmp_mol)
            # import pdb
            # pdb.set_trace()
            src_graph=mol2graph(mol)

            assert (len(src_graph['edge_feat']) == src_graph['edge_index'].shape[1])
            assert (len(src_graph['node_feat']) == src_graph['num_nodes'])


            # Gen X
            data.__num_nodes__ = int(src_graph['num_nodes'])
            data.edge_index = src_graph['edge_index']
            data.edge_attr = src_graph['edge_feat']
            data.x = src_graph['node_feat']
            data.all_rel_pos_3d = src_graph['rel_pos_3d']
            data.reverse = 0
            data.edge_index = torch.from_numpy(data.edge_index).to(torch.int64)
            data.edge_attr = torch.from_numpy(data.edge_attr).to(torch.int64)
            data.x = torch.from_numpy(data.x).to(torch.int64)
            data.reverse = torch.tensor([data.reverse], dtype=torch.int64)
            data.xyz2smiles = xyz2smiles

            data = preprocess_item(data, noise=False)
            data.adj = data.adj.numpy()
            data.attn_bias = data.attn_bias.numpy()
            data.attn_edge_type = data.attn_edge_type.numpy()
            data.rel_pos = data.rel_pos.numpy()
            data.edge_input = data.edge_input.numpy()
            data.all_rel_pos_3d_1 = data.all_rel_pos_3d_1.numpy()

            data_list.append(data)

        if self.pre_filter is not None:
            data_list = [data for data in data_list if self.pre_filter(data)]
        if self.pre_transform is not None:
            data_list = [self.pre_transform(data) for data in data_list]

        data, slices = self.collate(data_list)
        if self.use_pbc:
            data['cell'] = torch.tensor(old_data['cell'], dtype=torch.float32)
            data['edge_index'] = torch.tensor(old_data['edge_index'], dtype=torch.int64)
            data['neighbors'] = torch.tensor(old_data['neighbors'], dtype=torch.int64)
            data['cell_offsets'] = torch.tensor(old_data['cell_offsets'], dtype=torch.int64)

            slices['cell'] = slices['y']
            slices['neighbors'] = slices['y']
            tracker = 0
            slice_list = [0]
            for a_neighbor in old_data['neighbors']:
                tracker = tracker + int(a_neighbor)
                slice_list.append(tracker)
            slices['cell_offsets'] = torch.tensor(slice_list, dtype=torch.int64)
            slices['edge_index'] = torch.tensor(slice_list, dtype=torch.int64)

        print('Saving...')
        torch.save((data, slices), self.processed_paths[0])

    def get_idx_split(self, data_size, train_size, valid_size, seed):
        ids = shuffle(range(data_size), random_state=seed)
        train_idx, val_idx, test_idx = torch.tensor(ids[:train_size]), torch.tensor(
            ids[train_size:train_size + valid_size]), torch.tensor(ids[train_size + valid_size:])
        split_dict = {'train': train_idx, 'valid': val_idx, 'test': test_idx}
        return split_dict
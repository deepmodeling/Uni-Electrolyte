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
from ..model.spatial.oa_reactdiff.utils.xyz2mol import xyz2mol

# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.


from rdkit import Chem
import rdkit.Chem.AllChem as AllChem
import joblib
import math
from scipy.spatial.distance import cdist
import torch
import numpy as np

# import pyximport
# pyximport.install(setup_args={'include_dirs': np.get_include()})
#
# ===================== NODE START =====================
atomic_num_list = list(range(119))
chiral_tag_list = list(range(4))
degree_list = list(range(11))
possible_formal_charge_list = list(range(16))
possible_numH_list = list(range(9))
possible_number_radical_e_list = list(range(5))
possible_hybridization_list = ['SP', 'SP2', 'SP3', 'SP3D', 'SP3D2', 'S']
possible_is_aromatic_list = [False, True]
possible_is_in_ring_list = [False, True]
explicit_valence_list = list(range(13))
implicit_valence_list = list(range(13))
total_valence_list = list(range(26))
total_degree_list = list(range(32))


def simple_atom_feature(atom):
    atomic_num = atom.GetAtomicNum()
    assert atomic_num in atomic_num_list

    chiral_tag = int(atom.GetChiralTag())
    assert chiral_tag in chiral_tag_list

    degree = atom.GetTotalDegree()
    assert degree in degree_list

    possible_formal_charge = atom.GetFormalCharge()
    possible_formal_charge_transformed = possible_formal_charge + 5
    assert possible_formal_charge_transformed in possible_formal_charge_list

    possible_numH = atom.GetTotalNumHs()
    assert possible_numH in possible_numH_list
    # 5
    possible_number_radical_e = atom.GetNumRadicalElectrons()
    assert possible_number_radical_e in possible_number_radical_e_list

    possible_hybridization = str(atom.GetHybridization())
    assert possible_hybridization in possible_hybridization_list
    possible_hybridization = possible_hybridization_list.index(possible_hybridization)

    possible_is_aromatic = atom.GetIsAromatic()
    assert possible_is_aromatic in possible_is_aromatic_list
    possible_is_aromatic = possible_is_aromatic_list.index(possible_is_aromatic)

    possible_is_in_ring = atom.IsInRing()
    assert possible_is_in_ring in possible_is_in_ring_list
    possible_is_in_ring = possible_is_in_ring_list.index(possible_is_in_ring)

    explicit_valence = atom.GetExplicitValence()
    assert explicit_valence in explicit_valence_list
    # 10
    implicit_valence = atom.GetImplicitValence()
    assert implicit_valence in implicit_valence_list

    total_valence = atom.GetTotalValence()
    assert total_valence in total_valence_list

    total_degree = atom.GetTotalDegree()
    assert total_degree in total_degree_list

    sparse_features = [
        atomic_num, chiral_tag, degree, possible_formal_charge_transformed, possible_numH,
        possible_number_radical_e, possible_hybridization, possible_is_aromatic, possible_is_in_ring, explicit_valence,
        implicit_valence, total_valence, total_degree,
    ]
    return sparse_features


def easy_bin(x, bin):
    x = float(x)
    cnt = 0
    if math.isinf(x):
        return 120
    if math.isnan(x):
        return 121

    while True:
        if cnt == len(bin):
            return cnt
        if x > bin[cnt]:
            cnt += 1
        else:
            return cnt


def peri_features(atom, peri):
    rvdw = peri.GetRvdw(atom.GetAtomicNum())
    default_valence = peri.GetDefaultValence(atom.GetAtomicNum())
    n_outer_elecs = peri.GetNOuterElecs(atom.GetAtomicNum())
    rb0 = peri.GetRb0(atom.GetAtomicNum())
    sparse_features = [
        default_valence,
        n_outer_elecs,
        easy_bin(rvdw, [1.2, 1.5, 1.55, 1.6, 1.7, 1.8, 2.4]),
        easy_bin(rb0, [0.33, 0.611, 0.66, 0.7, 0.77, 0.997, 1.04, 1.54])
    ]
    return sparse_features


def envatom_feature(mol, radius, atom_idx):
    env = Chem.FindAtomEnvironmentOfRadiusN(mol, radius, atom_idx, useHs=True)
    submol = Chem.PathToSubmol(mol, env, atomMap={})
    return submol.GetNumAtoms()


def envatom_features(mol, atom):
    return [
        envatom_feature(mol, r, atom.GetIdx()) for r in range(2, 9)
    ]


def atom_to_feature_vector(atom, peri, mol):
    sparse_features = []
    sparse_features.extend(simple_atom_feature(atom))
    sparse_features.extend(peri_features(atom, peri))
    sparse_features.extend(envatom_features(mol, atom))
    sparse_features.append(easy_bin(atom.GetProp('_GasteigerCharge'),
                                    [-0.87431233, -0.47758285, -0.38806704, -0.32606976, -0.28913129,
                                     -0.25853269, -0.24494531, -0.20136365, -0.12197541, -0.08234462,
                                     -0.06248558, -0.06079668, -0.05704827, -0.05296379, -0.04884997,
                                     -0.04390136, -0.03881107, -0.03328515, -0.02582824, -0.01916618,
                                     -0.01005982, 0.0013529, 0.01490858, 0.0276433, 0.04070013,
                                     0.05610381, 0.07337645, 0.08998278, 0.11564625, 0.14390777,
                                     0.18754518, 0.27317209, 1.]))
    return sparse_features


import os.path as osp
from rdkit import RDConfig
from rdkit.Chem import ChemicalFeatures

fdef_name = osp.join(RDConfig.RDDataDir, 'BaseFeatures.fdef')
chem_feature_factory = ChemicalFeatures.BuildFeatureFactory(fdef_name)


def donor_acceptor_feature(x_num, mol):
    chem_feature_factory_feats = chem_feature_factory.GetFeaturesForMol(mol)
    features = np.zeros([x_num, 2], dtype=np.int64)
    for i in range(len(chem_feature_factory_feats)):
        if chem_feature_factory_feats[i].GetFamily() == 'Donor':
            node_list = chem_feature_factory_feats[i].GetAtomIds()
            for j in node_list:
                features[j, 0] = 1
        elif chem_feature_factory_feats[i].GetFamily() == 'Acceptor':
            node_list = chem_feature_factory_feats[i].GetAtomIds()
            for j in node_list:
                features[j, 1] = 1
    return features


chiral_centers_list = ['R', 'S']


def chiral_centers_feature(x_num, mol):
    features = np.zeros([x_num, 1], dtype=np.int64)
    t = Chem.FindMolChiralCenters(mol)
    for i in t:
        idx, type = i
        features[idx] = chiral_centers_list.index(type) + 1  # 0 for not center
    return features


# ===================== NODE END =====================

# ===================== BOND START =====================
possible_bond_type_list = list(range(32))
possible_bond_stereo_list = list(range(16))
possible_is_conjugated_list = [False, True]
possible_is_in_ring_list = [False, True]
possible_bond_dir_list = list(range(16))


def bond_to_feature_vector(bond):
    # 0
    bond_type = int(bond.GetBondType())
    assert bond_type in possible_bond_type_list

    bond_stereo = int(bond.GetStereo())
    assert bond_stereo in possible_bond_stereo_list

    is_conjugated = bond.GetIsConjugated()
    assert is_conjugated in possible_is_conjugated_list
    is_conjugated = possible_is_conjugated_list.index(is_conjugated)

    is_in_ring = bond.IsInRing()
    assert is_in_ring in possible_is_in_ring_list
    is_in_ring = possible_is_in_ring_list.index(is_in_ring)

    bond_dir = int(bond.GetBondDir())
    assert bond_dir in possible_bond_dir_list

    bond_feature = [
        bond_type,
        bond_stereo,
        is_conjugated,
        is_in_ring,
        bond_dir,
    ]
    return bond_feature


# ===================== BOND END =====================

# ===================== ATTN START =====================
def get_rel_pos(mol):
    try:
        new_mol = Chem.AddHs(mol)
        res = AllChem.EmbedMultipleConfs(new_mol, numConfs=10)
        ### MMFF generates multiple conformations
        res = AllChem.MMFFOptimizeMoleculeConfs(new_mol)
        new_mol = Chem.RemoveHs(new_mol)
        index = np.argmin([x[1] for x in res])
        energy = res[index][1]
        conf = new_mol.GetConformer(id=int(index))
    except:
        new_mol = mol
        AllChem.Compute2DCoords(new_mol)
        energy = 0
        conf = new_mol.GetConformer()

    atom_poses = []
    for i, atom in enumerate(new_mol.GetAtoms()):
        if atom.GetAtomicNum() == 0:
            return [[0.0, 0.0, 0.0]] * len(new_mol.GetAtoms())
        pos = conf.GetAtomPosition(i)
        atom_poses.append([pos.x, pos.y, pos.z])
    atom_poses = np.array(atom_poses, dtype=float)
    rel_pos_3d = cdist(atom_poses, atom_poses)
    return rel_pos_3d


def shortest_path(mol):
    # GetDistanceMatrix returns the molecules 2D (topological) distance matrix:
    dm = Chem.GetDistanceMatrix(mol)
    return dm


''' ===================== Graph 2 Seq ==================== '''

# ===================== ATTN START =====================

curmax = 0
ditched = 0


def mol2graph(mol):
    """

    """
    # build networkx graph for bfs

    AllChem.ComputeGasteigerCharges(mol)
    peri = Chem.rdchem.GetPeriodicTable()
    g_edge_attr = []
    # atoms
    i = 0
    atom_features_list = []
    mol_conformer = mol.GetConformer()
    for atom in mol.GetAtoms():
        atom_features_list.append(atom_to_feature_vector(atom, peri, mol))

    pos = mol.GetConformer().GetPositions()
    x = np.array(atom_features_list, dtype=np.int64)
    x = np.concatenate([x, donor_acceptor_feature(x.shape[0], mol)], axis=1)
    x = np.concatenate([x, chiral_centers_feature(x.shape[0], mol)], axis=1)

    # adj_mat_indx && adj_mat
    atom_num = len(x)
    adj_mat = adj = torch.zeros(atom_num, atom_num)

    # bonds
    num_bond_features = 5
    if len(mol.GetBonds()) > 0:  # mol has bonds
        edges_list = []
        edge_features_list = []
        for bond in mol.GetBonds():
            i = bond.GetBeginAtomIdx()
            j = bond.GetEndAtomIdx()
            begin_atom = bond.GetBeginAtom()
            end_atom = bond.GetEndAtom()

            edge_feature = bond_to_feature_vector(bond)
            # add edges in both directions
            edges_list.append((i, j))
            '''new'''
            # adjacency matrix

            edge_features_list.append(edge_feature)
            edges_list.append((j, i))

            edge_features_list.append(edge_feature)

        # data.edge_index: Graph connectivity in COO format with shape [2, num_edges]
        edge_index = np.array(edges_list, dtype=np.int64).T

        # data.edge_attr: Edge feature matrix with shape [num_edges, num_edge_features]
        edge_attr = np.array(edge_features_list, dtype=np.int64)

    else:  # mol has no bonds
        edge_index = np.empty((2, 0), dtype=np.int64)
        edge_attr = np.empty((0, num_bond_features), dtype=np.int64)

    '''New'''

    # attn
    rel_pos_3d = shortest_path(mol)
    graph = dict()

    # graph['node_edge_seq'] = nx.to_numpy_array(G,weight="edge").tolist()

    graph['edge_index'] = edge_index
    graph['edge_feat'] = edge_attr
    graph['node_feat'] = x  # 第一个特征是原子数
    graph['num_nodes'] = len(x)
    graph['rel_pos_3d'] = rel_pos_3d  # 拓扑距离
    graph["pos"] = pos  # 真正的3D坐标

    return graph


# the original target prediction class
# need to be adjusted for new multiple-targets prediction task
class g2g_thuEMol(InMemoryDataset):
    def __init__(self, root='dataset/', transform=None, pre_transform=None, pre_filter=None, load_target_list: list=None, use_pbc: bool=False):
        self.load_target_list = load_target_list
        self.use_pbc = use_pbc

        super(g2g_thuEMol, self).__init__(root, transform, pre_transform, pre_filter)

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
            mols=xyz2mol(atoms=z_i.tolist(),coordinates=R_i.tolist())
            if type(mols)!=list:
                raise Exception(osp.join(self.raw_dir, self.raw_file_names),"molecule %s xyz2mol error"%(i))
            if len(mols)!=1:
                raise Exception(osp.join(self.raw_dir, self.raw_file_names), "molecule %s xyz2mol error" % (i))
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
            data.xyz2smiles = xyz2smiles


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
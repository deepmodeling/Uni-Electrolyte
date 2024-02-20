# Copyright AISI
# Data transformation and distance calculator for Periodic Boundary Conditions(PBC)
# Part of the code is modified from Open Catalyst Project:
# 1. Data transformation: ocp/ocpmodels/preprocessing/atoms_to_graphs.py#L91
# 2. Distance calculator: ocp/ocpmodels/common/utils.py#L509


import os
import shutil

import ase
import numpy as np
from ase.db import connect
from ase.io.cif import read_cif
from ase.io.proteindatabank import read_proteindatabank, write_proteindatabank
from pymatgen.io.ase import AseAtomsAdaptor


def cif_2_db(cif_root: str, db_path: str):
    cwd_ = os.getcwd()
    os.chdir(cif_root)
    with connect(db_path) as db:
        for a_file in os.listdir('/'):
            identity = os.path.splitext(a_file)[0]
            with open(a_file, 'r') as f_r:
                for an_atoms in read_cif(f_r, index=slice(None, None, None)):
                    pass
            db.write(an_atoms, identity=int(identity))
    os.chdir(cwd_)


def pdb_2_db(pdb_root: str, db_path: str):
    cwd_ = os.getcwd()
    os.chdir(pdb_root)
    with connect(db_path) as db:
        for a_file in os.listdir('/'):
            identity = os.path.splitext(a_file)[0]
            with open(a_file, 'r') as f_r:
                for an_atoms in read_proteindatabank(f_r, index=slice(None, None, None)):
                    pass
            db.write(an_atoms, identity=int(identity))
    os.chdir(cwd_)


def get_pbc_data(a_row: ase.db.core.AtomsRow, max_neighbor: int = 20, cutoff: float = 8.0):
    an_atoms = a_row.toatoms()
    struct = AseAtomsAdaptor.get_structure(an_atoms)
    _c_index, _n_index, _offsets, n_distance = struct.get_neighbor_list(
        r=cutoff, numerical_tol=0, exclude_self=True
    )

    _nonmax_idx = []
    for i in range(len(an_atoms)):
        idx_i = (_c_index == i).nonzero()[0]
        # sort neighbors by distance, remove edges larger than max_neighbors
        idx_sorted = np.argsort(n_distance[idx_i])[: max_neighbor]
        _nonmax_idx.append(idx_i[idx_sorted])
    _nonmax_idx = np.concatenate(_nonmax_idx)
    # Stack center and neighbor index and reshapes distances
    c_index = _c_index[_nonmax_idx]
    n_index = _n_index[_nonmax_idx]
    n_distance = n_distance[_nonmax_idx]
    offsets = _offsets[_nonmax_idx]

    edge_index = np.vstack((n_index, c_index))

    # remove distances smaller than a tolerance ~ 0. The small tolerance is
    # needed to correct for pymatgen's neighbor_list returning self atoms
    # in a few edge cases.
    nonzero = np.where(n_distance >= 1e-8)[0]
    edge_index = edge_index[:, nonzero]
    cell_offsets = offsets[nonzero]
    num_neighbors = len(nonzero)

    return edge_index, cell_offsets, num_neighbors, an_atoms.cell.array


class pbc_info_collector:
    def __init__(self, properties):
        self.R = []
        self.N = []
        self.Z = []
        self.properties = properties
        self.info_dict = {}
        for a_property in self.properties:
            self.info_dict.update({a_property: []})
        # for pbc
        self.neighbors = []
        self.cell = []
        self.edge_index = []
        self.cell_offsets = None

    def collect_row(self, a_row):
        for a_property in self.properties:
            old_list = self.info_dict[a_property]
            old_list.extend(a_row.data[a_property])
            self.info_dict[a_property] = old_list
        self.N.append(a_row.natoms)
        self.Z.extend(a_row.numbers)
        if len(self.R) == 0:
            self.R = a_row.positions
        else:
            self.R = np.vstack((self.R, a_row.positions))

    def collect_pbc_row(self, a_row: ase.db.core.AtomsRow):
        edge_index, cell_offsets, num_neighbors, cell = get_pbc_data(a_row=a_row)
        self.neighbors.append(num_neighbors)
        self.cell.append(cell)
        if len(self.edge_index) == 0:
            self.edge_index = edge_index
            self.cell_offsets = cell_offsets
        else:
            self.edge_index = np.hstack((self.edge_index, edge_index))
            self.cell_offsets = np.vstack((self.cell_offsets, cell_offsets))


def db_2_pbc_npz(db_path: str, properties: list, npz_path: str = None):
    a_info_clc = pbc_info_collector(properties)
    with connect(db_path) as db:
        for a_row in db.select():
            a_info_clc.collect_row(a_row)
            a_info_clc.collect_pbc_row(a_row)
    if not npz_path:
        npz_path = 'thuEMol.npz'
    np.savez(npz_path, Z=np.array(a_info_clc.Z),
             R=a_info_clc.R, N=np.array(a_info_clc.N),
             cell=np.array(a_info_clc.cell), neighbors=np.array(a_info_clc.neighbors),
             edge_index=a_info_clc.edge_index, cell_offsets=a_info_clc.cell_offsets,
             **a_info_clc.info_dict)


def db_2_pbc_pyG_data(db_path: str, properties: list, pyG_data_folder: str):
    cwd_ = os.getcwd()
    db_path = os.path.abspath(db_path)
    if os.path.exists(pyG_data_folder):
        shutil.rmtree(pyG_data_folder)
    os.makedirs(pyG_data_folder)
    os.chdir(pyG_data_folder)
    os.makedirs('raw')
    os.chdir('raw')
    db_2_pbc_npz(db_path=db_path, properties=properties, npz_path='thuEMol.npz')
    os.chdir(cwd_)


def get_pbc_distances(
        pos,
        edge_index,
        cell,
        cell_offsets,
        neighbors,
        return_offsets=False,
        return_distance_vec=False,
):
    import torch
    row, col = edge_index

    distance_vectors = pos[row] - pos[col]

    # correct for pbc
    neighbors = neighbors.to(cell.device)
    cell = torch.repeat_interleave(cell, neighbors, dim=0)
    offsets = cell_offsets.float().view(-1, 1, 3).bmm(cell.float()).view(-1, 3)
    distance_vectors += offsets

    # compute distances
    distances = distance_vectors.norm(dim=-1)

    # redundancy: remove zero distances
    nonzero_idx = torch.arange(len(distances), device=distances.device)[
        distances != 0
        ]
    edge_index = edge_index[:, nonzero_idx]
    distances = distances[nonzero_idx]

    out = {
        "edge_index": edge_index,
        "distances": distances,
    }

    if return_distance_vec:
        out["distance_vec"] = distance_vectors[nonzero_idx]

    if return_offsets:
        out["offsets"] = offsets[nonzero_idx]

    return out


def get_vol_from_file(file_path: str):
    with open(file_path, 'r') as f:
        for a_line in f.readlines():
            if a_line.startswith(' Molecular volume'):
                break
    vol = float(a_line.split(' Ang')[0].split(' ')[-1])
    return vol


def estimate_vol_with_multiwfn(multiwfn_path: str, multiwfn_inp_path: str):
    single_struct_path = os.path.abspath('single_struct.pdb')
    multiwfn_out_path = os.path.abspath('multiwfn_out.txt')
    os.system(f'{multiwfn_path} {single_struct_path}<{multiwfn_inp_path} > {multiwfn_out_path}')
    vol = get_vol_from_file(multiwfn_out_path)
    return vol


def check_packmol_out(file_path: str):
    flag = 0
    with open(file_path, 'r') as f:
        for a_line in f.readlines():
            if a_line.startswith('                                 Success'):
                flag = 1
    return flag


def edit_packmol_inp(old_inp_path: str, edge_length: float, pack_num: int):
    shutil.copy(src=old_inp_path, dst='temp.txt')
    with open('packmol_inp.txt', 'w') as f_w, open('temp.txt', 'r') as f_r:
        for a_line in f_r.readlines():
            if a_line.startswith('  number'):
                f_w.write(f'  number {str(pack_num)}\n')
            elif a_line.startswith('  inside cube'):
                f_w.write(f'  inside cube 0. 0. 0. {str(edge_length)}\n')
            else:
                f_w.write(a_line)


def get_box_with_packmol(vol: float, pack_num: int, packmol_path: str, packmol_inp_path: str,
                         default_enlarge_factor: float = 1.5, default_max_tolrance: int = 11):
    total_vol = vol * pack_num * default_enlarge_factor
    min_edge_length = total_vol ** (1 / 3)
    for tolerance in np.arange(0, default_max_tolrance):
        edge_length = min_edge_length + tolerance
        edit_packmol_inp(old_inp_path=packmol_inp_path,
                         pack_num=pack_num, edge_length=edge_length)
        os.system(f'{packmol_path} < packmol_inp.txt > packmol_out.txt')
        flag = check_packmol_out('packmol_out.txt')
        if flag == 0:
            os.remove('packmol_inp.txt')
            os.remove('packmol_out.txt')
        else:
            break
    if flag == 0:
        raise RuntimeError('Packmol exceeds max tolrance.')
    else:
        print(tolerance)
        print(edge_length)


def db_2_pdb_pipeline(db_path: str, workbase: str, dump_root: str,
                      multiwfn_path: str, multiwfn_inp_path: str,
                      multiwfn_ini_path: str,
                      packmol_path: str, packmol_inp_path: str, pack_num: int,
                      default_enlarge_factor: float = 1.5,
                      default_max_tolrance: int = 11):
    new_path_list = []
    for a_path in [db_path, workbase, packmol_path, packmol_inp_path, multiwfn_path, multiwfn_inp_path, dump_root, multiwfn_ini_path]:
        new_path_list.append(os.path.abspath(a_path))
    db_path, workbase, packmol_path, packmol_inp_path, multiwfn_path, multiwfn_inp_path, dump_root, multiwfn_ini_path = new_path_list
    os.makedirs(workbase, exist_ok=True)
    os.makedirs(dump_root, exist_ok=True)
    cwd_ = os.getcwd()
    with connect(db_path) as db:
        for a_row in db.select():
            an_ep_id = a_row.ep_id
            os.chdir(workbase)
            os.makedirs(str(an_ep_id))
            os.chdir(str(an_ep_id))
            an_atoms = a_row.toatoms()
            write_proteindatabank('single_struct.pdb', an_atoms)
            shutil.copy(src=multiwfn_ini_path, dst='settings.ini')
            try:
                vol = estimate_vol_with_multiwfn(multiwfn_path=multiwfn_path, multiwfn_inp_path=multiwfn_inp_path)
            except Exception as e:
                print(e)
                print(os.getcwd())
                continue
            try:
                get_box_with_packmol(vol=vol, pack_num=pack_num,
                                     packmol_path=packmol_path, packmol_inp_path=packmol_inp_path)
            except Exception as e:
                print(e)
                print(os.getcwd())
                continue
            shutil.copy(src=r'packed_struct.pdb', dst=os.path.join(dump_root, f'{str(an_ep_id)}.pdb'))
            os.remove('settings.ini')
    os.chdir(cwd_)

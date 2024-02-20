# Copyright AISI
import os

import numpy as np
from ase import Atoms
from collections import Counter
from ase.db import connect
from ase.data import chemical_symbols
from uni_electrolyte.evaluator.dataset.data_transform import split_db_2_train_valid_test, edit_ase_db


class edm_info_collector:
    def __init__(self, properties, max_natoms):
        self.max_natoms = max_natoms
        self.R = []
        self.N = []
        self.Z = []
        self.properties = properties
        self.info_dict = {}
        for a_property in self.properties:
            self.info_dict.update({a_property: []})

    def collect_row(self, a_row):
        for a_property in self.properties:
            old_list = self.info_dict[a_property]
            old_list.extend(a_row.data[a_property])
            self.info_dict[a_property] = old_list
        self.N.append(a_row.natoms)
        a_charge = a_row.numbers
        a_charge = np.pad(a_charge, (0, self.max_natoms - len(a_charge)), mode='constant')
        self.Z.append(a_charge)
        a_pos = a_row.positions
        a_pos = np.pad(a_pos, ((0, self.max_natoms - a_pos.shape[0]), (0, 0)), mode='constant').reshape((1, -1, 3))
        if len(self.N) == 1:
            self.R = a_pos
        else:
            self.R = np.vstack((self.R, a_pos))


def db_2_edm_npz(db_path: str, properties: list, npz_path: str = None, max_natoms: int = 30):
    a_info_clc = edm_info_collector(properties, max_natoms)
    with connect(db_path) as db:
        for a_row in db.select():
            a_info_clc.collect_row(a_row)
    if not npz_path:
        npz_path = 'thuEMol.npz'
    np.savez(npz_path, charges=np.array(a_info_clc.Z),
             positions=a_info_clc.R, num_atoms=np.array(a_info_clc.N),
             **a_info_clc.info_dict)


def get_edm_info(db_path: str):
    n_atoms_list = []
    atoms_type_list = []
    with connect(db_path) as db:
        for a_row in db.select():
            n_atoms_list.append(a_row.natoms)
            atoms_type_list.extend(a_row.numbers)
    n_atoms_counts = Counter(n_atoms_list)
    n_atoms_counts_info = {key: value for key, value in n_atoms_counts.items()}
    atoms_type_counts = Counter(atoms_type_list)
    atoms_type_counts_info = {key: value for key, value in atoms_type_counts.items()}
    return n_atoms_counts_info, atoms_type_counts_info


def update_edm_info(template: dict, n_atoms_counts_info: dict, atoms_type_counts_info: dict):
    symbol_list = []
    index_list = sorted(list(atoms_type_counts_info.keys()))
    atoms_type_counts_list = []
    for a_number in index_list:
        symbol_list.append(chemical_symbols[a_number])
        # index_list.append(idx)
        atoms_type_counts_list.append(atoms_type_counts_info[a_number])
    template['atom_encoder'] = dict(zip(symbol_list, index_list))
    template['atom_decoder'] = symbol_list
    template['n_nodes'] = n_atoms_counts_info
    template['atom_types'] = dict(zip(index_list, atoms_type_counts_list))
    template['max_n_nodes'] = max(n_atoms_counts_info.keys())
    max_col_list = ['#FFFFFF99', 'C7', 'C3', 'C1', 'C5',
                   'C6', 'C4', 'C8', 'C9', 'C10',
                   'C11', 'C12', 'C13', 'C14']
    max_radius_list = [0.3, 0.6, 0.6, 0.6, 0.6,
                   0.6, 0.6, 0.6, 0.6, 0.6,
                   0.6, 0.6, 0.6, 0.6, 0.6,
                   0.6]
    template['colors_dic'] = max_col_list[:len(index_list)]
    template['radius_dic'] = max_radius_list[:len(index_list)]
    return template


def db_2_edm_data_pipeline(old_db_path: str, properties: list, output_dir: str,
                                num_train: int, num_valid: int):
    from learn_edm.configs.datasets_config import get_dataset_info
    template = get_dataset_info('thu_5w', False)
    cwd_ = os.getcwd()
    output_dir = os.path.abspath(output_dir)
    old_db_path = os.path.abspath(old_db_path)
    if os.path.exists(output_dir):
        print('Use previous data.')
        os.chdir(output_dir)
        n_atoms_counts_info, atoms_type_counts_info = get_edm_info('./db/train.db')
    else:
        print('Preparing EDM data.')
        os.makedirs(output_dir)
        os.chdir(output_dir)
        split_db_2_train_valid_test(old_db_path=old_db_path, properties=properties, output_db_dir='./db',
                                    num_train=num_train, num_valid=num_valid)
        os.makedirs('./qm9')
        n_atoms_counts_info, atoms_type_counts_info = get_edm_info('./db/train.db')
        db_2_edm_npz(db_path='./db/train.db', npz_path='./qm9/train.npz',
                     max_natoms=max(n_atoms_counts_info.keys()), properties=properties)
        valid_n_atoms_counts_info, _ = get_edm_info('./db/valid.db')
        db_2_edm_npz(db_path='./db/valid.db', npz_path='./qm9/valid.npz',
                     max_natoms=max(valid_n_atoms_counts_info.keys()), properties=properties)
        test_n_atoms_counts_info, _ = get_edm_info('./db/test.db')
        db_2_edm_npz(db_path='./db/test.db', npz_path='./qm9/test.npz',
                     max_natoms=max(test_n_atoms_counts_info.keys()), properties=properties)
        print('EDM data preparation done.')
    new_template = update_edm_info(template=template, n_atoms_counts_info=n_atoms_counts_info,
                                       atoms_type_counts_info=atoms_type_counts_info)
    os.chdir(cwd_)
    return new_template


def edm_npz_2_db(npz_path: str, db_path: str, properties_name_list: list):
    src_info = np.load(npz_path)
    src_charges = src_info['charges']
    src_positions = src_info['positions']
    edm_id = src_info['index']
    src_num_atoms = src_info['num_atoms']

    with connect(db_path) as dump_db:
        for idx, an_id in enumerate(edm_id):
            a_num_atoms = src_num_atoms[idx]
            a_pos = src_positions[idx]
            a_charges = src_charges[idx]
            an_atoms = Atoms(numbers=a_charges[:a_num_atoms], positions=a_pos[:a_num_atoms])
            a_properties_list = []
            for a_property_name in properties_name_list:
                a_properties_list.append(float(src_info[a_property_name][idx]))
            data = dict(zip(properties_name_list, a_properties_list))
            dump_db.write(atoms=an_atoms, data=data, edm_id=an_id)
    edit_ase_db(db_path=db_path, properties=properties_name_list)


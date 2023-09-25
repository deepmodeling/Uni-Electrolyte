# Copyright AISI
import csv
import os
import shutil

import rdkit
import ase
from ase.atom import Atom
from ase.atoms import Atoms
from ase.db import connect
# from typing import List
from ase.io import read, write
from rdkit import Chem
from rdkit import Geometry
from rdkit.Chem import AllChem
from rdkit.Chem import rdMolAlign
from rdkit.Chem import rdmolfiles
import numpy as np



def mol_2_atom(mol: rdkit.Chem.rdchem.Mol):
    conf = mol.GetConformer()
    an_atoms = Atoms()
    for i in range(conf.GetNumAtoms()):
        position = conf.GetAtomPosition(i)
        atom = mol.GetAtoms()[i]
        a_symbol = atom.GetSymbol()
        an_new_atom = Atom(symbol=a_symbol, position=(position.x, position.y, position.z))
        an_atoms.append(an_new_atom)
    return an_atoms

def atom_2_mol(an_atoms: ase.atoms.Atoms):
    write(filename='temp.xyz', images=an_atoms)
    a_mol = rdmolfiles.MolFromXYZFile('temp.xyz')
    os.remove('temp.xyz')
    return a_mol


def edit_ase_db(db_path, properties: list):
    with connect(db_path) as db:
        meta = db.metadata
        if not "_distance_unit" in meta.keys():
            meta["_distance_unit"] = 'Ang'
        if not "_property_unit_dict" in meta.keys():
            tmp_dict = {}
            for property in properties:
                tmp_dict.update({property: "Hartree"})
            meta["_property_unit_dict"] = tmp_dict
        if "atomrefs" not in meta.keys():
            meta["atomrefs"] = {}
        db.metadata = meta


def xyz_2_db(xyz_path: str, db_path: str, properties: list, has_identity: bool=None):
    with connect(db_path) as db_w:
        for an_atoms in read(xyz_path, index=':'):
            data = {}
            for property in properties:
                data.update({property: [0]})
            if has_identity:
                for an_id in an_atoms.info.keys():
                    an_id = int(an_id)
                    break
                db_w.write(an_atoms, data=data, identity=an_id)
            else:
                db_w.write(an_atoms, data=data)
    edit_ase_db(db_path=db_path, properties=properties)


def get_atoms_from_coords(file_path: str, key_word: str):
    flag = 0
    new_atoms = Atoms()
    key_word = ' "' + key_word
    with open(file_path) as f:
        for a_line in f.readlines():
            if a_line.startswith(f'{key_word}'):
                flag = 1
                continue
            if a_line.startswith(' ],') and flag == 1:
                break
            if a_line.startswith(' ]') and flag == 1:
                break
            if flag == 1:
                atoms_info = a_line.split('"')[1].split()
                an_atom = Atom(symbol=atoms_info[0],
                               position=(float(atoms_info[1]), float(atoms_info[2]), float(atoms_info[3])))
                new_atoms.append(an_atom)
    return new_atoms


def thu_crood_2_db(crood_folder_path: str, db_path: str, properties: list, key_word: str):
    cwd_ = os.getcwd()
    crood_folder_path = os.path.abspath(crood_folder_path)
    with connect(db_path) as db_w:
        for a_file in os.listdir(crood_folder_path):
            os.chdir(crood_folder_path)
            ep_id = int(a_file.split('_')[0].split('-')[-1])
            an_atoms = get_atoms_from_coords(file_path=a_file, key_word=key_word)
            data = {}
            for property in properties:
                data.update({property: [0]})
            db_w.write(an_atoms, data=data, identity=ep_id)
    os.chdir(cwd_)
    edit_ase_db(db_path=db_path, properties=properties)


def change_db_prop_from_csv(csv_path: str, db_path: str, properties: list, csv_id_idx: int):
    csv_reader = csv.reader(open(csv_path))
    with connect('dummy_csv.db') as db, connect(db_path) as db_change:
        for i, row in enumerate(csv_reader):
            if i == 0:
                idx_list = []
                for property in properties:
                    flag = 0
                    for row_idx, a_row_property in enumerate(row):
                        if property == a_row_property:
                            idx_list.append(row_idx)
                            flag = 1
                            break
                    if flag == 0:
                        raise RuntimeError(f'Property {property} has not been found in csv file.')
                property_idx_dict = dict(zip(properties, idx_list))
                continue
            data = {}
            for property in properties:
                data.update({property: [float(row[property_idx_dict[property]])]})
            an_id = int(row[csv_id_idx].split('-')[-1])
            db.write(data=data, identity=an_id, atoms=Atoms())
        for a_row in db_change.select():
            new_data = db.get(identity=a_row.identity).data
            id = db.get(identity=a_row.identity).id
            db_change.update(id, data=new_data)
    os.remove('dummy_csv.db')


def smile_2_db(smile_path: str, db_path: str, fail_smile_path: str, properties: list):
    print('Each row corresponds to a smile by default.')
    real_count = 0
    fail_count = 0
    with connect(db_path) as db, open(smile_path, 'r') as smi_r:
        for i, a_line in enumerate(smi_r.readlines()):
            a_smile = a_line.strip()
            if a_smile == '':
                print('An empty line is detected.')
                continue
            try:
                a_mol = Chem.MolFromSmiles(a_smile)
                a_mol_with_H = Chem.AddHs(a_mol)
                AllChem.EmbedMolecule(a_mol_with_H, useRandomCoords=True, maxAttempts=1000000)
                AllChem.MMFFOptimizeMolecule(a_mol_with_H)
                an_atoms = mol_2_atom(mol=a_mol_with_H)
                data = {}
                for property in properties:
                    data.update({property: [0]})
                db.write(atoms=an_atoms, data=data, smile=a_smile)
                real_count = real_count + 1
            except Exception as e:
                print(e)
                fail_count = fail_count + 1
                print(f'real: {real_count}')
                print(f'fail: {fail_count}')
                with open(fail_smile_path, 'a') as f_f:
                    f_f.write(a_smile)
                    f_f.write('\n')
    edit_ase_db(db_path=db_path, properties=properties)


def csv_2_db(csv_path: str, db_path: str, fail_smile_path: str, properties: list, smile_idx: int):
    real_count = 0
    fail_count = 0
    csv_reader = csv.reader(open(csv_path))
    with connect(db_path) as db:
        for i, row in enumerate(csv_reader):
            if i == 0:
                idx_list = []
                for property in properties:
                    flag = 0
                    for row_idx, a_row_property in enumerate(row):
                        if property == a_row_property:
                            idx_list.append(row_idx)
                            flag = 1
                            break
                    if flag == 0:
                        raise RuntimeError(f'Property {property} has not been found in csv file.')
                property_idx_dict = dict(zip(properties, idx_list))
                continue
            a_smile = row[smile_idx]
            try:
                a_mol = Chem.MolFromSmiles(a_smile)
                a_mol_with_H = Chem.AddHs(a_mol)
                AllChem.EmbedMolecule(a_mol_with_H, useRandomCoords=True, maxAttempts=1000000)
                AllChem.MMFFOptimizeMolecule(a_mol_with_H)
                an_atoms = mol_2_atom(mol=a_mol_with_H)
                data = {}
                for property in properties:
                    data.update({property: [float(row[property_idx_dict[property]])]})
                db.write(atoms=an_atoms, data=data, smile=a_smile)
                real_count = real_count + 1
            except Exception as e:
                print(e)
                fail_count = fail_count + 1
                print(f'real: {real_count}')
                print(f'fail: {fail_count}')
                with open(fail_smile_path, 'a') as f_f:
                    f_f.write(a_smile)
                    f_f.write('\n')
    edit_ase_db(db_path=db_path, properties=properties)


class info_collector:
    def __init__(self, properties):
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
        self.Z.extend(a_row.numbers)
        if len(self.N) == 1:
            self.R = a_row.positions
        else:
            self.R = np.vstack((self.R, a_row.positions))


def db_2_npz(db_path: str, properties: list, npz_path: str = None):
    a_info_clc = info_collector(properties)
    with connect(db_path) as db:
        for a_row in db.select():
            a_info_clc.collect_row(a_row)
    if not npz_path:
        npz_path = 'thuEMol.npz'
    np.savez(npz_path, Z=np.array(a_info_clc.Z),
             R=a_info_clc.R, N=np.array(a_info_clc.N),
             **a_info_clc.info_dict)


def db_2_pyG_data(db_path: str, properties: list, pyG_data_folder: str):
    cwd_ = os.getcwd()
    db_path = os.path.abspath(db_path)
    if os.path.exists(pyG_data_folder):
        shutil.rmtree(pyG_data_folder)
    os.makedirs(pyG_data_folder)
    os.chdir(pyG_data_folder)
    os.makedirs('raw')
    os.chdir('raw')
    db_2_npz(db_path=db_path, properties=properties, npz_path='thuEMol.npz')
    os.chdir(cwd_)

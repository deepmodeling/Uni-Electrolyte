#registry.dp.tech/dptech/prod-17396/sub:20240919
#(改变明康生成模型的推断，过滤不合适结果)
#/opt/uni_electrolyte/src/uni_electrolyte/evaluator/dataset/data_transform.py

# Copyright AISI
import json
import contextlib
import csv
import io
import os
import random
import shutil
from collections import Counter
from collections import deque

import ase
import matplotlib.pyplot as plt
import numpy as np
import rdkit
import seaborn as sns
from ase.atom import Atom
from ase.atoms import Atoms
from ase.data import covalent_radii
from ase.db import connect
# from typing import List
from ase.io import read, write
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.rdDetermineBonds import DetermineBonds
from rdkit.rdBase import WrapLogs


def smiles_2_xyz(smiles: str, output_file_path: str):
    # Create a molecule from the SMILES string
    mol = Chem.MolFromSmiles(smiles)

    # Add hydrogen atoms
    mol = Chem.AddHs(mol)

    # Generate a 3D conformation
    AllChem.EmbedMolecule(mol)

    # Optimize the geometry
    AllChem.MMFFOptimizeMolecule(mol)

    # Get the atomic positions
    conf = mol.GetConformer()
    atoms = [conf.GetAtomPosition(i) for i in range(mol.GetNumAtoms())]

    # Write the XYZ file
    xyz_content = f'{mol.GetNumAtoms()}\n\n'
    for atom, pos in zip(mol.GetAtoms(), atoms):
        symbol = atom.GetSymbol()
        x, y, z = pos
        xyz_content += f'{symbol} {x:10.6f} {y:10.6f} {z:10.6f}\n'
    with open(output_file_path, 'w') as f:
        f.write(xyz_content)


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
    raw_mol = Chem.MolFromXYZFile('temp.xyz')
    mol = Chem.Mol(raw_mol)
    DetermineBonds(mol, useHueckel=True)
    os.remove('temp.xyz')
    return mol


def atom_2_smile(an_atoms: ase.atoms.Atoms):
    a_mol = atom_2_mol(an_atoms)
    a_mol = Chem.RemoveHs(a_mol)
    a_smile = Chem.MolToSmiles(a_mol, isomericSmiles=False)
    return a_smile


def smile_2_atom(smile: str, maxAttempts: int=1000000):
    a_mol = Chem.MolFromSmiles(smile)
    a_mol_with_H = Chem.AddHs(a_mol)
    AllChem.EmbedMolecule(a_mol_with_H, useRandomCoords=True, maxAttempts=maxAttempts)
    AllChem.MMFFOptimizeMolecule(a_mol_with_H)
    an_atoms = mol_2_atom(mol=a_mol_with_H)
    return an_atoms


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


def has_benzene_ring(smiles):
    # 解析SMILES表示法
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        # 生成分子的拓扑图
        Chem.AssignStereochemistry(mol, force=True, cleanIt=True)
        Chem.AssignAtomChiralTagsFromStructure(mol, -1)
        # 检查分子中是否包含苯环
        ssr = Chem.GetSymmSSSR(mol)
        for ring in ssr:
            if len(ring) == 6:
                # 检查环的原子是否都是碳原子
                if all(mol.GetAtomWithIdx(atom).GetAtomicNum() == 6 for atom in ring):
                    if all(mol.GetAtomWithIdx(atom).GetIsAromatic() for atom in ring):
                        return True
    return False


def has_OO_or_OH_bond(smiles):
    mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)
    flag_OO, flag_OH = False, False
    for bond in mol.GetBonds():
        atom1 = bond.GetBeginAtom()
        atom2 = bond.GetEndAtom()
        if atom1.GetAtomicNum() == 8 and atom2.GetAtomicNum() == 8:
            flag_OO = True  # 存在氧原子之间的键
        if (atom1.GetAtomicNum() == 8 and atom2.GetAtomicNum() == 1) or \
           (atom1.GetAtomicNum() == 1 and atom2.GetAtomicNum() == 8):
            flag_OH = True  # 存在氧原子和氢原子之间的键
    return flag_OO, flag_OH


def cas_to_smiles(cas_id):
    import pubchempy as pcp

    compound = pcp.get_compounds(cas_id, 'name')[0]
    return compound.canonical_smiles

def get_substructure_cas(smiles, return_first: bool = True):
    import pubchempy as pcp
    import re

    cas_rns = []
    results = pcp.get_synonyms(smiles, 'smiles')
    for result in results:
        for syn in result.get('Synonym', []):
            match = re.match('(\d{2,7}-\d\d-\d)', syn)
            if match and return_first:
                return match.group(1)
                cas_rns.append(match.group(1))
    return cas_rns


def xyz_2_db(xyz_path: str, db_path: str, properties: list, has_identity: bool = None):
    with connect(db_path) as db_w:
        for an_atoms in read(xyz_path, index=':'):
            a_mol = atom_2_mol(an_atoms)
            a_mol = Chem.RemoveHs(a_mol)
            a_smile = Chem.MolToSmiles(a_mol)
            data = {}
            for property in properties:
                data.update({property: [0]})
            if has_identity:
                for an_id in an_atoms.info.keys():
                    an_id = int(an_id)
                    break
                db_w.write(an_atoms, data=data, identity=an_id, smile=a_smile)
            else:
                db_w.write(an_atoms, data=data, smile=a_smile)
    edit_ase_db(db_path=db_path, properties=properties)

def xyz_folder_2_db(xyz_folder_path: str, db_path: str, properties: list, has_identity: bool = None):
    with connect(db_path) as db_w:
        for a_xyz_file in os.listdir(xyz_folder_path):
            an_atoms = read(os.path.join(xyz_folder_path, a_xyz_file))
            a_mol = atom_2_mol(an_atoms)
            a_mol = Chem.RemoveHs(a_mol)
            a_smile = Chem.MolToSmiles(a_mol)
            data = {}
            for property in properties:
                data.update({property: [0]})
            if has_identity:
                file_name = os.path.splitext(a_xyz_file)[0]
                an_id = int(file_name.split('-')[-1])
                db_w.write(an_atoms, data=data, identity=an_id, smile=a_smile)
            else:
                db_w.write(an_atoms, data=data, smile=a_smile)
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
                if property in ['dielectric_constant', 'viscosity']:
                    data.update({property: [np.log10(float(row[property_idx_dict[property]]))]})
                else:
                    data.update({property: [float(row[property_idx_dict[property]])]})
            an_id = int(row[csv_id_idx].split('-')[-1])
            db.write(data=data, identity=an_id, atoms=Atoms())
        for a_row in db_change.select():
            new_data = db.get(identity=a_row.identity).data
            db_change.update(a_row.id, data=new_data)
    os.remove('dummy_csv.db')


def smile_2_db(smile_path: str, db_path: str, fail_smile_path: str, properties: list, maxAttempts: int=1000000):
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
                an_atoms = smile_2_atom(smile=a_smile, maxAttempts=maxAttempts)
                data = {}
                for property in properties:
                    data.update({property: [0]})
                db.write(atoms=an_atoms, data=data, smile=a_smile)
                real_count = real_count + 1
            except Exception as e:
                print(e)
                fail_count = fail_count + 1
                with open(fail_smile_path, 'a') as f_f:
                    f_f.write(a_smile)
                    f_f.write('\n')
    print(f'real: {real_count}')
    print(f'fail: {fail_count}')
    edit_ase_db(db_path=db_path, properties=properties)


def get_smiles_from_db(db_path: str, smile_file_path: str):
    with open(smile_file_path, 'w') as f_w, connect(db_path) as db:
        for a_row in db.select():
            f_w.write(a_row.smile)
            f_w.write('\n')


def smile_to_inchi(smile):
    mol = Chem.MolFromSmiles(smile)
    inchi = Chem.MolToInchi(mol)
    return inchi


def smile_to_maccs_fp_arr(smiles):
    mol = Chem.MolFromSmiles(smiles)
    fingerprint = AllChem.GetMACCSKeysFingerprint(mol)
    fingerprint_array = np.array(list(fingerprint.ToBitString())).astype(int)
    return fingerprint_array


def get_csv_from_db(db_path: str, csv_path: str, decorated_property_names: dict):
    import pandas as pd
    target_list = list(decorated_property_names.keys())
    info_dict = {}
    for a_target in target_list:
        a_info_list = []
        with connect(db_path) as db:
            for a_row in db.select():
                a_info_list.append(a_row.data[a_target][0])
        info_dict.update({a_target: a_info_list})
    smile_list = []
    with connect(db_path) as db:
        for a_row in db.select():
            smile_list.append(a_row.smile)
    info_dict.update({'Smiles': smile_list})
    info_df = pd.DataFrame(info_dict)
    info_df = info_df.rename(columns=decorated_property_names)
    info_df.to_csv(csv_path, index=False)


def csv_2_db(csv_path: str, db_path: str, fail_smile_path: str, properties: list, smile_idx: int,output_csv_path:str=None):
    real_count = 0
    fail_count = 0
    csv_reader = csv.reader(open(csv_path))

    if output_csv_path is not None:
        fp_out_csv = open(output_csv_path,'w')
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
                if output_csv_path is not None:
                    fp_out_csv.write(','.join(row))
                continue
            a_smile = row[smile_idx]
            try:
                an_atoms = smile_2_atom(smile=a_smile)
                data = {}
                for property in properties:
                    data.update({property: [float(row[property_idx_dict[property]])]})
                db.write(atoms=an_atoms, data=data, smile=a_smile)
                real_count = real_count + 1
                if output_csv_path is not None:
                    fp_out_csv.write(','.join(row))
            except Exception as e:
                print(e)
                fail_count = fail_count + 1
                print(f'real: {real_count}')
                print(f'fail: {fail_count}')
                with open(fail_smile_path, 'a') as f_f:
                    f_f.write(a_smile)
                    f_f.write('\n')
    edit_ase_db(db_path=db_path, properties=properties)
    if output_csv_path is not None:
        fp_out_csv.close()


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


def split_db(old_db_path: str, new_db_path_1: str, new_db_path_2: str, num_db_2: int, properties: list):
    id_list = []
    with connect(old_db_path) as db:
        for a_row in db.select():
            id_list.append(a_row.id)
    random.shuffle(id_list)
    with connect(old_db_path) as src_db, connect(new_db_path_1) as new_db_1, connect(new_db_path_2) as new_db_2:
        for a_row in src_db.select():
            an_atoms = a_row.toatoms()
            if a_row.id in id_list[-num_db_2:]:
                new_db_2.write(atoms=an_atoms, data=a_row.data)
            else:
                new_db_1.write(atoms=an_atoms, data=a_row.data)
    edit_ase_db(db_path=new_db_path_2, properties=properties)
    edit_ase_db(db_path=new_db_path_1, properties=properties)


def split_db_2_train_valid_test(old_db_path: str, properties: list, output_db_dir: str,
                                num_train: int, num_valid: int):
    cwd_ = os.getcwd()
    id_list = []
    with connect(old_db_path) as db:
        for a_row in db.select():
            id_list.append(a_row.id)
    random.shuffle(id_list)
    old_db_path = os.path.abspath(old_db_path)
    os.makedirs(output_db_dir, exist_ok=True)
    os.chdir(output_db_dir)
    with connect(old_db_path) as src_db, connect('train.db') as db_1:
        for a_row in src_db.select():
            an_atoms = a_row.toatoms()
            if a_row.id in id_list[:num_train]:
                db_1.write(atoms=an_atoms, data=a_row.data)
    with connect(old_db_path) as src_db, connect('valid.db') as db_2:
        for a_row in src_db.select():
            an_atoms = a_row.toatoms()
            if a_row.id in id_list[num_train:num_valid + num_train]:
                db_2.write(atoms=an_atoms, data=a_row.data)
    with connect(old_db_path) as src_db, connect('test.db') as db_3:
        for a_row in src_db.select():
            an_atoms = a_row.toatoms()
            if a_row.id in id_list[num_valid + num_train:]:
                db_3.write(atoms=an_atoms, data=a_row.data)
    edit_ase_db(db_path='train.db', properties=properties)
    edit_ase_db(db_path='test.db', properties=properties)
    edit_ase_db(db_path='valid.db', properties=properties)
    os.chdir(cwd_)


def stack_info_clc_unit(info_clc_unit: info_collector, full_info_clc: info_collector):
    if len(full_info_clc.N) == 0:
        full_info_clc = info_clc_unit
    else:
        full_info_clc.Z.extend(info_clc_unit.Z)
        full_info_clc.N.extend(info_clc_unit.N)
        full_info_clc.R = np.vstack((full_info_clc.R, info_clc_unit.R))
        for a_property in info_clc_unit.properties:
            old_list = full_info_clc.info_dict[a_property]
            old_list.extend(info_clc_unit.info_dict[a_property])
            full_info_clc.info_dict[a_property] = old_list
    return full_info_clc


def db_2_npz(db_path: str, properties: list, npz_path: str = None, max_unit_len: int = 10000):
    full_info_clc = info_collector(properties)
    info_clc_unit = info_collector(properties)
    with connect(db_path) as db:
        for idx, a_row in enumerate(db.select()):
            info_clc_unit.collect_row(a_row)
            if (idx + 1) % max_unit_len == 0:
                full_info_clc = stack_info_clc_unit(info_clc_unit=info_clc_unit, full_info_clc=full_info_clc)
                info_clc_unit = info_collector(properties)
        # append last epoch
        if (idx + 1) % max_unit_len != 0:
            full_info_clc = stack_info_clc_unit(info_clc_unit=info_clc_unit, full_info_clc=full_info_clc)
    if not npz_path:
        npz_path = 'thuEMol.npz'
    np.savez(npz_path, Z=np.array(full_info_clc.Z),
             R=full_info_clc.R, N=np.array(full_info_clc.N),
             **full_info_clc.info_dict)


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


def change_db_property(db_path: str, enlarge: bool = True):
    with connect(db_path) as db:
        for a_row in db.select():
            identity = a_row.identity
            old_vs = a_row.data['viscosity'][0]
            old_dc = a_row.data['dielectric_constant'][0]
            if enlarge:
                new_dc = pow(10, old_dc)
                new_vs = pow(10, old_vs)
            else:
                new_dc = np.log10(old_dc)
                new_vs = np.log10(old_vs)
            old_data = a_row.data
            old_data['viscosity'] = [new_vs]
            old_data['dielectric_constant'] = [new_dc]
            db.update(a_row.id, data=old_data)


def change_pyg_property(old_npz_path: str, new_npz_path: str, enlarge: bool = True):
    info = np.load(old_npz_path, allow_pickle=True)
    info = dict(info)
    old_vs = info['viscosity']
    old_dc = info['dielectric_constant']
    if enlarge:
        new_vs = np.power(old_vs, 10)
        new_dc = np.power(old_dc, 10)
    else:
        new_vs = np.log10(old_vs)
        new_dc = np.log10(old_dc)
    info['viscosity'] = new_vs
    info['dielectric_constant'] = new_dc
    np.savez(new_npz_path, **info)


def check_topo_unit(an_atoms: ase.atoms.Atoms,
                    placement_cutoff: float = 1.7,
                    covalent_radius_factor: float = 1.1,
                    cluster_tolerance: float = 0.5):
    from schnetpack_gschnet.transform.neighborlist import msp_neighbor_list

    n_atoms = len(an_atoms.numbers)
    if n_atoms < 2:
        return 5
    try:
        new_cell = np.ptp(an_atoms.positions, axis=0) + 0.1
        # set cell and center
        an_atoms.set_cell(new_cell, scale_atoms=False)
        an_atoms.center()
    except:
        an_atoms.set_cell([1.0, 1.0, 1.0], scale_atoms=False)

    # compute neighborhood
    _idx_i, _idx_j, _r_ij = msp_neighbor_list("ijd", an_atoms, placement_cutoff)

    # check cluster
    cluster = np.nonzero(_r_ij <= cluster_tolerance)[0]
    if len(cluster) > 0:
        return 3

    # here we use covalent radii to add additional bonds
    thresh = (
            covalent_radii[an_atoms.numbers[_idx_i]] + covalent_radii[an_atoms.numbers[_idx_j]]
    )
    idcs = np.nonzero(_r_ij <= (thresh * covalent_radius_factor))[0]
    _idx_i = _idx_i[idcs]
    _idx_j = _idx_j[idcs]

    # check if there are atoms without neighbors, i.e. disconnected atoms
    n_nbh = np.bincount(_idx_i, minlength=n_atoms)
    if np.count_nonzero(n_nbh == 0) > 0:
        return 2
    # store where the neighbors in _idx_j of each center atom in _idx_i start
    # assuming that _idx_i is ordered
    start_idcs = np.empty(n_nbh.size + 1, dtype=int)
    start_idcs[0] = 0
    start_idcs[1:] = np.cumsum(n_nbh)
    # check connectivity of atoms given the neighbor list
    unseen = np.ones(n_atoms, dtype=bool)
    unseen[0] = False
    count = 1
    queue = deque([0])
    while queue and count < n_atoms:
        atom = queue.popleft()
        neighbors = _idx_j[start_idcs[atom]: start_idcs[atom + 1]]
        for neighbor in neighbors:
            if unseen[neighbor]:
                unseen[neighbor] = False
                count += 1
                queue.append(neighbor)
    if count == n_atoms:
        return 0
    else:
        return 1


def get_inchi_smiles_unit(an_atoms: ase.atoms.Atoms):
    # Capture warnings
    f = io.StringIO()
    with contextlib.redirect_stderr(f):
        try:
            a_mol = atom_2_mol(an_atoms)
        except:
            return 4, None, None
        a_mol = Chem.RemoveHs(a_mol)
        an_inchi = Chem.MolToInchi(a_mol)
        a_smile = Chem.MolToSmiles(a_mol)
    output = f.getvalue()
    if len(output) > 0:
        return 4, None, None
    else:

        return 0, an_inchi, a_smile



def has_carbon_carbon_double_bond(mol):
    """
    判断给定的分子对象是否包含碳碳双键。

    参数:
    mol : rdkit.Chem.Mol
        分子对象。

    返回:
    bool
        如果分子中存在碳碳双键，则返回True；否则返回False。
    """
    for bond in mol.GetBonds():
        if bond.GetBondType() == Chem.BondType.DOUBLE:
            begin_atom = bond.GetBeginAtom()
            end_atom = bond.GetEndAtom()
            if begin_atom.GetAtomicNum() == 6 and end_atom.GetAtomicNum() == 6:
                return True
    return False
def has_carbon_carbon_triple_bond(mol):
    """
    判断给定的分子对象是否包含碳碳三键。

    参数:
    mol : rdkit.Chem.Mol
        分子对象。

    返回:
    bool
        如果分子中存在碳碳三键，则返回True；否则返回False。
    """
    for bond in mol.GetBonds():
        if bond.GetBondType() == Chem.BondType.TRIPLE:
            begin_atom = bond.GetBeginAtom()
            end_atom = bond.GetEndAtom()
            if begin_atom.GetAtomicNum() == 6 and end_atom.GetAtomicNum() == 6:
                return True
    return False

def has_three_membered_ring(mol):
    """
    判断给定的分子对象是否包含三元环和4元环。

    参数:
    mol : rdkit.Chem.Mol
        分子对象。

    返回:
    bool
        如果分子中存在三元环，则返回True；否则返回False。
    """
    ring_info = mol.GetRingInfo()
    for ring_atoms in ring_info.AtomRings():
        if len(ring_atoms) == 3 :
            return True
    return False

def has_4_membered_ring(mol):
    """
    判断给定的分子对象是否包含三元环和4元环。

    参数:
    mol : rdkit.Chem.Mol
        分子对象。

    返回:
    bool
        如果分子中存在4元环，则返回True；否则返回False。
    """
    ring_info = mol.GetRingInfo()
    for ring_atoms in ring_info.AtomRings():
        if  len(ring_atoms) == 4:
            return True
    return False

def has_bridged_rings(mol):
    """
    判断给定的分子对象是否包含桥环结构。

    参数:
    mol : rdkit.Chem.Mol
        分子对象。

    返回:
    bool
        如果分子中存在桥环结构，则返回True；否则返回False。
    """
    ring_info = mol.GetRingInfo()
    atom_rings = ring_info.AtomRings()

    for i,ring_i in enumerate(atom_rings):
        for j,ring_j in enumerate(atom_rings):
            if i>j:
                tmp=len(set(ring_i) & set(ring_j))
                if tmp==0: # 两个环没有公共原子
                    pass
                elif tmp==2:# 两个环有2个公共原子
                    pass
                elif tmp==1: # 两个环有1个公共原子
                    pass
                else:
                    return True
    return False

def has_CHO(mol):
    CHO_smarts = 'C(=O)[H]'
    CHO_pattern = Chem.MolFromSmarts(CHO_smarts)
    mol_=AllChem.AddHs(mol)
    if mol_ and mol_.HasSubstructMatch(CHO_pattern):
        return True
    return False



def check_topo(old_db_path: str,
               properties: list,
               new_db_path: str,
               error_code_pic_path: str,
               placement_cutoff: float = 1.7,
               covalent_radius_factor: float = 1.1,
               cluster_tolerance: float = 0.5):
    """
    Check the topology of an atoms.
    :return:
    0: Successfully passed topology test.
    1: More than one fully connected graphs are found. They are disconnected.
    2: More than one seperated atoms are found.
    3: Clusters are found.
    4: Rdkit warnning
    5: Not a Molecule
    6: has_carbon_carbon_double_bond
    7: has_carbon_carbon_triple_bond
    8:has_three_membered_ring
    9:has_4_membered_ring
    10:has_bridged_rings
    11:has_CHO
    """
    error_types = ['Disconnected', 'Single Atom', 'Cluster', 'Rdkit Warning', 'Not a Molecule',
                   'Carbon-Carbon Double Bond', 'Carbon-Carbon Triple Bond', 'Three Membered Ring',
                    'Four Membered Ring', 'Bridged Ring', 'CHO']
    error_code_list = []
    WrapLogs()  # Transform the RDKit logs to Python's stderr stream
    with connect(old_db_path) as old_db, connect(new_db_path) as new_db:
        for a_row in old_db.select():
            an_atoms = a_row.toatoms()
            topo_code = check_topo_unit(an_atoms=an_atoms,
                                        placement_cutoff=placement_cutoff,
                                        covalent_radius_factor=covalent_radius_factor,
                                        cluster_tolerance=cluster_tolerance)
            if topo_code > 0:
                error_code_list.append(topo_code)
                continue
            topo_code, an_inchi, a_smile = get_inchi_smiles_unit(an_atoms=an_atoms)
            if topo_code > 0:
                error_code_list.append(topo_code)
                continue

            # 20240919 by yin
            mol = AllChem.MolFromSmiles(a_smile)
            if mol is None:
                continue
            if has_carbon_carbon_double_bond(mol):
                error_code_list.append(6)
                continue
            if has_carbon_carbon_triple_bond(mol):
                error_code_list.append(7)
                continue
            if has_three_membered_ring(mol):
                error_code_list.append(8)
                continue
            if has_4_membered_ring(mol):
                error_code_list.append(9)
                continue
            if has_bridged_rings(mol):
                error_code_list.append(10)
                continue
            if has_CHO(mol):
                error_code_list.append(11)
                continue
            #end


            new_db.write(atoms=an_atoms, data=a_row.data, smile=a_smile, inchi=an_inchi)
    edit_ase_db(db_path=new_db_path, properties=properties)
    if len(error_code_list) == 0:
        return ' '
    counts = Counter(error_code_list)
    y = []
    x = sorted(counts.keys())
    err_str = ''

    real_error_types = []
    for an_error_code in x:
        y.append(counts[an_error_code])
        real_error_types.append(error_types[an_error_code - 1])
        err_str = err_str + f'{error_types[an_error_code - 1]}: {counts[an_error_code]}; '
    plt.bar(range(len(x)), y)
    plt.title(f"Total Counts: {len(error_code_list)}")
    plt.ylabel("Count")
    plt.xticks(ticks=range(len(x)), labels=real_error_types)
    plt.savefig(error_code_pic_path, dpi=400, bbox_inches='tight')
    plt.close()
    return err_str


def de_redundancy_db(old_db_path: str, properties: list, new_db_path: str):
    uni_inchi_set = set()
    with connect(old_db_path) as old_db, connect(new_db_path) as new_db:
        for a_row in old_db.select():
            an_inchi = a_row.inchi
            if an_inchi in uni_inchi_set:
                continue
            an_atoms = a_row.toatoms()
            uni_inchi_set.add(an_inchi)
            data = a_row.data
            for property in properties:
                data.update({property: [0]})
            new_db.write(atoms=an_atoms, smile=a_row.smile, inchi=a_row.inchi, data=data)
    edit_ase_db(db_path=new_db_path, properties=properties)


def remove_a_smile(old_db_path: str, new_db_path: str, the_smile: str, properties: list=None):
    with connect(old_db_path) as old_db, connect(new_db_path) as new_db:
        for a_row in old_db.select():
            if a_row.smile == the_smile:
                print('Found this SMILES!')
                continue
            new_db.write(a_row)
    if properties:
        edit_ase_db(db_path=new_db_path, properties=properties)


def remove_seen_db(old_db_path: str, new_db_path: str, chk_db_path: str, properties: list):
    chk_inchi_set = set()
    with connect(chk_db_path) as chk_db:
        for a_row in chk_db.select():
            a_chk_smile = a_row.smile
            a_chk_inchi = smile_to_inchi(a_chk_smile)
            chk_inchi_set.add(a_chk_inchi)
    with connect(old_db_path) as old_db, connect(new_db_path) as new_db:
        for a_row in old_db.select():
            an_old_inchi = a_row.inchi
            if an_old_inchi in chk_inchi_set:
                continue
            an_atoms = a_row.toatoms()
            new_db.write(atoms=an_atoms, smile=a_row.smile, inchi=an_old_inchi, data=a_row.data)
    edit_ase_db(db_path=new_db_path, properties=properties)


def apply_rascore_filter_db(old_db_path: str, filted_db_path: str, properties: list, rascore_threshold: float,
                            old_dist_pic_path: str, filted_dist_pic_path: str):
    from RAscore import RAscore_XGB

    ra_scorer = RAscore_XGB.RAScorerXGB()
    with connect(old_db_path) as old_db, connect(filted_db_path) as new_db:
        old_ra_score_list = []
        filted_ra_score_list = []
        for a_row in old_db.select():
            a_smile = a_row.smile
            a_ra_score = ra_scorer.predict(a_smile)
            old_ra_score_list.append(a_ra_score)
            old_data = a_row.data
            old_data['ra_score'] = [float(a_ra_score)]
            old_db.update(a_row.id, data=old_data)
            if a_ra_score > rascore_threshold:
                an_atoms = a_row.toatoms()
                new_db.write(atoms=an_atoms, smile=a_row.smile, data=old_data, inchi=a_row.inchi)
                filted_ra_score_list.append(a_ra_score)
    edit_ase_db(db_path=filted_db_path, properties=properties)

    g = sns.displot(old_ra_score_list)
    ax = g.ax
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.2f}'))
    ax.set_xlabel('RAScore')
    plt.title(f'Total Counts: {len(old_ra_score_list)}')
    plt.savefig(old_dist_pic_path, dpi=400, bbox_inches='tight')
    plt.close()

    g = sns.displot(filted_ra_score_list)
    ax = g.ax
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.2f}'))
    ax.set_xlabel('RAScore')
    plt.title(f'Total Counts: {len(filted_ra_score_list)}')
    plt.savefig(filted_dist_pic_path, dpi=400, bbox_inches='tight')
    plt.close()


def clc_info(workbase: str, raw_db_path: str, err_str: str, chk_db_path: str = None, rascore_threshold: float = 0.8):
    def _clc_info_unit(db_path: str, custom_line_1: str, a_count: int = None,
                       custom_line_2: str = None, custom_line_3: str = None):
        with connect(db_path) as db:
            new_count = db.count()
            f_w.write(f'{custom_line_1}\n')
            f_w.write(str(new_count))
            if custom_line_2:
                f_w.write(f'\n{custom_line_2}\n')
                f_w.write(str(a_count - new_count))
            if custom_line_3:
                f_w.write(f'\n{custom_line_3}')
            f_w.write('\n########################################\n')
        count_info.update({custom_line_1: new_count})
        return new_count

    cwd_ = os.getcwd()
    os.chdir(workbase)
    count_info = {}
    with open('info.txt', 'w') as f_w:
        a_count = _clc_info_unit(db_path=raw_db_path, custom_line_1='Successfully generated molecules:')
        a_count = _clc_info_unit(a_count=a_count, db_path='passed_topo.db',
                                 custom_line_1='Passed topological check molecules:',
                                 custom_line_2='Topological check filtered molecules:',
                                 custom_line_3=f'{err_str}')
        a_count = _clc_info_unit(a_count=a_count, db_path='de_redundancy.db',
                                 custom_line_1='Non-duplicated molecules:',
                                 custom_line_2='Duplicated molecules:')
        if chk_db_path:
            a_count = _clc_info_unit(a_count=a_count, db_path='unseen.db',
                                     custom_line_1='Unseen molecules:',
                                     custom_line_2='Seen molecules:')
        a_count = _clc_info_unit(a_count=a_count, db_path='synthesizable.db',
                                 custom_line_1='Synthesizable molecules:',
                                 custom_line_2=f'RAScore (threshold={str(rascore_threshold)}) filtered molecules:')
    with open("info.json", "w") as f:
        json.dump(count_info, f, indent=4)
    os.chdir(cwd_)


def clean_db_pipeline(raw_db_path: str, output_dir: str,
                      properties: list, rascore_threshold: float,
                      chk_db_path: str = None,
                      placement_cutoff: float = 1.7,
                      covalent_radius_factor: float = 1.1,
                      cluster_tolerance: float = 0.5):
    output_dir = os.path.abspath(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    err_str = check_topo(old_db_path=raw_db_path,
                         new_db_path=os.path.join(output_dir, 'passed_topo.db'),
                         properties=properties,
                         placement_cutoff=placement_cutoff,
                         covalent_radius_factor=covalent_radius_factor,
                         cluster_tolerance=cluster_tolerance,
                         error_code_pic_path=os.path.join(output_dir, 'error_topo.png'))
    temp_db_handle = os.path.join(output_dir, 'de_redundancy.db')
    de_redundancy_db(old_db_path=os.path.join(output_dir, 'passed_topo.db'),
                     new_db_path=temp_db_handle,
                     properties=properties)
    if chk_db_path:
        chk_db_path = os.path.abspath(chk_db_path)
        remove_seen_db(old_db_path=temp_db_handle,
                       chk_db_path=chk_db_path,
                       new_db_path=os.path.join(output_dir, 'unseen.db'),
                       properties=properties)
        temp_db_handle = os.path.join(output_dir, 'unseen.db')
    apply_rascore_filter_db(old_db_path=temp_db_handle,
                            filted_db_path=os.path.join(output_dir, 'synthesizable.db'),
                            properties=properties,
                            rascore_threshold=rascore_threshold,
                            old_dist_pic_path=os.path.join(output_dir, 'unseen_ra_score_dist.png'),
                            filted_dist_pic_path=os.path.join(output_dir, 'synthesizable_ra_score_dist.png'))
    clc_info(workbase=output_dir, raw_db_path=raw_db_path, err_str=err_str,
             chk_db_path=chk_db_path, rascore_threshold=rascore_threshold)


def get_total_num_from_json(abs_raw_path: str, info_line: str, n_jobs: int):
    total_num = 0
    for a_sub_job in range(n_jobs):
        os.chdir(abs_raw_path)
        os.chdir(str(a_sub_job))
        os.chdir('generated_molecules')
        with open(r"info.json") as f:
            data = json.load(f)
        total_num = total_num + data[info_line]
    return total_num


def merge_all_db(abs_raw_path: str, abs_cooked_path: str, db_name: str, n_jobs: int, properties: list):
    uni_inchi_set = set()
    cooked_db = os.path.join(abs_cooked_path, db_name)
    for a_sub_job in range(n_jobs):
        os.chdir(abs_raw_path)
        os.chdir(str(a_sub_job))
        os.chdir('generated_molecules')
        with connect(db_name) as old_db, connect(cooked_db) as new_db:
            for a_row in old_db.select():
                an_inchi = a_row.inchi
                if an_inchi in uni_inchi_set:
                    continue
                uni_inchi_set.add(an_inchi)
                an_atoms = a_row.toatoms()
                new_db.write(atoms=an_atoms, smile=a_row.smile, inchi=a_row.inchi, data=a_row.data)
    edit_ase_db(db_path=cooked_db, properties=properties)
    with connect(cooked_db) as new_db:
        merged_num = new_db.count()
    return merged_num

def simple_merge_dbs(new_db_path: str, src_db_path_list: list, properties: list):
    with connect(new_db_path) as new_db:
        for a_src_db_path in src_db_path_list:
            with connect(a_src_db_path) as src_db:
                for a_row in src_db.select():
                    new_db.write(a_row)
    edit_ase_db(db_path=new_db_path, properties=properties)


def get_props_npy_from_db(db_path: str, dump_folder_path: str, properties: list):
    cwd_ = os.getcwd()
    db_path = os.path.abspath(db_path)
    os.chdir(dump_folder_path)
    for a_prop in properties:
        info_list = []
        with connect(db_path) as db:
            for a_row in db.select():
                info_list.append(a_row.data[a_prop][0])
        info_arr = np.array(info_list)
        np.save(arr=info_arr, file=f'{a_prop}.npy')
    os.chdir(cwd_)

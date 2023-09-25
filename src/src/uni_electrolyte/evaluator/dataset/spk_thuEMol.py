# A schnetpack data format to properly incorporate Thu-ChenXiang electrolyte database.
# Part of this code are borrowed from schnetpack,
# see https://github.com/atomistic-machine-learning/schnetpack

import io
import logging
import os
import re
import shutil
import tarfile
import tempfile
from typing import List, Optional, Dict
from urllib import request as request

import numpy as np
from ase import Atoms
from ase.io.extxyz import read_xyz
from tqdm import tqdm

import torch
from schnetpack.data import *
import schnetpack.properties as structure
from schnetpack.data import AtomsDataModuleError, AtomsDataModule


class spk_thuEMol(AtomsDataModule):
    """QM9 benchmark database for organic molecules.

    The QM9 database contains small organic molecules with up to nine non-hydrogen atoms
    from including C, O, N, F. This class adds convenient functions to download QM9 from
    figshare and load the data into pytorch.

    References:

        .. [#qm9_1] https://ndownloader.figshare.com/files/3195404

    """

    # properties


    def __init__(
            self,
            datapath: str,
            batch_size: int,
            num_train: Optional[int] = None,
            num_val: Optional[int] = None,
            num_test: Optional[int] = None,
            split_file: Optional[str] = "split.npz",
            format: Optional[AtomsDataFormat] = AtomsDataFormat.ASE,
            load_properties: Optional[List[str]] = None,
            remove_uncharacterized: bool = False,
            val_batch_size: Optional[int] = None,
            test_batch_size: Optional[int] = None,
            transforms: Optional[List[torch.nn.Module]] = None,
            train_transforms: Optional[List[torch.nn.Module]] = None,
            val_transforms: Optional[List[torch.nn.Module]] = None,
            test_transforms: Optional[List[torch.nn.Module]] = None,
            num_workers: int = 2,
            num_val_workers: Optional[int] = None,
            num_test_workers: Optional[int] = None,
            property_units: Optional[Dict[str, str]] = None,
            distance_unit: Optional[str] = None,
            data_workdir: Optional[str] = None,
            **kwargs
    ):
        """

        Args:
            datapath: path to dataset
            batch_size: (train) batch size
            num_train: number of training examples
            num_val: number of validation examples
            num_test: number of test examples
            split_file: path to npz file with data partitions
            format: dataset format
            load_properties: subset of properties to load
            remove_uncharacterized: do not include uncharacterized molecules.
            val_batch_size: validation batch size. If None, use test_batch_size, then batch_size.
            test_batch_size: test batch size. If None, use val_batch_size, then batch_size.
            transforms: Transform applied to each system separately before batching.
            train_transforms: Overrides transform_fn for training.
            val_transforms: Overrides transform_fn for validation.
            test_transforms: Overrides transform_fn for testing.
            num_workers: Number of data loader workers.
            num_val_workers: Number of validation data loader workers (overrides num_workers).
            num_test_workers: Number of test data loader workers (overrides num_workers).
            property_units: Dictionary from property to corresponding unit as a string (eV, kcal/mol, ...).
            distance_unit: Unit of the atom positions and cell as a string (Ang, Bohr, ...).
            data_workdir: Copy data here as part of setup, e.g. cluster scratch for faster performance.
        """
        super().__init__(
            datapath=datapath,
            batch_size=batch_size,
            num_train=num_train,
            num_val=num_val,
            num_test=num_test,
            split_file=split_file,
            format=format,
            load_properties=load_properties,
            val_batch_size=val_batch_size,
            test_batch_size=test_batch_size,
            transforms=transforms,
            train_transforms=train_transforms,
            val_transforms=val_transforms,
            test_transforms=test_transforms,
            num_workers=num_workers,
            num_val_workers=num_val_workers,
            num_test_workers=num_test_workers,
            property_units=property_units,
            distance_unit=distance_unit,
            data_workdir=data_workdir,
            **kwargs
        )
        if os.path.exists(r'split.npz'):
            os.remove(r'split.npz')
            os.remove(r'splitting.lock')
        property_unit_dict = {}
        for a_property in load_properties:
            property_unit_dict.update({a_property: "Hartree"})
        self.property_unit_dict = property_unit_dict

    # To do: add new property
    def prepare_data(self):
        dataset = load_dataset(datapath=self.datapath,
                               format=self.format,
                               property_units=self.property_unit_dict,
                               )

    def predict_dataloader(self) -> AtomsLoader:
        self._predict_dataloader = AtomsLoader(
            self.test_dataset,
            batch_size=self.test_batch_size,
            num_workers=self.num_test_workers,
            pin_memory=self._pin_memory,
        )
        return self._predict_dataloader
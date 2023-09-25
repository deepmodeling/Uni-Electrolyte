import os
import shutil

from uni_electrolyte.evaluator.model.spatial import PaiNN
from uni_electrolyte.evaluator.dataset import spk_thuEMol, xyz_2_db
from uni_electrolyte.evaluator.trainer import ModelOutput, SinglePropertyClrTask
import schnetpack as spk
import schnetpack.transform as trn

import torch
import torchmetrics
import pytorch_lightning as pl
from pytorch_lightning import loggers as pl_loggers

##################################################################################################
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


if __name__ == "__main__":
    workbase = r'./output/inference_from_xyz'
    input_xyz_path = r'./input/data/dummy.xyz'

    targets = ['binding_e', 'dielectric_constant', 'viscosity', 'homo', 'lumo']
    target = targets[0]

    ##################################################################################################
    cutoff = 20
    n_atom_basis = 128

    pairwise_distance = spk.atomistic.PairwiseDistances()  # calculates pairwise distances between atoms
    radial_basis = spk.nn.GaussianRBF(n_rbf=20, cutoff=cutoff)

    schnet = PaiNN(
        n_atom_basis=n_atom_basis, n_interactions=3,
        radial_basis=radial_basis,
        cutoff_fn=spk.nn.CosineCutoff(cutoff)
    )
    pred_U0 = spk.atomistic.Atomwise(n_in=n_atom_basis, output_key=target)

    nnpot = spk.model.NeuralNetworkPotential(
        representation=schnet,
        input_modules=[pairwise_distance],
        output_modules=[pred_U0],
        postprocessors=[trn.CastTo64()]
    )

    output_U0 = ModelOutput(
        name=target,
        loss_fn=torch.nn.MSELoss(),
        loss_weight=1.,
        metrics={
            "MAE": torchmetrics.MeanAbsoluteError()
        }
    )

    task = SinglePropertyClrTask(
        model=nnpot,
        outputs=[output_U0],
        optimizer_cls=torch.optim.AdamW,
        optimizer_args={"lr": 5e-4},
        predict_property=target,
        scheduler_args={
            'base_lr': 1e-5,
            'max_lr': 5e-4,
            'step_size_up': 10,
            'step_size_down': 40,
            'lr_mode': "exp_range",
        },
        dump_info_path=os.path.join(workbase, 'infer_output')
    )
    ##################################################################################################
    logger = pl_loggers.TensorBoardLogger(save_dir=workbase)
    callbacks = [
        spk.train.ModelCheckpoint(
            model_path=os.path.join(workbase, "best_val_inf"),
            filename='{epoch:08d}-{val_loss:.6f}',
            save_top_k=3,
            save_last=True,
            monitor="val_loss",
        )
    ]

    trainer = pl.Trainer(
        callbacks=callbacks,
        accelerator='gpu',
        devices=[0],
        logger=logger,
        default_root_dir=workbase,
        max_epochs=1,  # for testing, we restrict the number of epochs
    )

    # trainer.fit(task, datamodule=thuEMolData)
    ##################################################################################################
    ##################################################################################################
    ##################################################################################################
    output_db_path = os.path.join(workbase, 'output.db')
    output_db_path = os.path.abspath(output_db_path)
    xyz_2_db(xyz_path=input_xyz_path, db_path=output_db_path, properties=[target])
    thu_test_Data = spk_thuEMol(
        datapath=output_db_path,
        batch_size=100,
        num_train=1,
        num_val=1,
        # num_test=3000, # Comment out for test and predict
        load_properties=[target],
        transforms=[
            trn.ASENeighborList(cutoff=20.),
            trn.CastTo32()
        ],
        pin_memory=False,
        num_workers=2
    )
    thu_test_Data.prepare_data()
    thu_test_Data.setup()
    trainer.predict(model=task, datamodule=thu_test_Data, ckpt_path='./input/last.ckpt', return_predictions=False)

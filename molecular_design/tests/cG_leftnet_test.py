import os

import pytorch_lightning as pl
import schnetpack as spk
import torch
from pytorch_lightning.callbacks.model_summary import ModelSummary
from pytorch_lightning.loggers import TensorBoardLogger
from schnetpack.transform import SubtractCenterOfMass, CastTo32, CastTo64
from schnetpack_gschnet.model import ConditionalGenerativeSchNet, ConditioningModule, VectorialConditionEmbedding
from schnetpack_gschnet.task import ConditionalGenerativeSchNetTask
from schnetpack_gschnet.transform import OrderByDistanceToOrigin, ConditionalGSchNetNeighborList, BuildAtomsTrajectory
from torch.optim.lr_scheduler import CyclicLR
from uni_electrolyte.evaluator.model.spatial.leftnet_gen_version import LEFTNet
from uni_electrolyte.generator import spk_thuEMolGen
from uni_electrolyte.generator.spk_callback import ModelCheckpoint


class MyTensorBoardLogger(TensorBoardLogger):
    def save(self):
        pass


if __name__ == "__main__":
    workbase = r'./output/train_test_output'
    my_logger = MyTensorBoardLogger(save_dir=workbase)  # avoid bugs
    ###############################################################################################################
    input_data_path = r'./fp_debug.db'
    thuEMolGenData = spk_thuEMolGen(
        datapath=input_data_path,
        batch_size=4,  # stay to your old setting, toggle smaller if there is memory error.
        num_train=16,  # stay to your old setting
        num_val=12,  # stay to your old setting
        data_workdir=r'./real_input',
        placement_cutoff=1.7,
        transforms=[
            SubtractCenterOfMass(),  # Subtract center of mass from positions.
            OrderByDistanceToOrigin(),  # Order atoms by their distance to the origin.
            ConditionalGSchNetNeighborList(
                model_cutoff=10,
                prediction_cutoff=10,
                placement_cutoff=1.7,
                environment_provider='matscipy',
                use_covalent_radii=True,
                covalent_radius_factor=1.1
            ),
            BuildAtomsTrajectory(
                centered=True,
                origin_type=121,
                focus_type=122,
                stop_type=123,
                # draw_random_samples=30
            ),
            CastTo32()
        ],
        num_workers=1,
    )
    thuEMolGenData.prepare_data()
    thuEMolGenData.setup()
    ###################################################################
    cutoff = 8
    pairwise_distance = spk.atomistic.PairwiseDistances()  # calculates pairwise distances between atoms
    #######################################################################
    schnet = LEFTNet(
        num_layers=6,
        hidden_channels=128,
        num_radial=96,
        cutoff=cutoff,
        max_z=130
    )
    ###################################################################
    fp_condition = VectorialConditionEmbedding(
        condition_name='fingerprint',
        n_in=167,
        n_features=64,
        n_layers=3,
        required_data_properties=['fingerprint']
    )
    real_fp_conditions = ConditioningModule(
        condition_embeddings=[fp_condition],
        n_features=128,
        n_layers=5
    )
    ###################################################################
    ###################################################################
    cg_schnet = ConditionalGenerativeSchNet(
        representation=schnet,
        atom_types=[1, 6, 8],
        origin_type=121,
        focus_type=122,
        stop_type=123,
        model_cutoff=10,
        prediction_cutoff=10,
        placement_cutoff=1.7,
        conditioning=real_fp_conditions,
        type_prediction_n_hidden=[206, 156, 106, 56],
        distance_prediction_n_hidden=[264, 273, 282, 291],
        input_modules=[pairwise_distance],  # new
        postprocessors=[CastTo64()]
    )
    ###################################################################
    ###################################################################
    ###################################################################
    task = ConditionalGenerativeSchNetTask(
        model=cg_schnet,
        scheduler_cls=CyclicLR,
        scheduler_args={
            'base_lr': 1e-5,
            'max_lr': 5e-4,
            'step_size_up': 7,
            'step_size_down': 28,
            'mode': "exp_range",
            'cycle_momentum': False,
            # 'smoothing_factor': 0.0
        },
        optimizer_args={
            'lr': 1e-4
        },
        scheduler_monitor='val_loss'
    )
    #############################################################################
    callbacks = [
        ModelCheckpoint(
            valid_best_model_path=os.path.join(workbase, 'valid_best.pt'),
            last_model_path=os.path.join(workbase, 'last.pt'),
            filename='{epoch:08d}-{val_loss:.6f}',
            save_top_k=3,
            save_last=True,
            monitor="val_loss",
            save_weights_only=True
        ),
        ModelSummary(max_depth=-1)
    ]

    trainer = pl.Trainer(
        callbacks=callbacks,
        accelerator='gpu',

        devices=[0],

        logger=my_logger,
        default_root_dir=workbase,
        max_epochs=500,  # for testing, we restrict the number of epochs
    )

    trainer.fit(task, datamodule=thuEMolGenData)

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from ase.db import connect
from rdkit import Chem
from rdkit import DataStructs
from rdkit.Chem import MACCSkeys
from uni_electrolyte.evaluator.inference.pyG_entry import decorated_property_names_reverse

__all__ = ["get_reversed_infer_target_list", "simple_2D_plot", "simple_kde_plot", "get_sim_list", "simple_plot_sim", 'simple_get_model']


def get_reversed_infer_target_list(infer_target_list: list):
    reversed_infer_target_list = []
    for a_target in infer_target_list:
        reversed_infer_target_list.append(decorated_property_names_reverse[a_target])
    return reversed_infer_target_list


def simple_2D_plot(leftnet_result_dir, target_info: dict = None):
    cwd_ = os.getcwd()
    os.chdir(leftnet_result_dir)
    homo_arr = np.load(r'homo.npy')
    lumo_arr = np.load(r'lumo.npy')
    df = pd.DataFrame({'HOMO': homo_arr, 'LUMO': lumo_arr})

    fig, ax = plt.subplots()

    sns.set_style("white")
    sns.kdeplot(x=df.HOMO, y=df.LUMO, cmap="Blues", shade=True)
    if target_info['mode'] == 'dot':
        plt.scatter(x=target_info['homo'], y=target_info['lumo'], marker='x', label='Target')
    else:
        from matplotlib.patches import Rectangle

        xmin = target_info['homo']['min']
        xmax = target_info['homo']['max']
        ymin = target_info['lumo']['min']
        ymax = target_info['lumo']['max']

        rectangle = Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, fill=False, linestyle='--', edgecolor='gray', label='Target interval')
        ax.add_patch(rectangle)

    plt.legend(loc='best')
    plt.xlabel('HOMO(eV)')
    plt.ylabel('LUMO(eV)')
    plt.savefig('./leftnet_evaluation_heatmap.png', dpi=400, bbox_inches='tight')
    plt.close()
    os.chdir(cwd_)


def simple_kde_plot(leftnet_result_dir, binding_e, chk_db_path):
    old_binding_e = []

    cwd_ = os.getcwd()
    os.chdir(leftnet_result_dir)
    binding_e_arr = np.load(r'binding_e.npy')
    sns.set_style("white")
    sns.kdeplot(binding_e_arr, label='Generated')
    if chk_db_path:
        chk_db_path = os.path.abspath(chk_db_path)
        with connect(chk_db_path) as old_db:
            for a_row in old_db.select():
                old_binding_e.append(a_row.data['binding_e'][0])
        sns.kdeplot(np.array(old_binding_e), label='Train')
    plt.scatter(x=binding_e, y=0, marker='^', label='Target', s=200, c='red')
    plt.legend(loc='best')
    plt.xlabel('Binding energy (eV)')
    plt.savefig('./leftnet_evaluation_kde.png', dpi=400, bbox_inches='tight')
    os.chdir(cwd_)


def get_sim_list(db_path: str, target_maccs):
    sim_list = []
    with connect(db_path) as db:
        for a_row in db.select():
            a_smile = a_row.smile
            a_mol = Chem.MolFromSmiles(a_smile)
            a_maccs = MACCSkeys.GenMACCSKeys(a_mol)
            similarity = DataStructs.FingerprintSimilarity(target_maccs, a_maccs)
            sim_list.append(similarity)
            db.update(a_row.id, similarity=similarity)
    return sim_list


def simple_plot_sim(target_smile: str, gen_db_path: str, dump_path: str,
                    chk_db_has_sim: bool = False, chk_db_path: str = None):
    target_mol = Chem.MolFromSmiles(target_smile)
    target_maccs = MACCSkeys.GenMACCSKeys(target_mol)
    gen_sim_list = get_sim_list(db_path=gen_db_path, target_maccs=target_maccs)

    sns.set_style("white")
    sns.kdeplot(np.array(gen_sim_list), label='Generated')

    if chk_db_path:
        if chk_db_has_sim:
            old_sim_list = []
            with connect(chk_db_path) as db:
                for a_row in db.select():
                    old_sim_list.append(a_row.similarity)
        else:
            old_sim_list = get_sim_list(db_path=chk_db_path, target_maccs=target_maccs)
        sns.kdeplot(np.array(old_sim_list), label='Train')

    plt.xlabel('Similarity')
    plt.legend(loc='best')
    plt.savefig(dump_path, dpi=400, bbox_inches='tight')


def simple_get_model(mode: str):
    from uni_electrolyte.evaluator.model.spatial.leftnet_gen_version import LEFTNet
    from schnetpack_gschnet.task import ConditionalGenerativeSchNetTask
    from schnetpack_gschnet.model import ConditionalGenerativeSchNet, ConditioningModule, ScalarConditionEmbedding, VectorialConditionEmbedding, CompositionEmbedding
    import schnetpack as spk
    from schnetpack.transform import CastTo64
    from torch.optim.lr_scheduler import CyclicLR

    # ###################################################################
    schnet = LEFTNet(
        num_layers=6,
        hidden_channels=128,
        num_radial=96,
        cutoff=8,
        max_z=130,
        is_train=False
    )
    ###################################################################
    atom_types = [1, 6, 8]
    if mode == 'fp':
        fp_condition = VectorialConditionEmbedding(
            condition_name='fingerprint',
            n_in=167,
            n_features=64,
            n_layers=3,
            required_data_properties=['fingerprint']
        )
        condition_list = [fp_condition]
    elif mode == 'be_formular':
        comp_condition = CompositionEmbedding(
            atom_types=[1, 6, 8],
            n_atom_basis=16,
            n_features_concentration=64,
            n_layers_concentration=3,
            n_features_n_atoms=64,
            n_layers_n_atoms=3,
            condition_min_n_atoms=0.,
            condition_max_n_atoms=10,
            grid_spacing_n_atoms=2.5,
        )
        binding_e_condition = ScalarConditionEmbedding(
            condition_name='binding_e',
            condition_min=-4,
            condition_max=0,
            grid_spacing=0.5,
            n_features=64,
            n_layers=3,
            required_data_properties=['binding_e']
        )
        condition_list = [comp_condition, binding_e_condition]
    elif mode == 'homo_lumo':
        homo_condition = ScalarConditionEmbedding(
            condition_name='homo',
            condition_min=-9,
            condition_max=-2,
            grid_spacing=1,
            n_features=64,
            n_layers=3,
            required_data_properties=['homo']
        )
        lumo_condition = ScalarConditionEmbedding(
            condition_name='lumo',
            condition_min=-4,
            condition_max=10,
            grid_spacing=2,
            n_features=64,
            n_layers=3,
            required_data_properties=['lumo']
        )
        condition_list = [homo_condition, lumo_condition]
    elif mode == 'sp_rs_sa':
        sp_condition = ScalarConditionEmbedding(
            condition_name='sp',
            condition_min=0,
            condition_max=1,
            grid_spacing=0.1,
            n_features=64,
            n_layers=3,
            required_data_properties=['sp']
        )
        rs_condition = ScalarConditionEmbedding(
            condition_name='rs',
            condition_min=0,
            condition_max=1,
            grid_spacing=0.1,
            n_features=64,
            n_layers=3,
            required_data_properties=['rs']
        )
        sa_condition = ScalarConditionEmbedding(
            condition_name='sa',
            condition_min=0,
            condition_max=1,
            grid_spacing=0.1,
            n_features=64,
            n_layers=3,
            required_data_properties=['sa']
        )
        condition_list = [sp_condition, rs_condition, sa_condition]
        atom_types.append(9)
    else:
        print('Please check the mode.')
    real_conditions = ConditioningModule(
        condition_embeddings=condition_list,
        n_features=128,
        n_layers=5
    )
    ###################################################################
    pairwise_distance = spk.atomistic.PairwiseDistances()  # calculates pairwise distances between atoms
    ###################################################################
    cg_schnet = ConditionalGenerativeSchNet(
        representation=schnet,
        atom_types=atom_types,
        origin_type=121,
        focus_type=122,
        stop_type=123,
        model_cutoff=10,
        prediction_cutoff=10,
        placement_cutoff=1.7,
        conditioning=real_conditions,
        type_prediction_n_hidden=[206, 156, 106, 56],
        distance_prediction_n_hidden=[264, 273, 282, 291],
        input_modules=[pairwise_distance], # new
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
    return task


if __name__ == "__main__":
    from uni_electrolyte.generator.gen_utils import simple_get_model

    task = simple_get_model(mode='fp')

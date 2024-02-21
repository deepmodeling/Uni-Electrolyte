import os

import numpy as np
from uni_electrolyte.evaluator.dataset import clean_db_pipeline, get_smiles_from_db
from uni_electrolyte.evaluator.inference.pyG_entry import pyG_infer_from_db
from uni_electrolyte.generator.cg_schnet_gen_workers import *
from uni_electrolyte.generator.gen_utils import *

__all__ = ['comp_be_pipeline', 'homo_lumo_pipeline', 'edm_gen_pipeline', 'fp_pipeline']


def homo_lumo_interval(target_info: dict, gen_ckpt_path: str, batch_size: int = 20, is_cgleftnet: bool = False):
    n_dot_per_interval = target_info['n_dot_per_interval']
    n_samples_per_dot = target_info['n_samples_per_dot']
    print(f'Number of total condition dots are: {n_dot_per_interval ** 2}')
    print(f'Number of total generated molecules are: {n_samples_per_dot * n_dot_per_interval ** 2}')
    condition_dots_container = []
    for condition in ['homo', 'lumo']:
        condition_dots = np.linspace(target_info[condition]['min'], target_info[condition]['max'], n_dot_per_interval,
                                     endpoint=True)
        condition_dots_container.append(condition_dots)
    homo_lumo_mesh = np.array(np.meshgrid(*condition_dots_container)).T.reshape(-1, len(condition_dots_container))
    for idx, a_condition in enumerate(homo_lumo_mesh):
        print(f'Current condition dots/Total condition dots: {idx + 1}/{n_dot_per_interval ** 2}')
        homo_lumo_gen(homo=float(a_condition[0]),
                      lumo=float(a_condition[1]),
                      gen_ckpt_path=gen_ckpt_path,
                      n_molecules=n_samples_per_dot,
                      batch_size=batch_size, is_cgleftnet=is_cgleftnet)


def clean_and_score(workbase: str, leftnet_result_dir: str, eval_batch_size: int = 20,
                    rascore_threshold: float = 0.8, chk_db_path: str = None, eval_ckpt_path: str = None,
                    infer_target_list: list = ['homo', 'lumo', 'binding_e', 'dielectric_constant', 'viscosity']):
    clean_db_pipeline(raw_db_path=os.path.join(workbase, 'generated_molecules', 'raw.db'),
                      chk_db_path=chk_db_path,
                      output_dir=os.path.join(workbase, 'generated_molecules'),
                      properties=infer_target_list,
                      rascore_threshold=rascore_threshold)
    get_smiles_from_db(db_path=os.path.join(workbase, 'generated_molecules', 'synthesizable.db'),
                       smile_file_path=os.path.join(workbase, 'generated_molecules', 'synthesizable_smiles.txt'))
    if len(infer_target_list) > 0:
        eval_ckpt_path = os.path.abspath(eval_ckpt_path)
        pyG_infer_from_db(db_path=os.path.join(workbase, 'generated_molecules', 'synthesizable.db'),
                          target_list=infer_target_list,
                          eval_ckpt_path=eval_ckpt_path,
                          output_directory=leftnet_result_dir,
                          infer_batch_size=eval_batch_size)


def comp_be_pipeline(composition: str, binding_e: float, gen_ckpt_path: str,
                     n_molecules: int = 10000, gen_batch_size: int = 20, eval_batch_size: int = 20,
                     rascore_threshold: float = 0.8, chk_db_path: str = None, eval_ckpt_path: str = None,
                     infer_target_list: list = ['homo', 'lumo', 'binding_e', 'dielectric_constant', 'viscosity'],
                     is_reverse_infer_target_list: bool = False, is_cgleftnet: bool = False):
    if is_reverse_infer_target_list:
        infer_target_list = get_reversed_infer_target_list(infer_target_list)

    cwd_ = os.getcwd()
    comp_be_gen(composition=composition, binding_e=binding_e,
                gen_ckpt_path=gen_ckpt_path,
                n_molecules=n_molecules, batch_size=gen_batch_size, is_cgleftnet=is_cgleftnet)
    leftnet_result_dir = os.path.join(cwd_, 'generated_molecules', 'leftnet')
    clean_and_score(workbase=cwd_, eval_batch_size=eval_batch_size, rascore_threshold=rascore_threshold,
                    leftnet_result_dir=leftnet_result_dir, chk_db_path=chk_db_path,
                    eval_ckpt_path=eval_ckpt_path, infer_target_list=infer_target_list)
    if 'binding_e' in infer_target_list:
        simple_kde_plot(leftnet_result_dir=leftnet_result_dir, binding_e=binding_e, chk_db_path=chk_db_path)
    os.chdir(cwd_)


def fp_pipeline(target_smile: str, gen_ckpt_path: str,
                eval_ckpt_path: str = None,
                eval_batch_size: int = 20,
                chk_db_path: str = None,
                n_molecules: int = 10000, gen_batch_size: int = 20,
                rascore_threshold: float = 0.8, chk_db_has_sim: bool = True,
                infer_target_list: list = ['homo', 'lumo', 'binding_e', 'dielectric_constant', 'viscosity'],
                is_reverse_infer_target_list: bool = False, is_cgleftnet: bool = False):
    if is_reverse_infer_target_list:
        infer_target_list = get_reversed_infer_target_list(infer_target_list)

    cwd_ = os.getcwd()
    fp_gen(target_smile=target_smile, gen_ckpt_path=gen_ckpt_path,
           n_molecules=n_molecules, batch_size=gen_batch_size, is_cgleftnet=is_cgleftnet)
    leftnet_result_dir = os.path.join(cwd_, 'generated_molecules', 'leftnet')
    clean_and_score(workbase=cwd_, eval_batch_size=eval_batch_size, rascore_threshold=rascore_threshold,
                    leftnet_result_dir=leftnet_result_dir, chk_db_path=chk_db_path,
                    eval_ckpt_path=eval_ckpt_path, infer_target_list=infer_target_list)
    simple_plot_sim(gen_db_path=os.path.join(cwd_, 'generated_molecules', 'synthesizable.db'),
                    target_smile=target_smile, chk_db_path=chk_db_path,
                    dump_path=os.path.join(cwd_, 'generated_molecules', 'similarity.png'),
                    chk_db_has_sim=chk_db_has_sim)
    os.chdir(cwd_)


def homo_lumo_pipeline(target_info: dict,
                       eval_ckpt_path: str,
                       eval_batch_size: int = 20,
                       gen_batch_size: int = 20,
                       gen_ckpt_path: str = None,
                       chk_db_path: str = None,
                       rascore_threshold: float = 0.8,
                       infer_target_list: list = ['homo', 'lumo', 'binding_e', 'dielectric_constant', 'viscosity'],
                       is_reverse_infer_target_list: bool = False,
                       is_cgleftnet: bool = False):
    if is_reverse_infer_target_list:
        infer_target_list = get_reversed_infer_target_list(infer_target_list)

    cwd_ = os.getcwd()
    if target_info['mode'] == 'dot':
        homo_lumo_gen(homo=target_info['homo'], lumo=target_info['lumo'], gen_ckpt_path=gen_ckpt_path,
                      n_molecules=target_info['n_molecules'], batch_size=gen_batch_size, is_cgleftnet=is_cgleftnet)
    elif target_info['mode'] == 'interval':
        homo_lumo_interval(target_info=target_info, gen_ckpt_path=gen_ckpt_path,
                           batch_size=gen_batch_size, is_cgleftnet=is_cgleftnet)
    else:
        print('Only dot and interval modes are supported.')
        raise NotImplementedError
    leftnet_result_dir = os.path.join(cwd_, 'generated_molecules', 'leftnet')
    clean_and_score(workbase=cwd_, eval_batch_size=eval_batch_size, rascore_threshold=rascore_threshold,
                    leftnet_result_dir=leftnet_result_dir, chk_db_path=chk_db_path,
                    eval_ckpt_path=eval_ckpt_path, infer_target_list=infer_target_list)
    if 'homo' in infer_target_list and 'lumo' in infer_target_list:
        simple_2D_plot(leftnet_result_dir=leftnet_result_dir, target_info=target_info)
    os.chdir(cwd_)


def edm_gen_pipeline(train_workbase: str,
                     target_info: dict,
                     diffusion_steps: int,
                     eval_batch_size: int = 20, chk_db_path: str = None,
                     n_sweeps=100, n_frames=100, eval_ckpt_path: str = None,
                     rascore_threshold: float = 0.8,
                     infer_target_list: list = ['homo', 'lumo', 'binding_e', 'dielectric_constant', 'viscosity'],
                     fix_noise: bool = False, fixed_natoms=None,
                     is_reverse_infer_target_list: bool = False):
    from uni_electrolyte.generator.edm_gen_workers import edm_conditional_sample

    if is_reverse_infer_target_list:
        infer_target_list = get_reversed_infer_target_list(infer_target_list)

    cwd_ = os.getcwd()
    os.makedirs(os.path.join(cwd_, 'generated_molecules'), exist_ok=True)
    raw_db_path = os.path.join(cwd_, 'generated_molecules', 'raw.db')
    edm_conditional_sample(train_workbase=train_workbase,
                           out_db_path=os.path.join(cwd_, 'generated_molecules', 'raw.db'),
                           target_info=target_info,
                           n_sweeps=n_sweeps, n_frames=n_frames,
                           fix_noise=fix_noise,
                           diffusion_steps=diffusion_steps, fixed_natoms=fixed_natoms)
    leftnet_result_dir = os.path.join(cwd_, 'generated_molecules', 'leftnet')
    clean_and_score(workbase=cwd_, eval_batch_size=eval_batch_size, rascore_threshold=rascore_threshold,
                    leftnet_result_dir=leftnet_result_dir, chk_db_path=chk_db_path,
                    eval_ckpt_path=eval_ckpt_path, infer_target_list=infer_target_list)
    if 'homo' in infer_target_list and 'lumo' in infer_target_list:
        simple_2D_plot(leftnet_result_dir=leftnet_result_dir, target_info=target_info)
    os.chdir(cwd_)

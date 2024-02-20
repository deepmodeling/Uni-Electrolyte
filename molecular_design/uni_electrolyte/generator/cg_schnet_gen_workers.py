import os

import torch
from omegaconf import DictConfig
from uni_electrolyte.evaluator.dataset import smile_to_maccs_fp_arr
from uni_electrolyte.generator.gen_utils import simple_get_model

from .generate import generate

__all__ = ['comp_be_gen', 'fp_gen', 'homo_lumo_gen', 'three_props_gen']


def get_cgleftnet_model(gen_ckpt_path: str, model_name: str):
    task = simple_get_model(mode=model_name)
    task.model.representation.is_train = False
    device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device("cpu")
    ckpt = torch.load(os.path.join(gen_ckpt_path, f'{model_name}.pt'))
    task.load_state_dict(ckpt['model_state_dict'])
    task.to(device=device)
    return task.model


def comp_be_gen(composition: str, binding_e: float,
                gen_ckpt_path: str,
                workbase: str = None,
                n_molecules: int = 10000, batch_size: int = 20, is_cgleftnet: bool = False):
    condition_list = ['binding_e', 'composition']
    condition_str = '_'.join(condition_list)
    a_dict = DictConfig(
        content={
            'outputfile': 'raw.db',
            'workdir': workbase,
            'use_gpu': True,
            'generate': {
                'n_molecules': n_molecules,
                'batch_size': batch_size,
                'max_n_atoms': 50,
                'grid_distance_min': 0.7,
                'grid_spacing': 0.05,
                'temperature_term': 0.1,
                'grid_batch_size': 0,
                'conditions': {
                    'trajectory': condition_list
                }
            },
            'original_conditions': condition_str,
            'debug': {
                'run': False
            },
            'settings': {
                'conditions': {
                    'trajectory': {
                        'binding_e': binding_e,
                        'composition': composition
                    }
                }
            },
            'view_molecules': False,
            'remove_workdir': True
        }
    )
    if os.path.isfile(gen_ckpt_path):
        if not is_cgleftnet:
            model = torch.load(gen_ckpt_path)['hyper_parameters']['model']
        else:
            gen_ckpt_folder, _ = os.path.split(gen_ckpt_path)
            os.rename(src=gen_ckpt_path, dst=os.path.join(gen_ckpt_folder, 'be_formular.pt'))
            model = get_cgleftnet_model(gen_ckpt_path=gen_ckpt_folder, model_name='be_formular')
    else:
        if is_cgleftnet:
            model = get_cgleftnet_model(gen_ckpt_path=gen_ckpt_path, model_name='be_formular')
        else:
            model = torch.load(os.path.join(gen_ckpt_path, 'be_formular.ckpt'))['hyper_parameters']['model']
    generate(config=a_dict, model=model)


def fp_gen(target_smile: str,
           gen_ckpt_path: str,
           workbase: str = None,
           n_molecules: int = 10000,
           batch_size: int = 20,
           task=None,
           is_cgleftnet: bool = False):
    tgt_arr = smile_to_maccs_fp_arr(target_smile)
    tgt_arr_to_list = tgt_arr.astype(float).tolist()
    condition_list = ['fingerprint']
    condition_str = condition_list[0]
    a_dict = DictConfig(
        content={
            'outputfile': 'raw.db',
            'workdir': workbase,
            'use_gpu': True,
            'generate': {
                'n_molecules': n_molecules,
                'batch_size': batch_size,
                'max_n_atoms': 50,
                'grid_distance_min': 0.7,
                'grid_spacing': 0.05,
                'temperature_term': 0.1,
                'grid_batch_size': 0,
                'conditions': {
                    'trajectory': condition_list
                }
            },
            'original_conditions': condition_str,
            'debug': {
                'run': False
            },
            'settings': {
                'conditions': {
                    'trajectory': {
                        'fingerprint': tgt_arr_to_list,
                    }
                }
            },
            'view_molecules': False,
            'remove_workdir': True
        }
    )
    if os.path.isfile(gen_ckpt_path):
        if not is_cgleftnet:
            model = torch.load(gen_ckpt_path)['hyper_parameters']['model']
        else:
            gen_ckpt_folder, _ = os.path.split(gen_ckpt_path)
            os.rename(src=gen_ckpt_path, dst=os.path.join(gen_ckpt_folder, 'fp.pt'))
            model = get_cgleftnet_model(gen_ckpt_path=gen_ckpt_folder, model_name='fp')
    else:
        if is_cgleftnet:
            model = get_cgleftnet_model(gen_ckpt_path=gen_ckpt_path, model_name='fp')
        else:
            model = torch.load(os.path.join(gen_ckpt_path, 'fp.ckpt'))['hyper_parameters']['model']
    generate(config=a_dict, model=model)


def homo_lumo_gen(homo: float, lumo: float,
                  gen_ckpt_path: str,
                  workbase: str = None,
                  n_molecules: int = 10000,
                  batch_size: int = 20,
                  is_cgleftnet: bool = False):
    condition_list = ['homo', 'lumo']
    condition_str = '_'.join(condition_list)
    a_dict = DictConfig(
        content={
            'outputfile': 'raw.db',
            'workdir': workbase,
            'use_gpu': True,
            'generate': {
                'n_molecules': n_molecules,
                'batch_size': batch_size,
                'max_n_atoms': 50,
                'grid_distance_min': 0.7,
                'grid_spacing': 0.05,
                'temperature_term': 0.1,
                'grid_batch_size': 0,
                'conditions': {
                    'trajectory': condition_list
                }
            },
            'original_conditions': condition_str,
            'debug': {
                'run': False
            },
            'settings': {
                'conditions': {
                    'trajectory': {
                        'homo': homo,
                        'lumo': lumo
                    }
                }
            },
            'view_molecules': False,
            'remove_workdir': True
        }
    )
    if os.path.isfile(gen_ckpt_path):
        if not is_cgleftnet:
            model = torch.load(gen_ckpt_path)['hyper_parameters']['model']
        else:
            gen_ckpt_folder, _ = os.path.split(gen_ckpt_path)
            os.rename(src=gen_ckpt_path, dst=os.path.join(gen_ckpt_folder, 'homo_lumo.pt'))
            model = get_cgleftnet_model(gen_ckpt_path=gen_ckpt_folder, model_name='homo_lumo')
    else:
        if is_cgleftnet:
            model = get_cgleftnet_model(gen_ckpt_path=gen_ckpt_path, model_name='homo_lumo')
        else:
            model = torch.load(os.path.join(gen_ckpt_path, 'homo_lumo.ckpt'))['hyper_parameters']['model']
    generate(config=a_dict, model=model)

def three_props_gen(sp: float, rs: float, sa: float,
                    gen_ckpt_path: str, batch_size: int = 5, workbase: str = None,
                    n_molecules: int = 1000,
                    is_cgleftnet: bool = False):
    condition_list = ['sp', 'rs', 'sa']
    condition_str = '_'.join(condition_list)
    a_dict = DictConfig(
        content={
            'outputfile': 'raw.db',
            'workdir': workbase,
            'use_gpu': True,
            'generate': {
                'n_molecules': n_molecules,
                'batch_size': batch_size,
                'max_n_atoms': 50,
                'grid_distance_min': 0.7,
                'grid_spacing': 0.05,
                'temperature_term': 0.1,
                'grid_batch_size': 0,
                'conditions': {
                    'trajectory': condition_list
                }
            },
            'original_conditions': condition_str,
            'debug': {
                'run': False
            },
            'settings': {
                'conditions': {
                    'trajectory': {
                        'sp': sp,
                        'rs': rs,
                        'sa': sa
                    }
                }
            },
            'view_molecules': False,
            'remove_workdir': True
        }
    )
    if os.path.isfile(gen_ckpt_path):
        if not is_cgleftnet:
            model = torch.load(gen_ckpt_path)['hyper_parameters']['model']
        else:
            gen_ckpt_folder, _ = os.path.split(gen_ckpt_path)
            os.rename(src=gen_ckpt_path, dst=os.path.join(gen_ckpt_folder, 'sp_rs_sa.pt'))
            model = get_cgleftnet_model(gen_ckpt_path=gen_ckpt_folder, model_name='sp_rs_sa')
    else:
        if is_cgleftnet:
            model = get_cgleftnet_model(gen_ckpt_path=gen_ckpt_path, model_name='sp_rs_sa')
        else:
            model = torch.load(os.path.join(gen_ckpt_path, 'sp_rs_sa.ckpt'))['hyper_parameters']['model']
    generate(config=a_dict, model=model)

import os
from pathlib import Path
from typing import List, Union

from uni_electrolyte.evaluator.dataset import clean_db_pipeline, get_smiles_from_db
from uni_electrolyte.evaluator.inference.pyG_entry import pyG_infer_from_db, decorated_property_names, three_property_names
from uni_electrolyte.generator.cg_schnet_gen_workers import *
from uni_electrolyte.generator.edm_gen_workers import edm_conditional_sample
from uni_electrolyte.generator.gen_utils import *

__all__ = ['comp_be_pipeline_class', 'homo_lumo_pipeline_class', 'edm_gen_pipeline_class', 'fp_pipeline_class',
           'BasePipeline', 'ThreePropsPipeline']


class BasePipeline:
    def __init__(self):
        self.workbase = os.getcwd()
        self.gen_folder = os.path.join(self.workbase, 'generated_molecules')
        self.gen_db_path = os.path.join(self.gen_folder, 'synthesizable.db')
        self.leftnet_result_dir = os.path.join(self.gen_folder, 'leftnet')

    def set_gen_info(self, gen_ckpt_path: Union[str, Path], gen_batch_size: int = 20,
                     n_molecules: int = 20, is_cgleftnet: bool = False):
        self.gen_ckpt_path = os.path.abspath(gen_ckpt_path)
        self.gen_batch_size = gen_batch_size
        self.n_molecules = n_molecules
        self.is_cgleftnet = is_cgleftnet

    def set_clean_score_info(self, eval_folder_path: Union[str, Path], eval_batch_size: int = 20,
                             infer_target_list: List[str] = ['homo', 'lumo', 'binding_e', 'dielectric_constant',
                                                             'viscosity'],
                             chk_db_path: Union[str, Path] = "",
                             rascore_threshold: float = 0.8,
                             is_reverse_infer_target_list: bool = False,
                             decorated_property_names: dict = decorated_property_names):
        self.eval_folder_path = eval_folder_path
        self.eval_batch_size = eval_batch_size
        self.is_reverse_infer_target_list = is_reverse_infer_target_list
        if is_reverse_infer_target_list:
            self.infer_target_list = get_reversed_infer_target_list(infer_target_list)
        else:
            self.infer_target_list = infer_target_list
        self.decorated_property_names = decorated_property_names
        self.chk_db_path = chk_db_path
        self.rascore_threshold = rascore_threshold

    def clean_and_score(self):
        clean_db_pipeline(raw_db_path=os.path.join(self.gen_folder, 'raw.db'),
                          chk_db_path=self.chk_db_path,
                          output_dir=os.path.join(self.gen_folder),
                          properties=self.infer_target_list,
                          rascore_threshold=self.rascore_threshold)
        get_smiles_from_db(db_path=self.gen_db_path,
                           smile_file_path=os.path.join(self.gen_folder, 'synthesizable_smiles.txt'))
        if len(self.infer_target_list) > 0:
            pyG_infer_from_db(db_path=self.gen_db_path,
                              target_list=self.infer_target_list,
                              eval_ckpt_path=self.eval_folder_path,
                              output_directory=self.leftnet_result_dir,
                              infer_batch_size=self.eval_batch_size,
                              decorated_property_names=self.decorated_property_names)

    def gen(self):
        pass

    def plot_results(self):
        pass

    def run(self):
        self.gen()
        self.clean_and_score()
        self.plot_results()

    def run_with_dpdispatcher(self):
        pass


class ThreePropsPipeline(BasePipeline):
    def set_gen_info(self, sp, sa, rs, gen_ckpt_path, gen_batch_size, n_molecules, is_cgleftnet):
        super().set_gen_info(gen_ckpt_path=gen_ckpt_path, gen_batch_size=gen_batch_size,
                             n_molecules=n_molecules, is_cgleftnet=is_cgleftnet)
        self.sp = sp
        self.sa = sa
        self.rs = rs

    def gen(self):
        three_props_gen(sp=self.sp, rs=self.rs, sa=self.sa, gen_ckpt_path=self.gen_ckpt_path,
                        n_molecules=self.n_molecules, batch_size=self.gen_batch_size, is_cgleftnet=self.is_cgleftnet)

    def plot_results(self):
        three_props_plot(leftnet_result_dir=self.leftnet_result_dir)


class EDMPipeline(BasePipeline):
    def set_gen_info(self, train_workbase: str, sp, sa, rs, diffusion_steps: int,
            fix_noise: bool = False, fixed_natoms=None, n_sweeps=100, n_frames=100, custom_natoms_list=None):
        self.train_workbase = train_workbase
        self.target_info = {
            'sp': {'max': sp + 0.00001, 'min': sp, 'mean': sp},
            'rs': {'max': rs + 0.00001, 'min': rs, 'mean': rs},
            'sa': {'max': sa + 0.00001, 'min': sa, 'mean': sa},
        }
        self.diffusion_steps = diffusion_steps
        self.fix_noise = fix_noise
        self.fixed_natoms = fixed_natoms
        self.n_frames = n_frames
        self.n_sweeps = n_sweeps
        self.custom_natoms_list = custom_natoms_list

    def gen(self):
        os.makedirs(self.gen_folder, exist_ok=True)
        edm_conditional_sample(train_workbase=self.train_workbase,
                               out_db_path=os.path.join(self.gen_folder, 'raw.db'),
                               target_info=self.target_info, diffusion_steps=self.diffusion_steps,
                               fix_noise=self.fix_noise, fixed_natoms=self.fixed_natoms,
                               n_frames=self.n_frames, n_sweeps=self.n_sweeps,
                               custom_natoms_list=self.custom_natoms_list)

    def plot_results(self):
        three_props_plot(leftnet_result_dir=self.leftnet_result_dir)




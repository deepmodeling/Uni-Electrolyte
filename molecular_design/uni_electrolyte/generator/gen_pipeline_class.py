import os
from pathlib import Path
from typing import Union, List

from uni_electrolyte.evaluator.dataset import clean_db_pipeline, get_smiles_from_db
from uni_electrolyte.evaluator.inference.pyG_entry import pyG_infer_from_db, decorated_property_names, three_property_names
from uni_electrolyte.generator.cg_schnet_gen_workers import *
from uni_electrolyte.generator.gen_utils import *

__all__ = ['comp_be_pipeline_class', 'homo_lumo_pipeline_class', 'edm_gen_pipeline_class', 'fp_pipeline_class']


class BasePipeline:
    def __init__(self,
                 gen_ckpt_path: Union[str, Path] = '',
                 eval_ckpt_path: Union[str, Path] = '',
                 chk_db_path: Union[str, Path] = '',
                 eval_batch_size: int = 20,
                 gen_batch_size: int = 20,
                 rascore_threshold: float = 0.8,
                 infer_target_list: List[str] = ['homo', 'lumo', 'binding_e', 'dielectric_constant', 'viscosity'],
                 is_reverse_infer_target_list: bool = False
                 ):
        self.workbase = os.getcwd()
        self.gen_folder = os.path.join(self.workbase, 'generated_molecules')
        self.gen_db_path = os.path.join(self.gen_folder, 'synthesizable.db')
        self.leftnet_result_dir = os.path.join(self.gen_folder, 'leftnet')
        self.gen_ckpt_path = gen_ckpt_path
        self.eval_ckpt_path = eval_ckpt_path
        self.chk_db_path = chk_db_path
        self.eval_batch_size = eval_batch_size
        self.gen_batch_size = gen_batch_size
        self.rascore_threshold = rascore_threshold
        if is_reverse_infer_target_list:
            self.infer_target_list = get_reversed_infer_target_list(infer_target_list)
        else:
            self.infer_target_list = infer_target_list

    def clean_and_score(self, decorated_property_names=decorated_property_names):
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
                              eval_ckpt_path=self.eval_ckpt_path,
                              output_directory=self.leftnet_result_dir,
                              infer_batch_size=self.eval_batch_size,
                              decorated_property_names=decorated_property_names)

    def run(self):
        pass


class HomoLumoPipeline(BasePipeline):

    def run(self, target_info: HomoLumoTargetInfo, is_cgleftnet: bool = False):
        if target_info.mode == 'dot':
            homo_lumo_gen(homo=target_info.params.homo,
                          lumo=target_info.params.lumo,
                          gen_ckpt_path=self.gen_ckpt_path,
                          n_molecules=target_info.params.n_molecules,
                          batch_size=self.gen_batch_size,
                          is_cgleftnet=is_cgleftnet)
        else:
            for idx, a_condition in enumerate(get_homo_lumo_mesh(mesh_target_info=target_info.params)):
                print(f'Current condition dots/Total condition dots: {idx + 1}/{n_dot_per_interval ** 2}')
                homo_lumo_gen(homo=float(a_condition[0]),
                              lumo=float(a_condition[1]),
                              gen_ckpt_path=self.gen_ckpt_path,
                              n_molecules=target_info.params.n_samples_per_dot,
                              batch_size=self.gen_batch_size, is_cgleftnet=is_cgleftnet)
        self.clean_and_score()
        if 'homo' in self.infer_target_list and 'lumo' in self.infer_target_list:
            simple_2D_plot(leftnet_result_dir=self.leftnet_result_dir, target_info=target_info)


class FingerPrintPipeline(BasePipeline):

    def run(self, target_smile: str, is_cgleftnet: bool = False, n_molecules: int = 10000, chk_db_has_sim: bool = True):
        fp_gen(target_smile=target_smile, gen_ckpt_path=self.gen_ckpt_path, n_molecules=n_molecules,
               batch_size=self.gen_batch_size, is_cgleftnet=is_cgleftnet)
        self.clean_and_score()
        simple_plot_sim(gen_db_path=self.gen_db_path, target_smile=target_smile,
                        dump_path=os.path.join(self.gen_folder, 'similarity.png'),
                        chk_db_has_sim=chk_db_has_sim, chk_db_path=self.chk_db_path)


class CompBePipeline(BasePipeline):

    def run(self, composition: str, binding_e: float, is_cgleftnet: bool = False, n_molecules: int = 10000):
        comp_be_gen(composition=composition, binding_e=binding_e, gen_ckpt_path=self.gen_ckpt_path,
                    n_molecules=n_molecules, batch_size=self.gen_batch_size, is_cgleftnet=is_cgleftnet)
        self.clean_and_score()
        if 'binding_e' in self.infer_target_list:
            simple_kde_plot(leftnet_result_dir=self.leftnet_result_dir,
                            binding_e=binding_e, chk_db_path=self.chk_db_path)


class ThreePropsPipeline(BasePipeline):

    def run(self, sp: float, rs: float, sa: float, is_cgleftnet: bool = False, n_molecules: int = 10000):
        three_props_gen(sp=sp, rs=rs, sa=sa, gen_ckpt_path=self.gen_ckpt_path,
                        n_molecules=n_molecules, batch_size=self.gen_batch_size, is_cgleftnet=is_cgleftnet)
        self.clean_and_score(decorated_property_names=three_property_names)
        three_props_plot(leftnet_result_dir=self.leftnet_result_dir)


class EDMPipeline(BasePipeline):

    def run(self, train_workbase: str, target_info: HomoLumoTargetInfo, diffusion_steps: int,
            fix_noise: bool = False, fixed_natoms=None, n_sweeps=100, n_frames=100):
        from uni_electrolyte.generator.edm_gen_workers import edm_conditional_sample

        edm_conditional_sample(train_workbase=train_workbase, target_info=target_info,
                               out_db_path=os.path.join(self.gen_folder, 'raw.db'),
                               n_sweeps=n_sweeps, n_frames=n_frames, fix_noise=fix_noise,
                               diffusion_steps=diffusion_steps, fixed_natoms=fixed_natoms)
        self.clean_and_score()
        if 'homo' in self.infer_target_list and 'lumo' in self.infer_target_list:
            simple_2D_plot(leftnet_result_dir=self.leftnet_result_dir, target_info=target_info)


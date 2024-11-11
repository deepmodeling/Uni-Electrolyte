
#registry.dp.tech/dptech/prod-17396/sub:
#增加HOMOLUMO可视化结果
#/root/launching_entry/gen_score_screen.py


import os
import shutil
from pathlib import Path
from uni_electrolyte.hamiltonian.dptb_utils import dptb_infer_from_ase_db
from uni_electrolyte.hamiltonian.common_tools import generate_cube_files, cubes_2_htmls
from uni_electrolyte.evaluator.dataset.data_transform import csv_2_db, smile_2_db, xyz_2_db
from dp.launching.cli import to_runner, SubParser, default_minimal_exception_handler, run_sp_and_exit
from dp.launching.typing import BaseModel, Field
from dp.launching.typing import InputFilePath, OutputDirectory, MinMaxRange
from dp.launching.typing import Int, Float, List, Enum, String, Set, Union, Literal, Optional
from dp.launching.typing.io import InputMoleculeContent
from uni_electrolyte.evaluator.inference import pyG_infer, pyg_infer_with_dpdispatcher, screen_csv_with_conditions
from uni_electrolyte.generator.gen_pipeline import comp_be_pipeline, homo_lumo_pipeline, fp_pipeline, \
    homo_lumo_pipeline_diff


class TargetOptions(String, Enum):
    """
    Define the target to be predicted.
    """
    binding_e = 'Binding_Energy'
    dielectric_constant = 'Dielectric_Constant'
    viscosity = 'Viscosity'
    homo = 'HOMO'
    lumo = 'LUMO'


class predict_property_only(BaseModel):
    type: Literal['predict_property_only']
    input_file_path: InputFilePath = Field(..., description='Path to input file.')
    target: Set[TargetOptions] = Field(..., description='Target to be predicted.')


def score_task(opts: predict_property_only, output_directory):
    models_path = r'/opt/ckpt/eval'
    target_list = []
    for a_target in opts.target:
        target_list.append(a_target.value)
    pyG_infer(input_file_path=opts.input_file_path.get_full_path(),
              target=target_list,
              output_directory=output_directory,
              eval_ckpt_path=models_path,
              leftnet_param={
                  'num_layers': 8,
                  'hidden_channels': 128,
                  'num_radial': 96,
                  'cutoff': 12,
              })

#########################################################################################
class predict_property_and_screen(BaseModel):
    type: Literal['predict_property_and_screen']
    HOMO_range: MinMaxRange = Field(default=(-8, -7), description="The targeted HOMO interval. In unit eV.",
                                    min_value=-9, max_value=-2, step=0.01)
    LUMO_range: MinMaxRange = Field(default=(8, 9), description="The targeted LUMO interval. In unit eV.",
                                    min_value=-4, max_value=10, step=0.01)
    binding_energy_range: MinMaxRange = Field(default=(-2, -1),
                                              description="The targeted binding_energy interval. In unit eV.",
                                              min_value=-4, max_value=0, step=0.01)
    log_viscosity_range: MinMaxRange = Field(default=(-1, -0.3),
                                             description="The targeted viscosity interval. In log form and unit mPa*s without log.",
                                             min_value=-2.25, max_value=2.25, step=0.01)
    log_dielectric_constant_range: MinMaxRange = Field(default=(0.74, 0.81),
                                                       description="The targeted dielectric constant interval. In log form",
                                                       min_value=0, max_value=2, step=0.01)
    input_file_path: InputFilePath = Field(..., description='Path to input file.')


def screen_task(opts: predict_property_and_screen, output_directory):
    models_path = r'/opt/ckpt/eval'
    pyG_infer(input_file_path=opts.input_file_path.get_full_path(),
              target=['Binding_Energy', 'Dielectric_Constant', 'Viscosity', 'HOMO', 'LUMO'],
              output_directory=output_directory,
              eval_ckpt_path=models_path,
              leftnet_param={
                  'num_layers': 8,
                  'hidden_channels': 128,
                  'num_radial': 96,
                  'cutoff': 12,
              }
              )
    os.chdir(output_directory)
    screen_csv_with_conditions(input_csv_abs_path='output_properties.csv',
                               output_csv_abs_path='screen_results.csv',
                               conditions_dict={
                                   'Binding energy(eV)': opts.binding_energy_range.get_value(),
                                   'HOMO(eV)': opts.HOMO_range.get_value(),
                                   'LUMO(eV)': opts.LUMO_range.get_value(),
                                   'Dielectric constant': [pow(10, opts.log_dielectric_constant_range.lower),
                                                           pow(10, opts.log_dielectric_constant_range.upper)],
                                   'Viscosity (mPa*s)': [pow(10, opts.log_viscosity_range.lower),
                                                         pow(10, opts.log_viscosity_range.upper)],
                               })
#########################################################################################
# Targeted formular and binding energy
class Binding_Energy_and_Formular(BaseModel):
    type: Literal['Binding_Energy_and_Formular']
    formular: String = Field(default='C4H10O2', description='The targeted formular')
    targeted_binding_e: Float = Field(default=-1, description='The targeted binding energy')
    n_molecules: Int = Field(default=500, description='Total number of molecules to be generated')
    # rascore_threshold: Optional[Float] = Field(default=0.8, description='Total number of molecules to be generated')



def be_formular_task(opts: Binding_Energy_and_Formular, output_directory):
    cwd_ = os.getcwd()
    target_list = ['Binding_Energy', 'Dielectric_Constant', 'Viscosity', 'HOMO', 'LUMO']
    # for a_target in opts.target:
    #     target_list.append(a_target.value)
    comp_be_pipeline(
        composition=opts.formular,
        binding_e=opts.targeted_binding_e,
        n_molecules=opts.n_molecules,
        infer_target_list=target_list,
        eval_batch_size=50,
        gen_batch_size=50,
        rascore_threshold=0.8,
        gen_ckpt_path=r'/opt/ckpt/gen',
        eval_ckpt_path=r'/opt/ckpt/homo_lumo_gen_utils/ckpt',
        is_reverse_infer_target_list=True,
        is_cgleftnet=True
    )
    shutil.copytree(src=os.path.join(cwd_, 'generated_molecules'),
                    dst=os.path.join(output_directory, 'Gen_with_Score_Results'))


# Generate similar molecules
class Structure_FingerPrint(BaseModel):
    type: Literal['Structure_FingerPrint']
    smiles: Optional[InputMoleculeContent] = Field(content_type="smiles", description="A smiles editor.")
    n_molecules: Int = Field(default=500, description='Total number of molecules to be generated')


def fp_task(opts: Structure_FingerPrint, output_directory):
    cwd_ = os.getcwd()
    target_list = ['Binding_Energy', 'Dielectric_Constant', 'Viscosity', 'HOMO', 'LUMO']
    # for a_target in opts.target:
    #     target_list.append(a_target.value)
    fp_pipeline(
        target_smile=opts.smiles.get_value(),
        n_molecules=opts.n_molecules,
        infer_target_list=target_list,
        eval_batch_size=50,
        gen_batch_size=50,
        rascore_threshold=0.8,
        gen_ckpt_path=r'/opt/ckpt/cg_schnet_gen',
        eval_ckpt_path=r'/opt/ckpt/homo_lumo_gen_utils/ckpt',
        is_reverse_infer_target_list=True,
    )
    shutil.copytree(src=os.path.join(cwd_, 'generated_molecules'),
                    dst=os.path.join(output_directory, 'Gen_with_Score_Results'))


# Targeted homo-lumo
class HOMO_LUMO(BaseModel):
    type: Literal['HOMO_LUMO']
    HOMO_range: MinMaxRange = Field(default=(-8, -7), description="The targeted HOMO interval. In unit eV.",
                                    min_value=-9, max_value=-2, step=0.01)
    LUMO_range: MinMaxRange = Field(default=(7, 9), description="The targeted LUMO interval. In unit eV.", min_value=-4,
                                    max_value=10, step=0.01)
    n_molecules: Int = Field(default=200, description='Total number of molecules to be generated.')


def homo_lumo_task(opts: HOMO_LUMO, output_directory):
    cwd_ = os.getcwd()
    target_list = ['Binding_Energy', 'Dielectric_Constant', 'Viscosity', 'HOMO', 'LUMO']

    n_molecules = opts.n_molecules
    import math

    n_molecules = math.ceil(n_molecules / 50) * 50
    n_dot_per_interval = math.ceil(math.sqrt(n_molecules / 50))
    homo_lumo_pipeline_diff(
        target_info={'mode': 'interval',
                     'homo': {'min': opts.HOMO_range.lower, 'max': opts.HOMO_range.upper},
                     'lumo': {'min': opts.LUMO_range.lower, 'max': opts.LUMO_range.upper},
                     'n_dot_per_interval': n_dot_per_interval,
                     'n_samples_per_dot': 50},
        infer_target_list=target_list,
        eval_batch_size=50,
        ckpt_folder_path=r'/opt/ckpt/homo_lumo_gen_utils/ckpt',
        edm_json_path=r'/opt/ckpt/homo_lumo_gen_utils/real_edm_input.json',
        classifier_json_path=r'/opt/ckpt/homo_lumo_gen_utils/real_classifier_input.json',
        is_reverse_infer_target_list=True,
        rascore_threshold=0.8,
        scale=5
    )
    shutil.copytree(src=os.path.join(cwd_, 'generated_molecules'),
                    dst=os.path.join(output_directory, 'Gen_with_Score_Results'))


class gen_Model(BaseModel):
    gen_mode: Union[HOMO_LUMO, Structure_FingerPrint, Binding_Energy_and_Formular] = Field(discriminator="type")
    output_directory: OutputDirectory = Field(default='./output')
    n_grids: Int = Field(default=75, description='The number of grids in the 3D space each dim.')


def gen_task(opts: gen_Model):
    if opts.gen_mode.type == 'HOMO_LUMO':
        homo_lumo_task(opts.gen_mode, opts.output_directory.get_full_path())
    elif opts.gen_mode.type == 'Structure_FingerPrint':
        fp_task(opts.gen_mode, opts.output_directory.get_full_path())
    elif opts.gen_mode.type == 'Binding_Energy_and_Formular':
        be_formular_task(opts.gen_mode, opts.output_directory.get_full_path())
    else:
        raise NotImplementedError

    ase_db_path =f"{opts.output_directory.get_full_path()}/Gen_with_Score_Results/synthesizable.db"
    ham_output_dir=f"{opts.output_directory.get_full_path()}/ham_output"
    # 1. get predicted hamiltonian matrix
    dptb_infer_from_ase_db(ase_db_path=ase_db_path, out_path=ham_output_dir)
    # 2. get cube files with pyscf overlap
    generate_cube_files(ase_db_path=ase_db_path, out_path=ham_output_dir, n_grid=opts.n_grids, basis='def2svp')

class score_screen_Model(BaseModel):
    Screen_Switch: Union[predict_property_only, predict_property_and_screen] = Field(discriminator="type")
    output_directory: OutputDirectory = Field(default='./output')
    n_grids: Int = Field(default=75, description='The number of grids in the 3D space each dim.')


def score_screen_task(opts: score_screen_Model):
    if opts.Screen_Switch.type == 'predict_property_only':
        score_task(opts.Screen_Switch, opts.output_directory.get_full_path())
    elif opts.Screen_Switch.type == 'predict_property_and_screen':
        screen_task(opts.Screen_Switch, opts.output_directory.get_full_path())
    else:
        raise NotImplementedError

    ase_db_path =f"{opts.output_directory.get_full_path()}/data/input.db"
    ham_output_dir=f"{opts.output_directory.get_full_path()}/ham_output"
    # 1. get predicted hamiltonian matrix
    dptb_infer_from_ase_db(ase_db_path=ase_db_path, out_path=ham_output_dir)
    # 2. get cube files with pyscf overlap
    generate_cube_files(ase_db_path=ase_db_path, out_path=ham_output_dir, n_grid=opts.n_grids, basis='def2svp')

class HOMO_LUMO_orbit_Model(BaseModel):
    n_grids: Int = Field(default=75, description='The number of grids in the 3D space each dim.')
    smiles_name: String = Field(default='smiles', description='The name of the column in the csv file.')
    csv_file_path: String = Field( description='The path of the csv file.')
    output_directory: OutputDirectory = Field(default='./output')

def HOMO_LUMO_orbit_task(opts:  HOMO_LUMO_orbit_Model):

    import pandas as pd
    df=pd.read_csv(opts.csv_file_path)

    properties=df.columns.tolist()
    smiles_idx=properties.index(opts.smiles_name)

    if not os.path.exists(opts.output_directory.get_full_path()):
        os.mkdir(opts.output_directory.get_full_path())
    ase_db_path=f"{opts.output_directory.get_full_path()}/dump.db"
    fail_smiles_path=f"{opts.output_directory.get_full_path()}/fail_smiles.txt"
    ham_output_dir=f"{opts.output_directory.get_full_path()}/ham_output"
    output_csv_path=f"{opts.output_directory.get_full_path()}/output.csv"
    csv_2_db(csv_path=opts.csv_file_path, db_path=ase_db_path, fail_smile_path=fail_smiles_path,
             properties=df.columns.tolist(), smile_idx=smiles_idx,output_csv_path=output_csv_path)
    # 1. get predicted hamiltonian matrix
    dptb_infer_from_ase_db(ase_db_path=ase_db_path, out_path=ham_output_dir)
    # 2. get cube files with pyscf overlap
    generate_cube_files(ase_db_path=ase_db_path, out_path=ham_output_dir, n_grid=opts.n_grids, basis='def2svp')
    # 3. visualize cube files
    cubes_2_htmls(out_path='ham_output', iso_value=0.03)

def to_parser():
    return {
        "score_screen": SubParser(score_screen_Model, score_screen_task, "Predict properties for uploaded database."),
        "gen_with_score": SubParser(gen_Model, gen_task, "Generate molecules and predict properties."),
        "HOMO_LUMO_orbit": SubParser(HOMO_LUMO_orbit_Model, HOMO_LUMO_orbit_task, "Clean the database."),
    }


if __name__ == '__main__':
    import sys

    run_sp_and_exit(
        to_parser(),
        description="Example",
        version="0.1.0",
        exception_handler=default_minimal_exception_handler,
    )

import os
import shutil

import numpy as np
import pandas as pd
import torch
from ase.db import connect
from torch_geometric.data import DataLoader
from uni_electrolyte.evaluator.dataset import thuEMol
from uni_electrolyte.evaluator.dataset import xyz_2_db, smile_2_db, db_2_pyG_data, edit_ase_db
from uni_electrolyte.evaluator.inference import pyG_inference_without_label
from uni_electrolyte.evaluator.model.spatial import LEFTNet
from uni_electrolyte.evaluator.trainer import pyG_trainer

decorated_property_names = {
    'binding_e': 'Binding energy(eV)',
    'homo': 'HOMO(eV)',
    'lumo': 'LUMO(eV)',
    'dielectric_constant': 'Dielectric constant',
    'viscosity': 'Viscosity (mPa*s)',
}

three_property_names = {
    'sp': 'Solvating Power',
    'rs': 'Reductive Stability',
    'sa': 'SEI-fluorinating Ability',
}

decorated_property_names_reverse = {
    'binding_e': 'Binding_Energy',
    'homo': 'HOMO',
    'lumo': 'LUMO',
    'dielectric_constant': 'Dielectric_Constant',
    'viscosity': 'Viscosity',
}

decorated_property_names_reverse = dict(
    zip(decorated_property_names_reverse.values(), decorated_property_names_reverse.keys()))


leftnet_param = {
    'num_layers': 6,
    'hidden_channels': 128,
    'num_radial': 96,
    'cutoff': 8,
}


def screen_csv_with_conditions(input_csv_abs_path: str, output_csv_abs_path: str, conditions_dict: dict):
    input_df = pd.read_csv(input_csv_abs_path)
    for column, value_range in conditions_dict.items():
        ouput_df = input_df[(input_df[column] >= value_range[0]) & (input_df[column] <= value_range[1])]
    ouput_df.to_csv(output_csv_abs_path, index=False)


def pyG_infer_from_db(db_path, target_list, eval_ckpt_path, output_directory,
                      abs_data_path=None, infer_batch_size=50, use_sigmoid=False,
                      leftnet_param=leftnet_param, decorated_property_names=decorated_property_names):
    if not abs_data_path:
        abs_data_path = output_directory
    output_directory = os.path.abspath(output_directory)

    # for Early stop and Final csv preparation
    smile_list = []
    with connect(db_path) as db:
        for a_row in db.select():
            smile_list.append(a_row.smile)
        if 'inchi' in a_row._keys:
            gen_flag = 1
        else:
            gen_flag = 0
    assert len(smile_list)>0, f'Input empty db or db has no SMILES'

    pyG_data_path = os.path.join(abs_data_path, 'input_pyG_data')
    db_2_pyG_data(db_path=db_path, properties=target_list, pyG_data_folder=pyG_data_path)
    dataset = thuEMol(root=pyG_data_path, load_target_list=target_list)
    for a_target in target_list:
        model = LEFTNet(
            num_layers=leftnet_param['num_layers'],
            hidden_channels=leftnet_param['hidden_channels'],
            num_radial=leftnet_param['num_radial'],
            cutoff=leftnet_param['cutoff'],
            use_sigmoid=use_sigmoid
        )

        a_model_path = os.path.join(eval_ckpt_path, f'{a_target}.pt')

        device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device("cpu")
        if torch.cuda.is_available():
            device = torch.device('cuda:0')
            ckpt = torch.load(a_model_path)
        else:
            device = torch.device("cpu")
            ckpt = torch.load(a_model_path, map_location=torch.device('cpu'))
        trainer = pyG_trainer()
        model.load_state_dict(ckpt['model_state_dict'])
        model.to(device=device)

        test_dataset = dataset
        print('Dataset size:', len(test_dataset))

        evaluation = pyG_inference_without_label(dump_info_path=output_directory, property=a_target)
        info = trainer.val(model=model, data_loader=DataLoader(test_dataset, infer_batch_size, shuffle=False),
                           energy_and_force=False, p=0, evaluation=evaluation, device=device)
    cwd_2 = os.getcwd()
    os.chdir(abs_data_path)
    with open('input_smile.txt', 'w') as f:
        for a_smile in smile_list:
            f.write(a_smile)
            f.write('\n')
    os.chdir(output_directory)
    info_dict = {'Smiles': smile_list}
    real_info_map = {}
    for a_target in target_list:
        a_info = np.load(f'{a_target}.npy')
        info_dict.update({decorated_property_names[a_target]: a_info})
        real_info_map.update({a_target: a_info})
    info_df = pd.DataFrame(info_dict)
    info_df.to_csv('output_properties.csv', index=False)
    os.chdir(cwd_2)
    with connect(db_path) as db, connect('temp.db') as db_w:
        for idx, a_row in enumerate(db.select()):
            an_atoms = a_row.toatoms()
            data = {}
            for a_target in target_list:
                data.update({a_target:[float(real_info_map[a_target][idx])]})
            if gen_flag:
                # data.update({'ra_score': [a_row.data['ra_score'][0]]})
                db_w.write(an_atoms, smile=a_row.smile, data=data, inchi=a_row.inchi)
            else:
                db_w.write(an_atoms, smile=a_row.smile, data=data)
    os.remove(db_path)
    os.rename(src='temp.db', dst=db_path)
    edit_ase_db(db_path=db_path, properties=target_list)




def pyG_infer(input_file_path, target, output_directory, eval_ckpt_path):
    target_list = []
    for a_target in target:
        target_list.append(decorated_property_names_reverse[a_target])
    print(target_list)

    abs_data_path = os.path.abspath(os.path.join(output_directory, 'data'))
    os.makedirs(abs_data_path, exist_ok=True)
    db_path = os.path.join(abs_data_path, 'input.db')

    file_basename = os.path.basename(input_file_path)
    if file_basename.endswith('.xyz'):
        xyz_2_db(xyz_path=input_file_path, db_path=db_path, properties=target_list)
    else:
        fail_smile_path = os.path.join(abs_data_path, 'fail_smile')
        smile_2_db(smile_path=input_file_path, db_path=db_path,
                   properties=target_list, fail_smile_path=fail_smile_path, maxAttempts=100)
    pyG_infer_from_db(db_path=db_path, target_list=target_list, eval_ckpt_path=eval_ckpt_path,
                      output_directory=output_directory, abs_data_path=abs_data_path)


def infer_one_smile(target_smile: str, eval_ckpt_path: str):
    cwd_ = os.getcwd()
    os.makedirs('leftnet_infer', exist_ok=True)
    os.chdir('leftnet_infer')
    with open('input_smile', 'w') as f_w:
        f_w.write(target_smile)
    smile_2_db(smile_path='input_smile',
               db_path=r'input.db',
               fail_smile_path='failed_smile',
               properties=list(decorated_property_names.keys()))
    pyG_infer_from_db(db_path='input.db',
                      target_list=list(decorated_property_names.keys()),
                      eval_ckpt_path=eval_ckpt_path,
                      output_directory=r'./')
    info = pd.read_csv(r'output_properties.csv')
    prop_arr = np.array([info['Binding energy(eV)'][0], info['Dielectric constant'][0], info['Viscosity (mPa*s)'][0],
                         info['HOMO(eV)'][0], info['LUMO(eV)'][0]])
    shutil.copy(src=r'output_properties.csv', dst=os.path.join(cwd_, r'input_smiles_properties.csv'))
    os.chdir(cwd_)
    return prop_arr



def pyg_infer_with_dpdispatcher(machine_info, cmdline):
    from dpdispatcher import Machine, Resources, Task, Submission

    os.environ['BOHR_TICKET'] = machine_info['ticket']

    machine_dict = {
        "batch_type": "Bohrium",
        "context_type": "Bohrium",
        'local_root': "./",

        'remote_root': './test_dpdispatcher',
        'remote_profile': {
            "email": machine_info['email'],
            "password": '',
            "project_id": machine_info['project_id'],
            "input_data": {
                "job_type": "container",
                "log_file": "log",
                "job_name": "Uni_electrolyte_property_prediction",
                "disk_size": 200,
                "scass_type": machine_info['hardware'],
                "platform": machine_info['platform'],
                "image_name": "registry.dp.tech/dptech/prod-11729/gen_score_screen:1229"
            }
        }
    }
    resource_dict = {
        'number_node': 1,
        'cpu_per_node': 4,
        'gpu_per_node': 1,
        'queue_name': "GPU",
        'group_size': 4,
        "envs": {
            "PYTHONUNBUFFERED": "true",
            "BOHR_TICKET": machine_info['ticket'],
        },
    }

    machine = Machine.load_from_dict(machine_dict=machine_dict)

    resources = Resources.load_from_dict(resource_dict)

    local_files = os.listdir('/')

    task1 = Task(
        command=cmdline,
        task_work_path='/',
        forward_files=local_files,
        backward_files=['output/*', 'out.txt'], outlog='out.txt')

    task_list = [task1]

    submission = Submission(work_base='./',
                            machine=machine,
                            resources=resources,
                            task_list=task_list,
                            forward_common_files=[],
                            backward_common_files=[]
                            )

    submission.run_submission(check_interval=10, clean=True)


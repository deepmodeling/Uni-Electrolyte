import os

import torch
from uni_electrolyte.evaluator.dataset import thuEMol
from uni_electrolyte.evaluator.inference import pyG_inference_without_label
from uni_electrolyte.evaluator.model.spatial import LEFTNet
from uni_electrolyte.evaluator.trainer import pyG_trainer
from uni_electrolyte.evaluator.dataset import xyz_2_db, smile_2_db, db_2_pyG_data
from torch_geometric.data import DataLoader


def pyG_infer(input_file_path, target, output_directory, models_path):
    output_directory = os.path.abspath(output_directory)
    abs_data_path = os.path.abspath(os.path.join(output_directory, 'data'))
    os.makedirs(abs_data_path, exist_ok=True)
    db_path = os.path.join(abs_data_path, 'input.db')
    pyG_data_path = os.path.join(abs_data_path, 'input_pyG_data')
    file_basename = os.path.basename(input_file_path)
    if file_basename.endswith('.xyz'):
        xyz_2_db(xyz_path=input_file_path, db_path=db_path, properties=[target])
    else:
        fail_smile_path = os.path.join(abs_data_path, 'fail_smile')
        smile_2_db(smile_path=input_file_path, db_path=db_path,
                   properties=[target], fail_smile_path=fail_smile_path)
    db_2_pyG_data(db_path=db_path, properties=[target], pyG_data_folder=pyG_data_path)

    model = LEFTNet(
        num_layers=6,
        hidden_channels=192,
        num_radial=96,
        cutoff=8
    )

    a_model_path = os.path.join(models_path, f'{target}.pt')

    device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device("cpu")
    trainer = pyG_trainer()
    ckpt = torch.load(a_model_path)
    model.load_state_dict(ckpt['model_state_dict'])
    model.to(device=device)
    dataset = thuEMol(root=pyG_data_path, load_target_list=[target])
    dataset.data.y = dataset.data[target]
    split_idx = dataset.get_idx_split(len(dataset.data.y), train_size=0, valid_size=0, seed=42)
    test_dataset = dataset[split_idx['test']]
    print('Dataset size:', len(test_dataset))

    evaluation = pyG_inference_without_label(dump_info_path=output_directory, property=target)
    info = trainer.val(model=model, data_loader=DataLoader(test_dataset, 50, shuffle=False),
                       energy_and_force=False, p=0, evaluation=evaluation, device=device)

import os
import shutil

import torch
from ase.db import connect
from ase.io import read
from learn_edm.eval_conditional_qm9 import get_args_gen, get_generator, get_dataloader
from learn_edm.qm9.sampling import sample_sweep_conditional
from learn_edm.qm9.utils import compute_mean_mad
from learn_edm.qm9.visualizer import save_xyz_file
from torch.distributions.categorical import Categorical
from tqdm import trange

__all__ = ['edm_conditional_sample']

def edm_conditional_sample(train_workbase: str,
                           out_db_path: str, target_info: dict, diffusion_steps: int,
                           n_sweeps=100, n_frames=100, fix_noise: bool=False, fixed_natoms=None):
    if fix_noise:
        print('Caution: fix_noise is ture, meaning samples in the same sweep will use the same noise.')
    else:
        print('Caution: fix_noise is false, may encounter warnings.')


    args = get_args_gen(dir_path=train_workbase)
    dataloaders = get_dataloader(args)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    property_norms = compute_mean_mad(dataloaders, args.conditioning, args.dataset)

    model, nodes_dist, prop_dist, dataset_info = get_generator(dir_path=train_workbase,
                                                               dataloaders=dataloaders,
                                                               device=device,
                                                               args_gen=args,
                                                               property_norms=property_norms,
                                                               is_update=True)
    model.T = diffusion_steps
    output_temp_dir = './temp'


    n_nodes_dist_train_dict = dataset_info['n_nodes']
    n_nodes_list = list(n_nodes_dist_train_dict.keys())
    counts_list = list(n_nodes_dist_train_dict.values())
    torch_nodes_dist = Categorical(torch.tensor(counts_list))

    num_conditions = len(prop_dist.distributions)
    total_num = (n_frames**num_conditions)*n_sweeps
    print(f'Total generated molecules is: {total_num}.')
    with connect(out_db_path) as db:
        for iii in trange(n_sweeps):
            if fixed_natoms:
                nodesxsample = torch.tensor([fixed_natoms]*(n_frames ** num_conditions))
            else:
                index_sample = torch_nodes_dist.sample((n_frames ** num_conditions,))
                nodesxsample = torch.tensor([n_nodes_list[i] for i in index_sample])

            # print(nodesxsample)
            one_hot, charges, x, node_mask = sample_sweep_conditional(args=args, device=device,
                                                                      generative_model=model, target_info=target_info,
                                                                      dataset_info=dataset_info, prop_dist=prop_dist,
                                                                      n_frames=n_frames, nodesxsample=nodesxsample,
                                                                      fix_noise=fix_noise)
            save_xyz_file(output_dir=output_temp_dir, one_hot=one_hot, positions=x,
                          dataset_info=dataset_info, name='conditional', node_mask=node_mask)
            for a_file in os.listdir(output_temp_dir):
                an_atoms = read(os.path.join(output_temp_dir, a_file))
                db.write(an_atoms)
            shutil.rmtree(output_temp_dir)



# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.



from collator import collator
from custom_dataset import EmbeddingDataset

from pytorch_lightning import LightningDataModule
#import torch
from torch.nn import functional as F
from torch.utils.data import DataLoader

from functools import partial

dataset = None

def get_dataset(dataset_name,input_file=None,loaded_target_list=None):
    global dataset

    # if dataset is not None:  #这两行代码会导致每次query不更新dm
    #     return dataset

    # max_node is set to max(max(num_val_graph_nodes), max(num_test_graph_nodes))

    dataset = {
        # 'num_class':
        #'loss_fn': F.binary_cross_entropy,
        'metric': 'train_loss',
        'dataset': EmbeddingDataset(root="data/"+dataset_name,input_file=input_file,loaded_target_list=loaded_target_list),
        'max_node': 1000,
    }

    print(f' > {dataset_name} loaded!')
    print(dataset)
    print(f' > dataset info ends')
    return dataset


class GraphDataModule(LightningDataModule):
    def __init__(
        self,
        dataset_name,
        input_file=None,
        num_workers: int = 0,
        batch_size: int = 1,
        seed: int = 42,
        multi_hop_max_dist: int = 5,
        rel_pos_max: int = 1024,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.dataset_name = dataset_name
        self.dataset = get_dataset(self.dataset_name,input_file=input_file)
        self.dataset_test = self.dataset['dataset']
       
        
        self.num_workers = num_workers
        self.batch_size = batch_size

        self.multi_hop_max_dist = multi_hop_max_dist
        self.rel_pos_max = rel_pos_max
        self.seed = seed
        



    def setup(self, stage: str = None):
        self.dataset_test = self.dataset['dataset']

    def test_dataloader(self):
        loader = DataLoader(
            self.dataset_test,
            batch_size=1,
            shuffle=False,
            num_workers=self.num_workers,
            pin_memory=True,
            persistent_workers = True,
            collate_fn=partial(collator, max_node=9999, multi_hop_max_dist=self.multi_hop_max_dist, rel_pos_max=self.rel_pos_max),
        )
        print('len(test_dataloader)', len(loader))
        return loader
    
    def predict_dataloader(self):
        loader = DataLoader(
            self.dataset_test,
            batch_size=1,
            shuffle=False,
            num_workers=self.num_workers,
            pin_memory=True,
            persistent_workers = True,
            collate_fn=partial(collator, max_node=9999, multi_hop_max_dist=self.multi_hop_max_dist, rel_pos_max=self.rel_pos_max),
        )
        print('len(test_dataloader)', len(loader))
        return loader


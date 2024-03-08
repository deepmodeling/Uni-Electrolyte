# A torch-geometric inference script to properly incorporate Thu-ChenXiang electrolyte database.
# Part of this code are borrowed from dive-into-graph project,
# see https://github.com/divelab/DIG/blob/dig-stable/dig/threedgraph/evaluation/eval.py


import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import torch
from .visualize import plot_heatmap, plot_rank, plot_rel, rename_file
from scipy import stats
from sklearn.metrics import r2_score

class pyG_inference_test:
    def __init__(self, dump_info_path: str, info_file_flag: str, property: str):
        os.makedirs(dump_info_path, exist_ok=True)
        self.dump_info_path = os.path.abspath(dump_info_path)
        self.info_file_flag = info_file_flag
        self.property = property

    def eval(self, input_dict, use_r2_score: bool=True):
        cwd_ = os.getcwd()
        y_pred, y_true = input_dict['y_pred'], input_dict['y_true']
        os.chdir(self.dump_info_path)
        y_pred_flatten = torch.flatten(y_pred).detach().cpu().numpy()
        y_true_flatten = torch.flatten(y_true).detach().cpu().numpy()

        if self.property in ['viscosity', 'dielectric_constant']:
            y_true_flatten = pow(10, y_true_flatten)
            y_pred_flatten = pow(10, y_pred_flatten)

        with open("pred", "w") as pred:
            pred.writelines(list(map(lambda x: str(x) + "\n", y_pred_flatten)))
        with open("target", "w") as true:
            true.writelines(list(map(lambda x: str(x) + "\n", y_true_flatten)))
        if use_r2_score:
            r = r2_score(y_true_flatten, y_pred_flatten)
        else:
            r, _ = stats.pearsonr(y_true_flatten, y_pred_flatten)
        r = round(r, 3)
        mae_e = np.mean(np.abs(y_true_flatten - y_pred_flatten))
        mae_e = round(mae_e, 3)
        print(f'{self.info_file_flag} mae: {str(mae_e)}\n')
        print(f'{self.info_file_flag} corr: {str(r)}\n')
        plot_rel(label=y_true_flatten, prediction=y_pred_flatten, flag=self.info_file_flag, mae=mae_e, r2=r)
        plot_heatmap(label=y_true_flatten, prediction=y_pred_flatten, flag=self.info_file_flag, mae=mae_e, r2=r)
        plot_rank(label=y_true_flatten, prediction=y_pred_flatten, flag=self.info_file_flag, use_r2_score=use_r2_score)
        rename_file(flag=self.info_file_flag)
        os.chdir(cwd_)

        return {'mae': mae_e}


class pyG_inference_train:
    def __init__(self):
        pass

    def eval(self, input_dict):
        y_pred, y_true = input_dict['y_pred'], input_dict['y_true']
        y_pred_flatten = torch.flatten(y_pred).detach().cpu().numpy()
        y_true_flatten = torch.flatten(y_true).detach().cpu().numpy()

        mae_e = np.mean(np.abs(y_true_flatten - y_pred_flatten))

        return {'mae': mae_e}


class pyG_inference_without_label:
    def __init__(self, dump_info_path: str, property: str):
        os.makedirs(dump_info_path, exist_ok=True)
        self.dump_info_path = os.path.abspath(dump_info_path)
        self.property = property

    def eval(self, input_dict):
        cwd_ = os.getcwd()
        y_pred = input_dict['y_pred']
        os.chdir(self.dump_info_path)
        y_pred_flatten = torch.flatten(y_pred).detach().cpu().numpy()
        if self.property in ['viscosity', 'dielectric_constant']:
            y_pred_flatten = pow(10, y_pred_flatten)

        with open(f"{self.property}", "w") as pred:
            pred.writelines(list(map(lambda x: str(x) + "\n", y_pred_flatten)))

        np.save(f"{self.property}.npy", y_pred_flatten)
        os.chdir(cwd_)

        return {'mae': None}

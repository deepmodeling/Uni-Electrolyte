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

def reversed_ratio_fun(pred_list,true_list):
    # reverse_ratio
    pair_list = list(zip(pred_list,true_list))
    pair_list.sort(key=lambda x: x[1])
    r_num = 0
    for i, pair1 in enumerate(pair_list):
        for j, pair2 in enumerate(pair_list):
            if j > i:
                if pair2[0] < pair1[0]:
                    r_num += 1
    total_pair_num = len(pair_list) * (len(pair_list) - 1) / 2
    reversed_ratio = r_num / total_pair_num

    return reversed_ratio

def value_precision_recall(pred_list, true_list, value):
    TP=np.sum(np.logical_and(pred_list<value ,true_list<value))
    P=np.sum(pred_list<value )
    T=np.sum(true_list<value)
    precision=TP/P
    recall=TP/T
    return precision,recall,T


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
            log_y_true_flatten=y_true_flatten
            log_y_pred_flatten=y_pred_flatten
            y_true_flatten = pow(10, y_true_flatten)
            y_pred_flatten = pow(10, y_pred_flatten)
            #

        with open("pred", "w") as pred:
            pred.writelines(list(map(lambda x: str(x) + "\n", y_pred_flatten)))
        with open("target", "w") as true:
            true.writelines(list(map(lambda x: str(x) + "\n", y_true_flatten)))
        output_dict={"y_true":input_dict["y_true"].flatten().tolist(),"y_pred":input_dict["y_pred"].flatten().tolist()}
        df=pd.DataFrame(output_dict)
        df.to_csv("pred_target_%s.csv"%(self.property))
        if use_r2_score:
            r = r2_score(y_true_flatten, y_pred_flatten)
        else:
            r, _ = stats.pearsonr(y_true_flatten, y_pred_flatten)
        r = round(r, 3)
        mae_e = np.mean(np.abs(y_true_flatten - y_pred_flatten))
        mae_e = round(mae_e, 3)

        mae_ratio = np.average(np.abs(y_pred_flatten /y_true_flatten - 1))
        mae_ratio=round(mae_ratio,3)
        spearmanr_v=round(stats.spearmanr( y_pred_flatten,y_true_flatten)[0],3)
        reversed_ratio=round(reversed_ratio_fun(y_pred_flatten,y_true_flatten),3)

        if self.property in ['viscosity', 'dielectric_constant']:
            log_mae = float(np.mean(np.abs(log_y_true_flatten - log_y_pred_flatten)))
            print('%s log mae: %.3f' % (self.info_file_flag, log_mae))
        print(f'{self.info_file_flag} mae: {str(mae_e)}')
        print(f'{self.info_file_flag} corr: {str(r)}')
        print(f'{self.info_file_flag} mae_ratio: {str(mae_ratio)}')
        print(f'{self.info_file_flag} spearmanr: {str(spearmanr_v)}')
        print(f'{self.info_file_flag} reversed_ratio: {str(reversed_ratio)}')
        plot_rel(label=y_true_flatten, prediction=y_pred_flatten, flag=self.info_file_flag, mae=mae_e, r2=r)
        plot_heatmap(label=y_true_flatten, prediction=y_pred_flatten, flag=self.info_file_flag, mae=mae_e, r2=r)
        plot_rank(label=y_true_flatten, prediction=y_pred_flatten, flag=self.info_file_flag, use_r2_score=use_r2_score)
        rename_file(flag=self.info_file_flag)
        os.chdir(cwd_)

        return {'mae': mae_e}


class pyG_inference_train:
    def __init__(self,property:str):
        self.property=property
        pass

    def eval(self, input_dict,use_r2_score:bool=True):



        y_pred, y_true = input_dict['y_pred'], input_dict['y_true']
        y_pred_flatten = torch.flatten(y_pred).detach().cpu().numpy()
        y_true_flatten = torch.flatten(y_true).detach().cpu().numpy()
        if self.property in ['viscosity', 'dielectric_constant']:
            log_y_true_flatten=y_true_flatten
            log_y_pred_flatten=y_pred_flatten
            y_true_flatten = pow(10, y_true_flatten)
            y_pred_flatten = pow(10, y_pred_flatten)


        if use_r2_score:
            r = r2_score(y_true_flatten, y_pred_flatten)
        else:
            r, _ = stats.pearsonr(y_true_flatten, y_pred_flatten)
        r = round(r, 3)
        mae_e = float(np.mean(np.abs(y_true_flatten - y_pred_flatten)))
        mae_e = round(mae_e, 3)

        mae_ratio = np.average(np.abs(y_pred_flatten /y_true_flatten - 1))
        mae_ratio=round(mae_ratio,3)
        spearmanr_v=round(stats.spearmanr( y_pred_flatten,y_true_flatten)[0],3)
        reversed_ratio=round(reversed_ratio_fun(y_pred_flatten,y_true_flatten),3)

        if self.property in ['viscosity', 'dielectric_constant']:
            log_mae = float(np.mean(np.abs(log_y_true_flatten - log_y_pred_flatten)))
            print(' log mae: %.3f' % ( log_mae))
        print(f' mae: {str(mae_e)}')
        print(f' corr: {str(r)}')
        print(f' mae_ratio: {str(mae_ratio)}')
        print(f' spearmanr: {str(spearmanr_v)}')
        print(f'  reversed_ratio: {str(reversed_ratio)}')


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

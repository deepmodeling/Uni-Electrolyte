# Copyright AISI


import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import torch
from scipy import stats
import shutil
from warnings import simplefilter



def rename_file(flag):
    os.rename(src='pred', dst=f'{flag}_pred')
    os.rename(src='target', dst=f'{flag}_target')


def file_2_npy(file_path: str):
    value_list = []
    with open(file_path, 'r') as f_r:
        for a_line in f_r.readlines():
            a_line.strip()
            value_list.append(float(a_line))
    return np.array(value_list)


def plot_rel(label, prediction, flag: str, mae: float, r2: float, ):
    fig = plt.figure()

    sns_data = pd.DataFrame({'Prediction': prediction, 'Label': label})

    sns.set_theme(style="darkgrid")
    cmap = sns.light_palette((260, 75, 60), input="husl", as_cmap=True)
    g = sns.jointplot(y='Prediction', x='Label', marker='+', label='Distribution Dots', truncate=False,
                      kind='reg', data=sns_data, palette=cmap,
                      line_kws={'label': 'Regression Line'})

    plt.plot(label, label, label=f"Reference Line", c='y')
    plt.legend(loc='best')
    plt.savefig(f'{flag}_scatter_corr_{str(r2)}_mae_{str(mae)}.png', dpi=400)
    plt.close()


def plot_rank(label, prediction, flag: str):
    label = np.array(label)
    prediction = np.array(prediction)

    info_dict = dict(zip(label, prediction))
    ranks = []
    new_prediction = []
    new_prediction_rank = []
    sorted_label = sorted(label)
    for a_rank, a_label in enumerate(sorted_label):
        ranks.append(a_rank)
        a_prediction = info_dict[a_label]
        new_prediction.append(a_prediction)
        for idx, an_old_pred in enumerate(sorted(prediction)):
            if an_old_pred == a_prediction:
                new_prediction_rank.append(idx)
                break

    ######################################################################################################################
    ######################################################################################################################

    fig = plt.figure()
    plt.scatter(ranks, new_prediction, label='Corresponding prediction', marker='x')
    plt.scatter(ranks, sorted_label, label='Sorted label', marker='+')
    plt.xlabel('Ranks')
    plt.ylabel('Values')
    plt.legend(loc='best')
    plt.savefig(f'{flag}_Sorted_label_prediction.png', dpi=400, bbox_inches='tight')
    plt.close()

    ######################################################################################################################
    ######################################################################################################################

    fig = plt.figure()
    plt.scatter(ranks, new_prediction_rank, marker='+')
    plt.xlabel('Ranks')
    plt.ylabel('Corresponding ranks')
    spearman = stats.spearmanr(label.copy(), prediction.copy())[0]
    spearman = round(spearman, 3)
    plt.savefig(f'{flag}_spearman_{str(spearman)}.png', dpi=400, bbox_inches='tight')
    plt.close()

    ######################################################################################################################
    ######################################################################################################################

    fig = plt.figure()
    plt.scatter(np.arange(100), new_prediction[:100], label='Corresponding prediction', marker='x')
    plt.scatter(np.arange(100), sorted_label[:100], label='Sorted label', marker='+')
    plt.xlabel('Ranks')
    plt.ylabel('Values')
    plt.legend(loc='best')

    r, _ = stats.pearsonr(new_prediction[:100].copy(), sorted_label[:100].copy())
    r = round(r, 3)
    plt.title(f'Correlation: {str(r)}')
    plt.savefig(f'{flag}_top_100_corr_{str(r)}.png', dpi=400, bbox_inches='tight')
    plt.close()

    ######################################################################################################################
    ######################################################################################################################

    fig = plt.figure()
    plt.scatter(ranks[-100:], new_prediction[-100:], label='Corresponding prediction', marker='x')
    plt.scatter(ranks[-100:], sorted_label[-100:], label='Sorted label', marker='+')
    plt.xlabel('Ranks')
    plt.ylabel('Values')
    plt.legend(loc='best')

    r, _ = stats.pearsonr(new_prediction[-100: ].copy(), sorted_label[-100: ].copy())
    r = round(r, 3)
    plt.title(f'Correlation: {str(r)}')

    plt.savefig(f'{flag}_bottom_100_corr_{str(r)}.png', dpi=400, bbox_inches='tight')
    plt.close()

    ######################################################################################################################
    ######################################################################################################################

    fig = plt.figure()
    plt.scatter(np.arange(100), new_prediction_rank[:100], marker='+')
    plt.plot(np.arange(100), np.arange(100), label='Reference')
    plt.ylim(0, 100)
    plt.xlabel('Ranks')
    plt.ylabel('Corresponding ranks')
    tracker = 0
    for a_rank in new_prediction_rank[:100]:
        if a_rank < 100:
            tracker = tracker + 1
    plt.legend(loc='best')

    spearman = stats.spearmanr(np.array(sorted_label)[:100].copy(), np.array(new_prediction)[:100].copy())[0]
    spearman = round(spearman, 3)
    plt.title(f'Spearman: {str(spearman)}')

    plt.savefig(f'{flag}_top_100_hit_{str(tracker)}_spearman_{spearman}.png', dpi=400, bbox_inches='tight')
    plt.close()

######################################################################################################################
######################################################################################################################
    fig = plt.figure()
    plt.scatter(ranks[-100:], new_prediction_rank[-100:], marker='+')

    spearman = stats.spearmanr(np.array(sorted_label)[-100:].copy(), np.array(new_prediction)[-100:].copy())[0]
    spearman = round(spearman, 3)
    plt.title(f'Spearman: {str(spearman)}')

    plt.xlabel('Ranks')
    plt.ylabel('Corresponding ranks')
    tracker = 0
    for a_rank in new_prediction_rank[-100:]:
        if a_rank > ranks[-100]:
            tracker = tracker + 1

    plt.plot(ranks[-100:], ranks[-100:], label='Reference')
    plt.ylim(ranks[-100], ranks[-1])

    plt.legend(loc='best')
    plt.savefig(f'{flag}_bottom_100_hit_{str(tracker)}_spearman_{spearman}.png', dpi=400, bbox_inches='tight')
    plt.close()



def plot_heatmap(label, prediction, flag: str, mae: float, r2: float,
                xlim_a=0, xlim_b=0, ylim_a=0, ylim_b=0, x_y_range=1, ):
    label = np.array(label)
    prediction = np.array(prediction)

    fig = plt.figure()
    front1 = {'weight': 'normal', 'size': 12}
    front2 = {'weight': 'normal', 'size': 14}

    plt.xlabel(f'Label of {flag}', front1)  # 绘制x轴
    plt.ylabel(f'Prediction of {flag}', front1)  # 绘制y轴
    plt.tick_params(axis='both', which='major', length=6, width=2, direction='in', labelsize=14)  # 设置主坐标轴刻度大小
    plt.tick_params(axis='both', which='minor', length=3, width=1, direction='in', labelsize=14)  # 设置次坐标轴刻度大小

    x = label
    y = prediction
    # Calculate the point density
    xy = np.vstack([x, y])
    z = stats.gaussian_kde(xy)(xy)

    # Sort the points by density, so that the densest points are plotted last
    idx = z.argsort()
    x, y, z = x[idx], y[idx], z[idx]

    ax = plt.gca()

    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    ax.spines['right'].set_linewidth(2)
    ax.spines['top'].set_linewidth(2)
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'

    plt.scatter(x, y, c=z, cmap='Reds', marker='+')
    x_ = [min(label) - x_y_range, max(label) + x_y_range]
    y_ = x_
    plt.plot(x_, y_, ls='--', c='k', alpha=0.5)

    cb1 = plt.colorbar()

    font = {
            'color': 'black',
            'weight': 'normal',
            'size': 10,
            }

    cb1.set_label('Density', fontdict=font)

    if xlim_a != 0 and xlim_b != 0:
        plt.xlim(xlim_a, xlim_b)
    if ylim_a != 0 and ylim_b != 0:
        plt.ylim(ylim_a, ylim_b)
    plt.subplots_adjust(left=0.15)  # 左边距

    # plt.show()
    plt.savefig(f'{flag}_heatmap_corr_{str(r2)}_mae_{str(mae)}.png', dpi=400)
    plt.close()

# a warnning about deprecated pandas feature is filter out
simplefilter(action='ignore', category=FutureWarning)
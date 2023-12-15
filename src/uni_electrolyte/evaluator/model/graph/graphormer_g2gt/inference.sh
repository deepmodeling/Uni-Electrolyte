# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

#!/usr/bin/env bash

[ -z "${arch}" ] && arch="--ffn_dim 2048 --hidden_dim 768 --dropout_rate 0.1 \
--intput_dropout_rate 0.1 --attention_dropout_rate 0.1 --n_layer 8 \
--peak_lr 2.5e-4 --end_lr 1e-6 --head_size 24 --weight_decay 0.00 \
--edge_type one_hop --warmup_updates 1000 --tot_updates 500000"
[ -z "$ckpt_name" ] && ckpt_name=last.ckpt
default_root_dir=$PWD
export NCCL_SOCKET_IFNAME=lo
export CUDA_VISIBLE_DEVICES=0
n_gpu=1
\
python entry.py --input_file qsar.csv --output_file qsar --num_workers 5 --seed 0 --batch_size 1 \
      --dataset_name qsar \
      --gpus $n_gpu --accelerator ddp  $arch \
      --default_root_dir $default_root_dir \
      --progress_bar_refresh_rate 1 \
      # --limit_predict_batches=0.05


# copy to target
# mkdir -p logits/$ckpt_name
# cp y_pred.pt logits/$ckpt_name/y_pred.pt

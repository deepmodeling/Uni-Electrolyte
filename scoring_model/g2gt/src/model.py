# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

#from IPython import embed
from data import get_dataset
from lr import PolynomialDecayLR
from torch.optim.lr_scheduler import CyclicLR
# from torchmetrics import PrecisionRecallCurve
# import sys
import torch
import math
import torch.nn as nn
import pytorch_lightning as pl
from utils.flag import flag, flag_bounded
import numpy as np
import torch.nn.functional as F
import sys
#from pprint import pprint
from torch.autograd import Variable
np.set_printoptions(threshold=sys.maxsize)
torch.set_printoptions(threshold=sys.maxsize)
torch.set_printoptions(precision=10)
#from scipy.spatial.distance import cdist
from scipy import sparse as sp
import pandas as pd
#import scipy
import networkx as nx
np.random.seed(0)
#import random


# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

IF_3D=False

def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

def softplus_inverse(x):
    return x + np.log(-np.expm1(-x))

class RBFLayer(nn.Module):
    def __init__(self, K=64, cutoff=10, dtype=torch.float):
        super().__init__()
        self.cutoff = cutoff

        centers = torch.tensor(softplus_inverse(np.linspace(1.0, np.exp(-cutoff), K)), dtype=dtype)
        self.centers = nn.Parameter(F.softplus(centers))

        widths = torch.tensor([softplus_inverse(0.5 / ((1.0 - np.exp(-cutoff) / K)) ** 2)] * K, dtype=dtype)
        self.widths = nn.Parameter(F.softplus(widths))
    def cutoff_fn(self, D):
        x = D / self.cutoff
        x3, x4, x5 = torch.pow(x, 3.0), torch.pow(x, 4.0), torch.pow(x, 5.0)
        return torch.where(x < 1, 1-6*x5+15*x4-10*x3, torch.zeros_like(x))
    def forward(self, D):
        D = D.unsqueeze(-1)
        return self.cutoff_fn(D) * torch.exp(-self.widths*torch.pow((torch.exp(-D) - self.centers), 2))

@torch.jit.script
def gaussian(x, mean, std):
    pi = 3.14159
    a = (2*pi) ** 0.5
    return torch.exp(-0.5 * (((x - mean) / std) ** 2)) / (a * std)

class GaussianLayer(nn.Module):
    def __init__(self, K=128, edge_types=1024):
        super().__init__()
        self.K = K
        self.means = nn.Embedding(1, K)
        self.stds = nn.Embedding(1, K)
        self.mul = nn.Embedding(edge_types, 1)
        self.bias = nn.Embedding(edge_types, 1)
        nn.init.uniform_(self.means.weight, 0, 3)
        nn.init.uniform_(self.stds.weight, 0, 3)
        nn.init.constant_(self.bias.weight, 0)
        nn.init.constant_(self.mul.weight, 1)

    def forward(self, x, edge_types):
        mul = self.mul(edge_types)
        bias = self.bias(edge_types)
        x = mul * x.unsqueeze(-1) + bias
        x = x.expand(-1, -1, -1, self.K)
        mean = self.means.weight.float().view(-1)
        std = self.stds.weight.float().view(-1).abs() + 1e-5
        return gaussian(x.float(), mean, std).type_as(self.means.weight)

class NonLinear(nn.Module):
    def __init__(self, input, output_size, hidden=None):
        super(NonLinear, self).__init__()
        if hidden is None:
            hidden = input
        self.layer1 = nn.Linear(input, hidden)
        self.layer2 = nn.Linear(hidden, output_size)

    def forward(self, x):
        x = F.gelu(self.layer1(x))
        x = self.layer2(x)
        return x


class GraphFormer(pl.LightningModule):
    def __init__(
            self,
            n_layers,
            head_size,
            hidden_dim,
            dropout_rate,
            intput_dropout_rate,
            weight_decay,
            ffn_dim,
            dataset_name,
            warmup_updates,
            tot_updates,
            peak_lr,
            end_lr,
            edge_type,
            multi_hop_max_dist,
            attention_dropout_rate,
            flag=False,
            flag_m=3,
            flag_step_size=1e-3,
            flag_mag=1e-3,
            
        ):
        super().__init__()
        self.save_hyperparameters()
        self.head_size = head_size

        offset = 4


        self.atom_encoder = nn.Embedding(128 * 37 + 1, hidden_dim, padding_idx=0)
        self.edge_encoder = nn.Embedding(128 * 6 + 1, head_size, padding_idx=0)
        self.edge_type = edge_type
        if self.edge_type == 'multi_hop':
            self.edge_dis_encoder = nn.Embedding(128 * head_size * head_size,1)
        self.rel_pos_encoder = nn.Embedding(512, head_size, padding_idx=0)
        self.in_degree_encoder = nn.Embedding(512, hidden_dim, padding_idx=0)
        self.out_degree_encoder = nn.Embedding(512, hidden_dim, padding_idx=0)

        self.input_dropout = nn.Dropout(intput_dropout_rate)
        encoders = [EncoderLayer(hidden_dim, ffn_dim, dropout_rate, attention_dropout_rate, head_size)
                    for _ in range(n_layers)]

        
        '''NEW=============================================='''
        self.gelu = nn.GELU()
        self.atom_edge_encoder = nn.Embedding(118*4+32+(2)+1+20+offset, hidden_dim, padding_idx=0) # atom*chiral +bond+start+end+0+gapnumber+[nh] offset
        self.centrality_encoder = nn.Embedding(32, head_size, padding_idx=0)
        self.lpe_linear = nn.Linear(2,head_size)
        #self.lpe_linear2 = nn.Linear(head_size,head_size)
        self.lpe_linear3 = nn.Linear(30,head_size)
        self.position = PositionalEncoding(hidden_dim,0)
        
        self.outp_logits = nn.Linear(hidden_dim, 118*4+32+(2)+1+20+offset)
        
        ### ===== DECODER =====. need hidden_dim2, ffn_dim2
        
        decoders=[DecoderLayer(hidden_dim,ffn_dim, dropout_rate, attention_dropout_rate, head_size) for _ in range(n_layers)]
        self.decoderLayers = nn.ModuleList(decoders)
        self.layers = nn.ModuleList(encoders)
        


        self.graph_token = nn.Embedding(2, hidden_dim)
        self.graph_token_virtual_distance = nn.Embedding(1, head_size)
        
        #todo fix eval
        # self.evaluator = get_dataset(dataset_name)['evaluator']
        self.metric = get_dataset(dataset_name)['metric']
        #self.loss_fn = get_dataset(dataset_name)['loss_fn']
        self.dataset_name = dataset_name
        
        self.warmup_updates = warmup_updates
        self.tot_updates = tot_updates
        self.peak_lr = peak_lr
        self.end_lr = end_lr
        self.weight_decay = weight_decay
        self.multi_hop_max_dist = multi_hop_max_dist

        self.flag = flag
        self.flag_m = flag_m
        self.flag_step_size = flag_step_size
        self.flag_mag = flag_mag
        self.hidden_dim = hidden_dim
        self.automatic_optimization = not self.flag
 
        K = 256
        cutoff = 10
        self.rbf = RBFLayer(K, cutoff)
        self.rel_pos_3d_proj = nn.Linear(K, head_size)

        unfreeze = True
        
        self.atom_encoder.weight.requires_grad = unfreeze
        self.edge_encoder.weight.requires_grad = unfreeze
        self.rel_pos_encoder.weight.requires_grad = unfreeze
        self.in_degree_encoder.weight.requires_grad = unfreeze
        self.out_degree_encoder.weight.requires_grad = unfreeze

        self.atom_edge_encoder.weight.requires_grad = unfreeze
        self.centrality_encoder.weight.requires_grad = unfreeze
        self.lpe_linear.weight.requires_grad = unfreeze
        self.lpe_linear3.weight.requires_grad = unfreeze
        
        self.graph_token.weight.requires_grad = unfreeze
        self.graph_token_virtual_distance.weight.requires_grad = unfreeze


        #3D
        if IF_3D:
            self.bias_proj = NonLinear(K, head_size)
            self.gbf  = GaussianLayer(K,1056) #32*32+32 corresponds to the paired atomic num feature,which may be insufient
            self.edge_proj = nn.Linear(K, hidden_dim)
    def translate_encoder(self,batched_data, beam=1, perturb=None, y=None, valid = True):
        """Get output of encoder."""
        attn_bias, rel_pos, x ,_3D_pos= batched_data.attn_bias, batched_data.rel_pos, batched_data.x,batched_data.pos


        """
        attn_bias:(batch_num,atom_num+1,atom_num+1)  #+1是头部字符
        rel_pos，all_rel_pos_3d_1:(batch_num,atom_num,atom_num) ，20230905 目前这两个都是对称的拓扑距离矩阵，rel_pos比all_rel_pos_3d_1 大1
        x:(batch_num,atom_num,28)  0号特征为原子数
        """
        # import pdb
        # pdb.set_trace()
        in_degree, out_degree = batched_data.in_degree, batched_data.in_degree
        edge_input, attn_edge_type = batched_data.edge_input, batched_data.attn_edge_type
        all_rel_pos_3d_1 = batched_data.all_rel_pos_3d_1


        #3D feature & attn_bias
        if IF_3D:
            atomic_nums=x[:,:,0] #原子序数特征
            padding_mask=atomic_nums==0  # batch_size*atom_num mask mat
            batch_num=atomic_nums.shape[0]
            atom_num=atomic_nums.shape[1]
            edge_pair_atomic_num_type = atomic_nums.view(batch_num, atom_num, 1) *32 + atomic_nums.view(batch_num, 1, atom_num)
            delta_pos = _3D_pos.unsqueeze(1) - _3D_pos.unsqueeze(2)
            dist = delta_pos.norm(dim=-1)
            delta_pos /= dist.unsqueeze(-1) + 1e-5
            gbf_feature = self.gbf(dist, edge_pair_atomic_num_type)


            _3D_edge_features = gbf_feature.masked_fill(padding_mask.unsqueeze(1).unsqueeze(-1), 0.0)
            _3D_edge_features =self.edge_proj(_3D_edge_features.sum(dim=-2))

            _3d_graph_attn_bias = self.bias_proj(gbf_feature).permute(0, 3, 1, 2).contiguous()
            _3d_graph_attn_bias.masked_fill_(padding_mask.unsqueeze(1).unsqueeze(2), float("-inf"))

        #实时计算graph_attention_bias矩阵矩阵:(batch_num,head_size,atom_num+1,atom_num+1)
        # graph_attn_bias
        n_graph, n_node = x.size()[:2]
        graph_attn_bias = attn_bias.clone()
        #unsqueeze for multihead
        graph_attn_bias = graph_attn_bias.unsqueeze(1).repeat(1, self.head_size, 1, 1) # [n_graph, n_head, n_node+1, n_node+1]

        # rel pos
        rel_pos_bias = self.rel_pos_encoder(rel_pos).permute(0, 3, 1, 2) # [n_graph, n_node, n_node, n_head] -> [n_graph, n_head, n_node, n_node]
        graph_attn_bias[:, :, 1:, 1:] = graph_attn_bias[:, :, 1:, 1:] + rel_pos_bias

        rbf_result = self.rel_pos_3d_proj(self.rbf(all_rel_pos_3d_1)).permute(0, 3, 1, 2)
        graph_attn_bias[:, :, 1:, 1:] = graph_attn_bias[:, :, 1:, 1:] + rbf_result

        #3D
        if IF_3D:
            graph_attn_bias[:, :, 1:, 1:] = graph_attn_bias[:, :, 1:, 1:]+ _3d_graph_attn_bias  # 20230914


        # reset rel pos here
        t = self.graph_token_virtual_distance.weight.view(1, self.head_size, 1)  #add learnable para to head node of attn bias 
        graph_attn_bias[:, :, 1:, 0] = graph_attn_bias[:, :, 1:, 0] + t
        graph_attn_bias[:, :, 0, :] = graph_attn_bias[:, :, 0, :] + t

        # edge feature
        if self.edge_type == 'multi_hop':
            rel_pos_ = rel_pos.clone()
            rel_pos_[rel_pos_ == 0] = 1 # set pad to 1
            rel_pos_ = torch.where(rel_pos_ > 1, rel_pos_ - 1, rel_pos_) # set 1 to 1, x > 1 to x - 1
            if self.multi_hop_max_dist > 0:
                rel_pos_ = rel_pos_.clamp(0, self.multi_hop_max_dist)
                edge_input = edge_input[:, :, :, :self.multi_hop_max_dist, :]
            edge_input = self.edge_encoder(edge_input).mean(-2) #[n_graph, n_node, n_node, max_dist, n_head]
            max_dist = edge_input.size(-2)
            try:
                edge_input_flat = edge_input.permute(3,0,1,2,4).reshape(max_dist, -1, self.head_size)
                edge_input_flat = torch.bmm(edge_input_flat, self.edge_dis_encoder.weight.reshape(-1, self.head_size, self.head_size)[:max_dist, :, :])
                edge_input = edge_input_flat.reshape(max_dist, n_graph, n_node, n_node, self.head_size).permute(1,2,3,0,4)
                edge_input = (edge_input.sum(-2) / (rel_pos_.float().unsqueeze(-1))).permute(0, 3, 1, 2)
            except:
                print("Warning!!!!!!!!!!!!!!!!")
                edge_input = self.edge_encoder(attn_edge_type).mean(-2).permute(0, 3, 1, 2)

        else:
            edge_input = self.edge_encoder(attn_edge_type).mean(-2).permute(0, 3, 1, 2) # [n_graph, n_node, n_node, n_head] -> [n_graph, n_head, n_node, n_node]

        graph_attn_bias[:, :, 1:, 1:] = graph_attn_bias[:, :, 1:, 1:] + edge_input
        graph_attn_bias = graph_attn_bias + attn_bias.unsqueeze(1) # reset
        
        # node feauture + graph token
        node_feature = self.atom_encoder(x).mean(dim=-2)           # [n_graph, n_node, n_hidden]
        if self.flag and perturb is not None:
            node_feature += perturb

        if IF_3D:
            node_feature = node_feature + self.in_degree_encoder(in_degree) + self.out_degree_encoder(out_degree)+ _3D_edge_features  #20230914 add 3D dis mat feature
        else:
            node_feature = node_feature + self.in_degree_encoder(in_degree) + self.out_degree_encoder(out_degree)

        graph_token_feature = self.graph_token(batched_data.reverse)
        graph_token_feature = graph_token_feature.unsqueeze(1)


        graph_node_feature = torch.cat([graph_token_feature, node_feature], dim=1)
        enc_out = graph_node_feature
 
        for layer_cnt,enc_layer in enumerate(self.layers):
            # if layer_cnt<3: #para freeze
            #     for param_name,param in enc_layer.named_parameters():
            #         param.requires_grad = False
            enc_out = enc_layer(enc_out, graph_attn_bias,valid=valid)
        # import pdb
        # pdb.set_trace()
        return enc_out


    def forward(self, batched_data, perturb=None, y=None, valid = False):
        attn_bias, rel_pos, x = batched_data.attn_bias, batched_data.rel_pos, batched_data.x
        in_degree, out_degree = batched_data.in_degree, batched_data.in_degree
        edge_input, attn_edge_type = batched_data.edge_input, batched_data.attn_edge_type
        all_rel_pos_3d_1 = batched_data.all_rel_pos_3d_1

        # graph_attn_bias
        n_graph, n_node = x.size()[:2]
        graph_attn_bias = attn_bias.clone()
        #unsqueeze for multihead
        graph_attn_bias = graph_attn_bias.unsqueeze(1).repeat(1, self.head_size, 1, 1) # [n_graph, n_head, n_node+1, n_node+1]
        # rel pos
        rel_pos_bias = self.rel_pos_encoder(rel_pos).permute(0, 3, 1, 2) # [n_graph, n_node, n_node, n_head] -> [n_graph, n_head, n_node, n_node]
        graph_attn_bias[:, :, 1:, 1:] = graph_attn_bias[:, :, 1:, 1:] + rel_pos_bias

        rbf_result = self.rel_pos_3d_proj(self.rbf(all_rel_pos_3d_1)).permute(0, 3, 1, 2)
        graph_attn_bias[:, :, 1:, 1:] = graph_attn_bias[:, :, 1:, 1:] + rbf_result

        # reset rel pos here
        t = self.graph_token_virtual_distance.weight.view(1, self.head_size, 1)
        graph_attn_bias[:, :, 1:, 0] = graph_attn_bias[:, :, 1:, 0] + t
        graph_attn_bias[:, :, 0, :] = graph_attn_bias[:, :, 0, :] + t

        # edge feature
        if self.edge_type == 'multi_hop':
            rel_pos_ = rel_pos.clone()
            rel_pos_[rel_pos_ == 0] = 1 # set pad to 1
            rel_pos_ = torch.where(rel_pos_ > 1, rel_pos_ - 1, rel_pos_) # set 1 to 1, x > 1 to x - 1
            if self.multi_hop_max_dist > 0:
                rel_pos_ = rel_pos_.clamp(0, self.multi_hop_max_dist)
                edge_input = edge_input[:, :, :, :self.multi_hop_max_dist, :]
            edge_input = self.edge_encoder(edge_input).mean(-2) #[n_graph, n_node, n_node, max_dist, n_head]
            max_dist = edge_input.size(-2)
            try:
                edge_input_flat = edge_input.permute(3,0,1,2,4).reshape(max_dist, -1, self.head_size)
                edge_input_flat = torch.bmm(edge_input_flat, self.edge_dis_encoder.weight.reshape(-1, self.head_size, self.head_size)[:max_dist, :, :])
                edge_input = edge_input_flat.reshape(max_dist, n_graph, n_node, n_node, self.head_size).permute(1,2,3,0,4)
                edge_input = (edge_input.sum(-2) / (rel_pos_.float().unsqueeze(-1))).permute(0, 3, 1, 2)
            except:
                print("Warning!!!!!!!!!!!!!!!!")
                edge_input = self.edge_encoder(attn_edge_type).mean(-2).permute(0, 3, 1, 2)

        else:
            edge_input = self.edge_encoder(attn_edge_type).mean(-2).permute(0, 3, 1, 2) # [n_graph, n_node, n_node, n_head] -> [n_graph, n_head, n_node, n_node]

        graph_attn_bias[:, :, 1:, 1:] = graph_attn_bias[:, :, 1:, 1:] + edge_input
        graph_attn_bias = graph_attn_bias + attn_bias.unsqueeze(1) # reset
        
        # node feauture + graph token
        node_feature = self.atom_encoder(x).mean(dim=-2)           # [n_graph, n_node, n_hidden]
        if self.flag and perturb is not None:
            node_feature += perturb

        node_feature = node_feature + self.in_degree_encoder(in_degree) + self.out_degree_encoder(out_degree)
        graph_token_feature = self.graph_token(batched_data.reverse)
        graph_token_feature = graph_token_feature.unsqueeze(1)
        graph_node_feature = torch.cat([graph_token_feature, node_feature], dim=1)
        ##encoder part
        
        # transfomrer encoder
        # key value
        '''=================================new============================='''
        #tgt data
        if y is None:
            y = batched_data.y
            
        batch_size=y.size(0)
        y_attn_bias = batched_data.y_attn_bias
        y_graph_attn_bias = y_attn_bias.clone()

        #unsqueeze for multihead
        y_graph_attn_bias = y_graph_attn_bias.unsqueeze(1).repeat(1, self.head_size, 1, 1) # [n_graph, n_head, n_node+1, n_node+1]

        if batched_data.subsequent_mask is not None:
            tgt_subsq_mask = batched_data.subsequent_mask
            tgt_subsq_mask = tgt_subsq_mask.unsqueeze(0)
            tgt_subsq_mask = tgt_subsq_mask.unsqueeze(0).repeat(batch_size, self.head_size, 1, 1)
        else:
            tgt_subsq_mask = None

        '''=========Centrality section========'''
        central_input = batched_data.central_input
        central_input = self.centrality_encoder(central_input).permute(0, 3, 1, 2) # [n_graph, n_node, n_node, n_head] -> [n_graph, n_head, n_node, n_node]
        y_graph_attn_bias[:,:,1:,1:] = y_graph_attn_bias[:,:,1:,1:] + central_input #[n_graph, n_head, n_node, n_node]

        '''=========LPE section========'''
        #print(lpe_input.size(), end="lpepre mean\n")
        lpe_input = batched_data.lpe_input
        lpe_eigenval = batched_data.lpe_eigenval
        lpe_input = torch.cat((lpe_input.unsqueeze(-1),lpe_eigenval.unsqueeze(-1)),dim=-1)
        lpe_input = self.lpe_linear(lpe_input)
        lpe_input = self.gelu(lpe_input)
        lpe_input = torch.nansum(lpe_input,-1,keepdim = False)
        lpe_input = self.lpe_linear3(lpe_input)
        lpe_input = lpe_input.permute(0,3,1,2) # [n_graph, n_node, n_node, n_head] -> [n_graph, n_head, n_node, n_node]
        y_graph_attn_bias[:,:,1:,1:]= y_graph_attn_bias[:,:,1:,1:] + lpe_input
        y_graph_attn_bias = y_graph_attn_bias + y_attn_bias.unsqueeze(1)

        # model(input,prev_output)
        

        enc_out = graph_node_feature    
        

        for enc_layer in self.layers:
            enc_out = enc_layer(enc_out, graph_attn_bias,valid=valid)
        
        #print(enc_out.size())
        #enc_out=enc_out[:,torch.randperm(enc_out.size()[1])]

        '''=====================Decoder===================='''
        NE_feature = self.atom_edge_encoder(y)
        output = self.position(NE_feature)  

        for dec_layer in self.decoderLayers:
            # important
            output = dec_layer(output,enc_out,enc_out,tgt_subsq_mask,y_graph_attn_bias,valid=valid,check=False)

        
        # with torch.no_grad:


        

        output = self.outp_logits(output)

        return output

    def laplace_decomp(self,g, max_freqs, in_d):

        n = len(in_d)
        A = g.float()
        N = sp.diags(np.array(in_d).clip(1) ** -0.5, dtype=float)
        L = sp.eye(len(in_d)) - N * A * N

        # Eigenvectors with numpy
        EigVals, EigVecs = np.linalg.eigh(L)
        EigVals, EigVecs = EigVals[: max_freqs], EigVecs[:, :max_freqs]  # Keep up to the maximum desired number of frequencies

        # Normalize and pad EigenVectors
        EigVecs = torch.from_numpy(EigVecs).float().to(self.device)
        EigVecs = F.normalize(EigVecs, p=2, dim=1, eps=1e-12, out=None)
        
        if n<max_freqs:
            EigVecs = F.pad(EigVecs, (0, max_freqs-n), value=0)
        else:
            EigVecs= EigVecs
            
        #Save eigenvales and pad
        EigVals = torch.from_numpy(np.sort(np.abs(np.real(EigVals)))).to(self.device) #Abs value is taken because numpy sometimes computes the first eigenvalue approaching 0 from the negative
        
        if n<max_freqs:
            EigVals = F.pad(EigVals, (0, max_freqs-n), value=0).unsqueeze(0)
        else:
            EigVals=EigVals.unsqueeze(0)
            
        #Save EigVals node features
        Eigvals = EigVals.repeat(n,1)
        #print("in model",EigVecs)
        return EigVecs, Eigvals

    def make_laplacian_cent_attn_bias(self,pos_enc_dim, y):
        offset = 4
        M = len(y)
        lpe_bias = torch.zeros((M,pos_enc_dim),dtype=torch.float,device= self.device)
        lpe_eigenval = torch.zeros((M,pos_enc_dim),dtype=torch.float,device= self.device)
        #lpe_bias = [[]for i in range(M)]for i in range(M)
        cent_bias = torch.zeros((M),dtype=torch.long,device= self.device)
       

            # if last added is node then update lpe and centrality
            
        sub_NE = y
        G = nx.Graph()
        node_indx = -1
        check_prev = 0
        
        for j in range(M):       
            NodeEdge = sub_NE[j].item()
            #if padding
            if NodeEdge ==0:
                continue
            # if node
            if NodeEdge <=472+offset:
                check_prev = 0
                node_indx +=1
                G.add_nodes_from([(node_indx,{"node":NodeEdge})])   
            #if edge not node       
            elif NodeEdge <=504+offset:
                check_prev +=1
                G.add_edges_from([(node_indx,node_indx-check_prev,{"edge":NodeEdge})])
            elif NodeEdge > 506+offset and NodeEdge < 532 :         # split = 20
                check_prev =check_prev+ (NodeEdge-(506+offset))
        sub_adj =torch.tensor(nx.adjacency_matrix(G).todense())
        sub_ind = []
        for node in G.nodes:
            sub_ind.append(G.degree[node])
        # print("adj",nx.adjacency_matrix(G))
        # print("sub_adj",sub_adj)
        # print("sub_ind",sub_ind)
        sub_lpe,sub_eigenval = self.laplace_decomp(sub_adj,pos_enc_dim,sub_ind)

        #print("sub_lpe",sub_lpe)
        node_indx = 0
        for k in range(M):
            NodeEdge = sub_NE[k]
            # if node
            if NodeEdge != 0 and NodeEdge <=472+offset:
                lpe_bias[k] = sub_lpe[node_indx]
                lpe_eigenval[k] = sub_eigenval[node_indx]
                cent_bias[k] = min(sub_ind[node_indx],30)

                node_indx+=1

        # lpe_bias = torch.from_numpy(lpe_bias).float()
        # lpe_eigenval = torch.from_numpy(lpe_eigenval).float()
        #cent_bias = torch.from_numpy(cent_bias).long()

        return lpe_bias,lpe_eigenval,cent_bias

    def training_step(self, batched_data, batch_idx):
        # = batched_data.weight
                
        #global weight 
        if self.dataset_name == 'uspto':
            if not self.flag:
                batch_pos_enc = batched_data.lpe_input
                sign_flip = torch.rand(batch_pos_enc.size(-1),device=self.device)
                sign_flip[sign_flip>=0.5] = 1.0; sign_flip[sign_flip<0.5] = -1.0
                batch_pos_enc = batch_pos_enc * sign_flip.unsqueeze(0).unsqueeze(0).unsqueeze(0)
                batched_data.lpe_input = batch_pos_enc

                y_hat = self(batched_data)
                y_hat = y_hat.view(-1,y_hat.size(-1))
                y_gt = batched_data.y_gt.view(-1)
                
                mask = ~torch.isnan(y_gt)


                loss = self.loss_fn(y_hat[mask],y_gt[mask],ignore_index=0) 
     

            else:
                y_gt = batched_data.y.view(-1).float()
                forward = lambda perturb: self(batched_data, perturb)
                model_forward = (self, forward)
                n_graph, n_node = batched_data.x.size()[:2]
                perturb_shape = (n_graph, n_node, self.hidden_dim)

                optimizer = self.optimizers()
                optimizer.zero_grad()
                loss, _ = flag_bounded(model_forward, perturb_shape, y_gt, optimizer, batched_data.x.device, self.loss_fn,
                               m=self.flag_m, step_size=self.flag_step_size, mag=self.flag_mag)
                self.lr_schedulers().step()
        self.log('train_loss', loss.detach(),sync_dist=True)
        return loss

    def validation_step(self, batched_data, batch_idx):

        
        #print("validation_step")
        
        y_pred = self(batched_data,valid = True)

        y_pred = y_pred.view(-1,y_pred.size(-1))
        y_true = batched_data.y_gt
        y_true = y_true.view(-1)
        # y_pred_out = torch.argmax(y_pred_out,dim=-1)
        

        #loss = self.loss_fn(y_pred, y_true,ignore_index=-100) 

        return {
            'y_pred': y_pred,
            'y_true': y_true,
        }

    def validation_epoch_end(self, outputs):

        correct = 0
        l = 0
        print("validation_epoch_end")
        y_pred = torch.cat([i['y_pred'] for i in outputs])
        y_true = torch.cat([i['y_true'] for i in outputs])
        for i in outputs:

            if torch.equal(torch.argmax(i['y_pred'],dim=-1),i['y_true']):
                correct+=1
                out = torch.argmax(i['y_pred'],dim=-1)

        mask = ~torch.isnan(y_true)
        loss = self.loss_fn(y_pred[mask], y_true[mask],ignore_index=0) 
        g_acc = correct/len(outputs)
        print(f"graph acc: {g_acc}")
        acc = (torch.argmax(y_pred,dim=-1)==y_true).float().mean()


        self.log('graph accuracy', g_acc, sync_dist=True)
        self.log('validation accuracy', acc, sync_dist=True)
        self.log('validation loss', loss, sync_dist=True)
        print(f"valid accuracy: {acc}")
   
    def get_square_subsequent_mask(self,seq_len):
        mask = (torch.triu(torch.ones(seq_len, seq_len,device=self.device)) == 1).transpose(0, 1)
        mask = mask.float().masked_fill(mask == 0, float('-inf')).masked_fill(mask == 1, float(0.0))
        return mask


    def test_step(self, batched_data, batch_idx): #split

    

        
        
        return {
            'y_pred': prediction,
            'correct': correct,
            'y_true': y_true,
            'idx': batched_data.idx,
        }


    def test_epoch_end(self, outputs):
        import pickle
        import os
        total = 0
        correct = 0
        out_dic = {}
        i = 0
        path ="/home/liyou/Code/G2GT-2022-01-23/src/results/uspto-50k-split2-distilled-split2/"
        if not os.path.exists(path):
            os.mkdir(path)

        while os.path.exists(path+"out%s" % i):
            i += 1
        filename = path+"out"

        outfile = open(f"{filename}{i}","wb")
        for i in outputs:
            total +=1
            correct += i["correct"]
            idx = i['idx'][0].item()
            gt = i["y_true"].detach().cpu().numpy()
            results = i['y_pred']
            out_dic[idx] = [results,gt]
            #print(type(idx),idx,type(results))
        pickle.dump(out_dic,outfile)
        outfile.close()
        
        
        # y_true = torch.cat([i['y_true'] for i in outputs])

        # input_dict = {"y_true": y_true, "y_pred": y_pred}
        # acc = (y_pred==y_true).float().mean()
        acc = correct/total
        #print(f"valid accuracy: {acc}")
        self.log('inference accuracy', acc, sync_dist=True)
        #self.log('test_' + self.metric, self.evaluator.eval(input_dict)[self.metric], sync_dist=True)
        #return acc

    def configure_optimizers(self):

        optimizer = torch.optim.AdamW(self.parameters(), lr=self.peak_lr, weight_decay=self.weight_decay)
        lr_scheduler = {
            'scheduler': PolynomialDecayLR(
                optimizer,
                warmup_updates=self.warmup_updates,
                tot_updates=self.tot_updates,
                lr=self.peak_lr,
                end_lr=self.end_lr,
                power=2.0,
            ),
            'name': 'learning_rate',
            'interval':'step',
            'frequency': 1,
        }

        

        return [optimizer],[lr_scheduler]

    @staticmethod
    def add_model_specific_args(parent_parser):
        parser = parent_parser.add_argument_group("GraphFormer")
        parser.add_argument('--n_layers', type=int, default=12)
        parser.add_argument('--head_size', type=int, default=32)
        parser.add_argument('--hidden_dim', type=int, default=512)
        parser.add_argument('--ffn_dim', type=int, default=512)
        parser.add_argument('--intput_dropout_rate', type=float, default=0.1)
        parser.add_argument('--dropout_rate', type=float, default=0.1)
        parser.add_argument('--weight_decay', type=float, default=0.01)
        parser.add_argument('--attention_dropout_rate', type=float, default=0.1)
        # parser.add_argument('--checkpoint_path', type=str, default='')
        parser.add_argument('--warmup_updates', type=int, default=60000)
        parser.add_argument('--tot_updates', type=int, default=1000000)
        parser.add_argument('--peak_lr', type=float, default=2e-4)
        parser.add_argument('--end_lr', type=float, default=1e-5)
        parser.add_argument('--edge_type', type=str, default='multi_hop')
        parser.add_argument('--validate', action='store_true', default=False)
        parser.add_argument('--test', action='store_true', default=False)
        parser.add_argument('--dataset_name', type=str)
        # haha, 这些flag是干啥的?
        parser.add_argument('--flag', action='store_true')
        parser.add_argument('--flag_m', type=int, default=3)
        parser.add_argument('--flag_step_size', type=float, default=1e-3)
        parser.add_argument('--flag_mag', type=float, default=1e-3)
        parser.add_argument('--beam', type=int, default=1)
        return parent_parser

class PositionalEncoding(nn.Module):
    "Implement the PE function."
    def __init__(self, d_model, dropout, max_len=5000):
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)
        
        # Compute the positional encodings once in log space.
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2) *
                             -(math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer('pe', pe)
        
    def forward(self, x, valid=False):
        temp = Variable(self.pe[:, :x.size(1)], requires_grad=False)
        temp = self.dropout(temp)
        x = x + temp
        # if valid:
        #     return x
        return x


class FeedForwardNetwork(nn.Module):
    def __init__(self, hidden_size, ffn_size, dropout_rate):
        super(FeedForwardNetwork, self).__init__()

        self.layer1 = nn.Linear(hidden_size, ffn_size)
        self.gelu = nn.GELU()
        self.layer2 = nn.Linear(ffn_size, hidden_size)

    def forward(self, x):
        x = self.layer1(x)
        x = self.gelu(x)
        x = self.layer2(x)
        return x


class MultiHeadAttention(nn.Module):
    def __init__(self, hidden_size, attention_dropout_rate, head_size):
        super(MultiHeadAttention, self).__init__()

        self.head_size = head_size

        self.att_size = att_size = hidden_size // head_size
        self.scale = att_size ** -0.5

        self.linear_q = nn.Linear(hidden_size, head_size * att_size)
        self.linear_k = nn.Linear(hidden_size, head_size * att_size)
        self.linear_v = nn.Linear(hidden_size, head_size * att_size)
        self.att_dropout = nn.Dropout(attention_dropout_rate)

        self.output_layer = nn.Linear(head_size * att_size, hidden_size)

    def forward(self, q, k, v, attn_bias=None, subsq_mask = None, valid=False,check=False):
        orig_q_size = q.size()

        d_k = self.att_size
        d_v = self.att_size
        batch_size = q.size(0)


        q = self.linear_q(q).view(batch_size, -1, self.head_size, d_k)
        k = self.linear_k(k).view(batch_size, -1, self.head_size, d_k)
        v = self.linear_v(v).view(batch_size, -1, self.head_size, d_v)

        q = q.transpose(1, 2)                  # [b, h, q_len, d_k]
        v = v.transpose(1, 2)                  # [b, h, v_len, d_v]
        k = k.transpose(1, 2).transpose(2, 3)  # [b, h, d_k, k_len]

        q = q * self.scale

        x = torch.matmul(q, k)  # [b, h, q_len, k_len]
        if attn_bias is not None:
            x = x + attn_bias
        if subsq_mask is not None:
            x = x + subsq_mask

        x = torch.softmax(x, dim=-1)

        if not valid:
            x = self.att_dropout(x)

        x = x.matmul(v)  # [b, h, q_len, attn]

        x = x.transpose(1, 2).contiguous()  # [b, q_len, h, attn]
        x = x.view(batch_size, -1, self.head_size * d_v)

        x = self.output_layer(x)

        assert x.size() == orig_q_size
        return x


class EncoderLayer(nn.Module):
    def __init__(self, hidden_size, ffn_size, dropout_rate, attention_dropout_rate, head_size):
        super(EncoderLayer, self).__init__()

        self.self_attention_norm = nn.LayerNorm(hidden_size)
        self.self_attention = MultiHeadAttention(hidden_size, attention_dropout_rate, head_size)
        self.self_attention_dropout = nn.Dropout(dropout_rate)

        self.ffn_norm = nn.LayerNorm(hidden_size)
        self.ffn = FeedForwardNetwork(hidden_size, ffn_size, dropout_rate)
        self.ffn_dropout = nn.Dropout(dropout_rate)

    def forward(self, x, attn_bias=None,valid=False):
        y = self.self_attention_norm(x)
        
        y = self.self_attention(y, y, y, attn_bias,valid=True)
        if not valid:
            y = self.self_attention_dropout(y)
        x = x + y

        y = self.ffn_norm(x)
        y = self.ffn(y)
        if not valid:
            y = self.ffn_dropout(y)
        x = x + y
        return x


'''Important'''    
class DecoderLayer(nn.Module):
    def __init__(self, hidden_size, ffn_size, dropout_rate, attention_dropout_rate, head_size):
        super(DecoderLayer, self).__init__()
        
        self.self_attention_norm = nn.LayerNorm(hidden_size)
        '''Masked Attention'''
        self.self_mask_attention = MultiHeadAttention(hidden_size, attention_dropout_rate, head_size)
        self.self_attention_dropout = nn.Dropout(dropout_rate)
        
        '''Mem Attention'''
        self.mem_att_sublayer_norm = torch.nn.LayerNorm(hidden_size)
        self.self_mem_attention = MultiHeadAttention(hidden_size, attention_dropout_rate, head_size)
        self.self_mem_attention_dropout = nn.Dropout(dropout_rate)
        
        self.ffn_norm = nn.LayerNorm(hidden_size)
        self.ffn = FeedForwardNetwork(hidden_size, ffn_size, dropout_rate)
        self.ffn_dropout = nn.Dropout(dropout_rate)

    '''todo self_mem_attention, and masked self_attention '''
    def forward(self, x, memk,memv, tgt_padding_mask,attn_bias=None,valid=False,check=False):
        # if check:
        #     print("X0",x[0][20])

        y = self.self_attention_norm(x)

        y = self.self_mask_attention(y,y,y,attn_bias,subsq_mask=tgt_padding_mask,valid=valid,check=check)
        # if check:
        #     print("X2",y[0][20])
        if not valid:
            y = self.self_attention_dropout(y)
        x = x + y

        y = self.mem_att_sublayer_norm(x)
        y = self.self_mem_attention(y,memk,memv,valid=valid)
        if not valid:
            y = self.self_mem_attention_dropout(y)
        x = x+y
        # if check:
        #     print("X2",x[0][20])
        y = self.ffn_norm(x)
        y = self.ffn(y)
        if not valid:
            y = self.ffn_dropout(y)
        x = x + y
        # if check:
        #     print("X3",x[0][20])
        return x


from torch_geometric.nn import global_add_pool, global_mean_pool, global_max_pool, GlobalAttention

class PoolingLayer(nn.Module):
    def __init__(self,hidden_dim, method='dummy'):
        super(PoolingLayer, self).__init__()
        print(method,'method')
        self.method = method
        if method=="attention":
            self.query = nn.Linear(768, 1)
            self.key = nn.Linear(768, hidden_dim)
            self.ln = nn.LayerNorm(hidden_dim)
        if method=='self_attention':
            self.self_attention = MultiHeadAttention(hidden_dim, 0, 1)
            # self.pool = GlobalAttention(self.gate_nn)
        if method=='global_attention':
            self.global_attention = GlobalAttention(nn.Linear(768, 1))
    def forward(self,x, num_nodes = None, batch = None):
        # Pooling using first, first node of the hidden states.
        if self.method=='dummy':
            return x[:,0]
        # sum pooling.
        if self.method=='sum':
            # print(self.method,'this should be f')
            return x.sum(dim=1) #xdim [batch,nodes,hiddendim] --> [batch,hiddendim]
        # attention pooling
        if self.method=='attention':
            q = self.query(x)
            q = torch.softmax(q,dim=-1)
            x = self.key(x)
            x = self.ln(x)
            x = q*x
            x = x.sum(dim=1)
            return x
        if self.method=="self_attention":
            y = self.self_attention(x,x,x)
            y=y.sum(dim=1)
            return y
        if self.method=='global_attention':
            # To use global_attention, num_nodes and batch should not be None
            assert(batch is not None and num_nodes is not None)
            if num_nodes is not None:
                x = torch.cat([x[i, :num_nodes[i]] for i in range(x.shape[0])],
                              dim=0)
            y = self.global_attention(x, batch)
            return y

class FFN(nn.Module):
    def __init__(self, hidden_size, dropout_rate):
        super(FFN, self).__init__()

        self.layer1 = nn.Linear(hidden_size, hidden_size)
        self.gelu = nn.GELU()
        self.dropout = nn.Dropout(p=dropout_rate)
        self.ln = nn.LayerNorm(hidden_size)

    def forward(self, x):
        y = self.layer1(x)
        y = self.ln(y)
        y = self.gelu(y)
        y = self.dropout(y)
        return y

    
class DropoutOutputLayer(nn.Module):
    def __init__(
        self,
        input_dim,
        inner_dim,
        output_dim,
        activation_fn="tanh",
        pooler_dropout=0,
    ):
        super().__init__()
        self.dense = nn.Linear(input_dim, inner_dim)
        if activation_fn=="tanh":
            self.activation_fn = nn.Tanh()
        else:
            raise Exception
        self.dropout = nn.Dropout(p=pooler_dropout)
        self.out_proj = nn.Linear(inner_dim, output_dim)

    def forward(self, features, **kwargs):
        x = features
        x = self.dropout(x)
        x = self.dense(x)
        x = self.activation_fn(x)
        x = self.dropout(x)
        x = self.out_proj(x)
        return x

class Embedding_extractor(pl.LightningModule):
    def __init__(self, args):
        super().__init__()

        # Init the pretrained G2GT model.
        #self.checkpoint_path = args.default_root_dir + '/conf/pretrain_model/epoch=41-step=160120.ckpt'
        self.checkpoint_path = args.default_root_dir + '/pretrain_model/epoch=41-step=160120.ckpt'
        #self.checkpoint_path = args.default_root_dir + './epoch_41-step_160120.ckpt'
        # self.dataset_name = 'QH_binary'
        self.ptm = GraphFormer.load_from_checkpoint(
            # args.checkpoint_path,
            self.checkpoint_path,
            strict=False,
            n_layers=args.n_layers,
            head_size=args.head_size,
            hidden_dim=args.hidden_dim,
            attention_dropout_rate=args.attention_dropout_rate,
            dropout_rate=args.dropout_rate,
            intput_dropout_rate=args.intput_dropout_rate,
            weight_decay=args.weight_decay,
            ffn_dim=args.ffn_dim,
            dataset_name=args.dataset_name,
            warmup_updates=args.warmup_updates,
            tot_updates=args.tot_updates,
            peak_lr=args.peak_lr, #useless
            end_lr=args.peak_lr,  #useless
            edge_type=args.edge_type,
            multi_hop_max_dist=args.multi_hop_max_dist,
            flag=args.flag,
            flag_m=args.flag_m,
            flag_step_size=args.flag_step_size,
        )

        if args.freeze==True:
            print("freeze the bulk of rem ")
            self.ptm.freeze()
        else :
            print("no freeze")

        self.outpath = args.default_root_dir
        self.srcpath = args.default_root_dir+"/data/"+args.dataset_name
        downstream_ffn_dim = args.downstream_ffn_dim
        self.feature_extractor = self.ptm.translate_encoder
        self.pooling = PoolingLayer(downstream_ffn_dim, method='sum')
        self.args=args

        self.sigmoid_sup=args.sigmoid_sup
        self.sigmoid_inf=args.sigmoid_inf       
        self.output_layer=nn.Linear(downstream_ffn_dim, 1)
        self.output_sigmoid=nn.Sigmoid()
        self.dropout_output_layer=DropoutOutputLayer(
            input_dim=downstream_ffn_dim,
            inner_dim=downstream_ffn_dim,
            output_dim=1,
            activation_fn="tanh",
            pooler_dropout=0.2)

        self.validation_step_outputs = []
        self.train_step_outputs = []
        self.test_loss_outputs=[]
        self.test_outputs_dict={"smiles":[],"y_true":[],"y_pred":[],"idx":[],"EP_ID":[]}
        self.test_de_log_loss_outputs=[]
        self.test_de_log_ratio_loss_outputs=[]
        self.mae_loss=nn.L1Loss()
        self.predict_outputs_dict = {"smiles": [],   "y_pred": [], "idx": [], "EP_ID": []}


    def forward(self, x):

        x = self.feature_extractor(x)
        #x = self.pooling(x)
        x=x[:,0,:]
        # import pdb
        # pdb.set_trace()
        #x=self.output_layer(x)
        x=self.dropout_output_layer(x)
        y_pred=(self.sigmoid_sup-self.sigmoid_inf)*self.output_sigmoid(x)+self.sigmoid_inf
        return y_pred

    def configure_optimizers(self):

        params=self.parameters()
        #unfreezed_params=filter(lambda p:p.requires_grad,self.parameters())
        optimizer = torch.optim.AdamW(params, lr=self.args.peak_lr, weight_decay=self.args.weight_decay)
        # lr_scheduler = {
        #     'scheduler': PolynomialDecayLR(
        #         optimizer,
        #         warmup_updates=self.args.warmup_updates,
        #         tot_updates=self.args.tot_updates,
        #         lr=self.args.peak_lr,
        #         end_lr=self.args.end_lr,
        #         power=2.0,
        #     ),
        #     'name': 'learning_rate',
        #     'interval':'step',
        #     'frequency': 1,
        # }
        lr_scheduler = { 
            'scheduler': CyclicLR(
                optimizer,
                base_lr= self.args.end_lr,
                max_lr=self.args.peak_lr,
                mode ="exp_range",
                #gamma =0.9999,
                step_size_up=400,
                step_size_down=800,
                cycle_momentum=False,
            ),
            'name': 'learning_rate',      
            'interval':'step',
            'frequency': 1,
        }
        return [optimizer],[lr_scheduler]
 

    def predict_step(self, batch, batch_idx):
        x = batch
        y_pred = self(x)
      

        self.predict_outputs_dict["y_pred"] += y_pred.flatten().tolist()
        # import pdb
        # pdb.set_trace()
        self.predict_outputs_dict["smiles"] += list(batch.smiles)
        self.predict_outputs_dict["EP_ID"] += list(batch.EP_ID)
        self.predict_outputs_dict["idx"] += batch.idx.tolist()

        return {"pred": y_pred.detach().cpu().numpy(),'idx':batch_idx}

    def on_predict_epoch_end(self,a):



        predict_outputs_df = pd.DataFrame(self.predict_outputs_dict)
        predict_outputs_df.to_csv(self.args.predict_output_csv_file_path)


    def training_step(self, batch, batch_idx):
        # training_step defines the train loop.
        # it is independent of forward
        
        
        y_pred = self(batch)
        # import pdb
        # pdb.set_trace()
        loss = self.mae_loss(y_pred,batch.y)
        # Logging to TensorBoard (if installed) by default
        self.log("batch_train_loss", loss,prog_bar=True)
        self.train_step_outputs.append(loss)
        return loss

    def validation_step(self, batch, batch_idx):
        # training_step defines the train loop.
        # it is independent of forward
        
        
        y_pred = self(batch)
        # import pdb
        # pdb.set_trace()
        loss = self.mae_loss(y_pred,batch.y)
        # Logging to TensorBoard (if installed) by default
        self.log("batch_val_loss", loss,prog_bar=True)
        self.validation_step_outputs.append(loss)
        return loss

    def test_step(self, batch, batch_idx):
       
        # import pdb
        # pdb.set_trace()
        y_pred = self(batch) 
        
        loss =self.mae_loss(y_pred,batch.y)
        de_log_loss=self.mae_loss(torch.pow(10,y_pred),torch.pow(10,batch.y))
        de_log_ratio_loss=torch.mean(torch.abs(torch.pow(10,y_pred)/torch.pow(10,batch.y)-1))
        # Logging to TensorBoard (if installed) by default
        self.log("batch_test_loss", loss,prog_bar=True)
        self.log("batch_test_de_log_loss", de_log_loss )
        self.log("batch_de_log_ratio_loss",de_log_ratio_loss)
        
        self.test_loss_outputs.append(loss)
        self.test_de_log_loss_outputs.append(de_log_loss)
        self.test_de_log_ratio_loss_outputs.append(de_log_ratio_loss)

        self.test_outputs_dict["y_pred"]+=y_pred.flatten().tolist()
        self.test_outputs_dict["y_true"]+=batch.y.flatten().tolist()
        # import pdb
        # pdb.set_trace()
        self.test_outputs_dict["smiles"]+=list(batch.smiles)
        self.test_outputs_dict["EP_ID"]+=list(batch.EP_ID)
        self.test_outputs_dict["idx"]+=batch.idx.tolist()
        
        return loss

    def on_test_epoch_end(self):
       
        all_loss = torch.stack(self.test_loss_outputs)
        self.log('epoch_test_loss', torch.mean(all_loss), prog_bar=True)

        all_de_log_loss=torch.stack(self.test_de_log_loss_outputs)
        self.log('epoch_test_de_log_loss', torch.mean(all_de_log_loss), prog_bar=True)
     
        all_de_log_ratio_loss=torch.stack(self.test_de_log_ratio_loss_outputs)
        self.log('epoch_test_de_log_ratio_loss', torch.mean(all_de_log_ratio_loss), prog_bar=True)
     


        test_outputs_df=pd.DataFrame(self.test_outputs_dict)
        import datetime
        now = datetime.datetime.now() 
        test_outputs_df.to_csv("lightning_logs/%s/test_output_%s.csv"%(self.args.log_name,now.strftime("%Y%m%d%H%M%S")))
        self.test_loss_outputs.clear()
        self.test_de_log_loss_outputs.clear()
        #不重置这个字典可以使生成的csv有全部test集的测试结果
        self.test_outputs_dict["y_pred"]=[]
        self.test_outputs_dict["y_true"]=[]
        self.test_outputs_dict["smiles"]=[]
        self.test_outputs_dict["smiles"]=[]
        self.test_outputs_dict["idx"]=[]
        self.test_outputs_dict["EP_ID"]=[]
      

        pass
    

    def on_validation_epoch_end(self):
        #print("on_validation_epoch_end")
        # import pdb
        # pdb.set_trace()
        all_loss = torch.stack(self.validation_step_outputs)
        self.log('epoch_val_loss', torch.mean(all_loss))
        print('epoch_val_loss', torch.mean(all_loss).item())
   
        self.validation_step_outputs.clear()

        pass
    def on_train_epoch_end(self):
        #print("on_train_epoch_end")
        # import pdb
        # pdb.set_trace()
        all_loss = torch.stack(self.train_step_outputs)
        self.log('epoch_train_loss', torch.mean(all_loss))
        print('epoch_train_loss', torch.mean(all_loss).item())
        self.train_step_outputs.clear()
        pass

    # def validation_epoch_end(self,outputs):
    #     #print("validation_epoch_end")
    #     # import pdb
    #     # pdb.set_trace()
    #     pass
    #     #print("validation_epoch_end")
    #     #self.log('epoch_val_loss', torch.mean(torch.stack(outputs)), prog_bar=True)
       

    # def train_epoch_end(self,outputs): # no accessible 
    #     print("train_epoch_end")
    #     # import pdb
    #     # pdb.set_trace()
    #     pass

# borrowed from https://github.com/yuanqidu/M2Hub/blob/master/m2models/models/leftnet.py

### feature dimension
### variable name

import math
from math import pi
from typing import Optional, Tuple

import torch
from torch import nn
from torch.nn import Embedding

from torch_geometric.nn import radius_graph
from torch_geometric.nn.conv import MessagePassing
from torch_scatter import scatter
from .g2g_model import GraphFormer
from uni_electrolyte.evaluator.dataset.g2g_theEMOL.collator import pad_2d_unsqueeze,pad_3d_unsqueeze,\
            pad_attn_bias_unsqueeze,pad_edge_type_unsqueeze,pad_rel_pos_unsqueeze,pad_rel_pos_3d_unsqueeze,\
            pad_1d_unsqueeze
def swish(x):
    return x * torch.sigmoid(x)

## radial basis function to embed distances
## add comments: based on XXX code
class rbf_emb(nn.Module):
    '''
    modified: delete cutoff with r
    '''
    def __init__(self, num_rbf, rbound_upper, rbf_trainable=False):
        super().__init__()
        self.rbound_upper = rbound_upper
        self.rbound_lower = 0
        self.num_rbf = num_rbf
        self.rbf_trainable = rbf_trainable
        means, betas = self._initial_params()

        self.register_buffer("means", means)
        self.register_buffer("betas", betas)

    def _initial_params(self):
        start_value = torch.exp(torch.scalar_tensor(-self.rbound_upper))
        end_value = torch.exp(torch.scalar_tensor(-self.rbound_lower))
        means = torch.linspace(start_value, end_value, self.num_rbf)
        betas = torch.tensor([(2 / self.num_rbf * (end_value - start_value))**-2] *
                             self.num_rbf)
        return means, betas

    def reset_parameters(self):
        means, betas = self._initial_params()
        self.means.data.copy_(means)
        self.betas.data.copy_(betas)

    def forward(self, dist):
        dist=dist.unsqueeze(-1)
        rbounds = 0.5 * \
                  (torch.cos(dist * pi / self.rbound_upper) + 1.0)
        rbounds = rbounds * (dist < self.rbound_upper).float()
        return rbounds*torch.exp(-self.betas * torch.square((torch.exp(-dist) - self.means)))


class NeighborEmb(MessagePassing):

    def __init__(self, hid_dim: int):
        super(NeighborEmb, self).__init__(aggr='add')
        self.embedding = nn.Embedding(95, hid_dim)
        self.hid_dim = hid_dim
        self.ln_emb = nn.LayerNorm(hid_dim,
                                   elementwise_affine=False)

    def forward(self, z, s, edge_index, embs):
        s_neighbors = self.ln_emb(self.embedding(z))
        s_neighbors = self.propagate(edge_index, x=s_neighbors, norm=embs)

        s = s + s_neighbors
        return s

    def message(self, x_j, norm):
        return norm.view(-1, self.hid_dim) * x_j

class S_vector(MessagePassing):
    def __init__(self, hid_dim: int):
        super(S_vector, self).__init__(aggr='add')
        self.hid_dim = hid_dim
        self.lin1 = nn.Sequential(
            nn.Linear(hid_dim, hid_dim),
            nn.LayerNorm(hid_dim, elementwise_affine=False),
            nn.SiLU())

    def forward(self, s, v, edge_index, emb):
        s = self.lin1(s)
        emb = emb.unsqueeze(1) * v

        v = self.propagate(edge_index, x=s, norm=emb)
        return v.view(-1, 3, self.hid_dim)

    def message(self, x_j, norm):
        x_j = x_j.unsqueeze(1)
        a = norm.view(-1, 3, self.hid_dim) * x_j
        return a.view(-1, 3 * self.hid_dim)


class EquiMessagePassing(MessagePassing):
    def __init__(
            self,
            hidden_channels,
            num_radial,
    ):
        super(EquiMessagePassing, self).__init__(aggr="add", node_dim=0)

        self.hidden_channels = hidden_channels
        self.num_radial = num_radial
        self.dir_proj = nn.Sequential(
            nn.Linear(3 * self.hidden_channels + self.num_radial, self.hidden_channels * 3), nn.SiLU(inplace=True),
            nn.Linear(self.hidden_channels * 3, self.hidden_channels * 3), )

        self.x_proj = nn.Sequential(
            nn.Linear(hidden_channels, hidden_channels),
            nn.SiLU(),
            nn.Linear(hidden_channels, hidden_channels * 3),
        )
        self.rbf_proj = nn.Linear(num_radial, hidden_channels * 3)

        self.inv_sqrt_3 = 1 / math.sqrt(3.0)
        self.inv_sqrt_h = 1 / math.sqrt(hidden_channels)
        self.x_layernorm = nn.LayerNorm(hidden_channels)

        self.reset_parameters()

    def reset_parameters(self):
        nn.init.xavier_uniform_(self.x_proj[0].weight)
        self.x_proj[0].bias.data.fill_(0)
        nn.init.xavier_uniform_(self.x_proj[2].weight)
        self.x_proj[2].bias.data.fill_(0)
        nn.init.xavier_uniform_(self.rbf_proj.weight)
        self.rbf_proj.bias.data.fill_(0)
        self.x_layernorm.reset_parameters()
        ## question: why don't reset parameters for dir_proj?

    def forward(self, x, vec, edge_index, edge_rbf, weight, edge_vector):
        xh = self.x_proj(self.x_layernorm(x))

        rbfh = self.rbf_proj(edge_rbf)
        weight = self.dir_proj(weight)
        rbfh = rbfh * weight
        # propagate_type: (xh: Tensor, vec: Tensor, rbfh_ij: Tensor, r_ij: Tensor)
        dx, dvec = self.propagate(
            edge_index,
            xh=xh,
            vec=vec,
            rbfh_ij=rbfh,
            r_ij=edge_vector,
            size=None,
        )

        return dx, dvec

    def message(self, xh_j, vec_j, rbfh_ij, r_ij):
        x, xh2, xh3 = torch.split(xh_j * rbfh_ij, self.hidden_channels, dim=-1)
        xh2 = xh2 * self.inv_sqrt_3

        vec = vec_j * xh2.unsqueeze(1) + xh3.unsqueeze(1) * r_ij.unsqueeze(2)
        vec = vec * self.inv_sqrt_h

        return x, vec

    def aggregate(
            self,
            features: Tuple[torch.Tensor, torch.Tensor],
            index: torch.Tensor,
            ptr: Optional[torch.Tensor],
            dim_size: Optional[int],
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        x, vec = features
        x = scatter(x, index, dim=self.node_dim, dim_size=dim_size)
        vec = scatter(vec, index, dim=self.node_dim, dim_size=dim_size)
        return x, vec

    def update(
            self, inputs: Tuple[torch.Tensor, torch.Tensor]
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        return inputs


class FTE(nn.Module):
    def __init__(self, hidden_channels):
        super().__init__()
        self.hidden_channels = hidden_channels

        self.vec_proj = nn.Linear(
            hidden_channels, hidden_channels * 2, bias=False
        )
        self.xvec_proj = nn.Sequential(
            nn.Linear(hidden_channels * 2, hidden_channels),
            nn.SiLU(),
            nn.Linear(hidden_channels, hidden_channels * 3),
        )

        self.inv_sqrt_2 = 1 / math.sqrt(2.0)
        self.inv_sqrt_h = 1 / math.sqrt(hidden_channels)

        self.reset_parameters()

    def reset_parameters(self):
        nn.init.xavier_uniform_(self.vec_proj.weight)
        nn.init.xavier_uniform_(self.xvec_proj[0].weight)
        self.xvec_proj[0].bias.data.fill_(0)
        nn.init.xavier_uniform_(self.xvec_proj[2].weight)
        self.xvec_proj[2].bias.data.fill_(0)

    def forward(self, x, vec, node_frame):

        vec = self.vec_proj(vec)
        vec1,vec2 = torch.split(
                 vec, self.hidden_channels, dim=-1
             )

        # # # scalrization = torch.sum(vec1.unsqueeze(2) * node_frame.unsqueeze(-1), dim=1)
        # # # scalrization[:, 1, :] = torch.abs(scalrization[:, 1, :].clone())
        scalar = torch.sqrt(torch.sum(vec1 ** 2, dim=-2) + 1e-10)
        
        vec_dot = (vec1 * vec2).sum(dim=1)
        vec_dot = vec_dot * self.inv_sqrt_h

        x_vec_h = self.xvec_proj(
            torch.cat(
                [x, scalar], dim=-1
            )
        )
        xvec1, xvec2, xvec3 = torch.split(
            x_vec_h, self.hidden_channels, dim=-1
        )

        dx = xvec1 + xvec2 + vec_dot
        dx = dx * self.inv_sqrt_2

        dvec = xvec3.unsqueeze(1) * vec2

        return dx, dvec


class aggregate_pos(MessagePassing):

    def __init__(self, aggr='mean'):  
        super(aggregate_pos, self).__init__(aggr=aggr)

    def forward(self, vector, edge_index):
        v = self.propagate(edge_index, x=vector)

        return v


class EquiOutput(nn.Module):
    def __init__(self, hidden_channels):
        super().__init__()
        self.hidden_channels = hidden_channels

        self.output_network = nn.ModuleList(
            [
                # GatedEquivariantBlock(
                #     hidden_channels,
                #     hidden_channels // 2,
                # ),
                GatedEquivariantBlock(hidden_channels, 1),
            ]
        )

        self.reset_parameters()

    def reset_parameters(self):
        for layer in self.output_network:
            layer.reset_parameters()

    def forward(self, x, vec):
        for layer in self.output_network:
            x, vec = layer(x, vec)
        return vec.squeeze()


# Borrowed from TorchMD-Net
class GatedEquivariantBlock(nn.Module):
    """Gated Equivariant Block as defined in Schütt et al. (2021):
    Equivariant message passing for the prediction of tensorial properties and molecular spectra
    """

    def __init__(
        self,
        hidden_channels,
        out_channels,
    ):
        super(GatedEquivariantBlock, self).__init__()
        self.out_channels = out_channels

        self.vec1_proj = nn.Linear(
            hidden_channels, hidden_channels, bias=False
        )
        self.vec2_proj = nn.Linear(hidden_channels, out_channels, bias=False)

        self.update_net = nn.Sequential(
            nn.Linear(hidden_channels * 2, hidden_channels),
            nn.SiLU(),
            nn.Linear(hidden_channels, out_channels * 2),
        )

        self.act = nn.SiLU()

    def reset_parameters(self):
        nn.init.xavier_uniform_(self.vec1_proj.weight)
        nn.init.xavier_uniform_(self.vec2_proj.weight)
        nn.init.xavier_uniform_(self.update_net[0].weight)
        self.update_net[0].bias.data.fill_(0)
        nn.init.xavier_uniform_(self.update_net[2].weight)
        self.update_net[2].bias.data.fill_(0)

    def forward(self, x, v):
        vec1 = torch.norm(self.vec1_proj(v), dim=-2)
        vec2 = self.vec2_proj(v)

        x = torch.cat([x, vec1], dim=-1)
        x, v = torch.split(self.update_net(x), self.out_channels, dim=-1)
        v = v.unsqueeze(1) * vec2

        x = self.act(x)
        return x, v



class G2G_LEFTNet(nn.Module):
    def __init__(
            self,
            output_dim=1,
            cutoff=6.0, num_layers=4, readout="sum",
            hidden_channels=128, num_radial=96, eps=1e-10,
            use_pbc=False, use_sigmoid=False,device=None,g2g_checkpoint_path=None
    ):
        super(G2G_LEFTNet, self).__init__()
        self.device=device
        self.eps = eps
        self.num_layers = num_layers
        self.hidden_channels = hidden_channels
        self.cutoff = cutoff
        self.readout = readout


        self.z_emb_ln = nn.LayerNorm(hidden_channels, elementwise_affine=False)
        self.z_emb = Embedding(95, hidden_channels)
        
        self.radial_emb = rbf_emb(num_radial, cutoff)
        self.radial_lin = nn.Sequential(
            nn.Linear(num_radial, hidden_channels),
            nn.SiLU(inplace=True),
            nn.Linear(hidden_channels, hidden_channels))
        
        self.neighbor_emb = NeighborEmb(hidden_channels)

        self.S_vector = S_vector(hidden_channels)

        self.lin = nn.Sequential(
            nn.Linear(3, hidden_channels // 4),
            nn.SiLU(inplace=True),
            nn.Linear(hidden_channels // 4, 1))

        self.message_layers = nn.ModuleList()
        self.FTEs = nn.ModuleList()
        
        for _ in range(num_layers):
            self.message_layers.append(
                EquiMessagePassing(hidden_channels, num_radial).jittable()
            )
            self.FTEs.append(FTE(hidden_channels))

        if output_dim != 0:
            self.num_targets = output_dim

        self.last_layer = nn.Linear(hidden_channels, self.num_targets)
        # self.out_forces = EquiOutput(hidden_channels)
        
        # for node-wise frame
        self.mean_neighbor_pos = aggregate_pos(aggr='mean')

        self.inv_sqrt_2 = 1 / math.sqrt(2.0)

        self.reset_parameters()
        self.use_pbc = use_pbc
        self.use_sigmoid = use_sigmoid

        #g2g

        """
        logger=True, checkpoint_callback=True, default_root_dir='/root/Uni-Electrolyte/scoring_model/g2gt/src/', 
        gradient_clip_val=0.0, gradient_clip_algorithm='norm', process_position=0, num_nodes=1, num_processes=1, 
        devices=None, gpus=1, auto_select_gpus=False, tpu_cores=None, ipus=None, log_gpu_memory=None, 
        progress_bar_refresh_rate=1, overfit_batches=0.0, track_grad_norm=-1, check_val_every_n_epoch=1, 
        fast_dev_run=False, accumulate_grad_batches=1, max_epochs=None, min_epochs=None, max_steps=10001,
         min_steps=None, max_time=None, limit_train_batches=1.0, limit_val_batches=1.0, limit_test_batches=1.0, 
         limit_predict_batches=1.0, val_check_interval=1.0, flush_logs_every_n_steps=100, log_every_n_steps=50,
          accelerator=None, sync_batchnorm=False, precision=32, weights_summary='top', weights_save_path=None, 
          num_sanity_val_steps=2, truncated_bptt_steps=None, resume_from_checkpoint=None, profiler=None,
           benchmark=False, deterministic=False, reload_dataloaders_every_n_epochs=0, 
           reload_dataloaders_every_epoch=False, auto_lr_find=False, replace_sampler_ddp=True, 
           terminate_on_nan=False, auto_scale_batch_size=False, prepare_data_per_node=True, 
           plugins=<pytorch_lightning.plugins.training_type.ddp.DDPPlugin object at 0x7fa425deba60>,
            amp_backend='native', amp_level='O2', distributed_backend=None, move_metrics_to_cpu=False,
             multiple_trainloader_mode='max_size_cycle', stochastic_weight_avg=False, n_layers=8, head_size=24,
              hidden_dim=768, ffn_dim=2048, intput_dropout_rate=0.1, dropout_rate=0.1, weight_decay=0.0, 
              attention_dropout_rate=0.1, warmup_updates=1000, tot_updates=10000, peak_lr=0.00025, end_lr=1e-06,
               edge_type='one_hop', validate=False, test=False, dataset_name='inference_dataset_be', flag=False,
                flag_m=3, flag_step_size=0.001, flag_mag=0.001, beam=1, num_workers=11, batch_size=512, seed=42, 
                multi_hop_max_dist=5, rel_pos_max=1024, pooling='attention', downstream_ffn_dim=768, 
                downstream_dropout=0, input_filename=None, sigmoid_inf=-5.0, sigmoid_sup=1.0, epoch=None, 
                iid_test_dataset_name=None, iid_test_input_filename=None, ood_test_dataset_name=None,
                 ood_test_input_filename=None, freeze=False, log_name_prefix='inference', predicted_target='be',
                  loaded_target_list=['be'], inference=True, ID_name='EP_ID', 
                  predict_output_csv_file_path='./output/output_bohrium_be.csv', 
                  predict_input_csv_file_path='./input.csv', predict_dataset_name='inference_dataset_be',
                   log_name='inference_be_20240318111828'
        """

        self.ptm = GraphFormer.load_from_checkpoint(
            # args.checkpoint_path,
            g2g_checkpoint_path,
            strict=False,
            n_layers=8,
            head_size=24,
            hidden_dim=768,
            attention_dropout_rate=0.1,
            dropout_rate=0.1,
            intput_dropout_rate=0.1,
            weight_decay=0.00,
            ffn_dim=2048,
            dataset_name=None,
            warmup_updates=1000,
            tot_updates=10000,
            peak_lr=2.5e-4,  # useless
            end_lr=1e-6,  # useless
            edge_type="one_hop",
            multi_hop_max_dist=5,
            flag=False,
            flag_m=3,
            flag_step_size=0.001,
        )
        self.ptm.freeze()
        self.feature_extractor = self.ptm.translate_encoder

    def reset_parameters(self):
        self.z_emb.reset_parameters()
        self.radial_emb.reset_parameters()
        for layer in self.message_layers:
            layer.reset_parameters()
        for layer in self.FTEs:
            layer.reset_parameters()
        self.last_layer.reset_parameters()
        # self.out_forces.reset_parameters()
        for layer in self.radial_lin:
            if hasattr(layer, 'reset_parameters'):
                layer.reset_parameters()
        for layer in self.lin:
            if hasattr(layer, 'reset_parameters'):
                layer.reset_parameters()

    # @conditional_grad(torch.enable_grad())

    def preprocess_g2g_data(self,data,max_node=9999, multi_hop_max_dist=5,rel_pos_max=1024,device=None):

        for idx in range(len(data.y)):
            data.reverse[idx]= torch.from_numpy(data.reverse[idx])
            data.x[idx] = torch.from_numpy(data.x[idx])
            data.edge_input[idx] = torch.from_numpy(data.edge_input[idx])
            data.attn_bias[idx] = torch.from_numpy(data.attn_bias[idx])
            data.attn_edge_type[idx] = torch.from_numpy(data.attn_edge_type[idx])
            data.rel_pos[idx] = torch.from_numpy(data.rel_pos[idx])
            data.all_rel_pos_3d_1[idx] = torch.from_numpy(data.all_rel_pos_3d_1[idx])
            data.in_degree[idx] = torch.from_numpy(data.in_degree[idx])
            data.out_degree[idx] = torch.from_numpy(data.out_degree[idx])
            data.x[idx] = torch.from_numpy(data.x[idx])

        for idx in range(len(data.edge_input)):
            data.edge_input[idx]=data.edge_input[idx][:, :, :multi_hop_max_dist, :]
        for idx, _ in enumerate(data.attn_bias):
            data.attn_bias[idx][1:, 1:][data.rel_pos[idx] >= rel_pos_max] = float('-inf')


        max_node_num = max(i.shape[0] for i in data.x)
        max_dist = max(i.shape[-2] for i in data.edge_input)

        # retrosynthesis or forward synthesis
        data.reverse = torch.cat([i for i in data.reverse]).to(device)
        data.x = torch.cat([pad_2d_unsqueeze(i, max_node_num) for i in data.x]).to(device)
        data.edge_input = torch.cat([pad_3d_unsqueeze(i, max_node_num, max_node_num, max_dist) for i in data.edge_input]).to(device)
        data.attn_bias = torch.cat([pad_attn_bias_unsqueeze(i, max_node_num + 1) for i in data.attn_bias]).to(device)
        data.attn_edge_type = torch.cat([pad_edge_type_unsqueeze(i, max_node_num) for i in data.attn_edge_type]).to(device)
        data.rel_pos = torch.cat([pad_rel_pos_unsqueeze(i, max_node_num) for i in data.rel_pos]).to(device)
        data.all_rel_pos_3d_1 = torch.cat([pad_rel_pos_3d_unsqueeze(i, max_node_num) for i in data.all_rel_pos_3d_1]).to(device)
        data.in_degree = torch.cat([pad_1d_unsqueeze(i, max_node_num) for i in data.in_degree]).to(device)
        data.out_degree = torch.cat([pad_1d_unsqueeze(i, max_node_num) for i in data.out_degree]).to(device)

    def _forward(self, data):
        import pdb

        pdb.set_trace()
        self.preprocess_g2g_data(data)

        pos = data.pos
        batch = data.batch
        z = data.z.long()


        pos -= scatter(pos, batch, dim=0)[batch]

        if self.use_pbc:
            from uni_electrolyte.evaluator.dataset import get_pbc_distances
            out = get_pbc_distances(
                data.pos,
                data.edge_index,
                data.cell,
                data.cell_offsets,
                data.neighbors,
                return_distance_vec=True
            )
            edge_index = out["edge_index"]
            j, i = edge_index
            dist = out["distances"]
            vecs = out["distance_vec"]
        else:
            edge_index = radius_graph(pos, r=self.cutoff, batch=batch, max_num_neighbors=1000)
            j, i = edge_index
            vecs = pos[j] - pos[i]
            dist = vecs.norm(dim=-1)

        # embed z
        z_emb = self.z_emb_ln(self.z_emb(z))
        
        # # # # construct edges based on the cutoff value
        # # # edge_index = radius_graph(pos, r=self.cutoff, batch=batch)
        # # # i, j = edge_index
        
        # embed pair-wise distance
        # # # dist = torch.sqrt(torch.sum((pos[i] - pos[j]) ** 2, 1))
        # radial_emb shape: (num_edges, num_radial), radial_hidden shape: (num_edges, hidden_channels)
        radial_emb = self.radial_emb(dist)	
        radial_hidden = self.radial_lin(radial_emb)	
        rbounds = 0.5 * (torch.cos(dist * pi / self.cutoff) + 1.0)
        radial_hidden = rbounds.unsqueeze(-1) * radial_hidden

        # init invariant node features
        # shape: (num_nodes, hidden_channels)
        s = self.neighbor_emb(z, z_emb, edge_index, radial_hidden)

        # init equivariant node features
        # shape: (num_nodes, 3, hidden_channels)
        vec = torch.zeros(s.size(0), 3, s.size(1), device=s.device)

        # bulid edge-wise frame
        edge_diff = vecs
        edge_diff = edge_diff / (dist.unsqueeze(1) + self.eps)
        # noise = torch.clip(torch.empty(1,3).to(z.device).normal_(mean=0.0, std=0.1), min=-0.1, max=0.1)
        edge_cross = torch.cross(pos[i], pos[j])
        edge_cross = edge_cross / ((torch.sqrt(torch.sum((edge_cross) ** 2, 1).unsqueeze(1))) + self.eps)
        edge_vertical = torch.cross(edge_diff, edge_cross)
        # shape: (num_edges, 3, 3)
        edge_frame = torch.cat((edge_diff.unsqueeze(-1), edge_cross.unsqueeze(-1), edge_vertical.unsqueeze(-1)), dim=-1)

        node_frame = 0

        # LSE: local 3D substructure encoding
        # S_i_j shape: (num_nodes, 3, hidden_channels)
        S_i_j = self.S_vector(s, edge_diff.unsqueeze(-1), edge_index, radial_hidden)
        scalrization1 = torch.sum(S_i_j[i].unsqueeze(2) * edge_frame.unsqueeze(-1), dim=1)
        scalrization2 = torch.sum(S_i_j[j].unsqueeze(2) * edge_frame.unsqueeze(-1), dim=1)
        scalrization1[:, 1, :] = torch.abs(scalrization1[:, 1, :].clone())
        scalrization2[:, 1, :] = torch.abs(scalrization2[:, 1, :].clone())

        scalar3 = (self.lin(torch.permute(scalrization1, (0, 2, 1))) + torch.permute(scalrization1, (0, 2, 1))[:, :,
                                                                        0].unsqueeze(2)).squeeze(-1)
        scalar4 = (self.lin(torch.permute(scalrization2, (0, 2, 1))) + torch.permute(scalrization2, (0, 2, 1))[:, :,
                                                                        0].unsqueeze(2)).squeeze(-1)
        
        edge_weight = torch.cat((scalar3, scalar4), dim=-1) * rbounds.unsqueeze(-1)
        edge_weight = torch.cat((edge_weight, radial_hidden, radial_emb), dim=-1)

        
        for i in range(self.num_layers):
            ds, dvec = self.message_layers[i](
                s, vec, edge_index, radial_emb, edge_weight, edge_diff
            )

            s = s + ds
            vec = vec + dvec

            # FTE: frame transition encoding
            ds, dvec = self.FTEs[i](s, vec, node_frame)

            s = s + ds
            vec = vec + dvec

        s = self.last_layer(s)
        s = scatter(s, batch, dim=0, reduce=self.readout)
        if self.use_sigmoid:
            s = torch.sigmoid((s - 0.5) * 5)
        return s

    def forward(self, data):
        return self._forward(data)

    @property
    def num_params(self):
        return sum(p.numel() for p in self.parameters())





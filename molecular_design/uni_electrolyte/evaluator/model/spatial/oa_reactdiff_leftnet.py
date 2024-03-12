
import torch
from uni_electrolyte.evaluator.model.spatial.oa_reactdiff.trainer.pl_trainer import DDPMModule
from torch_geometric.nn import radius_graph
from torch import nn
from torch_scatter import scatter
EPS = 1e-6

class OA_REACTDIFF_LEFTNet(torch.nn.Module):
    def __init__(self,device):
        super(OA_REACTDIFF_LEFTNet, self).__init__()
        ddpm_trainer = DDPMModule.load_from_checkpoint(
            checkpoint_path="./model_file/pretrained-ts1x-diff.ckpt",
            map_location=device,
        )
        self.model = ddpm_trainer.ddpm.dynamics.model
        self.cutoff=self.model.cutoff
        self.last_layer = nn.Linear(8,1)
        #self.input_layer_norm= nn.LayerNorm(6)
    def forward(self,data):

        ATOM_MAPPING = {
            1: 0,
            6: 1,
            7: 2,
            8: 3,
            9: 4,
        }
        n_element = len(list(ATOM_MAPPING.keys()))


        pos = data.pos.to(torch.float32)
        batch = data.batch

        z = data.z.long().detach().tolist()

        _h_list = []
        # 原版的leftnet z shape: len(data.batch) 内容是原子号  oareactdiff版的是 len(data.batch)*8  其中，前5位是原子号one_hot 第6位是charge可为0 最后两位是扩散模型用的 见egnn_dynamics.EGNNDynamics.forward

        for atom_num in z:
            one_hot_v = [0] * n_element
            one_hot_v[ATOM_MAPPING[atom_num]] = 1
            _h = torch.tensor(one_hot_v + [0, ], device=pos.device, dtype=torch.float32)
            _h_list.append(_h)
        h = torch.stack(_h_list)
        ones=torch.ones(len(data.batch), 1,device=pos.device, dtype=torch.float32)
        zeros = torch.zeros(len(data.batch), 1,device=pos.device, dtype=torch.float32)
        h -= 0.5#h=self.input_layer_norm(h)
        h=torch.cat([h,ones, zeros], dim=1)
        pos=pos-torch.mean(pos,dim=0)

        edge_index = radius_graph(pos, r=self.cutoff, batch=batch, max_num_neighbors=1000)


        self.model.num_layers=3
        out_h,_,_=self.model.forward(h=h,pos=pos,edge_index=edge_index)
        out=self.last_layer(out_h)
        out = scatter(out, batch, dim=0, reduce="sum")
        return out
        pass
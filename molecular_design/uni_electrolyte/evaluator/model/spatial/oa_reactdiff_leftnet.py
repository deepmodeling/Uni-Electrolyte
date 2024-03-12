
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
        for atom_num in z:
            one_hot_v = [0] * n_element
            one_hot_v[ATOM_MAPPING[atom_num]] = 1
            _h = torch.tensor(one_hot_v + [0, 0, 0], device=pos.device, dtype=torch.float32)
            _h_list.append(_h)
        h = torch.stack(_h_list)
        edge_index = radius_graph(pos, r=self.cutoff, batch=batch, max_num_neighbors=1000)

        out_h,_,_=self.model.forward(h=h,pos=pos,edge_index=edge_index)
        out=self.last_layer(out_h)
        out = scatter(out, batch, dim=0, reduce=self.readout)
        return out
        pass
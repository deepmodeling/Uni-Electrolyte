
import torch
# import numpy as np
# from pympler import asizeof

def get_square_subsequent_mask(seq_len):
    mask = (torch.triu(torch.ones(seq_len, seq_len)) == 1).transpose(0, 1)
    mask = mask.float().masked_fill(mask == 0, float('-inf')).masked_fill(mask == 1, float(0.0))
    return mask
def make_std_mask(tgt, pad):
    "Create a mask to hide padding and future words."
    tgt_mask = (tgt != pad).unsqueeze(-2)
    tgt_mask = tgt_mask & Variable(
        subsequent_mask(tgt.size(-1)).type_as(tgt_mask.data))
    return tgt_mask

def pad_1d_unsqueeze(x, padlen):
    x = x + 1 # pad id = 0
    xlen = x.size(0)
    if xlen < padlen:
        new_x = x.new_zeros([padlen], dtype=x.dtype)
        new_x[:xlen] = x
        x = new_x
    return x.unsqueeze(0)
def pad_y_unsqueeze(x, padlen):
    #x = x + 1 # pad id = 0
    xlen = x.size(0)
    if xlen < padlen:
        new_x = x.new_zeros([padlen], dtype=x.dtype)
        new_x[:xlen] = x
        x = new_x
    return x.unsqueeze(0)

def pad_2d_unsqueeze(x, padlen):
    x = x + 1 # pad id = 0
    xlen, xdim = x.size()
    if xlen < padlen:
        new_x = x.new_zeros([padlen, xdim], dtype=x.dtype)
        new_x[:xlen, :] = x
        x = new_x
    return x.unsqueeze(0)

def pad_attn_bias_unsqueeze(x, padlen):
    xlen = x.size(0)
    if xlen < padlen:
        new_x = x.new_zeros([padlen, padlen], dtype=x.dtype).fill_(float('-inf'))
        new_x[:xlen, :xlen] = x
        new_x[xlen:, :xlen] = 0
        x = new_x
    return x.unsqueeze(0)
def pad_y_attn_bias_unsqueeze(x, padlen):
    xlen = x.size(0)
    if xlen < padlen:
        new_x = x.new_zeros([padlen, padlen], dtype=x.dtype).fill_(0)
        new_x[:xlen, :xlen] = x
        x = new_x
    return x.unsqueeze(0)

def pad_edge_type_unsqueeze(x, padlen):
    xlen = x.size(0)
    if xlen < padlen:
        new_x = x.new_zeros([padlen, padlen, x.size(-1)], dtype=x.dtype)
        new_x[:xlen, :xlen, :] = x
        x = new_x
    return x.unsqueeze(0)

def pad_rel_pos_unsqueeze(x, padlen):
    x = x + 1
    xlen = x.size(0)
    if xlen < padlen:
        new_x = x.new_zeros([padlen, padlen], dtype=x.dtype)
        new_x[:xlen, :xlen] = x
        x = new_x
    return x.unsqueeze(0)

def pad_centrality_unsqueeze(x, padlen):
    xlen = x.size(0)
    if xlen < padlen:
        new_x = x.new_zeros([padlen, padlen], dtype=x.dtype)
        new_x[:xlen, :xlen] = x
        x = new_x
    return x.unsqueeze(0)

def pad_rel_pos_3d_unsqueeze(x, padlen):
    xlen = x.size(0)
    if xlen < padlen:
        new_x = x.new_zeros([padlen, padlen], dtype=x.dtype)
        new_x[:xlen, :xlen] = x
        x = new_x
    return x.unsqueeze(0)

def pad_3d_unsqueeze(x, padlen1, padlen2, padlen3):
    x = x + 1
    xlen1, xlen2, xlen3, xlen4 = x.size()
    if xlen1 < padlen1 or xlen2 < padlen2 or xlen3 < padlen3:
        new_x = x.new_zeros([padlen1, padlen2, padlen3, xlen4], dtype=x.dtype)
        new_x[:xlen1, :xlen2, :xlen3, :] = x
        x = new_x
    return x.unsqueeze(0)

def pad_lpe_unsqueeze(x, padlen1, padlen2, padlen3):
    #print(x)
    try:
        xlen1, xlen2, xlen3 = x.size()
    except:
        raise Exception(type(x))
    try:
        if xlen1 < padlen1 or xlen2 < padlen2 or xlen3 < padlen3:
            new_x = torch.zeros([padlen1, padlen2, padlen3], dtype=x.dtype)
            new_x[:xlen1, :xlen2, :xlen3] = x
            x = new_x.unsqueeze(0)
        else:
            return x.unsqueeze(0).float()
    except:
        #print("b")
        return x.unsqueeze(0).float()

    return x.float()

weight = torch.ones(118*4+32+2+1+10,dtype=torch.float)
weight[0] = 0.1


class Batch():
    def __init__(self, idx, attn_bias, attn_edge_type, rel_pos, all_rel_pos_3d_1, 
    in_degree, out_degree, x, edge_input, y, y_gt ,reverse, num_nodes, batch,smiles,EP_ID):
        super(Batch, self).__init__()
        self.idx = idx
        self.in_degree, self.out_degree = in_degree, out_degree
        self.x= x
        self.attn_bias, self.attn_edge_type, self.rel_pos = attn_bias, attn_edge_type, rel_pos
        self.edge_input = edge_input
        self.all_rel_pos_3d_1 = all_rel_pos_3d_1
#         print("self")
        '''new'''
        self.y = y
        ##no need actually
        # global weight
        # self.weight = weight
        self.y_gt = y_gt
        self.reverse = reverse
        self.num_nodes = num_nodes
        self.batch = batch
        self.smiles=smiles
        self.EP_ID=EP_ID

    def to(self, device):
        self.idx = self.idx.to(device)
        self.in_degree, self.out_degree = self.in_degree.to(device), self.out_degree.to(device)
        self.x= self.x.to(device)
        self.attn_bias, self.attn_edge_type, self.rel_pos = self.attn_bias.to(device), self.attn_edge_type.to(device), self.rel_pos.to(device)
        self.edge_input = self.edge_input.to(device)
        self.all_rel_pos_3d_1 = self.all_rel_pos_3d_1.to(device)
        
        '''new'''
        self.y = self.y.to(device)
        # self.weight = self.weight.to(device)
        self.y_gt = self.y_gt.to(device)
        self.reverse = self.reverse.to(device)
        self.num_nodes = self.num_nodes.to(device)
        self.batch = self.batch.to(device)
        #self.y_max_NE_num = self.y_max_NE_num.to(device)
#         print("self")
        return self
    
    
    
    def __len__(self):
        return self.in_degree.size(0)


def collator(items, max_node=512, multi_hop_max_dist=20, rel_pos_max = 20,predicted_target="None"):
    # print("haha")
    
    items = [item for item in items if item is not None]
    items_ = [(item.idx, item.attn_bias, item.attn_edge_type, item.rel_pos, \
               item.in_degree, item.out_degree, item.x, \
               item.edge_input[:, :, :multi_hop_max_dist, :], getattr(item,predicted_target), \
               item.reverse,item.smiles,item.EP_ID) for item in items]
            # delete
            #    item.central_input, item.lpe_input, item.y_attn_bias, \
            #    item.lpe_eigenval) for item in items]
    idxs, attn_biases, attn_edge_types, rel_poses, in_degrees, out_degrees, xs, edge_inputs, ys, reverses,smiles,EP_ID = zip(*items_)
    # delete
    # central_inputs,lpe_inputs,y_attn_biases,lpe_eigenvals= zip(*items_)
    items_ = [(item.all_rel_pos_3d_1,) for item in items]

    all_rel_pos_3d_1s, = zip(*items_)
    
    #retrosynthesis or forward synthesis
    reverse = torch.cat([i for i in reverses])

    for idx, _ in enumerate(attn_biases):
        attn_biases[idx][1:, 1:][rel_poses[idx] >= rel_pos_max] = float('-inf')
    max_node_num = max(i.size(0) for i in xs)
    num_nodes = torch.tensor([i.size(0) + 1 for i in xs])
    batch = torch.cat([torch.full((x.size(0) + 1,), i, dtype=torch.long) for i, x in enumerate(xs)])
#     print("in5")
    max_dist = max(i.size(-2) for i in edge_inputs)
    
    '''new part'''
    y_gt = torch.cat([torch.tensor([[i]]) for i in ys])
    y = torch.cat([torch.tensor([[i]]) for i in ys])
    

    x = torch.cat([pad_2d_unsqueeze(i, max_node_num) for i in xs])
    edge_input = torch.cat([pad_3d_unsqueeze(i, max_node_num, max_node_num, max_dist) for i in edge_inputs])
    attn_bias = torch.cat([pad_attn_bias_unsqueeze(i, max_node_num + 1) for i in attn_biases])
    attn_edge_type = torch.cat([pad_edge_type_unsqueeze(i, max_node_num) for i in attn_edge_types])
    rel_pos = torch.cat([pad_rel_pos_unsqueeze(i, max_node_num) for i in rel_poses])
    all_rel_pos_3d_1 = torch.cat([pad_rel_pos_3d_unsqueeze(i, max_node_num) for i in all_rel_pos_3d_1s])
    in_degree = torch.cat([pad_1d_unsqueeze(i, max_node_num) for i in in_degrees])
    out_degree = torch.cat([pad_1d_unsqueeze(i, max_node_num) for i in out_degrees])

    return Batch(
        idx=torch.LongTensor(idxs),
        attn_bias=attn_bias,
        attn_edge_type=attn_edge_type,
        rel_pos=rel_pos,
        all_rel_pos_3d_1=all_rel_pos_3d_1,
        in_degree=in_degree,
        out_degree=out_degree,
        x=x,
        edge_input=edge_input,
        y=y,
        y_gt = y_gt,
        reverse = reverse,
        num_nodes = num_nodes,
        batch = batch,
        smiles=smiles,
        EP_ID=EP_ID
    )

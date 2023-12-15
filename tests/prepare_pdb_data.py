from uni_electrolyte.evaluator.dataset import db_2_pdb_pipeline


db_2_pdb_pipeline(
    db_path=r'/root/run_leftnet/data/old_vcm_db/train.db',
    workbase=r'./workbase_train',
    dump_root=r'./train',
    multiwfn_ini_path=r'/root/run_leftnet/multiwfn/settings.ini',
    multiwfn_inp_path=r'multiwfn_vol_input.txt',
    multiwfn_path=r'/root/run_leftnet/multiwfn/Multiwfn_noGUI',
    packmol_path=r'/root/run_leftnet/packmol/packmol/packmol',
    packmol_inp_path=r'packmol_init_inp.txt',
    pack_num=10,
)


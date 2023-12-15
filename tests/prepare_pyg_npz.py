from uni_electrolyte.evaluator.dataset import pdb_2_db, db_2_pbc_pyG_data, change_db_prop_from_csv


db_path = r'/root/run_leftnet/data/data_1010/db_data/iid_test.db'
pdb_2_db(pdb_root=r'/root/run_leftnet/data/data_1010/iid_test',
         db_path=db_path)
change_db_prop_from_csv(csv_path=r'/root/run_leftnet/data/old_vcm_csv/iid_test.csv',
                        db_path=db_path,
                        properties=['binding_e', 'viscosity', 'dielectric_constant'],
                        csv_id_idx=1)

db_2_pbc_pyG_data(db_path=db_path,
                  properties=['binding_e', 'viscosity', 'dielectric_constant'],
                  pyG_data_folder=r'/root/run_leftnet/data/data_1010/pyg_data/iid_test')

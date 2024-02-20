import numpy as np
import pandas as pd
import psycopg
from ase.db import connect
from pgvector.psycopg import register_vector
from psycopg.rows import dict_row
from tqdm import tqdm
from uni_electrolyte.evaluator.dataset.data_transform import smile_to_maccs_fp_arr
from uni_electrolyte.evaluator.inference.pyG_entry import infer_one_smile


def insert_db(table_name: str, db_path: str, enlarge_vs_dc: bool=True):
    with psycopg.connect(dbname='postgres', user="postgres", host="127.0.0.1", port=5432) as conn:
        register_vector(conn)
        conn.adapters.register_loader("numeric", psycopg.types.numeric.FloatLoader)
        with conn.cursor() as cur:
            cur.execute('CREATE EXTENSION IF NOT EXISTS vector')
            cur.execute(f'DROP TABLE IF EXISTS {table_name}')
            cur.execute(f'CREATE TABLE IF NOT EXISTS {table_name} '
                        '(EP_ID bigserial PRIMARY KEY, SMILES text, binding_e numeric, dielectric_constant numeric, '
                        'viscosity numeric, homo numeric, lumo numeric, struc_fp vector(167), prop_fp vector(5))')

            with cur.copy(
                    f"COPY {table_name} (EP_ID, SMILES, binding_e, dielectric_constant, viscosity, homo, lumo, struc_fp, prop_fp) FROM STDIN") as copy:
                with connect(db_path) as src_db:
                    for a_src_row in tqdm(src_db.select()):
                        info_list = [a_src_row.data.binding_e[0], a_src_row.data.dielectric_constant[0],
                                     a_src_row.data.viscosity[0],
                                     a_src_row.data.homo[0], a_src_row.data.lumo[0]]
                        copy.write_row(
                            [a_src_row.ep_id, a_src_row.smile,
                             info_list[0], info_list[1], info_list[2], info_list[3], info_list[4],
                             a_src_row.data.fingerprint,
                             np.array(info_list)])
            conn.commit()
            cur.execute(f'SELECT * FROM {table_name} LIMIT 1')
            info = cur.fetchone()
            print(info)


# insert_thu_db(table_name='test11', db_path=r'/home/postgres/workbase/db/merge_without_target_fp_exclude.db')


def query_db(smiles: str, table_name: str, top_k: int, mode: str=r'property', eval_ckpt_path: str=r'/home/postgres/leftnet_vcm'):
    with psycopg.connect(dbname='postgres', user="postgres", host="127.0.0.1", port=5432) as conn:
        register_vector(conn)
        conn.adapters.register_loader("numeric", psycopg.types.numeric.FloatLoader)
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('CREATE EXTENSION IF NOT EXISTS vector')
            # cur.execute(f'SELECT * FROM {table_name} LIMIT 1')
            if mode == 'property':
                cur.execute(f'SELECT * FROM {table_name} WHERE SMILES = %s LIMIT 1', (smiles,))
                matching_rows = cur.fetchall()
                if len(matching_rows) == 1:
                    q_arr = matching_rows[0]['prop_fp']
                    info_df = pd.DataFrame(dict(zip(['Binding energy(eV)', 'Dielectric constant', 'Viscosity (mPa*s)', 'HOMO(eV)', 'LUMO(eV)'], q_arr.reshape((-1,1)))))
                    info_df.insert(loc=0, column='SMILES', value=smiles)
                    info_df.to_csv(r'input_smiles_properties.csv', index=False)
                else:
                    q_arr = infer_one_smile(target_smile=smiles, eval_ckpt_path=eval_ckpt_path)
                # cur.execute(f'SELECT * FROM (SELECT * FROM {table_name} ORDER BY prop_fp <-> %s LIMIT {top_k}) AS subquery ORDER BY binding_e ASC', (q_arr,))
                cur.execute(f'SELECT * FROM {table_name} ORDER BY prop_fp <-> %s LIMIT {top_k}', (q_arr,))
            elif mode == 'structure':
                q_arr = smile_to_maccs_fp_arr(smiles)
                # cur.execute(f'SELECT * FROM (SELECT * FROM {table_name} ORDER BY struc_fp <-> %s LIMIT {top_k}) AS subquery ORDER BY binding_e ASC', (q_arr,))
                cur.execute(f'SELECT * FROM {table_name} ORDER BY struc_fp <-> %s LIMIT {top_k}', (q_arr,))
            else:
                raise NotImplementedError
            info = cur.fetchall()
    df = pd.DataFrame(data=info)
    # df = df.drop(columns=['struc_fp', 'prop_fp', 'ep_id'])
    df = df.drop(columns=['prop_fp'])
    real_decorated_property_names = {
        # 'ep_id': 'EP ID',
                                     'smiles': 'SMILES',
                                     'binding_e': 'Binding energy(eV)',
                                     'homo': 'HOMO(eV)',
                                     'lumo': 'LUMO(eV)',
                                     'dielectric_constant': 'Dielectric constant',
                                     'viscosity': 'Viscosity (mPa*s)',
                                     }
    df = df.rename(columns=real_decorated_property_names)
    df = df.head(50)
    return df


def screen_db(conditions_dict: dict, table_name: str='updated_thu_cho'):
    with psycopg.connect(dbname='postgres', user="postgres", host="127.0.0.1", port=5432) as conn:
        register_vector(conn)
        conn.adapters.register_loader("numeric", psycopg.types.numeric.FloatLoader)
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('CREATE EXTENSION IF NOT EXISTS vector')

            # Constructing the WHERE clause dynamically based on the conditions_dict
            where_clause = " AND ".join(
                [f"{key} BETWEEN {value[0]} AND {value[1]}" for key, value in conditions_dict.items()])

            cur.execute(f'SELECT * FROM {table_name} WHERE {where_clause} ORDER BY binding_e ASC')
            info = cur.fetchall()
    df = pd.DataFrame(data=info)
    df = df.drop(columns=['prop_fp'])
    real_decorated_property_names = {'ep_id': 'EP ID',
                                     'smiles': 'SMILES',
                                     'binding_e': 'Binding energy(eV)',
                                     'homo': 'HOMO(eV)',
                                     'lumo': 'LUMO(eV)',
                                     'dielectric_constant': 'Dielectric constant',
                                     'viscosity': 'Viscosity (mPa*s)',
                                     }
    df = df.rename(columns=real_decorated_property_names)
    df = df.head(50)
    return df


# query_db(smiles='COCCOC', table_name='test11', top_k=5)

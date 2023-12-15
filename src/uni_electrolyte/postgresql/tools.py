import pandas as pd
import psycopg
from ase.db import connect
from pgvector.psycopg import register_vector
from psycopg.rows import dict_row
from tqdm import tqdm
from uni_electrolyte.evaluator.dataset.data_transform import smile_to_maccs_fp_arr


def insert_db(table_name: str, db_path: str):
    with psycopg.connect(dbname='postgres', user="postgres", host="127.0.0.1", port=5432) as conn:
        register_vector(conn)
        conn.adapters.register_loader("numeric", psycopg.types.numeric.FloatLoader)
        with conn.cursor() as cur:
            cur.execute('CREATE EXTENSION IF NOT EXISTS vector')
            cur.execute(f'DROP TABLE IF EXISTS {table_name}')
            cur.execute(f'CREATE TABLE IF NOT EXISTS {table_name} '
                        '(EP_ID bigserial PRIMARY KEY, SMILES text, binding_e numeric, dielectric_constant numeric, '
                        'viscosity numeric, homo numeric, lumo numeric, FingerPrint vector(167))')

            with cur.copy(
                    f"COPY {table_name} (EP_ID, SMILES, binding_e, dielectric_constant, viscosity, homo, lumo, FingerPrint) FROM STDIN") as copy:
                with connect(db_path) as src_db:
                    for a_src_row in tqdm(src_db.select()):
                        copy.write_row(
                            [a_src_row.ep_id, a_src_row.smile, a_src_row.data.binding_e[0],
                             a_src_row.data.dielectric_constant[0],
                             a_src_row.data.viscosity[0], a_src_row.data.homo[0], a_src_row.data.lumo[0],
                             a_src_row.data.fingerprint])

            conn.commit()
            cur.execute(f'SELECT * FROM {table_name} LIMIT 1')
            info = cur.fetchone()
            print(info)


# insert_thu_db(table_name='test11', db_path=r'/home/postgres/workbase/db/merge_without_target_fp_exclude.db')


def query_db(smiles: str, table_name: str, top_k: int):
    q_arr = smile_to_maccs_fp_arr(smiles)
    with psycopg.connect(dbname='postgres', user="postgres", host="127.0.0.1", port=5432) as conn:
        register_vector(conn)
        conn.adapters.register_loader("numeric", psycopg.types.numeric.FloatLoader)
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute('CREATE EXTENSION IF NOT EXISTS vector')
            cur.execute(f'SELECT * FROM {table_name} LIMIT 1')
            cur.execute(f'SELECT * FROM {table_name} ORDER BY FingerPrint <-> %s LIMIT {top_k}', (q_arr,))
            info = cur.fetchall()
    df = pd.DataFrame(data=info)
    real_decorated_property_names = {'ep_id': 'EP ID',
                                     'smiles': 'SMILES',
                                     'binding_e': 'Binding energy(eV)',
                                     'homo': 'HOMO(eV)',
                                     'lumo': 'LUMO(eV)',
                                     'dielectric_constant': 'Dielectric constant',
                                     'viscosity': 'Viscosity (mPa*s)',
                                     'fingerprint': 'FingerPrint'
                                     }
    df = df.rename(columns=real_decorated_property_names)
    return df
# query_db(smiles='COCCOC', table_name='test11', top_k=5)

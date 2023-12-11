import sys
import os
from pathlib import Path
from dp.launching.typing import BaseModel, Field, OutputDirectory,InputFilePath, Int,  Union, String, Literal, Field, Enum
from dp.launching.cli import SubParser,default_minimal_exception_handler,run_sp_and_exit,to_runner
import pandas as pd
def SCORING_func(mol_file ,id_tag,output_dir):
    os.system("mkdir -p %s" % (output_dir))

    for target,sigmoid_inf,sigmoid_sup in [("be",-5,1),("log_dcs",-0.5,2.5),("log_vs",-4,3),("HOMO",-18,3),("LUMO",-8,13)]:

        os.system(f"export PYTHONPATH=\"$PYTHONPATH: /root/Uni-Electrolyte/scoring_model/g2gt/src \" && \
        python  /root/Uni-Electrolyte/scoring_model/g2gt/src/rem4electrolyte_data.py    --predicted_target {target}   \
        --predict_dataset_name inference_dataset_{target}  \
        --predict_input_csv_file_path {mol_file}  \
        --predict_output_csv_file_path {output_dir}/output_bohrium_{target}.csv \
        --log_name_prefix  inference \
        --inference \
        --ID_name {id_tag} \
        --sigmoid_inf {sigmoid_inf}  --sigmoid_sup {sigmoid_sup}    ")


    total_tmp_dict={}
    for target in ["be", "log_dcs", "log_vs", "HOMO", "LUMO"]:
        df=pd.read_csv( f"{output_dir}/output_bohrium_{target}.csv")
        for index, row in df.iterrows():
            ID = row['ID']
            smiles = row['smiles']
            y_pred = row['y_pred']
            if ID not in total_tmp_dict:
                total_tmp_dict[ID]={}
            if "smiles" not in  total_tmp_dict[ID]:
                total_tmp_dict[ID]["smiles"]=smiles
            elif smiles != total_tmp_dict[ID]["smiles"]:
                smiles2=total_tmp_dict[ID]["smiles"]
                raise Exception(f"ID:{ID} smiles not match smiles1:{smiles},smiles2:{smiles2}")
            total_tmp_dict[ID]["%s_pred"%(target)]=y_pred

    total_output_dataframe_dict = {id_tag: [],  "smiles": []}
    for target in ["be", "log_dcs", "log_vs", "HOMO", "LUMO"]:
        total_output_dataframe_dict["%s_pred" % (target)]= []
    for ID in total_tmp_dict:
        total_output_dataframe_dict[id_tag].append(ID)
        total_output_dataframe_dict["smiles"].append(total_tmp_dict[ID]["smiles"])
        for target in ["be", "log_dcs", "log_vs", "HOMO", "LUMO"]:
            total_output_dataframe_dict["%s_pred" % (target)].append(total_tmp_dict[ID]["%s_pred" % (target)])
    #rename:
    total_output_dataframe_dict["dcs_pred"]=total_output_dataframe_dict["log_dcs_pred"]
    del total_output_dataframe_dict["log_dcs_pred"]
    total_output_dataframe_dict["vs_pred"] = total_output_dataframe_dict["log_vs_pred"]
    del total_output_dataframe_dict["log_vs_pred"]

    total_output_dataframe=pd.DataFrame(total_output_dataframe_dict)
    total_output_dataframe.to_csv( f"{output_dir}/output_bohrium_total.csv", index=False)

class SCORING(BaseModel):
    type: Literal["SCORING"]
    mol_file: InputFilePath = Field("""CSV ,the CSV file has 2 columns, "smiles" and id tag .""",)
    id_tag:String=Field()


class Options(BaseModel):
    contact: SCORING
    output_dir: OutputDirectory = Field(
        default="./output"
    )  # default will be override after online


class global_opt(Options, BaseModel):
    ...


def runner(opts:  global_opt) -> int:
    SCORING_func(mol_file=opts.contact.mol_file,id_tag=opts.contact.id_tag,output_dir=opts.output_dir)


def to_parser():
    return to_runner(
        global_opt,
        runner,
        version="0.1.0",
        exception_handler=default_minimal_exception_handler,
    )


if __name__ == '__main__':
    import sys
    to_parser()(sys.argv[1:])

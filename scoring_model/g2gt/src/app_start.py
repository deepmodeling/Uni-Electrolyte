import sys
import os
from pathlib import Path
from dp.launching.typing import BaseModel, Field, OutputDirectory,InputFilePath, Int,  Union, String, Literal, Field, Enum
from dp.launching.cli import SubParser,default_minimal_exception_handler,run_sp_and_exit,to_runner

def SCORING_func(mol_file ,id_tag,output_dir):
    target = "be"
    os.system("export PYTHONPATH=\"$PYTHONPATH: /root/Uni-Electrolyte/scoring_model/g2gt/src \" && \
    python  /root/Uni-Electrolyte/scoring_model/g2gt/src/rem4electrolyte_data.py    --predicted_target %s   \
    --predict_dataset_name inference_dataset  \
    --predict_input_csv_file_path %s  \
    --predict_output_csv_file_path %s \
    --log_name_prefix  inference \
    --inference \
    --ID_name EP_ID \
    --sigmoid_inf -5  --sigmoid_sup 1    "%(target,InputFilePath,"./output/output_bohrium_%s.csv"%target))


class SCORING(BaseModel):
    type: Literal["SCORING"]
    mol_file: InputFilePath = Field("""CSV or sdf, the CSV file has 2 columns, "smiles" and id tag .
    In the sdf file, each conformation has id tag  and "smiles" tag
    Each smiles and ID could only appear once and correspond to a unique conformation.""",)
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
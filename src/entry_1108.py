import os
import shutil
import sys
from pathlib import Path

from dp.launching.cli import to_runner, SubParser, default_minimal_exception_handler, run_sp_and_exit
from dp.launching.typing import BaseModel, Field
from dp.launching.typing import BohriumUsername, BohriumTicket, BohriumProjectId, BohriumPlatform, BohriumMachineType
from dp.launching.typing import InputFilePath, OutputDirectory
from dp.launching.typing import Int, Float, List, Enum, String, Set

sys.path.append('.')

from sub_image.pyG_infer import leftnet_dpdispatcher
from sub_image.postgres import postgres_interaction


#########################################################################################


class TargetOptions(String, Enum):
    """
    Define the target to be predicted.
    """
    binding_e = 'Binding_Energy'
    dielectric_constant = 'Dielectric_Constant'
    # viscosity = 'Viscosity'
    # homo = 'HOMO'
    # lumo = 'LUMO'


class PostgresHandler(String, Enum):
    """
    Postgres database option
    """
    insert = 'insert'


class HardwareOptions(String, Enum):
    """
    Choose hardware for sub-models.
    """
    T4 = "1 * NVIDIA T4_16g"
    V100 = '1 * NVIDIA V100_16g'


class PlatformOptions(String, Enum):
    """
    Choose platform for sub-models.
    """
    ali = "ali"
    paratera = 'paratera'


class dpdispatcher_Model(BaseModel):
    """
    Define commandline parameters
    """
    # `...`表示这个是必须的参数
    input_file_path: InputFilePath = Field(..., description='Path to input file.')
    output_directory: OutputDirectory = Field(default='./output')
    target: Set[TargetOptions] = Field(..., description='Target to be predicted.')
    postgres_handler: Set[PostgresHandler] = Field(..., description='How to interact with postgres.')
    hardware: HardwareOptions = Field(..., description='Choose hardware for sub-models.')
    platform: PlatformOptions = Field(..., description='Choose platform for sub-models.')
    bohrium_username: BohriumUsername
    bohrium_project_id: BohriumProjectId
    bohrium_ticket: BohriumTicket


def leftnet_dpdispatcher_postgres(opts: dpdispatcher_Model):
    cwd_ = os.getcwd()
    target_list = []
    for a_target in opts.target:
        target_list.append(a_target.value)
    cmdline_list = ['python /root/launching_entry/entry_1026.py leftnet --input_file_path',
                    opts.input_file_path.get_path(), '--target']
    cmdline_list.extend(target_list)
    cmdline = ' '.join(cmdline_list)
    machine_info = {
        # 'password': opts.bohrium_password.get_value(),
        'email': opts.bohrium_username.get_value(),
        'ticket': opts.bohrium_ticket.get_value(),
        'project_id': int(opts.bohrium_project_id.get_value()),
        'hardware': opts.hardware.value,
        'platform': opts.platform.value
    }

    leftnet_dpdispatcher(machine_info=machine_info, cmdline=cmdline)

    shutil.copytree(src=os.path.join(cwd_, 'output'),
                    dst=os.path.join(opts.output_directory.get_full_path(), 'LEFTNet_Results'))

    postgres_workbase = os.path.join(cwd_, 'postgres')
    os.makedirs(postgres_workbase)
    shutil.copy(src=os.path.join(cwd_, 'output', 'output_properties.csv'),
                dst=os.path.join(postgres_workbase, 'output_properties.csv'))

    for an_interaction in opts.postgres_handler:
        postgres_interaction(postgres_handler=an_interaction.value, workbase=postgres_workbase)


def to_parser():
    return {
        "run_dump": SubParser(dpdispatcher_Model, leftnet_dpdispatcher_postgres,
                                          "Run leftnet with dpdispatcher and dump results to postgres"),
    }


if __name__ == '__main__':
    import sys

    run_sp_and_exit(
        to_parser(),
        description="Example",
        version="0.1.0",
        exception_handler=default_minimal_exception_handler,
    )

from loguru import logger
from dash import callback
from dash import Input, Output, State, no_update

from views.starter import render_molecule
from views.molecule import render_target_molecule
from topics import Topics

import controllers.validators.options  # noqa
import controllers.options  # noqa
import controllers.running  # noqa
import controllers.starter  # noqa
import controllers.editor  # noqa
import controllers.molecule  # noqa
import controllers.result  # noqa
import controllers.common  # noqa
import controllers.route  # noqa
import controllers.jobs  # noqa
import controllers.login  # noqa
import controllers.projects  # noqa

from ids import KETCHER_COMPONENT_ID

from rdkit import Chem


def are_same_molecule(smiles1, smiles2):
    mol1 = Chem.MolFromSmiles(smiles1)
    mol2 = Chem.MolFromSmiles(smiles2)
    if not mol1 or not mol2:
        return True

    # 标准化分子结构
    Chem.SanitizeMol(mol1)
    Chem.SanitizeMol(mol2)

    # 将标准化后的分子对象转化为 SMILES 进行比较
    standardized_smiles1 = Chem.MolToSmiles(mol1)
    standardized_smiles2 = Chem.MolToSmiles(mol2)

    # 比较标准化后的 SMILES 是否相同
    return standardized_smiles1 == standardized_smiles2


# @callback(
#     Output("molecule_editor_view", "children"),
#     Input("input-molecule", "value"),
#     State("viewport", "data"),
#     prevent_initial_call=True,
# )
# def input_molecule(mol, viewport):
#     logger.info(f"input molecule {mol}")
#     return render_molecule(mol, viewport)


@callback(
    Output("input-molecule", "value"),
    KETCHER_COMPONENT_ID.get_input("output_molecule"),
    [State("input-molecule", "value"), State("viewport", "data")],
    prevent_initial_call=True,
)
def sync_molecule(molecule, current_molecule, viewport):
    logger.info(
        f"sync molecule molecule {molecule} current_molecule {current_molecule}"
    )
    if are_same_molecule(molecule, current_molecule):
        return no_update
    return molecule


@callback(
    Topics.Slots.target_molecule.get_output("data"),
    KETCHER_COMPONENT_ID.get_output("input_molecule", allow_duplicate=False),
    Input("input-molecule", "value"),
    State("viewport", "data"),
    prevent_initial_call=True,
)
def sync_molecule_render(molecule, viewport):
    logger.info(f"sync molecule")
    return molecule, molecule

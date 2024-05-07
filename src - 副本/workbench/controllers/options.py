from loguru import logger
from dash import callback, Input, Output, ctx, State, ALL, no_update
from controllers.validators.options import validate_run_options
from views.options import render_rerun_backup
from models.session import JobStatus
from utils.rdkit_utils import validate_smiles
from topics import Topics

#
# @callback(
#     Output("btn-run", "disabled"),
#     [
#         Topics.Slots.target_molecule.get_input("data"),
#         Input("btn-run", "n_clicks"),
#         Topics.Slots.job_status.get_input("data"),
#     ],
#     [
#         Topics.Slots.token.get_state("data"),
#         State("input-bohrium-project", "value"),
#     ],
#     prevent_initial_call=True,
# )
# def toggle_run_button_disable(
#     smiles, run_n_clicks, job_status, token, bohrium_project_id
# ):
#     if not token:
#         return False
#     if ctx.triggered_id == "btn-run":
#         return bool(run_n_clicks)
#     elif (
#         isinstance(ctx.triggered_id, dict)
#         and ctx.triggered_id.get("name") == "job_status"
#     ):
#         return (
#             job_status not in (JobStatus.success, JobStatus.stopped, JobStatus.failed)
#             or not job_status
#         )
#     elif (
#         isinstance(ctx.triggered_id, dict)
#         and ctx.triggered_id.get("name") == "target_molecule"
#     ):
#         return not validate_smiles(smiles) or not bohrium_project_id
#     return True
#
#
# @callback(
#     Topics.Slots.options.get_output("data", allow_duplicate=False),
#     [
#         Topics.Slots.target_molecule.get_input("data"),
#         Input({"view": "options", "type": "input", "name": ALL}, "value"),
#     ],
#     [
#         Topics.Slots.target_molecule.get_state("data"),
#         State({"view": "options", "type": "input", "name": ALL}, "value"),
#     ],
# )
# def toggle_update_options(
#     target_molecule, triggered_value, state_molecule, state_value
# ):
#     if not target_molecule:
#         target_molecule = state_molecule
#     logger.info(
#         f"toggle_update_options "
#         f"target_molecule: {target_molecule}\n"
#         f"triggered_value: {triggered_value}\n"
#         f"state_value: {state_value}\n"
#         f"triggered_id: {ctx.triggered_id}\n"
#         f"states: {ctx.states_list}"
#     )
#     states_list = ctx.states_list[1]
#     tmp = {}
#     res = {}
#     for _, state in enumerate(states_list):
#         tmp[state["id"]["name"]] = state["value"]
#
#     logger.info(f"tmp {tmp}")
#     # rebuild fields for backend job
#
#     res["reaction_type"] = tmp.pop("reaction-type")
#     res["check_system"] = tmp.pop("check-system")
#     res["route_diversity"] = tmp.pop("route-diversity")
#     res["max_iteration"] = tmp.pop("max-iteration")[1]
#     res["debug"] = tmp.pop("demo-mode", False)
#     res["input_ligand"] = target_molecule
#     logger.info(f"return res {res}")
#     return res

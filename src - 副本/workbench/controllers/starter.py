from loguru import logger
from dash import Output, callback, ctx, Input, html
from utils.tracer import trace_time
from topics import Topics
import dash_bootstrap_components as dbc
from utils.rdkit_utils import validate_smiles
from utils.bohrium import get_projects, get_default_project


# fill input-bohrium-project when token changed
@callback(
    [
        Output("input-bohrium-project", "options"),
        Output("input-bohrium-project", "disabled"),
        Output("input-bohrium-project", "value"),
        Output("error-alert", "children", allow_duplicate=True),
    ],
    Topics.Slots.token.get_input("data"),
    prevent_initial_call=True,
)
def fill_bohrium_projects(token):
    if not token:
        return [], True, "", ""
    projects = get_projects(token)
    if not projects:
        return (
            [],
            True,
            "",
            dbc.Alert(
                [
                    "* No Bohrium Project found, Please visit ",
                    html.A(
                        "here", href="https://bohrium.dp.tech/projects", target="_blank"
                    ),
                    " to create one.",
                ],
                color="danger",
                className="dp-alert",
            ),
        )
    options = [{"label": p["projectName"], "value": p["projectId"]} for p in projects]
    return options, False, options[0]["value"], ""


@callback(
    Output("input-molecule", "valid"),
    Output("input-molecule-error-alert", "children"),
    Input("input-molecule", "value"),
    prevent_initial_call=True,
)
def toggle_validate_smiles(smiles):
    if not smiles:  # Empty input
        return False, None

    valid = validate_smiles(smiles)
    if valid:
        return True, None  # SMILES is valid
    else:
        return False, dbc.Alert(
            "* Invalid SMILES", color="danger", className="dp-alert"
        )  # SMILES is invalid

#
# # 当切换到 New 时展示 starter view
# @callback(
#     Output("row-starter-view", "style"),
#     [
#         Topics.Slots.exploration_name.get_input("data"),
#     ],
#     prevent_initial_call=True,
# )
# @trace_time
# def toggle_starter_view(exp_name):
#     # TODO running 状态下切换 tab 有问题
#     logger.info(f"toggle_starter_view {ctx.triggered_id}, exp_name {exp_name}")
#     if (
#         isinstance(ctx.triggered_id, dict)
#         and ctx.triggered_id.get("name") == "exploration_name"
#     ):
#         if exp_name == "":
#             # raise Exception
#             return {
#                 "flex": "8",
#                 "minHeight": "400px",
#                 "height": "550px",
#                 "alignItems": "flexStart",
#                 "width": "100%",
#             }
#         else:
#             return {"display": "none"}
#     else:
#         return {"display": "none"}

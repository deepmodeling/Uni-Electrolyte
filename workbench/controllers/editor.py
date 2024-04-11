from loguru import logger
from dash import callback, Input, Output, ctx, State, ALL, no_update
from dash.exceptions import PreventUpdate

from views.editor import render_workflow
from utils.token_helper import get_user_id
from models.session import Session, JobStatus
from utils.tracer import trace_time
from topics import Topics
from utils.metrics import log_metrics


@callback(
    [
        Output("row-main-view", "style", allow_duplicate=True),
        Output("row-main-view", "children", allow_duplicate=True),
    ],
    [
        Input("btn-run", "n_clicks"),
        Topics.Slots.job_id.get_input("data"),
        Topics.Slots.job_status.get_input("data"),
    ],
    [
        Topics.Slots.exploration_name.get_state("data"),
        Topics.Slots.job_id.get_state("data"),
        Topics.Slots.token.get_state("data"),
    ],
    prevent_initial_call=True,
)
@trace_time
def toggle_main_view(n_clicks, job_id, job_status, exp_name, job_id_state, token):
    user_id = get_user_id(token)
    if not user_id:
        logger.error("failed to get_user_id")
        return no_update, no_update

    if ctx.triggered_id == "btn-run":
        return {
            "display": "none",
        }, no_update

    if (
        isinstance(ctx.triggered_id, dict)
        and ctx.triggered_id.get("name") == "job_status"
    ):
        job_id = job_id_state
    if not job_id:
        return {
            "display": "none",
        }, no_update

    # fill route data to workflow
    if job_status == JobStatus.success:
        s: Session = Session.load(user_id)
        exp = s.explorations[s.get_exploration_index(exp_name)]
        job = exp.jobs[exp.get_job_index(job_id)]
        routes = job.routes
        if not routes:
            workflow = ""
        else:
            workflow = render_workflow(
                exp_name, job_id, 0, routes[0].workflow, routes[0].download_smiles
            )

        return {
            "flex": "8",
            "display": "flex",
            "paddingRight": "0.2rem",
            # "paddingLeft": "0.2rem",
        }, workflow
    else:
        return {
            "display": "none",
        }, no_update


@callback(
    Output("row-main-view", "children", allow_duplicate=True),
    Input(
        {
            "view": "result",
            "table": "table-candidate-routes",
            "type": "tr",
            "index": ALL,
            "job": ALL,
        },
        "n_clicks",
    ),
    [
        Topics.Slots.exploration_name.get_state("data"),
        Topics.Slots.job_id.get_state("data"),
        Topics.Slots.token.get_state("data"),
    ],
    prevent_initial_call=True,
)
@trace_time
def toggle_render_workflow(n_clicks, exp_name, job_id, token):
    logger.info(
        f"toggle_render_workflow n_clicks {n_clicks} trigger_id {ctx.triggered_id}"
    )
    if not any(n_clicks):
        return no_update
    index = int(ctx.triggered_id.get("index"))
    user_id = get_user_id(token)
    if not user_id:
        logger.error("failed to get_user_id")
        return no_update
    if not exp_name:
        return no_update
    s: Session = Session.load(user_id)
    exp = s.explorations[s.get_exploration_index(exp_name)]
    job = exp.jobs[exp.get_job_index(job_id)]
    workflow = job.routes[index].workflow
    smiles = job.routes[index].download_smiles

    return render_workflow(exp_name, job_id, index, workflow, smiles)

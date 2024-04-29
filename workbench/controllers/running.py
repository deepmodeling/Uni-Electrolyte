import re
from loguru import logger
from dash import callback, Input, Output, ctx, State, no_update, dcc
from dash.exceptions import PreventUpdate
from launching.app import submit_job, get_job_status, get_job_result
from models.session import Session, Exploration, Job, JobStatus, ExplorationStatus
from utils.token_helper import get_user_id
from utils.id import get_uuid
from utils.tracer import trace_time
from topics import Topics
from utils.enhanced_callback import callback_with_metrics
import dash_bootstrap_components as dbc
#
#
# @callback(
#     [
#         Output("row-running-view", "style"),
#         Output("row-starter-view", "style", allow_duplicate=True),
#         Output("progress-interval", "disabled", allow_duplicate=True),
#     ],
#     [
#         Input("btn-run", "n_clicks"),
#         Topics.Slots.job_status.get_input("data"),
#     ],
#     [
#         Topics.Slots.token.get_state("data"),
#         Topics.Slots.username.get_state("data"),
#     ],
#     prevent_initial_call=True,
# )
# @trace_time
# def toggle_running_view(n_clicks, job_status, token, username):
#     logger.info(f"toggle_running_view {n_clicks} {job_status}")
#     if not token:
#         return no_update, no_update, no_update
#     if ctx.triggered_id == "btn-run" and n_clicks:
#         return (
#             {
#                 "flex": "8",
#                 "display": "flex",
#                 "minHeight": "400px",
#                 "alignItems": "flexStart",
#             },
#             {
#                 "display": "none",
#             },
#             no_update,
#         )
#     if not job_status:
#         return (
#             {
#                 "display": "none",
#             },
#             no_update,
#             True,
#         )
#     elif job_status in (
#         JobStatus.init,
#         JobStatus.preprocessed,
#         JobStatus.finished,
#         JobStatus.submitted,
#         JobStatus.start,
#         JobStatus.running,
#         JobStatus.downloading,
#         JobStatus.pending,
#     ):
#         return (
#             {
#                 "flex": "8",
#                 "display": "flex",
#                 "minHeight": "400px",
#                 "alignItems": "flexStart",
#             },
#             no_update,
#             False,
#         )
#     elif job_status in (JobStatus.failed, JobStatus.stopped):
#         return (
#             {
#                 "display": "none",
#             },
#             {
#                 "display": "none",
#             },
#             True,
#         )
#     elif job_status == JobStatus.success:
#         # success
#         return (
#             {
#                 "display": "none",
#             },
#             no_update,
#             True,
#         )
#     else:
#         logger.info(f"toggle_running_view job status {job_status}")
#         return no_update, no_update, no_update
#

# @callback(
#     [
#         Output("progress-run", "value"),
#         Output("progress-run", "label"),
#         Topics.Slots.job_status.get_output("data"),
#         Topics.Slots.exploration_status.get_output("data"),
#     ],
#     [
#         Input(
#             "progress-interval",
#             "n_intervals",
#         )
#     ],
#     [
#         Topics.Slots.job_id.get_state("data"),
#         Topics.Slots.job_status.get_state("data"),
#         Topics.Slots.exploration_name.get_state("data"),
#         Topics.Slots.token.get_state("data"),
#     ],
#     prevent_initial_call=True,
# )
# @trace_time
# def update_progress(n, job_id, current_job_status, exploration_name, token):
#     # get job status
#     # save session
#     # save current_job_status
#     # save current_exploration_status
#
#     logger.info("start update_progress")
#     user_id = get_user_id(token)
#     if not user_id:
#         logger.error("failed to get_user_id")
#         return
#     s = Session.load(user_id)
#     exp_idx = s.get_exploration_index(exploration_name)
#     exp: Exploration = s.explorations[exp_idx]
#
#     job_idx = exp.get_job_index(job_id)
#     job = exp.jobs[job_idx]
#
#     job_status = get_job_status(job_id)
#     label = job_status
#     # TODO get real progress from output
#     if job_status == JobStatus.running:
#         exp.status = ExplorationStatus.running
#         value = 50
#     elif job_status == JobStatus.init:
#         exp.status = ExplorationStatus.running
#         value = 10
#     elif job_status == JobStatus.preprocessed:
#         exp.status = ExplorationStatus.running
#         value = 20
#     elif job_status == JobStatus.submitted:
#         exp.status = ExplorationStatus.running
#         value = 30
#     elif job_status == JobStatus.finished:
#         exp.status = ExplorationStatus.running
#         value = 70
#     elif job_status == JobStatus.downloading:
#         exp.status = ExplorationStatus.running
#         value = 90
#     elif job_status == JobStatus.success:
#         value = 100
#         exp.status = ExplorationStatus.success
#     elif job_status in (JobStatus.failed, JobStatus.stopped):
#         value = 100
#         exp.status = ExplorationStatus.failed
#     else:
#         value = no_update
#         exp.status = ExplorationStatus.running
#     if current_job_status != job_status:
#         logger.info(f"job status changed! {current_job_status} -> {job_status}")
#         job.status = job_status
#         # get result if job success
#         if job_status == JobStatus.success:
#             routes_data = get_job_result(job_id)
#             job.set_routes(routes_data)
#         exp.jobs[job_idx] = job
#         s.explorations[exp_idx] = exp
#         # s.updated_at = datetime.now().isoformat()
#         s.save()
#
#     return value, label, job_status, exp.status
#
#
# @callback(
#     Output("input-project-error-alert", "children"),
#     Input("input-project-name", "value"),
# )
# def validate_project_name(project_name):
#     # TODO regex that only contain letters, numbers and hyphens
#     if project_name:
#         pattern = r"^[a-zA-Z0-9\-]+$"  # 匹配字母、数字和连字符
#         if re.match(pattern, project_name):
#             return None  # 项目名符合规则，返回空表示无错误
#         else:
#             return False, dbc.Alert(
#                 "* Project name can only contain letters, numbers, and hyphens.",
#                 color="danger",
#                 className="dp-alert",
#             )  # SMILES is invalid
#
#     else:
#         return None  # 若项目名为空，则不显示错误信息
#

@callback_with_metrics(
    [
        Topics.Slots.exploration_name.get_output("data"),
        Topics.Slots.exploration_status.get_output("data"),
        Topics.Slots.job_id.get_output("data"),
        Topics.Slots.job_status.get_output("data"),
        #Topics.Slots.target_molecule.get_output("data"),
    ],
    [
        Input("predict_properties_btn-run", "n_clicks"),
    ],
    [
        Topics.Slots.exploration_name.get_state("data"),
        State("input-project-name", "value"),
        #State("input-molecule", "value"),
        Topics.Slots.token.get_state("data"),
        Topics.Slots.predict_properties_options.get_state("data"),
        #Topics.Slots.target_molecule.get_state("data"),
        State("input-bohrium-project", "value"),
    ],
    prevent_initial_call=True,
)
@trace_time
def do_run_exploration(
    n_clicks,
    exploration_name,
    input_exp_name,
    #target_molecule,
    token,
    params,
    #target_molecule_state,
    bohrium_project_id,
):
    if not n_clicks:
        raise PreventUpdate

    # do_run_exploration
    # submit jobs
    # save session to redis( only put current exploration)
    # save exploration_name if not state.exploration_name
    # save current_exploration_status to init
    # save current_jobs_status to init
    # save current_jobs_id to init
    # performance issue: do_run_exploration took 3.8596789836883545 seconds
    logger.info(
        f"exploration_name: {exploration_name} \n"
        f"input_exp_name: {input_exp_name} \n"
        f"token: {token} \n"
        f"params: {params} \n"
        f"bohrium_project_id: {bohrium_project_id} \n"
    )

    user_id = get_user_id(token)
    logger.info(f"user_id: {user_id}")
    if not user_id:
        logger.error("failed to get_user_id")
        raise PreventUpdate
    s = Session.load(user_id)
    session_id=s.session_id
    logger.info(f"session_id: {session_id}")
    if not exploration_name:
        exploration_name = input_exp_name
    if not exploration_name:
        logger.error("exploration_name is empty")
        raise PreventUpdate
    exp_idx = s.get_exploration_index(exploration_name)
    size = len(s.explorations)
    if exp_idx == -1:
        exp = Exploration(
            id=get_uuid(),
            name=exploration_name,
            #target_molecule=target_molecule,
            bohrium_project_id=bohrium_project_id,
        )
        s.explorations.append(exp)
        exp_idx = size
    else:
        exp: Exploration = s.explorations[exp_idx]

    # save params to topics and load params
    # if not params.get("input_ligand", ""):
    #     params["input_ligand"] = target_molecule
    logger.info(
        f"start do_run_exploration {exploration_name}   \n"
        f"    params {params}"
    )
    params["brm_token"] = token
    job_id =222222
    # submit_job(
    #     token,
    #     params=params,
    #     job_name=exploration_name,
    #     bohrium_project_id=bohrium_project_id,
    # )
    job = Job(id=job_id, name=job_id)
    exp.jobs.append(job)
    s.explorations[exp_idx] = exp
    # s.updated_at = datetime.now()
    s.save()
    logger.info(
        f"finish do_run_exploration exploration_name {exploration_name}, exp.status {exp.status},"
        f" job_id {job_id}, job.status {job.status}"
    )

    return exploration_name, exp.status, job_id, job.status#, target_molecule

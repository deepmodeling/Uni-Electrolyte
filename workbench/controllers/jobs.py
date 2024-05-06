from datetime import datetime
from loguru import logger
from dash import callback, Input, Output, ctx, State, ALL, no_update
from utils.token_helper import get_user_id
from models.session import Session, JobStatus, RUNNING_JOB_STATUS
from views.jobs import render_jobs
from launching.app import get_job_status, get_job_result
from utils.tracer import trace_time
from topics import Topics


@callback(
    [
        Output(
            {
                "view": "jobs",
                "table": "job",
                "type": "tr",
                "index": ALL,
            },
            "className",
        ),
        Topics.Slots.job_id.get_output("data"),
        Topics.Slots.job_status.get_output("data"),
    ],
    Input("Query molecules with similar properties", "n_clicks"),
    [
        Topics.Slots.exploration_name.get_state("data"),
        Topics.Slots.token.get_state("data"),
    ],
    prevent_initial_call=True,
)
@trace_time
def toggle_render_job_active(n_clicks, exp_name, token):
    return no_update, no_update, no_update
    if not ctx.triggered_id:
        return no_update
    logger.info(
        f"toggle_render_job_active index {ctx.triggered_id.get('index')} n_clicks {n_clicks} trigger_id {ctx.triggered_id}"
    )
    user_id = get_user_id(token)
    if not user_id:
        logger.error("failed to get_user_id")
        return no_update, no_update, no_update
    index = int(ctx.triggered_id.get("index"))
    if not any(n_clicks):
        index = -1
    class_names = ["" for i in range(0, len(n_clicks))]
    class_names[index] = "table-active"
    s: Session = Session.load(user_id)
    exp = s.explorations[s.get_exploration_index(exp_name)]
    job = exp.jobs[index]
    return class_names, job.id, job.status


@callback(
    Output("table-jobs", "children"),
    [
        Input(
            "tabs",
            "active_tab",
        ),
        Topics.Slots.exploration_name.get_input("data"),
        Input(
            "progress-interval",
            "n_intervals",
        )
    ],
    [
        Topics.Slots.token.get_state("data"),
    ],
    prevent_initial_call=True,
)
@trace_time
def toggle_job_tab(tab_id, exp_name,n, token):
    # TODO performance issue: batch query job status for performance issue.
    logger.info(f"toggle_job_tab {tab_id} {exp_name}")
    if ctx.triggered_id == "tabs" and tab_id != "tab-jobs":
        return no_update
    user_id = get_user_id(token)
    if not user_id:
        logger.error("failed to get_user_id")
        return no_update
    if not exp_name:
        return render_jobs([])
    s: Session = Session.load(user_id)

    # get jobs from launching api and update status.
    exp_idx = s.get_exploration_index(exp_name)
    exp = s.explorations[exp_idx]
    jobs = exp.jobs
    logger.info(f"jobs {len(exp.jobs)}")
    changed = False
    for i in range(len(jobs)):
        job = jobs[i]
        if job.status in RUNNING_JOB_STATUS or (
            job.status == JobStatus.success and not job.routes
        ):
            status = get_job_status(job.id)
            job.status = status
            if status == JobStatus.success:
                logger.info(f"get_job_result {job.id}")
                routes_data = get_job_result(job.id)
                # if routes_data:
                #     job.set_routes(routes_data)
            jobs[i] = job
            changed = True
    if changed:
        s.explorations[exp_idx].jobs = jobs
        s.updated_at = datetime.now().isoformat()
        s.save()
    return render_jobs(s.explorations[exp_idx].jobs)

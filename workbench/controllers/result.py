from loguru import logger
from dash import callback, Input, Output, ctx, ALL, State, no_update

#from views.result import render_backup_reactions
from utils.token_helper import get_user_id
from models.session import Session, Exploration, Job, Route
from topics import Topics
from launching.app import get_job_output_path
#from views.route import render_candidate_routes
#
#
# @callback(
#     Output("table-backup-reactions", "children"),
#     [
#         Input({"view": "editor-main", "job": ALL, "route": ALL}, "selectionEvent"),
#         Input("btn-run", "n_clicks"),
#     ],
#     [
#         State("viewport", "data"),
#         Topics.Slots.token.get_state("data"),
#     ],
#     prevent_initial_call=True,
# )
# def toggle_detail_view(events, run_n_clicks, viewport, token):
#     logger.info(f"toggle_detail_view selected event {events}")
#     if (
#         isinstance(ctx.triggered_id, dict)
#         and ctx.triggered_id.get("view") == "editor-main"
#         and events
#         and events[0]
#     ):
#         event = events[0]
#         event_type = event.get("type")
#         if event_type != "node":
#             logger.info(f"skip type {event_type} event for now.")
#         nodes = event.get("nodes")
#         if not nodes or len(nodes) < 1:
#             logger.warning(f"skip type {event_type} event due to no nodes found.")
#             return render_backup_reactions([], viewport)
#         smiles = nodes[0]["data"]["value"]
#
#         # get backup_reactions
#         exp_name = nodes[0]["data"]["exp_name"]
#         job_id = nodes[0]["data"]["job_id"]
#         route_id = nodes[0]["data"]["route_id"]
#         user_id = get_user_id(token)
#         if not user_id:
#             logger.error("failed to get_user_id")
#             return no_update
#         if not exp_name:
#             return no_update
#         s: Session = Session.load(user_id)
#         exp = s.explorations[s.get_exploration_index(exp_name)]
#         job = exp.jobs[exp.get_job_index(job_id)]
#         route: Route = job.routes[route_id]
#
#         backup_reactions = route.workflow.get("backup_reactions").get(smiles, [])
#
#         return render_backup_reactions(backup_reactions, viewport)
#     else:
#         return render_backup_reactions([], viewport)
#
#
# @callback(
#     Output(
#         {
#             "view": "result",
#             "table": "table-backup-reactions",
#             "type": "tr",
#             "index": ALL,
#             "smiles": ALL,
#         },
#         "className",
#     ),
#     Input(
#         {
#             "view": "result",
#             "table": "table-backup-reactions",
#             "type": "tr",
#             "index": ALL,
#             "smiles": ALL,
#         },
#         "n_clicks",
#     ),
#     prevent_initial_call=True,
# )
# def toggle_reaction_active(n_clicks):
#     if not ctx.triggered_id:
#         return no_update
#     logger.info(
#         f"toggle_reaction_active index "
#         f"{ctx.triggered_id.get('index')} n_clicks {n_clicks} trigger_id {ctx.triggered_id}"
#     )
#     index = int(ctx.triggered_id.get("index"))
#     class_names = ["" for i in range(0, len(n_clicks))]
#     class_names[index] = "table-active"
#     return class_names
#
#
# @callback(
#     Output("tabs", "active_tab"),
#     [
#         Input({"view": "editor-main", "job": ALL, "route": ALL}, "selectionEvent"),
#         Topics.Slots.exploration_name.get_input("data"),
#     ],
#     prevent_initial_call=True,
# )
# def toggle_tabs(events, exp_name):
#     if ctx.triggered_id.get("view") == "editor-main" and events and events[0]:
#         return "tab-backups"
#     elif ctx.triggered_id.get("type") == "topics" and exp_name != "":
#         return "tab-jobs"
#     else:
#         return no_update
#
#
# @callback(
#     [
#         Output("table-candidate-routes", "children", allow_duplicate=True),
#         Output("table-backup-reactions", "children", allow_duplicate=True),
#     ],
#     Topics.Slots.exploration_name.get_input("data"),
#     prevent_initial_call=True,
# )
# def clear_tables(exp_name):
#     if not exp_name:
#         return render_candidate_routes("", []), render_backup_reactions([], "")
#     return no_update, no_update



#显示所有结果为分子的任务的结果
@callback(
    Output("Exploration Details","mainChildren", allow_duplicate=True),
    [
        Input("Result test",  "n_clicks"),
    ],
    prevent_initial_call=True,
)
def toggle_molecule_result_view(n_clicks):
    if n_clicks:
        logger.info(f"toggle_molecule_result_view selected event {n_clicks}")
        job_id = 12330944
        output_path = get_job_output_path(job_id)
        return output_path
    else:
        return no_update
    # get_job_output_path
    # if (
    #     isinstance(ctx.triggered_id, dict)
    #     and ctx.triggered_id.get("view") == "editor-main"
    #     and events
    #     and events[0]
    # ):
    #     event = events[0]
    #     event_type = event.get("type")
    #     if event_type != "node":
    #         logger.info(f"skip type {event_type} event for now.")
    #     nodes = event.get("nodes")
    #     if not nodes or len(nodes) < 1:
    #         logger.warning(f"skip type {event_type} event due to no nodes found.")
    #         return render_backup_reactions([], viewport)
    #     smiles = nodes[0]["data"]["value"]
    #
    #     # get backup_reactions
    #     exp_name = nodes[0]["data"]["exp_name"]
    #     job_id = nodes[0]["data"]["job_id"]
    #     route_id = nodes[0]["data"]["route_id"]
    #     user_id = get_user_id(token)
    #     if not user_id:
    #         logger.error("failed to get_user_id")
    #         return no_update
    #     if not exp_name:
    #         return no_update
    #     s: Session = Session.load(user_id)
    #     exp = s.explorations[s.get_exploration_index(exp_name)]
    #     job = exp.jobs[exp.get_job_index(job_id)]
    #     route: Route = job.routes[route_id]
    #
    #     backup_reactions = route.workflow.get("backup_reactions").get(smiles, [])
    #
    #     return render_backup_reactions(backup_reactions, viewport)
    # else:
    #     return render_backup_reactions([], viewport)


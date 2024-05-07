# from loguru import logger
# from dash import callback, Input, Output, ctx, ALL, State, no_update
#
# from views.route import render_candidate_routes
# from models.session import Session
# from utils.token_helper import get_user_id
# from topics import Topics
# from utils.enhanced_callback import callback_with_metrics
#
#
# # TODO 改为监听 job id 和 status 变更
# # @callback(
# #     Output(
# #         "table-candidate-routes",
# #         "children",
# #         allow_duplicate=True
# #     ),
# #     [
# #         Input(
# #             "progress-run",
# #             "value"
# #         ),
# #     ],
# #     prevent_initial_call=True
# # )
# # def toggle_route_view(progress):
# #     logger.info(f"toggle_route_view progress {progress}")
# #     if int(progress) == 100:
# #         return render_candidate_routes(route_data)
# #     else:
# #         return no_update
#
#
# @callback_with_metrics(
#     Output(
#         {
#             "view": "result",
#             "table": "table-candidate-routes",
#             "type": "tr",
#             "index": ALL,
#             "job": ALL,
#         },
#         "className",
#     ),
#     Input(
#         {
#             "view": "result",
#             "table": "table-candidate-routes",
#             "type": "tr",
#             "index": ALL,
#             "job": ALL,
#         },
#         "n_clicks",
#     ),
#     prevent_initial_call=True,
# )
# def toggle_route_active(n_clicks):
#     logger.info(
#         f"toggle_route_active index {ctx.triggered_id.get('index')} n_clicks {n_clicks} trigger_id {ctx.triggered_id}"
#     )
#     index = int(ctx.triggered_id.get("index"))
#     class_names = ["" for i in range(0, len(n_clicks))]
#     class_names[index] = "table-active"
#     return class_names
#
#
# @callback(
#     Output("table-candidate-routes", "children"),
#     Input(
#         "tabs",
#         "active_tab",
#     ),
#     [
#         Topics.Slots.exploration_name.get_state("data"),
#         Topics.Slots.job_id.get_state("data"),
#         Topics.Slots.job_status.get_state("data"),
#         Topics.Slots.token.get_state("data"),
#     ],
#     prevent_initial_call=True,
# )
# def toggle_route_tab(tab_id, exp_name, job_id, job_status, token):
#     logger.info(f"toggle_route_tab {tab_id} {exp_name}")
#     if tab_id != "tab-routes":
#         return no_update
#     user_id = get_user_id(token)
#     if not user_id:
#         logger.error("failed to get_user_id")
#         return no_update
#     if not exp_name:
#         return no_update
#     s: Session = Session.load(user_id)
#     exp = s.explorations[s.get_exploration_index(exp_name)]
#     job = exp.jobs[exp.get_job_index(job_id)]
#     routes = job.routes
#     logger.info(f"routes {len(routes)}")
#     return render_candidate_routes(job_id, routes)

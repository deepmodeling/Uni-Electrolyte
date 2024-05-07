# from loguru import logger
# from dash import callback, no_update, ALL, ctx, Input, State
# from dash.exceptions import PreventUpdate
# from utils.token_helper import get_user_key, get_user_id
# from models.session import Session, Exploration, Job
# from topics import Topics
# from views.projects import DeleteProjectModal, ProjectMenu
# from utils.metrics import log_metrics
# from utils.enhanced_callback import callback_with_metrics
#
#
# # toggle render projects when btn-run clicked
# @callback(
#     [
#         ProjectMenu.Slots.main_menu.get_output("label"),
#         ProjectMenu.Slots.main_menu.get_output("children"),
#     ],
#     [
#         Input("btn-run", "n_clicks"),
#     ],
#     [
#         Topics.Slots.exploration_name.get_state("data"),
#         Topics.Slots.token.get_state("data"),
#         State("input-project-name", "value"),
#     ],
#     prevent_initial_call=True,
# )
# def toggle_re_render_projects(n_clicks, exp_name, token, exp_name_input):
#     logger.info(
#         f"toggle_re_render_projects {n_clicks} {exp_name} input {exp_name_input}"
#     )
#
#     if not exp_name:
#         exp_name = exp_name_input
#     if not n_clicks or not exp_name or not token:
#         raise PreventUpdate
#     user_id = get_user_id(token)
#     if not user_id:
#         logger.error("failed to get_user_id")
#         raise PreventUpdate
#     s: Session = Session.load(user_id)
#
#     exp_names = [exp.name for exp in s.explorations]
#     if exp_name not in exp_names:
#         exp_names.append(exp_name)
#     return exp_name, ProjectMenu.render(exp_names)
#
#
# # toggle start view when select New Project
# @callback_with_metrics(
#     [
#         Topics.Slots.exploration_name.get_output("data"),
#         Topics.Slots.job_id.get_output("data"),
#         Topics.Slots.target_molecule.get_output("data"),
#         ProjectMenu.Slots.main_menu.get_output("label"),
#     ],
#     [
#         ProjectMenu.Slots.new_project.get_input("n_clicks"),
#     ],
#     [Topics.Slots.token.get_state("data"), Topics.Slots.username.get_state("data")],
#     prevent_initial_call=True,
#     dp_metrics_name="create_project",
# )
# def toggle_topics(n_clicks, token, username):
#     logger.info(f"toggle_start_view n_clicks {n_clicks}")
#     log_metrics(
#         username,
#         "project",
#         "new",
#     )
#     if not token:
#         raise PreventUpdate
#     if not n_clicks:
#         raise PreventUpdate
#     user_id = get_user_id(token)
#     if not user_id:
#         logger.error("failed to get_user_id")
#         raise PreventUpdate
#     return "", "", "", "Projects"
#
#
# # delete job_id job_status explorations_status when exploration_name is empty
# @callback(
#     [
#         Topics.Slots.job_id.get_output("data"),
#         Topics.Slots.job_status.get_output("data"),
#         Topics.Slots.exploration_status.get_output("data"),
#         Topics.Slots.target_molecule.get_output("data"),
#     ],
#     [
#         Topics.Slots.exploration_name.get_input("data"),
#     ],
#     prevent_initial_call=True,
# )
# def delete_state(exp_name):
#     logger.info(f"delete_state exp_name {exp_name}")
#     if not exp_name:
#         return "", "", "", ""
#     return no_update, no_update, no_update, no_update
#
#
# # delete exp when modal modal_button clicked
# @callback_with_metrics(
#     [
#         DeleteProjectModal.Slots.modal.get_output("is_open"),
#         ProjectMenu.Slots.main_menu.get_output("label"),
#         Topics.Slots.exploration_name.get_output("data"),
#         ProjectMenu.Slots.main_menu.get_output("children"),
#     ],
#     [
#         DeleteProjectModal.Slots.modal_button.get_input("n_clicks"),
#     ],
#     [
#         Topics.Slots.exploration_name.get_state("data"),
#         Topics.Slots.token.get_state("data"),
#     ],
#     prevent_initial_call=True,
# )
# def delete_exp(n_clicks, exp_name, token):
#     logger.info(f"delete_exp n_clicks {n_clicks} exp_name {exp_name}")
#     if not token or not n_clicks or not exp_name:
#         raise PreventUpdate
#     user_id = get_user_id(token)
#     if not user_id:
#         logger.error("failed to get_user_id")
#         raise PreventUpdate
#     s: Session = Session.load(user_id)
#     exp_idx = s.get_exploration_index(exp_name)
#     del s.explorations[exp_idx]
#     s.save()
#     exp_names = [exp.name for exp in s.explorations]
#
#     return False, "Projects", "", ProjectMenu.render(exp_names)
#
#
# # toggle current_exp and current_exp_status when select project in menu
# @callback_with_metrics(
#     [
#         Topics.Slots.exploration_name.get_output("data"),
#         Topics.Slots.exploration_status.get_output("data"),
#         Topics.Slots.target_molecule.get_output("data"),
#         ProjectMenu.Slots.main_menu.get_output("label"),
#     ],
#     [
#         ProjectMenu.Slots.select_project.get_input("n_clicks", pattern=ALL),
#     ],
#     [
#         Topics.Slots.token.get_state("data"),
#     ],
#     prevent_initial_call=True,
# )
# def toggle_select_project(n_clicks, token):
#     logger.info(f"toggle_select_project n_clicks {n_clicks} {ctx.triggered_id}")
#     if not token or not any(n_clicks):
#         raise PreventUpdate
#     exp_name = ctx.triggered_id.get("id")
#     user_id = get_user_id(token)
#     if not user_id:
#         logger.error("failed to get_user_id")
#         raise PreventUpdate
#     s: Session = Session.load(user_id)
#     exp = s.explorations[s.get_exploration_index(exp_name)]
#     return exp.name, exp.status, exp.target_molecule, exp_name
#
#
# # toggle fill project menu when token exists
# @callback(
#     [
#         ProjectMenu.Slots.main_menu.get_output("children"),
#     ],
#     [
#         Topics.Slots.token.get_input("data"),
#     ],
#     prevent_initial_call=True,
# )
# def toggle_fill_project_menu(token):
#     logger.info("toggle_fill_project_menu")
#     if not token:
#         raise PreventUpdate
#     user_id = get_user_id(token)
#     if not user_id:
#         logger.error("failed to get_user_id")
#         raise PreventUpdate
#     s: Session = Session.load(user_id)
#     exps = s.explorations
#     exp_names = [exp.name for exp in exps]
#     return (ProjectMenu.render(exp_names),)
#
#
# # toggle delete project modal when click "Delete Project" button
# @callback(
#     [
#         DeleteProjectModal.Slots.modal.get_output("is_open"),
#         DeleteProjectModal.Slots.project_name.get_output("children"),
#     ],
#     [
#         ProjectMenu.Slots.delete_project.get_input("n_clicks"),
#     ],
#     [
#         Topics.Slots.exploration_name.get_state("data"),
#         Topics.Slots.token.get_state("data"),
#     ],
#     prevent_initial_call=True,
# )
# def toggle_delete_project_modal(n_clicks, exp_name, token):
#     logger.info(f"toggle_delete_project_modal n_clicks {n_clicks} exp_name {exp_name}")
#     if not n_clicks:
#         raise PreventUpdate
#
#     if not exp_name:
#         raise PreventUpdate
#     if not token:
#         raise PreventUpdate
#     user_id = get_user_id(token)
#     if not user_id:
#         logger.error("failed to get_user_id")
#         raise PreventUpdate
#     s: Session = Session.load(user_id)
#     exps = s.explorations
#     exp = None
#     for e in exps:
#         if e.name == exp_name:
#             exp = e
#             break
#     if not exp:
#         logger.error(f"failed to find exp {exp_name}")
#         raise PreventUpdate
#     return True, exp_name
#
#
# # @callback(
# #     [
# #         Output(
# #             "list-explorations",
# #             "children"
# #         )
# #     ],
# #     [
# #         Topics.Slots.token.get_input("data"),
# #         Topics.Slots.exploration_name.get_input("data"),
# #     ],
# #     [
# #         Topics.Slots.token.get_state("data"),
# #     ],
# #
# # )
# # @trace_time
# # def toggle_render_projects(token, exp_name, token_in_state):
# #     logger.info(f"start toggle_render_projects exp_name {exp_name}")
# #     if not token:
# #         token = token_in_state
# #     user_id = get_user_id(token)
# #     if not user_id:
# #         logger.error("failed to get_user_id")
# #         return no_update,
# #     s: Session = Session.load(user_id)
# #     exps = s.explorations
# #     active_index = 0
# #     for i in range(len(exps)):
# #         if exp_name == exps[i].name:
# #             active_index = i+1
# #     logger.info(f"active_index {active_index}")
# #     return render_projects(exps, active_index),
#
#
# # @callback(
# #     [
# #         Output(
# #             {
# #                 "view": "projects",
# #                 "type": "list_group_item",
# #                 "index": ALL
# #             },
# #             "active",
# #             allow_duplicate=True
# #         ),
# #         Topics.Slots.exploration_name.get_output("data"),
# #         Topics.Slots.exploration_status.get_output("data"),
# #         Topics.Slots.job_id.get_output("data"),
# #         Topics.Slots.job_status.get_output("data"),
# #         Topics.Slots.target_molecule.get_output("data"),
# #     ],
# #     [
# #         Input(
# #             {
# #                 "view": "projects",
# #                 "type": "list_group_item",
# #                 "index": ALL
# #             },
# #             "n_clicks"
# #         )
# #     ],
# #     [
# #         Topics.Slots.token.get_state("data"),
# #     ],
# #     prevent_initial_call=True,
# # )
# # @trace_time
# # def toggle_select_project(n_clicks, token):
# #     # 点击(nclick)后切换 active，
# #     # 并更新 exp_name, exp_status, job_id, job_status
# #
# #     if not ctx.triggered_id or not any(n_clicks):
# #         flags = [no_update for i in range(0, len(n_clicks))]
# #         return flags, no_update, no_update, no_update, no_update, no_update
# #     idx = ctx.triggered_id.get('index')
# #     logger.info(f"toggle_select_project {idx} nclicks {n_clicks}")
# #
# #     flags = [False for i in range(0, len(n_clicks))]
# #     flags[idx] = True
# #
# #     user_id = get_user_id(token)
# #     if not user_id:
# #         logger.error("failed to get_user_id")
# #         return no_update
# #     s: Session = Session.load(user_id)
# #     exps = s.explorations
# #     logger.info(f"toggle_select_project lens {len(exps)} exps {[x.name for x in exps]}")
# #
# #     exp_name = ""
# #     exp_status = ""
# #     job_id = ""
# #     job_status = ""
# #     target_molecule = ""
# #     if idx != 0:
# #         exp = exps[idx-1]
# #         exp_name = exp.name
# #         exp_status = exp.status
# #         job_id = exp.jobs[-1].id if exp.jobs else ""
# #         job_status = exp.jobs[-1].status if exp.jobs else ""
# #         target_molecule = exp.target_molecule
# #         logger.info(f"toggle_select_project exp {exp_name} job_id {job_id}")
# #     return flags, exp_name, exp_status, job_id, job_status, target_molecule

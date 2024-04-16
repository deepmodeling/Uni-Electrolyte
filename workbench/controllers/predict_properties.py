from loguru import logger
from dash import callback, no_update, ALL, ctx, Input, State,Output
from dash.exceptions import PreventUpdate
# from utils.token_helper import get_user_key, get_user_id
# from models.session import Session, Exploration, Job
# from topics import Topics
# from views.projects import DeleteProjectModal, ProjectMenu
# from utils.metrics import log_metrics
# from utils.enhanced_callback import callback_with_metrics


#
# @callback(
#     Output("Predict properties", "children"),
#     [Input("Predict properties", "n_clicks")]
# )
# def update_output(n_clicks):
#     print("dddddddddddddddddddddddddddddddddddddddddd")
#     if n_clicks is not None:
#         # 在这里编写你要输出的内容
#         output_text = "菜单项被点击了！"
#         return output_text
#     else:
#         return ""
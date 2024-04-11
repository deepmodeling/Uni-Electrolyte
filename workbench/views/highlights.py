import dash_bootstrap_components as dbc
from dash import html
from models.session import Exploration
from views.helper import get_modalable_molecule
from typing import List
from loguru import logger


def render_projects(exps: List[Exploration], active_index: int = 0):
    logger.info(f"render_projects active_index")
    res = []
    for i in range(len(exps)):
        exp = exps[i]
        res.append(
            dbc.ListGroupItem(
                exp.name.capitalize(),
                id={"view": "project", "type": "list_group_item", "index": i + 1},
                color="primary",
                action=True,
                active=(i + 1) == active_index,
            )
        )
        if (i + 1) == active_index:
            logger.info(f"render_projects active {i}")
    return res


# def exploration_view():
#     return html.Div(
#         dbc.ListGroup(
#             [
#                 dbc.ListGroupItem(
#                     "*New*",
#                     id={"view": "exploration", "type": "list_group_item", "index": 0},
#                     color="primary",
#                     action=True,
#                     active=True,
#                     style={"display": "none"},
#                 ),
#             ],
#             flush=True,
#             id="list-explorations",
#             style={
#                 "paddingRight": "0.5rem",
#                 "maxHeight": "250px",
#                 "overflowY": "auto",
#             },
#         ),
#         id="view-exploration",
#         style={
#             "maxHeight": "250px",
#         },
#     )

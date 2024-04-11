from loguru import logger
import dash_bootstrap_components as dbc
from dash import html, dcc


def running_view():
    return html.Div(
        [
            dbc.Label("Running, View logs below in result view."),
            html.Div(id="running_view"),
            html.Div(
                [
                    dcc.Interval(
                        id="progress-interval",
                        n_intervals=0,
                        interval=2000,
                        disabled=True,
                    ),
                ],
                {"type": "placeholder", "name": "progress-interval"}
            ),

            dbc.Progress(
                value=10,
                id="progress-run",
                animated=True,
                striped=True
            ),
        ]
    )

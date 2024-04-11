import dash_bootstrap_components as dbc
from dash import html
from dash_xterm import DashXterm


def render_logs():
    ...


def logs_view():
    return html.Div(
        [
            DashXterm(
                id="xterm",
                label="logs",
                value="logs",
            )
        ],
        style={"width": "100%", "height": "300px"}
    )

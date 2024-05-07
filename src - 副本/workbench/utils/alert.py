import time
from typing import Literal
import dash_bootstrap_components as dbc
from dash import html


def status_alert(
    message,
    color="green",
    duration=3,
    frame: Literal["disappear", "hidden"] = "disappear",
):
    current = time.time()
    return dbc.Alert(
        html.P(
            message,
            style={"margin": "0px"},
        ),
        color="light",
        style={
            "animation": f"{frame} {duration}s forwards",
            "textAlign": "center",
            "color": color,
            "padding": "0.2rem",
        },
        id=str(current),
    )

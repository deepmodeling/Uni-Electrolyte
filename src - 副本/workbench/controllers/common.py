
from dash import callback, Input, Output


@callback(
    Output("viewport", "data"),
    Input("breakpoints", "width"),
    Input("breakpoints", "height"),
)
def save_viewport(width: str, height: str):
    return {
        "width": width,
        "height": height,
    }

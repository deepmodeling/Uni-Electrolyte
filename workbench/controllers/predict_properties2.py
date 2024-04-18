from loguru import logger
from dash import callback, no_update, ALL, ctx, Input, State,Output
from dash.exceptions import PreventUpdate
from dash import html, dcc
import dash_bootstrap_components as dbc
from views.helper import render_section, render_secondary_section
from views.predict_properties import options_view,screen_switch_view
@callback(
    Output("Predict Property And Screen","children"),
    [Input("Screen molecules from database","n_clicks")]
)
def show_screen_switch(n_clicks):
    print("dddddddddddddddddddddddddddddddddddddddddd")
    if n_clicks is not None:
        print("eeeeeeeeeeeeeeeeeeeeeeeeeee")

        return screen_switch_view()



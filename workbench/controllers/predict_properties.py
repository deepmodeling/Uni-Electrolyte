from loguru import logger
from dash import callback, no_update, ALL, ctx, Input, State,Output
from dash.exceptions import PreventUpdate
from dash import html, dcc
import dash_bootstrap_components as dbc
from views.helper import render_section, render_secondary_section
from views.predict_properties import options_view

# @callback(
#     Output("Predict Property And Screen","style", allow_duplicate=True),
#     [Input("Screen molecules from database","n_clicks"),],
#     prevent_initial_call=True,
# )
# def show_screen_switch(value):
#     print("show_screen_switch")
#     if value=="Predict Property And Screen":
#         return None
#     else:
#         return ""



@callback(
     [Output("left sidebar","sidebarChildren", allow_duplicate=True),Output("right sidebar","sidebarChildren", allow_duplicate=True)],
    [Input("Predict properties", "n_clicks")],
    prevent_initial_call=True,
)
def show_predict_properties(n_clicks):
    print("show_predict_properties")
    if n_clicks is not None:
        # 在这里编写你要输出的内容

        right_sidebar= dbc.Row(
                            render_secondary_section(
                                "Configure Exploration", "", options_view()
                            ),
                            id="row-options-view",
                            style={
                                "height": "100%",
                                "alignItems": "flexStart",
                                "paddingRight": "2%",
                                "paddingTop": "1rem",
                            },
                        ),
                        # UserTrack.get_component(),
        left_sidebar= dbc.Row(
                            render_secondary_section(
                                "Upload Files", "","Upload Files"
                            ),
                            id="row-options-view",
                            style={
                                "height": "100%",
                                "alignItems": "flexStart",
                                "paddingRight": "2%",
                                "paddingTop": "1rem",
                            },
                        ),
        return left_sidebar,right_sidebar
    else:
        return "",""
from loguru import logger
from dash import callback, no_update, ALL, ctx, Input, State,Output
from dash.exceptions import PreventUpdate
from dash import html, dcc
import dash_bootstrap_components as dbc
from views.helper import render_section, render_secondary_section
from views.Retrosynthesis import  middle_view




@callback(
     [Output("left sidebar", "sidebarChildren", allow_duplicate=True),
         Output("Exploration Details","mainChildren", allow_duplicate=True),
      Output("right sidebar","sidebarChildren", allow_duplicate=True)],
    [Input("Retrosynthesis", "n_clicks")],
    prevent_initial_call=True,
)
def show_Retrosynthesis(n_clicks):
    print("Retrosynthesis")
    if n_clicks is not None:
        # 在这里编写你要输出的内容



        right_sidebar= dbc.Row(
                            render_secondary_section(
                                "Options", "", middle_view()
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
        return "",right_sidebar,""
    else:
        return "","",""
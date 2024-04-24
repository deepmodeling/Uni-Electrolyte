from loguru import logger
from dash import callback, no_update, ALL, ctx, Input, State,Output
from dash.exceptions import PreventUpdate
from dash import html, dcc
import dash_bootstrap_components as dbc
from views.helper import render_section, render_secondary_section
from views.Generate_molecules_and_predict_properties import  right_view




@callback(
     [Output("left sidebar", "sidebarChildren", allow_duplicate=True),
         Output("Exploration Details","mainChildren", allow_duplicate=True),
      Output("right sidebar","sidebarChildren", allow_duplicate=True)],
    [Input("Generate molecules and predict properties", "n_clicks")],
    prevent_initial_call=True,
)
def show_Generate_molecules_and_predict_properties(n_clicks):
    print("show_Query_molecules_with_similar_properties")
    if n_clicks is not None:
        # 在这里编写你要输出的内容



        right_sidebar= dbc.Row(
                            render_secondary_section(
                                "Options", "", right_view()
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
        return "","",right_sidebar
    else:
        return "","",""
from loguru import logger
from dash import callback, no_update, ALL, ctx, Input, State,Output
from dash.exceptions import PreventUpdate
from dash import html, dcc
import dash_bootstrap_components as dbc
from views.helper import render_section, render_secondary_section
from views.Generate_molecules_and_predict_properties import  middle_view

@callback(
    [
        Output({
            "view": "Generate_molecules_and_predict_properties",
            "type": "input",
            "name": "HOMO LUMO Options ",
        }, "style", allow_duplicate=True),
        Output({
                    "view": "Generate_molecules_and_predict_properties",
                    "type": "input",
                    "name": "Binding enegry and formular",
                },"style", allow_duplicate=True),
        Output({
                    "view": "Generate_molecules_and_predict_properties",
                    "type": "input",
                    "name": "Structure finger print",
                },"style", allow_duplicate=True),


    ],
    [Input({
                    "view": "Generate_molecules_and_predict_properties",
                    "type": "input",
                    "name": "Gen mode options ",
                },"value"),],
    prevent_initial_call=True,
)
def show_gen_switch(value):
    print("show_gen_switch")
    if value=="HOMO LUMO":
        return None,{"display": "none"},{"display": "none"}
    elif value=="Binding enegry and formular":
        return {"display": "none"},None,{"display": "none"}
    elif value=="Structure finger print":
        return {"display": "none"},{"display": "none"},None
    else:
        return {"display": "none"},{"display": "none"},{"display": "none"}

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
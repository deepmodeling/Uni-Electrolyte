from loguru import logger
from dash import callback, no_update, ALL, ctx, Input, State,Output
from dash.exceptions import PreventUpdate
from dash import html, dcc
import dash_bootstrap_components as dbc
from views.helper import render_section, render_secondary_section
from views.predict_properties import left_view,right_view
from topics import Topics
@callback(
    Output("Predict property and screen RangeSlider","style", allow_duplicate=True),
    [Input({
                    "view": "predict_properties",
                    "type": "input",
                    "name": "screen-switch",
                },"value"),],
    prevent_initial_call=True,
)
def show_screen_switch(value):
    print("show_screen_switch")
    if value=="Predict property and screen":
        return None
    else:
        return {"display": "none"}

@callback(
     [Output("left sidebar", "sidebarChildren", allow_duplicate=True),
     Output("right sidebar","sidebarChildren", allow_duplicate=True),
     Output("Exploration Details","sidebarChildren", allow_duplicate=True),
     Output("Exploration Details","mainChildren", allow_duplicate=True),],
    [Input("Predict properties", "n_clicks")],
    prevent_initial_call=True,
)
def show_predict_properties(n_clicks):
    print("show_predict_properties")
    if n_clicks is not None:
        # 在这里编写你要输出的内容

        left_sidebar= dbc.Row(
                            render_secondary_section(
                                "Upload Files", "",left_view()
                            ),
                            id="row-options-view",
                            style={
                                "height": "100%",
                                "alignItems": "flexStart",
                                "paddingRight": "2%",
                                "paddingTop": "1rem",
                            },
                        ),

        right_sidebar= dbc.Row(
                            render_secondary_section(
                                "Configure exploration", "", right_view()
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
        return left_sidebar,right_sidebar,"",""
    else:
        return "","","",""




@callback(
    Topics.Slots.options.get_output("data", allow_duplicate=False),
    [
        Topics.Slots.target_molecule.get_input("data"),
        Input({"view": "predict_properties", "type": "input", "name": ALL}, "value"),
    ],
    [
        Topics.Slots.target_molecule.get_state("data"),
        State({"view": "predict_properties", "type": "input", "name": ALL}, "value"),
    ],
)
def toggle_update_options(
    target_molecule, triggered_value, state_molecule, state_value
):
    if not target_molecule:
        target_molecule = state_molecule
    logger.info(
        f"toggle_update_options "
        f"target_molecule: {target_molecule}\n"
        f"triggered_value: {triggered_value}\n"
        f"state_value: {state_value}\n"
        f"triggered_id: {ctx.triggered_id}\n"
        f"states: {ctx.states_list}"
    )
    states_list = ctx.states_list[1]
    tmp = {}
    res = {}
    for _, state in enumerate(states_list):
        tmp[state["id"]["name"]] = state["value"]

    logger.info(f"tmp {tmp}")
    # rebuild fields for backend job

    res["reaction_type"] = tmp.pop("reaction-type")
    res["check_system"] = tmp.pop("check-system")
    res["route_diversity"] = tmp.pop("route-diversity")
    res["max_iteration"] = tmp.pop("max-iteration")[1]
    res["debug"] = tmp.pop("demo-mode", False)
    res["input_ligand"] = target_molecule
    logger.info(f"return res {res}")
    return res

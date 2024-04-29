
from launching.app import submit_job, get_job_status, get_job_result
from models.session import Session, Exploration, Job, JobStatus, ExplorationStatus
from utils.token_helper import get_user_id
from utils.id import get_uuid
from utils.tracer import trace_time
from utils.enhanced_callback import callback_with_metrics
from utils.alert import status_alert
from loguru import logger
from dash import callback, no_update, ALL, ctx, Input, State,Output
from dash.exceptions import PreventUpdate
from dash import html, dcc
import dash_bootstrap_components as dbc
from views.helper import render_section, render_secondary_section
from views.predict_properties import middle_view,right_view
from topics import Topics
import dash_uploader as du
@callback(
    Output( {
                    "view": "predict_properties",
                    "type": "input",
                    "name": "predict_property_and_screen_rangeSlider",
                },"style", allow_duplicate=True),
    [Input({
                    "view": "predict_properties",
                    "type": "input",
                    "name": "screen_switch",
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
    [   Output( {
                    "view": "predict_properties",
                    "type": "input",
                    "name": "input_a_molecule_options",
                },"style",allow_duplicate=True),
        Output( {
                    "view": "predict_properties",
                    "type": "input",
                    "name": "draw_a_molecule_options",
                }, "style", allow_duplicate=True),
        Output( {
                    "view": "predict_properties",
                    "type": "input",
                    "name": "upload_input_option",
                },"style", allow_duplicate=True),


    ],
    [Input({
                    "view": "predict_properties",
                    "type": "input",
                    "name": "input_mode_options",
                },"value"),],
    prevent_initial_call=True,
)
def show_input_switch(value):
    print("show_gen_switch")
    if value=="Input a molecule with SMILES":
        return None,{"display": "none"},{"display": "none"}
    if value=="Draw a molecule":
        return {"display": "none"}, None,{"display": "none"}
    elif value=="Upload molecules with file " :
        return {"display": "none"},{"display": "none"},None
    else:
        return {"display": "none"},{"display": "none"},{"display": "none"}


@callback(
     [#Output("left sidebar", "sidebarChildren", allow_duplicate=True),
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

        middle_main= dbc.Row(
                            render_secondary_section(
                                "Upload Files", "",middle_view()
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
        return right_sidebar,"",middle_main
    else:
        return  "","",""


# 上传 csv 后，解析 header
# @du.callback(
#     output=Topics.Slots.predict_properties_options.get_output("data", allow_duplicate=True),
#     state=[
#         Topics.Slots.token.get_state("data"),
#         Topics.Slots.predict_properties_options.get_state("data"),
#     ],
#     id={
#                         "view": "predict_properties",
#                         "type": "input",
#                         "name": "upload",
#                     }
# )
# def upload_predict_data(status: du.UploadStatus, token, predict_properties_options: dict):
#     if not predict_properties_options:
#         predict_properties_options = {}
#     user_id = get_user_id(token)
#     if not user_id:
#         return no_update, no_update
#
#     session = Session.load(user_id)
#     if not session:
#         return status_alert("Session not found.", color="danger"), no_update
#
#     if status.is_completed:
#         if len(status.uploaded_files) == 0:
#             return status_alert("No file uploaded.", color="danger"), no_update
#         elif len(status.uploaded_files) > 1:
#             return status_alert("Only one file is allowed.", color="danger"), no_update
#         fpath = status.uploaded_files[0]
#         predict_properties_options["predict_data_path"] = str(fpath)
#         return predict_properties_options




@callback_with_metrics(
    [Topics.Slots.predict_properties_options.get_output("data", allow_duplicate=False),
    Output("predict_properties_btn-run","disabled",allow_duplicate=False),
    ],
    [
        Input("predict_properties_btn-conf", "n_clicks"),
    ],
    [ State({
        "view": "predict_properties",
        "type": "input",
        "name": "input_mode_options"}, "value"),
        State({
                    "view": "predict_properties",
                    "type": "input",
                    "name": "input_a_molecule",
                },"value"),
        State( {
                    "view": "predict_properties",
                    "type": "input",
                    "name": "input_a_molecule_options",
                },"value"),
        State({
                    "view": "predict_properties",
                    "type": "input",
                    "name": "draw_a_molecule",
                },"output_molecule"),
        State({
                    "view": "predict_properties",
                    "type": "input",
                    "name": "draw_a_molecule_options",
                },"value"),

        State({
                    "view": "predict_properties",
                    "type": "input",
                    "name": "upload_input_option",
                },"value"),
        State({
                    "view": "predict_properties",
                    "type": "input",
                    "name": "target_selection",
                },"value"),
        State({
                    "view": "predict_properties",
                    "type": "input",
                    "name": "screen_switch",
                },"value"),
        State({
                            "view": "predict_properties",
                            "type": "input",
                            "name": "HOMO_range_rangeSlider",
                        },"value"),
        State({
                            "view": "predict_properties",
                            "type": "input",
                            "name": "LUMO_range_rangeSlider",
                        },"value"),
        State({
                            "view": "predict_properties",
                            "type": "input",
                            "name": "binding_energy_range_rangeSlider",
                        },"value"),
        State({
                            "view": "predict_properties",
                            "type": "input",
                            "name": "log_viscosity_range_rangeSlider",
                        },"value"),
        State({
                            "view": "predict_properties",
                            "type": "input",
                            "name": "log_dielectric_constant_range_rangeSlider",
                        },"value"),
        State({
                    "view": "predict_properties",
                    "type": "input",
                    "name": "predict_property_and_screen_rangeSlider",
                },"value"),
        State({
            "view": "predict_properties",
            "type": "input",
            "name": "upload",
        }, "uploadedFileNames"),
State({
            "view": "predict_properties",
            "type": "input",
            "name": "upload",
        }, "upload_id"),
],
    prevent_initial_call=True,
)
@trace_time
def update_options(
    n_clicks,
input_mode_options,input_a_molecule,input_a_molecule_options,draw_a_molecule,draw_a_molecule_options,
upload_input_option,target_selection,screen_switch,HOMO_range_rangeSlider,LUMO_range_rangeSlider,
binding_energy_range_rangeSlider,log_viscosity_range_rangeSlider,log_dielectric_constant_range_rangeSlider,
predict_property_and_screen_rangeSlider,uploadedFileNames,upload_id
):
    if n_clicks:

        res={
            "input_mode_options":input_mode_options,
            "input_a_molecule":input_a_molecule,
            "input_a_molecule_options":input_a_molecule_options,
            "draw_a_molecule":draw_a_molecule,
            "draw_a_molecule_options":draw_a_molecule_options,
            "upload_input_option":upload_input_option,
            "target_selection":target_selection,
           "screen_switch":screen_switch,
            "HOMO_range_rangeSlider":HOMO_range_rangeSlider,
            "LUMO_range_rangeSlider":LUMO_range_rangeSlider,
            "binding_energy_range_rangeSlider":binding_energy_range_rangeSlider,
            "log_viscosity_range_rangeSlider":log_viscosity_range_rangeSlider,
            "log_dielectric_constant_range_rangeSlider":log_dielectric_constant_range_rangeSlider,
           "predict_property_and_screen_rangeSlider":predict_property_and_screen_rangeSlider,
            "uploadedFileNames":uploadedFileNames,"upload_id":upload_id,
        }
        logger.info(res)
        return res,False

    if not n_clicks:
        raise PreventUpdate





from launching.app import submit_job, get_job_status, get_job_result
from models.session import Session, Exploration, Job, JobStatus, ExplorationStatus
from utils.token_helper import get_user_id
from utils.id import get_uuid
from utils.tracer import trace_time
from utils.enhanced_callback import callback_with_metrics

from loguru import logger
from dash import callback, no_update, ALL, ctx, Input, State,Output
from dash.exceptions import PreventUpdate
from dash import html, dcc
import dash_bootstrap_components as dbc
from views.helper import render_section, render_secondary_section
from views.predict_properties import middle_view,right_view
from topics import Topics
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
                    "name": "upload_input",
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


#"""
@callback_with_metrics(
    [
        Topics.Slots.exploration_name.get_output("data",allow_duplicate=True),
        Topics.Slots.exploration_status.get_output("data",allow_duplicate=True),
        Topics.Slots.job_id.get_output("data",allow_duplicate=True),
        Topics.Slots.job_status.get_output("data",allow_duplicate=True),
        Topics.Slots.target_molecule.get_output("data",allow_duplicate=True),
        Output({
                            "view": "predict_properties",
                            "type": "input",
                            "name": "alert",
                        },"children",allow_duplicate=True),
    ],
    [
        Input("predict_properties_btn-run", "n_clicks"),
    ],
    [
        Topics.Slots.exploration_name.get_state("data"),
        State("input-project-name", "value"),
        #State("input-molecule", "value"),
        Topics.Slots.token.get_state("data"),
        #Topics.Slots.options.get_state("data"),
        #Topics.Slots.target_molecule.get_state("data"),
        State("input-bohrium-project", "value"),
        State({"view": "predict_properties", "type": "input", "name": "input_mode_options"}, "value"),
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
                },"value"),
        State({
                    "view": "predict_properties",
                    "type": "input",
                    "name": "draw_a_molecule_options",
                },"value"),
        State({
                        "view": "predict_properties",
                        "type": "input",
                        "name": "upload",
                    },"value"),
        State({
                    "view": "predict_properties",
                    "type": "input",
                    "name": "upload_input",
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


    ],
    prevent_initial_call=True,
)
@trace_time
def do_run_exploration(
    n_clicks,
    exploration_name,
    input_exp_name,
    #target_molecule,
    token,
    #params,
    #target_molecule_state,
    bohrium_project_id,
input_mode_options,input_a_molecule,input_a_molecule_options,draw_a_molecule,draw_a_molecule_options,
upload,upload_input,target_selection,screen_switch,HOMO_range_rangeSlider,LUMO_range_rangeSlider,
binding_energy_range_rangeSlider,log_viscosity_range_rangeSlider,log_dielectric_constant_range_rangeSlider,
predict_property_and_screen_rangeSlider
):
    if n_clicks:
        print("dddddddddddddddd")
        print("n_clicks",n_clicks)
        print("exploration_name",exploration_name)
        print("input_exp_name",input_exp_name)
        print("token",token)
        print("bohrium_project_id",bohrium_project_id)
        print("input_mode_options",input_mode_options)
        print("input_a_molecule",input_a_molecule)
        print("input_a_molecule_options",input_a_molecule_options)
        print("draw_a_molecule",draw_a_molecule)
        print("draw_a_molecule_options",draw_a_molecule_options)
        print("upload",upload)
        print("upload_input",upload_input)
        print("target_selection",target_selection)
        print("screen_switch",screen_switch)
        print("HOMO_range_rangeSlider",HOMO_range_rangeSlider)
        print("LUMO_range_rangeSlider",LUMO_range_rangeSlider)
        print("binding_energy_range_rangeSlider",binding_energy_range_rangeSlider)
        print("log_viscosity_range_rangeSlider",log_viscosity_range_rangeSlider)
        print("log_dielectric_constant_range_rangeSlider",log_dielectric_constant_range_rangeSlider)
        print("predict_property_and_screen_rangeSlider",predict_property_and_screen_rangeSlider)
        return "","","","","","dddddddd"

    if not n_clicks:
        raise PreventUpdate

    # do_run_exploration
    # submit jobs
    # save session to redis( only put current exploration)
    # save exploration_name if not state.exploration_name
    # save current_exploration_status to init
    # save current_jobs_status to init
    # save current_jobs_id to init
    # performance issue: do_run_exploration took 3.8596789836883545 seconds
 

    user_id = get_user_id(token)
    if not user_id:
        logger.error("failed to get_user_id")
        raise PreventUpdate
    s = Session.load(user_id)
    if not exploration_name:
        exploration_name = input_exp_name
    if not exploration_name:
        logger.error("exploration_name is empty")
        raise PreventUpdate
    exp_idx = s.get_exploration_index(exploration_name)
    size = len(s.explorations)
    if exp_idx == -1:
        exp = Exploration(
            id=get_uuid(),
            name=exploration_name,
            target_molecule=target_molecule,
            bohrium_project_id=bohrium_project_id,
        )
        s.explorations.append(exp)
        exp_idx = size
    else:
        exp: Exploration = s.explorations[exp_idx]

    # save params to topics and load params
    if not params.get("input_ligand", ""):
        params["input_ligand"] = target_molecule
    logger.info(
        f"start do_run_exploration {exploration_name} for {target_molecule} \n"
        f"    params {params}"
    )
    params["brm_token"] = token
    job_id = submit_job(
        token,
        params=params,
        job_name=exploration_name,
        bohrium_project_id=bohrium_project_id,
    )
    job = Job(id=job_id, name=job_id)
    exp.jobs.append(job)
    s.explorations[exp_idx] = exp
    # s.updated_at = datetime.now()
    s.save()
    logger.info(
        f"finish do_run_exploration exploration_name {exploration_name}, exp.status {exp.status},"
        f" job_id {job_id}, job.status {job.status}"
    )

    return exploration_name, exp.status, job_id, job.status, target_molecule


"""
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
"""
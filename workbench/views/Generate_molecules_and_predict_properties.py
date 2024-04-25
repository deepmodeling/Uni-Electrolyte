from loguru import logger
from dash import callback, no_update, ALL, ctx, Input, State,Output
from dash.exceptions import PreventUpdate
from dash import html, dcc
import dash_bootstrap_components as dbc
from views.helper import render_section, render_secondary_section
import dash_ketcher
from ids import KETCHER_COMPONENT_ID
def middle_view():
    return html.Div(
        [
            dbc.Label("Gen Mode - Options ", className="dp-form-label"),
            dbc.Select(
                id=
                {
                    "view": "Generate_molecules_and_predict_properties",
                    "type": "input",
                    "name": "Gen Mode - Options ",
                },
                options=[
                    {"label": "HOMO LUMO", "value": "HOMO LUMO"},
                    {"label": "Binding Enegry And Formular", "value":"Binding Enegry And Formular"},
                    {"label": "Structure Finger Print","value":"Structure Finger Print"}
                ],
                value="HOMO LUMO",
            ),

            html.Div(

                [
                dbc.Label("Homo Range ", className="dp-form-label"),
                html.P("The targeted HOMO interval. In unit eV.", className="intro"),
                dcc.RangeSlider(
                    min=-9,
                    max=-2,
                    step=0.2,
                    marks=None,
                    value=[-8, -7],
                    tooltip={
                        "placement": "bottom",
                        # "always_visible": True,
                    },
                    id={
                        "view": "Generate_molecules_and_predict_properties",
                        "type": "input",
                        "name": "HOMO Range RangeSlider",
                    },
                ),
                dbc.Label("Lumo Range", className="dp-form-label"),
                html.P("The targeted LUMO interval. In unit eV.", className="intro"),
                dcc.RangeSlider(
                    min=-4,
                    max=10,
                    step=0.2,
                    marks=None,
                    value=[8, 9],
                    tooltip={
                        "placement": "bottom",
                        # "always_visible": True,
                    },
                    id={
                        "view":"Generate_molecules_and_predict_properties",
                        "type": "input",
                        "name": "LUMO Range RangeSlider",
                    },
                ),

                    ],
                id=
                {
                    "view": "Generate_molecules_and_predict_properties",
                    "type": "input",
                    "name": "HOMO LUMO Options ",
                },

            ),

            html.Div(

                [
                    dbc.Label("Formular", className="dp-form-label"),
                    html.P(" The targeted formular.", className="intro"),
                    dbc.Input(
                        id="Generate_molecules_and_predict_properties_Binding_Enegry_And_Formular_Formular",
                        name="molecule",
                        placeholder="200",
                        style={"width": "155px"},
                        valid=False,
                        value="",
                    ),
                    dbc.Label("Targeted Binding E ", className="dp-form-label"),
                    html.P(" The targeted binding energy", className="intro"),
                    dbc.Input(
                        id="Generate_molecules_and_predict_properties_Binding_Enegry_And_Formular_Targeted Binding E ",
                        name="molecule",
                        placeholder="200",
                        style={"width": "155px"},
                        valid=False,
                        value="",
                    ),

                ],
                id=
                {
                    "view": "Generate_molecules_and_predict_properties",
                    "type": "input",
                    "name": "Binding Enegry And Formular",
                },
                style={"display": "none"}
            ),

            html.Div(

                [
                    dbc.Label("Structure Finger Print", className="dp-form-label"),
                    # html.P("The targeted HOMO interval. In unit eV.", className="intro"),
                    dbc.Input(
                        id="Structure Finger Print_input-molecule",
                        name="molecule",
                        placeholder="SMILES required",
                        style={"width": "755px"},
                        valid=False,
                        value="",
                    ),
                    html.Div(
                        dash_ketcher.DashKetcher(
                            id="Structure Finger Print_input dash_ketcher",
                            input_molecule="",
                            style={
                                "height": "450px",
                                "width": "100%",
                                # "paddingBottom": "50px",
                            },
                        ),
                    ),

                ],
                id=
                {
                    "view": "Generate_molecules_and_predict_properties",
                    "type": "input",
                    "name": "Structure Finger Print",
                },
                style={"display": "none"}
            ),


            dbc.Label("N Molecules ", className="dp-form-label"),
            html.P("Total number of molecules to be generated.",
                   className="intro"),
            dbc.Input(
                id="Generate_molecules_and_predict_properties_N_Molecules_Input",
                name="molecule",
                placeholder="200",
                style={"width": "155px"},
                valid=False,
                value="",
            ),


            dbc.Button(
                "Start Exploration",
                id="Generate_molecules_and_predict_properties_btn-run",
                n_clicks=0,
                color="primary",
                className="me-6",
                disabled=False,
            ),
        ],
    )






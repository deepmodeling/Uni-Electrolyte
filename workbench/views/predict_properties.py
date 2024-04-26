from loguru import logger
from dash import callback, no_update, ALL, ctx, Input, State,Output
from dash.exceptions import PreventUpdate
from dash import html, dcc
import dash_bootstrap_components as dbc
from views.helper import render_section, render_secondary_section
import dash_ketcher
import dash_uploader as du

def middle_view():
    return html.Div(
        [
            dbc.Label("Input mode options ", className="dp-form-label"),
            dbc.Select(
                id=
                {
                    "view": "predict_properties",
                    "type": "input",
                    "name": "Input Mode - Options ",
                },
                options=[
                    {"label": "Upload molecules with file ", "value": "Upload molecules with file "},
                    {"label": "Draw a molecule", "value": "Draw a molecule"},

                ],
                value="Draw a molecule",
            ),

            html.Div(
                [
                    dbc.Label("Molecule to be predicted", className="dp-form-label"),
                    # html.P("The targeted HOMO interval. In unit eV.", className="intro"),
                    dbc.Input(
                        id="predict_properties_input-molecule",
                        name="molecule",
                        placeholder="SMILES required",
                        style={"width": "755px"},
                        valid=False,
                        value="",
                    ),
                    html.Div(
                        dash_ketcher.DashKetcher(
                            id="predict_properties_dash_ketcher",
                            input_molecule="",
                            style={
                                "height": "450px",
                                "width": "100%",
                                # "paddingBottom": "50px",
                            },
                        ),
                    ),
                ], id="predict_properties Draw a molecule options"),
            html.Div(
                du.Upload(
                    id=
                    {
                        "view": "predict_properties",
                        "type": "input",
                        "name": "upload",
                    }
                    ,
                    text="Drag and drop or select files (File with one SMILES per line or xyz file)",
                    max_files=1,
                    max_file_size=5 * 1024,  # 5GB
                    disabled=False,
                    pause_button=False,
                    cancel_button=False,
                    text_disabled="Log in to upload files",
                    # filetypes=["csv"],
                    default_style={
                        "width": "155px",
                        "height": "80px",
                        "cursor": "pointer",
                        "lineHeight": "10px",
                        "borderWidth": "1px",
                        "borderStyle": "dashed",
                        "borderRadius": "5px",
                        "textAlign": "center",
                        "marginTop": "1rem",
                        "marginBottom": "1rem",
                        "minHeight": "40px",
                    },
                ),
                id="predict_properties_upload-input",
                style=
                {
                    "display": "none",
                },
            ),

            dbc.Label("Target", className="dp-form-label"),
            html.P("Target properties to be predicted.", className="intro"),

            dbc.Checklist(
                id={
                    "view": "predict_properties",
                    "type": "input",
                    "name": "target_selection",
                },
                options=[
                    {"label": "Binding energy", "value": "Binding energy"},
                    {"label": "Dielectric constant", "value": "Dielectric constant"},
                    {"label": "Viscosity", "value": "Viscosity"},
                    {"label": "HOMO", "value": "HOMO"},
                    {"label": "LUMO", "value": "LUMO"},
                    # {"label": "Database", "value": "database"},
                ],

                value=["Binding energy", "Dielectric constant", "Viscosity", "HOMO", "LUMO"],
            ),
            html.Br(),


        ]

    )


def right_view():
    return html.Div(
        [
            # html.H5("Optimization Options", style={"fontWeight": "bold"})

            dbc.Label("Screen switch options", className="dp-form-label"),

            dbc.Select(
                id=
                {
                    "view": "predict_properties",
                    "type": "input",
                    "name": "screen-switch",
                },
                options=[
                    {"label": "Predict property only", "value": "Predict property only"},
                    {"label": "Predict property and screen", "value": "Predict property and screen"}
                ],

                value="Predict property only",
            ),

            html.Div(
                [
                    dbc.Label("HOMO range ", className="dp-form-label"),
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
                            "view": "predict_properties",
                            "type": "input",
                            "name": "HOMO range RangeSlider",
                        },
                    ),
                    dbc.Label("LUMO range", className="dp-form-label"),
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
                            "view": "predict_properties",
                            "type": "input",
                            "name": "LUMO range RangeSlider",
                        },
                    ),
                    dbc.Label("Binding energy range ", className="dp-form-label"),
                    html.P("The targeted binding energy interval. In unit eV.", className="intro"),
                    dcc.RangeSlider(
                        min=-4,
                        max=1,
                        step=0.2,
                        marks=None,
                        value=[-2, -1],
                        tooltip={
                            "placement": "bottom",
                            # "always_visible": True,
                        },
                        id={
                            "view": "predict_properties",
                            "type": "input",
                            "name": "Binding Energy Range RangeSlider",
                        },
                    ),
                    dbc.Label("Log viscosity range ", className="dp-form-label"),
                    html.P("The targeted viscosity interval. In log form and unit mPa*s without log.",
                           className="intro"),
                    dcc.RangeSlider(
                        min=-2.25,
                        max=2.25,
                        step=0.2,
                        marks=None,
                        value=[-1, -0.3],
                        tooltip={
                            "placement": "bottom",
                            # "always_visible": True,
                        },
                        id={
                            "view": "predict_properties",
                            "type": "input",
                            "name": "Log Viscosity Range RangeSlider",
                        },
                    ),
                    dbc.Label("Log dielectric constant range", className="dp-form-label"),
                    html.P("The targeted viscosity interval. In log form and unit mPa*s without log.",
                           className="intro"),
                    dcc.RangeSlider(
                        min=0,
                        max=2,
                        step=0.2,
                        marks=None,
                        value=[0.74, 0.81],
                        tooltip={
                            "placement": "bottom",
                            # "always_visible": True,
                        },
                        id={
                            "view": "predict_properties",
                            "type": "input",
                            "name": "Log Dielectric Constant Range RangeSlider",
                        },
                    ),

                ], id="Predict property and screen RangeSlider", style={"display": "none"}
            ),


            # dbc.Switch(
            #    id={
            #        "view": "options",
            #        "type": "input",
            #        "name": "use-backup",
            #    },
            #    value=False,
            #    disabled=True,
            # ),
            dbc.Button(
                "Start exploration",
                id="predict_properties_btn-run",
                n_clicks=0,
                color="primary",
                className="me-6",
                disabled=False,
            ),
        ],
    )






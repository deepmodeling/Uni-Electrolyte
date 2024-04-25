from loguru import logger
from dash import callback, no_update, ALL, ctx, Input, State,Output
from dash.exceptions import PreventUpdate
from dash import html, dcc
import dash_bootstrap_components as dbc
from views.helper import render_section, render_secondary_section
import dash_ketcher
from ids import KETCHER_COMPONENT_ID
import dash_uploader as du
def middle_view():
    return html.Div(
        [
            dbc.Label("Input mode options ", className="dp-form-label"),
            dbc.Select(
                id=
                {
                    "view": "Retrosynthesis",
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
                dbc.Label("Molecule to be synthesized", className="dp-form-label"),
                # html.P("The targeted HOMO interval. In unit eV.", className="intro"),
                dbc.Input(
                    id="Retrosynthesis_input-molecule",
                    name="molecule",
                    placeholder="SMILES required",
                    style={"width": "755px"},
                    valid=False,
                    value="",
                ),
                html.Div(
                    dash_ketcher.DashKetcher(
                        id="Retrosynthesis_dash_ketcher",
                        input_molecule="",
                        style={
                            "height": "450px",
                            "width": "100%",
                            # "paddingBottom": "50px",
                        },
                    ),
                ),
            ],id="Retrosynthesis Draw a molecule options"),
            html.Div(
                du.Upload(
                    id="upload-Retrosynthesis-input",
                    text="Drag and drop or select files ( One SMILES per line)",
                    max_files=1,
                    max_file_size=5 * 1024,  # 5GB
                    disabled=False,
                    pause_button=False,
                    cancel_button=False,
                    text_disabled="Log in to upload files",
                    #filetypes=["csv"],
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
                id="Retrosynthesis_upload-input",
                style=
                {
                    "display": "none",
                },
            ),
            dbc.Button(
                "Start exploration",
                id="Retrosynthesis_btn-run",
                n_clicks=0,
                color="primary",
                className="me-6",
                disabled=False,
            ),
        ]

    )






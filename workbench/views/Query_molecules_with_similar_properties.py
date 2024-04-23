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
            dbc.Label("Molecule to be searched", className="dp-form-label"),
            # html.P("The targeted HOMO interval. In unit eV.", className="intro"),
            dbc.Input(
                id="Query_molecules_with_similar_properties_input-molecule",
                name="molecule",
                placeholder="SMILES required",
                style={"width": "755px"},
                valid=False,
                value="",
            ),
            html.Div(
                dash_ketcher.DashKetcher(
                    id=KETCHER_COMPONENT_ID.get_identifier(),
                    input_molecule="",
                    style={
                        "height": "450px",
                        "width": "100%",
                        # "paddingBottom": "50px",
                    },
                ),
            ),
        ]

    )


def right_view():
    return html.Div(
        [
            dbc.Label("N Molecules ", className="dp-form-label"),
            html.P("Total number of molecules in the database to be returned. Maximum value is 50.", className="intro"),
            dbc.Input(
                id="Query_molecules_with_similar_properties_N_Molecules_Input",
                name="molecule",
                placeholder="25",
                style={"width": "755px"},
                valid=False,
                value="",
            ),
            "",
            dbc.Button(
                "Start Exploration",
                id="Query_molecules_with_similar_properties_btn-run",
                n_clicks=0,
                color="primary",
                className="me-6",
                disabled=False,
            ),
           ])






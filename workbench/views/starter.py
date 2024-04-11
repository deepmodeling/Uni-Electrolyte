import dash
from base64 import b64encode
from io import BytesIO
from loguru import logger
import dash_bootstrap_components as dbc
from dash import html
from views.helper import get_modalable_molecule
import dash_ketcher
from ids import KETCHER_COMPONENT_ID


def render_molecule(molecule, viewport):
    logger.info(f"render_molecule {molecule}")
    if molecule:
        return get_modalable_molecule(
            "img_starter_target_molecule",
            molecule,
            150,
            150,
            viewport,
        )

    # TODO
    # return PlotlyDashKetcher(
    #     id="editor_molecule",
    #     molecule=molecule,
    #     buttonLabel="Save Molecule"
    # )


def starter_view():
    return html.Div(
        [
            html.H6("Project Name"),
            dbc.Input(
                id="input-project-name",
                name="project-name",
                value="",
                style={"width": "755px"},
                valid=False,
                placeholder="Name can only contain letters, numbers and hyphens.",
            ),
            html.Div(
                id="input-project-error-alert",
                style={"width": "755px"},
            ),
            html.H6("Select Bohrium Project", style={"marginTop": "3em"}),
            html.P("Select the Bohrium project for billing", className="intro"),
            dbc.Select(
                id="input-bohrium-project",
                name="bohrium",
                style={"width": "755px", "backgroundColor": "transparent"},
                valid=False,
                disabled=True,
            ),
            html.Div(
                id="error-alert",
                style={"width": "755px"},
            ),
            html.H6("Configure Target Molecule", style={"marginTop": "2em"}),
            html.P("molecule to be synthesized", className="intro"),
            dbc.Input(
                id="input-molecule",
                name="molecule",
                placeholder="SMILES required",
                style={"width": "755px"},
                valid=False,
                value="",
            ),
            html.Div(
                id="input-molecule-error-alert",
                style={"width": "755px"},
            ),
            # html.Div(id="molecule_editor_view"),
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
        ],
    )

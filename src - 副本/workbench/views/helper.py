from loguru import logger
from copy import deepcopy

from dash import html
import dash_bootstrap_components as dbc
from dash_modalable import DashModalable

from utils.rdkit_utils import smi2svg, smi2png, validate_smiles, validate_reaction


def render_section(title, description, content):
    return dbc.Row(
        [html.H5(title) if title else "", content],
        style={
            "borderRadius": "1px",
            "backgroundColor": "#ffffff",
            "marginLeft": "0.8rem",
            "paddingTop": "1rem",
            # "marginRight": "0.2rem",
            # "boxShadow": "1px 1px 1px lightgrey",
        },
    )


def render_secondary_section(title, description, content):
    return dbc.Row(
        [
            html.H5(title) if title else "",
            html.P(description, className="intro") if description else "",
            content,
        ],
        style={
            "backgroundColor": "#f2f2f2",
            "marginLeft": "0.8rem",
            "alignContent": "baseline",
        },
    )


def get_modalable_molecule(
    id, smiles, width, height, viewport=None, reaction=False, auto_scale="height"
):
    if not reaction and not validate_smiles(smiles):
        return None
    if reaction and not validate_reaction(smiles):
        return None
    if isinstance(id, dict):
        modal_id = deepcopy(id)
        modal_id["use"] = "modal"
    else:
        modal_id = f"{id}-modal"
    viewport = viewport or {}
    modal_image_width = viewport.get("width", 1024) - 53
    modal_image_height = int(viewport.get("height", 960) * 0.8)
    if not reaction:
        children = html.Img(
            id=id,
            src=smi2svg(
                smiles,
                height,
                width,
                reaction=reaction,
            ),
        )
    else:
        if auto_scale == "width":
            style = {"cursor": "pointer", "width": f"{width}px"}
        else:
            style = {"cursor": "pointer", "height": f"{height}px"}

        children = html.Img(
            id=id,
            src=smi2png(smiles, modal_image_height, modal_image_width),
            style=style,
        )
    return DashModalable(
        children=children,
        modalChildren=html.Img(
            id=modal_id,
            src=smi2svg(
                smiles,
                modal_image_height,
                modal_image_width,
                opacity=0.95,
                reaction=reaction,
            ),
        ),
        modalZoomable=True,
        buttonOpen=False,
        modalStyle={"width": "100%", "height": "100%", "top": "53px"},
        style={"width": f"{width}px", "height": f"{height}px"},
    )

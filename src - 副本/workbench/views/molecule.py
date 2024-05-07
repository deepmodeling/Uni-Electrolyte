import dash_bootstrap_components as dbc
from dash import html

from views.helper import get_modalable_molecule


def render_target_molecule(molecule, viewport=None):
    if molecule:
        return get_modalable_molecule(
            "img_target_molecule",
            molecule,
            150,
            150,
            viewport,
        )


def render_selected_molecule(node, viewport=None):
    has_reference = "reference" in node["data"] and node["data"]["reference"] != ""
    has_title = has_reference and "title" in node["data"]["reference"]
    has_yield = has_reference and "yield" in node["data"]["reference"]
    has_smiles = has_reference and "smiles" in node["data"]["reference"]
    if node:
        return [
            dbc.Label(f"Price: {node['data'].get('price', '')}")
            if node["data"].get("commercial", False)
            else "",
            html.Br() if node["data"].get("commercial", False) else "",
            dbc.Label(f"Title: {node['data'].get('reference').get('title', '')}")
            if has_title
            else "",
            html.Br() if has_title else "",
            dbc.Label(f"Yield: {node['data'].get('reference').get('yield', '')}")
            if has_yield
            else "",
            html.Br() if has_yield else "",
            get_modalable_molecule(
                "img_selected_molecule",
                node["data"]["value"],
                150,
                150,
                viewport,
            ),
            dbc.Label(f"Reference Reaction:") if has_smiles else "",
            get_modalable_molecule(
                "img_selected_molecule_reference",
                node["data"]["reference"]["smiles"],
                150,
                150,
                viewport,
                reaction=True,
                auto_scale="width",
            )
            if has_smiles
            else "",
        ]


def molecule_view():
    return html.Div(
        [
            dbc.Label("Target Molecule", style={"fontWeight": "400"}),
            html.Div(id="target_molecule_view", style={"minHeight": "150px"}),
            dbc.Label("Selected Molecule", style={"fontWeight": "400"}),
            html.Div(id="selected_molecule_view", style={"minHeight": "150px"}),
        ]
    )

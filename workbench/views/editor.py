from dash_chemical_flow import ChemicalFlow
from fake_data.reaction import DRY_RUN_DATA
from views.helper import render_section
import dash_bootstrap_components as dbc
from dash import html


def editor_view():
    return ChemicalFlow(
        id={"view": "editor-main", "job": -1, "route": -1},
        label="my-label",
        nodes=[
            {
                "id": "1",
                "data": {
                    "value": "CCO",
                    "label": "CCO",
                    "commercial": True,
                    "price": "0.1/g",
                },
                "type": "molecule",
            },
        ],
        edges=[],
        smiles={},
    )


def render_workflow(exp_name, job_id, route_id, workflow, smiles):
    nodes = workflow["nodes"]
    edges = workflow["edges"]
    for i, _ in enumerate(nodes):
        nodes[i]["id"] = f"{job_id}-{route_id}-{nodes[i]['id']}"
        nodes[i]["data"]["route_id"] = route_id
        nodes[i]["data"]["job_id"] = job_id
        nodes[i]["data"]["exp_name"] = exp_name
    for i, _ in enumerate(edges):
        edges[i]["id"] = f"{job_id}-{route_id}-{edges[i]['id']}"
        edges[i]["source"] = f"{job_id}-{route_id}-{edges[i]['source']}"
        edges[i]["target"] = f"{job_id}-{route_id}-{edges[i]['target']}"
    return (
        render_section(
            "",
            "",
            dbc.Row(
                [
                    html.Div(
                        [
                            html.Label(
                                "Purple Nodes",
                                style={"color": "purple", "fontWeight": "bold"},
                            ),
                            html.Label("\u00A0means synthesis intermediates."),
                            html.Label(
                                "\u00A0Green Nodes",
                                style={"color": "green", "fontWeight": "bold"},
                            ),
                            html.Label("\u00A0means commercial available materials."),
                        ]
                    ),
                    ChemicalFlow(
                        id={"view": "editor-main", "job": job_id, "route": route_id},
                        label="my-label",
                        nodes=workflow["nodes"],
                        edges=workflow["edges"],
                        smiles=smiles,
                    ),
                ]
            ),
        ),
    )

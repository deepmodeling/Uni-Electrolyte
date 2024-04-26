import dash_bootstrap_components as dbc
from dash import html, dcc
from views.helper import get_modalable_molecule

"""
def render_rerun_backup(smiles, viewport=None):
    return (
        [
            get_modalable_molecule(
                "rerun_backup_molecule",
                smiles,
                250,
                100,
                viewport=viewport,
                reaction=True,
            ),
        ]
        if smiles
        else ""
    )


def options_view():
    return html.Div(
        [
            # html.H5("Optimization Options", style={"fontWeight": "bold"}),
            # dbc.Label("TODO: help messages.", style={"display": "block"}),
            dbc.Label("Reaction Type", className="dp-form-label"),
            html.P("Source of reactions used in synthesis routes.", className="intro"),
            dbc.Checklist(
                id={
                    "view": "options",
                    "type": "input",
                    "name": "reaction-type",
                },
                options=[
                    {"label": "AI", "value": "ai"},
                    {"label": "Template", "value": "expertsystem"},
                    {"label": "Similarity", "value": "similarity"},
                    #{"label": "Database", "value": "database"},
                ],
                inline=True,
                value=["ai", "expertsystem", "similarity"],
            ),
            html.Br(),
            dbc.Label("Check System", className="dp-form-label"),
            html.P(
                "Verification method used for non-database sourced reactions.",
                className="intro",
            ),
            dbc.Checklist(
                id={
                    "view": "options",
                    "type": "input",
                    "name": "check-system",
                },
                options=[
                    {"label":"AI", "value":"ai"},
                ],
                inline=True,
                value=["ai"],
            ),
            html.Br(),
            dbc.Label("Route Diversity", className="dp-form-label"),
            html.P(
                "Diversity of resulting paths, 'high' generates more results but might consume more time.",
                className="intro",
            ),
            dbc.RadioItems(
                id={
                    "view": "options",
                    "type": "input",
                    "name": "route-diversity",
                },
                options=[
                    {"label": "Normal", "value": "normal"}, 
                    {"label": "High", "value": "high"}
                ],
                inline=True,
                value="normal",
            ),
            html.Br(),
            dbc.Label("Max Iteration", className="dp-form-label"),
            html.P("Defaulting to 20 iterations.", className="intro"),
            dcc.RangeSlider(
                min=5,
                max=100,
                step=5,
                marks=None,
                value=[0, 20],
                tooltip={
                    "placement": "bottom",
                    # "always_visible": True,
                },
                id={
                    "view": "options",
                    "type": "input",
                    "name": "max-iteration",
                },
            ),
            # dbc.Label("Demo Mode", style={"fontWeight": "400"}),
            # dbc.Switch(
            #    id={
            #        "view": "options",
            #        "type": "input",
            #        "name": "demo-mode",
            #    },
            #    value=False,
            # ),
            # dbc.Label("Use Alternative Reaction", style={"fontWeight": "400"}),
            # dbc.Switch(
            #    id={
            #        "view": "options",
            #        "type": "input",
            #        "name": "use-backup",
            #    },
            #    value=False,
            #    disabled=True,
            # ),
            html.Div("", id="view_backup_rerun"),
            dbc.Button(
                "Start Exploration",
                id="btn-run",
                n_clicks=0,
                color="primary",
                className="me-6",
                disabled=True,
            ),
        ],
    )
"""
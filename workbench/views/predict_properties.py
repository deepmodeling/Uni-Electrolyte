from loguru import logger
from dash import callback, no_update, ALL, ctx, Input, State,Output
from dash.exceptions import PreventUpdate
from dash import html, dcc
import dash_bootstrap_components as dbc
from views.helper import render_section, render_secondary_section

def options_view():
    return html.Div(
        [
            # html.H5("Optimization Options", style={"fontWeight": "bold"})
            dbc.Label("Target", className="dp-form-label"),
            html.P("Target properties to be predicted.", className="intro"),




            dbc.Checklist(
                id={
                    "view": "options",
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
                inline=True,
                value=[ "Binding energy",  "Dielectric constant","Viscosity","HOMO","LUMO"],
            ),
            html.Br(),
            dbc.Label("Screen Switch - Options", className="dp-form-label"),
            dbc.RadioItems(
                id={
                    "view": "options",
                    "type": "input",
                    "name": "screen-switch",
                },
                options=[
                    {"label": "Predict Property Only", "value": "Predict Property Only"},
                    {"label": "Predict Property And Screen", "value": "Predict Property And Screen"}
                ],
                inline=True,
                value="Predict Property Only",
            ),
            html.Div("", id="Predict Property And Screen RangeSlider"),
            # dcc.RangeSlider(
            #     min=5,
            #     max=100,
            #     step=5,
            #     marks=None,
            #     value=[0, 20],
            #     tooltip={
            #         "placement": "bottom",
            #         # "always_visible": True,
            #     },
            #     id={
            #         "view": "options",
            #         "type": "input",
            #         "name": "max-iteration",
            #     },
            # ),
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
            #html.Div("", id="view_backup_rerun"),
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




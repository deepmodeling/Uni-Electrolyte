from loguru import logger
from dash import callback, no_update, ALL, ctx, Input, State,Output
from dash.exceptions import PreventUpdate
from dash import html, dcc
import dash_bootstrap_components as dbc
from views.helper import render_section, render_secondary_section

def options_view():
    return html.Div(
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
                    "view": "screen_molecules_from_database",
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
                    "view": "screen_molecules_from_database",
                    "type": "input",
                    "name": "LUMO Range RangeSlider",
                },
            ),
            dbc.Label("Binding Energy Range ", className="dp-form-label"),
            html.P("The targeted binding_energy interval. In unit eV.", className="intro"),
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
                    "view": "screen_molecules_from_database",
                    "type": "input",
                    "name": "Binding Energy Range RangeSlider",
                },
            ),
            dbc.Label("Log Viscosity Range ", className="dp-form-label"),
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
                    "view": "screen_molecules_from_database",
                    "type": "input",
                    "name": "Log Viscosity Range RangeSlider",
                },
            ),
            dbc.Label("Log Dielectric Constant Range", className="dp-form-label"),
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
                    "view": "screen_molecules_from_database",
                    "type": "input",
                    "name": "Log Dielectric Constant Range RangeSlider",
                },
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
                "Start Exploration",
                id="screen_molecules_from_database_btn-run",
                n_clicks=0,
                color="primary",
                className="me-6",
                disabled=True,
            ),
        ],
    )






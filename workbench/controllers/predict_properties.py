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
                value=[ "Binding energy",  "Binding energy","Viscosity","HOMO","LUMO"],
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



@callback(
    Output("Predict Property And Screen","children"),
    [Input({"view": "options",  "type": "input", "name": "screen-switch",},"value")]
)
def show_screen_switch(value):
    print("dddddddddddddddddddddddddddddddddddddddddd")
    if value=="Predict Property And Screen":
        print("eeeeeeeeeeeeeeeeeeeeeeeeeee")
        output=[
            dbc.Label("Homo Range ", className="dp-form-label"),
            html.P("The targeted HOMO interval. In unit eV.", className="intro"),
            dcc.RangeSlider(
                min=-9,
                max=-2,
                step=100,
                marks=None,
                value=[-8, -7],
                tooltip={
                    "placement": "bottom",
                    # "always_visible": True,
                },
                id={
                    "view": "options",
                    "type": "input",
                    "name": "HOMO Range RangeSlider",
                },
            ),
            dbc.Label("Lumo Range", className="dp-form-label"),
            html.P("The targeted LUMO interval. In unit eV.", className="intro"),
            dcc.RangeSlider(
                min=-4,
                max=-10,
                step=100,
                marks=None,
                value=[8, 9],
                tooltip={
                    "placement": "bottom",
                    # "always_visible": True,
                },
                id={
                    "view": "options",
                    "type": "input",
                    "name": "LUMO Range RangeSlider",
                },
            ),
            dbc.Label("Binding Energy Range ", className="dp-form-label"),
            html.P("The targeted binding_energy interval. In unit eV.", className="intro"),
            dcc.RangeSlider(
                min=-4,
                max=1,
                step=100,
                marks=None,
                value=[-2, -1],
                tooltip={
                    "placement": "bottom",
                    # "always_visible": True,
                },
                id={
                    "view": "options",
                    "type": "input",
                    "name": "Binding Energy Range RangeSlider",
                },
            ),
            dbc.Label("Log Viscosity Range ", className="dp-form-label"),
            html.P("The targeted viscosity interval. In log form and unit mPa*s without log.", className="intro"),
            dcc.RangeSlider(
                min=-2.25,
                max=2.25,
                step=100,
                marks=None,
                value=[-1, -0.3],
                tooltip={
                    "placement": "bottom",
                    # "always_visible": True,
                },
                id={
                    "view": "options",
                    "type": "input",
                    "name": "Log Viscosity Range RangeSlider",
                },
            ),
            dbc.Label("Log Dielectric Constant Range", className="dp-form-label"),
            html.P("The targeted viscosity interval. In log form and unit mPa*s without log.", className="intro"),
            dcc.RangeSlider(
                min=0,
                max=2 ,
                step=100,
                marks=None,
                value=[0.74, 0.81],
                tooltip={
                    "placement": "bottom",
                    # "always_visible": True,
                },
                id={
                    "view": "options",
                    "type": "input",
                    "name": "Log Dielectric Constant Range RangeSlider",
                },
            ),

        ]
        return output




@callback(
    [Output("left sidebar", "sidebarChildren"),
     Output("right sidebar","sidebarChildren"),
     Output("Exploration Details","sidebarChildren"),
     Output("Exploration Details","mainChildren"),
     ],
    [Input("Predict properties", "n_clicks")]
)
def show_predict_properties(n_clicks):

    if n_clicks is not None:
        # 在这里编写你要输出的内容
        print("ffffffffffffffffff")

        right_sidebar=[
                        dbc.Row(
                            render_secondary_section(
                                "Configure Exploration", "", options_view()
                            ),
                            id="row-options-view",
                            style={
                                "height": "100%",
                                "alignItems": "flexStart",
                                "paddingRight": "2%",
                                "paddingTop": "1rem",
                            },
                        ),
                        # UserTrack.get_component(),
                    ],


        output_text = "菜单项被点击了！"
        return output_text,right_sidebar,output_text,output_text
    else:
        return "","","",""
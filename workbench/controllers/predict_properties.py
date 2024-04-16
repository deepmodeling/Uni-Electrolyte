from loguru import logger
from dash import callback, no_update, ALL, ctx, Input, State,Output
from dash.exceptions import PreventUpdate
from dash import html, dcc
import dash_bootstrap_components as dbc
from views.helper import render_section, render_secondary_section
from views.predict_properties import options_view
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
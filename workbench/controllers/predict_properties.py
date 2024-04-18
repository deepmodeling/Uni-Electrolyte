from loguru import logger
from dash import callback, no_update, ALL, ctx, Input, State,Output
from dash.exceptions import PreventUpdate
from dash import html, dcc
import dash_bootstrap_components as dbc
from views.helper import render_section, render_secondary_section
from views.predict_properties import options_view,screen_switch_view
# @callback(
#     Output("Predict Property And Screen","children"),
#     [Input("Screen molecules from database","n_clicks")]
# )
# def show_screen_switch(n_clicks):
#     print("dddddddddddddddddddddddddddddddddddddddddd")
#     if n_clicks is not None:
#         print("eeeeeeeeeeeeeeeeeeeeeeeeeee")
#
#         return screen_switch_view()



@callback(
    [Output("left sidebar", "sidebarChildren"),
     Output("right sidebar","sidebarChildren"),
     Output("Exploration Details","sidebarChildren"),
     Output("Exploration Details","mainChildren"),
     ],
    [Input("Screen molecules from database", "n_clicks")]
)
def show_predict_properties2(n_clicks):

    if n_clicks is not None:
        # 在这里编写你要输出的内容
        print("ffffffffffffffffff")

        right_sidebar= dbc.Row(
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
        output_text = "菜单项被点击了！"
        return right_sidebar,output_text,output_text,output_text
    else:
        return "","","",""

@callback(
    [Output("left sidebar", "sidebarChildren"),
     Output("right sidebar","sidebarChildren"),
     Output("Exploration Details","sidebarChildren"),
     Output("Exploration Details","mainChildren"),
     ],
    [Input("Predict properties", "n_clicks")])
def show_predict_properties(n_clicks):
    if n_clicks is not None:
        # 在这里编写你要输出的内容
        print("ffffffffffffffffff")
        right_sidebar= dbc.Row(
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
        output_text = "菜单项被点击了！"
        return output_text,right_sidebar,output_text,output_text
    else:
        return "","","",""
import base64
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_pane_split import DashPaneSplit
from dash_breakpoints import WindowBreakpoints
from views.helper import render_section, render_secondary_section
from views.editor import editor_view
from views.starter import starter_view
from views.molecule import molecule_view
from views.options import options_view
from views.result import result_view
from views.jobs import jobs_view
from views.running import running_view
from views.tour import render_tour

# from views.summary import summary_view
from views.route import route_view
from views.login import LoginModal
from views.projects import ProjectMenu, DeleteProjectModal
from topics import Topics


for_helps_image = None
with open("./assets/retro-synthesis.jpeg", "rb") as f:
    for_helps_image = base64.b64encode(f.read()).decode("utf-8")


class UserTrack:
    @classmethod
    def get_component(cls):
        content = """<div style="display:inline-block;width:200px;"><script type="text/javascript" src="//rf.revolvermaps.com/0/0/7.js?i=5fgyqkslymj&amp;m=0&amp;c=ff0000&amp;cr1=ffffff&amp;sx=0" async="async"></script></div>"""
        return html.Iframe(
            srcDoc=content,
            style={
                "width": "240px",
                "height": "110px",
                "position": "fixed",
                "bottom": "0px",
                "left": "calc(100% - 200px)",
            },
        )


class MobileView:
    @classmethod
    def get_component(cls):
        return html.Div(
            html.P(
                "The current application does not support access from small-window devices such as mobile phones. Please use a desktop browser to access this application."
            ),
            id="mobile-view",
            style={"display": "none"},
        )


def render_app():
    layout = html.Div(
        [
            MobileView.get_component(),
            WindowBreakpoints(
                id="breakpoints",
            ),
            dcc.Store(id="viewport", storage_type="memory"),
            LoginModal.get_component(),
            DeleteProjectModal.get_component(),
            Topics.render(),
            dbc.NavbarSimple(
                links_left=False,
                fixed=True,
                children=[
                    ProjectMenu(),

                    dbc.DropdownMenu(
                        [
                            dbc.DropdownMenu(
                                label="Molecular design",
                                id="Molecular design",
                                children=
                                [
                                    dbc.DropdownMenuItem(
                                        "Predict properties",
                                        id="Predict properties",
                                    ),
                                    dbc.DropdownMenuItem(
                                        "Screen molecules from database",
                                        id="Screen molecules from database",
                                    ),
                                    dbc.DropdownMenuItem(
                                        "Query molecules with similar properties",
                                        id="Query molecules with similar properties",
                                    ),
                                    dbc.DropdownMenuItem(
                                        "Generate molecules and predict properties",
                                        id="Generate molecules and predict properties",
                                    ),
                                ],
                            )
                            ,
                            dbc.DropdownMenuItem(
                                "Retrosynthesis",
                                id="Retrosynthesis",
                            ),
                            dbc.DropdownMenuItem(
                                "Interfacial reaction",
                                id="Interfacial reaction",
                            ),
                        ],
                        label="Functions",
                        nav=True,
                        in_navbar=True,
                        style={"flexGrow": "1"},
                    ),

                    dbc.NavItem(
                        dbc.NavLink(
                            "More Apps",
                            href="https://app.bohrium.dp.tech/",
                            target="_blank",
                            external_link=True,
                        ),
                    ),
                    dbc.NavItem(
                        dbc.NavLink(
                            [
                                "Welcome, ",
                                html.Span("Guest User", id="span-username"),
                            ],
                            id="link-login",
                            href="#",
                        ),
                    ),
                    dbc.NavItem(
                        [
                            dbc.NavLink(
                                "help",
                                href="#",
                                id="for-helps",
                            ),
                            dbc.Popover(
                                html.Div(
                                    html.Img(
                                        src=f"data:image/jpeg;base64,{for_helps_image}",
                                        height="100%",
                                        width="100%",
                                    ),
                                    style={"width": 200, "height": 200},
                                ),
                                target="for-helps",
                                placement="bottom",
                                body=True,
                                trigger="hover",
                            ),
                        ],
                    )
                    if for_helps_image
                    else None,
                ],
                brand="Uni-Electrolyte",
                brand_href="/uni-electrolyte/workbench/",
                brand_style={"paddingTop": "3px", "fontWeight": "500"},
                color="rgba(89,49,150,.9)",
                dark=True,
                style={
                    "height": "45px",
                    "width": "100%",
                    "zIndex": "10000",
                    "backgroundImage": "unset",
                    "boxShadow": "0 1px 1px 0px rgb(0 0 0 / 50%)",
                    # "backgroundColor": "rgba(89,49,150,.9) !important",
                },
            ),
            DashPaneSplit(
                id="left sidebar",
                sidebarTitle="Upload files",
                containerStyle={"height": "calc(100% - 55px)"},
                splitMode="vertical",
                panelOrder="sidebarFirst",
                sidebarDefaultSize=200,
                sidebarMinSize=200,
                sidebarStyle={"display": "block"},
                sidebarChildren="Upload files sidebarChildren",
                # [
                #     dbc.Row(
                #         [
                #             render_secondary_section(
                #                 "Molecule",
                #                 "",
                #                 # "Click molecule to view in fullscreen mode.",
                #                 molecule_view(),
                #             ),
                #         ],
                #         id="row-molecule-view",
                #         style={"height": "60%", "paddingTop": "1rem"},
                #     )
                # ],
                mainChildren=DashPaneSplit(
                    id="right sidebar",
                    sidebarTitle="Options",
                    sidebarMinSize=200,
                    splitMode="vertical",
                    sidebarDefaultSize=306,
                    panelOrder="mainFirst",
                    sidebarStyle={
                        "overflowX": "hidden",
                        "height": "100%",
                    },
                    sidebarChildren="Options  sidebarChildren",
                    # [
                    #     dbc.Row(
                    #         render_secondary_section(
                    #             "Configure exploration", "", options_view()
                    #         ),
                    #         id="row-options-view",
                    #         style={
                    #             "height": "100%",
                    #             "alignItems": "flexStart",
                    #             "paddingRight": "2%",
                    #             "paddingTop": "1rem",
                    #         },
                    #     ),
                    #     # UserTrack.get_component(),
                    # ],
                    mainChildren=DashPaneSplit(
                        id="Exploration Details",
                        sidebarTitle="Exploration Details",
                        splitMode="horizontal",
                        sidebarDefaultSize=250,
                        sidebarSize=10,
                        panelOrder="mainFirst",
                        sidebarChildren="Exploration Details sidebarChildren",
                        # html.Div(
                        #     dbc.Tabs(
                        #         [
                        #             dbc.Tab(
                        #                 jobs_view(),
                        #                 label="Explorations",
                        #                 tab_id="tab-jobs",
                        #                 style={
                        #                     "paddingTop": "40px",
                        #                     "overflowY": "auto",
                        #                 },
                        #             ),
                        #             dbc.Tab(
                        #                 route_view(),
                        #                 label="Candidate Routes",
                        #                 tab_id="tab-routes",
                        #                 style={
                        #                     "paddingTop": "40px",
                        #                     "overflowY": "auto",
                        #                 },
                        #             ),
                        #             dbc.Tab(
                        #                 result_view(),
                        #                 label="Alternative Reactions",
                        #                 tab_id="tab-backups",
                        #                 style={
                        #                     "paddingTop": "40px",
                        #                     "overflowY": "auto",
                        #                 },
                        #             ),
                        #             # dbc.Tab(
                        #             #    summary_view(),
                        #             #    label="Summary",
                        #             #    tab_id="tab-summary",
                        #             # ),
                        #         ],
                        #         id="tabs",
                        #         active_tab="tab-routes",
                        #         style={
                        #             "position": "absolute",
                        #             "top": "1px",
                        #             "width": "100%",
                        #             "background": "#f9f9f9",
                        #         },
                        #     ),
                        #     style={
                        #         "width": "100%",
                        #         "height": "100%",
                        #         "marginTop": "0.2rem",
                        #         "background": "#f9f9f9",
                        #     },
                        # ),
                        mainChildren="Exploration Details mainChildren",
                        # [
                        #     dbc.Row(
                        #         render_section(
                        #             "Start a New Project", "", starter_view()
                        #         ),
                        #         id="row-starter-view",
                        #         style={
                        #             "flex": "8",
                        #             "minHeight": "400px",
                        #             "height": "100%",
                        #             "alignItems": "flexStart",
                        #             "width": "100%",
                        #         },
                        #     ),
                        #     dbc.Row(
                        #         render_section("", "", running_view()),
                        #         id="row-running-view",
                        #         style={
                        #             "flex": "8",
                        #             "display": "none",
                        #             "minHeight": "400px",
                        #             "height": "100%",
                        #             "alignItems": "flexStart",
                        #         },
                        #     ),
                        #     dbc.Row(
                        #         render_section("", "main view", editor_view()),
                        #         id="row-main-view",
                        #         style={
                        #             "flex": "8",
                        #             "display": "none",
                        #             "minHeight": "400px",
                        #             "height": "100%",
                        #             "alignItems": "flexStart",
                        #         },
                        #     ),
                        # ],
                        mainStyle={
                            "height": "100%",
                            "width": "100%",
                            "display": "flex",
                            "alignItems": "flexStart",
                            "justifyContent": "center",
                            "overflowY": "auto",
                        },
                        sidebarStyle={
                            "position": "relative",
                        },
                    ),
                ),
            ),
            render_tour(),
        ],
        style={"height": "100vh", "alignItems": "flexStart"},
    )
    return layout

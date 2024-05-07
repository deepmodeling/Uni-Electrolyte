import dash_bootstrap_components as dbc
from dash_id_utils import DashIDGenerator
from dash import html
from typing import List


class DeleteProjectModal:
    class Slots:
        modal = DashIDGenerator(
            page="project_control", type="modal", name="delete_project"
        )
        modal_body = DashIDGenerator(
            page="project_control", type="modal_body", name="delete_project"
        )
        project_name = DashIDGenerator(
            page="project_control", type="b", name="project_name"
        )
        modal_button = DashIDGenerator(
            page="project_control", type="modal_button", name="delete_project"
        )

    @classmethod
    def get_component(cls, is_open=False):
        return dbc.Modal(
            [
                dbc.ModalHeader(dbc.ModalTitle("Header"), close_button=True),
                dbc.ModalBody(
                    [
                        html.H4("Delete Project"),
                        html.P(
                            [
                                "Are you sure you want to delete project ",
                                html.B("", id=cls.Slots.project_name.get_identifier()),
                                "?",
                                html.Br(),
                                "This cannot be undone.",
                            ],
                            className="mb-0",
                        ),
                    ],
                    id=cls.Slots.modal_body.get_identifier(),
                ),
                dbc.ModalFooter(
                    [
                        dbc.Button(
                            "Delete",
                            id=cls.Slots.modal_button.get_identifier(),
                            className="ms-auto",
                            color="danger",
                        ),
                    ]
                ),
            ],
            id=cls.Slots.modal.get_identifier(),
            centered=True,
            is_open=is_open,
            size="sm",
        )


class ProjectMenu(dbc.DropdownMenu):
    class Slots:
        main_menu = DashIDGenerator("project_control", "dropdown_menu", "main_menu")
        new_project = DashIDGenerator(
            page="project_control", type="list_group_item", name="new"
        )
        open_project = DashIDGenerator(
            page="project_control", type="list_group_item", name="open"
        )
        delete_project = DashIDGenerator(
            page="project_control", type="list_group_item", name="delete"
        )
        select_project = DashIDGenerator(
            page="project_control", type="list_group_item", name="project"
        )

    def __init__(self, **kwargs):
        if "projects" in kwargs:
            children = self.render(kwargs["projects"])
        else:
            children = self.render()
        super().__init__(
            children,
            id=self.Slots.main_menu.get_identifier(),
            nav=True,
            in_navbar=True,
            label="Projects",
            style={"flexGrow": "1"},
            **kwargs
        )

    @classmethod
    def default_items(cls):
        return [
            dbc.DropdownMenuItem(
                "New Project",
                id=cls.Slots.new_project.get_identifier(),
            ),
            dbc.DropdownMenuItem(
                "Delete Project", id=cls.Slots.delete_project.get_identifier()
            ),
            dbc.DropdownMenuItem(divider=True, disabled=True),
            html.Div(
                "Switch Project",
                style={
                    "fontSize": "12px",
                    "display": "inherit",
                    "paddingLeft": "15px",
                },
            ),
        ]

    @classmethod
    def render(cls, projects=[]):
        default_items = cls.default_items()
        return default_items + [
            dbc.DropdownMenuItem(
                project, id=cls.Slots.select_project.get_identifier(project)
            )
            for project in projects
        ]

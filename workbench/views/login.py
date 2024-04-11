from datetime import datetime
from urllib.parse import urlencode

import jwt
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_iframe_message import DashIframeMessage
import requests


class LoginModal:
    id = {"page": "common", "type": "login-iframe"}
    modal_id = {"page": "common", "type": "login-modal"}

    @classmethod
    def get_component(cls, is_open=False):
        return dbc.Modal(
            [
                dbc.ModalBody(
                    DashIframeMessage(
                        src="https://platform.dp.tech/login?business=Bohrium&lang=en-us&utm_source=launching",
                        height="520px",
                        width="480px",
                        id=cls.modal_id,
                    ),
                    style={"overflow": "hidden"},
                ),
            ],
            id=cls.id,
            centered=True,
            is_open=is_open,
            style={"overflow": "hidden"},
        )

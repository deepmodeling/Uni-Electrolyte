import os
import sys
from dash import Dash
import dash_bootstrap_components as dbc

from controllers import *
from loguru import logger
from views import render_app
from flask import request
from flask import Response
from time import strftime

logger.remove()
logger.add(sys.stdout, level="DEBUG")

app = Dash(
    __name__,
    compress=True,
    external_scripts=[
        "https://static01.dp.tech/openfiles.mlops.dp.tech/v2/projects/workbench/afbd2617ef2143b4b97537b32fce334a/plotly.min.js"
    ],
    requests_pathname_prefix="/uni-electrolyte/workbench/",
    routes_pathname_prefix="/uni-electrolyte/workbench/",
    title="Uni Electrolyte",
    update_title=None,
    external_stylesheets=[
        "https://static01.dp.tech/openfiles.mlops.dp.tech/v1/static/npm/bootswatch@5.3.0/dist/pulse/bootstrap.min.css"
    ],
    prevent_initial_callbacks="initial_duplicate",
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

app.layout = render_app()
app._favicon = "favicon.png"


@app.server.after_request
def after_request(response: Response):
    if response.status_code in (500, 502, 503, 400):
        ts = strftime("[%Y-%b-%d %H:%M]")
        traceback_data = response.data.decode("utf-8")
        logger.exception(
            f"{ts} {request.remote_addr} {request.method} {request.scheme} {request.full_path} "
            f"ERROR callback error {response.status_code} {traceback_data}\n",
        )
    return response


server = app.server

if __name__ == "__main__":
    app.run_server(debug=os.getenv("PROD_ENV", None) != "true", host="0.0.0.0")

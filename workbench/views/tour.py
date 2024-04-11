from feffery_antd_components import AntdTour
from dash import html


def render_tour():
    """
    1. login
    2. model name
    3. upload training data
    4. start training
    5. predict(TODO)
    Returns tour on landing page if not shown ever
    -------

    """
    steps = [
        {
            "title": "Login",
            "description": "Login with your bohrium credential.",
            "targetId": "link-login",
        },
        {
            "title": "Input project name",
            "description": "Give your project a name",
            "targetId": "input-project-name",
        },
        {
            "title": "Select Bohrium Project",
            "description": "Select the Bohrium project for billing",
            "targetId": "input-bohrium-project",
        },
        {   
            "title": "Input Molecule",
            "description": "input molecule to be synthesized",
            "targetId": "input-molecule",
        },
        {
            "title": "Start Training!",
            "description": "After click this button, you will submit a bohrium job to synthesis target molecule",
            "targetId": "btn-run",
        },
    ]
    return AntdTour(steps=steps, open=False, id="tour")


import flask
from dash import no_update, callback, Input, Output, State
from dash.exceptions import PreventUpdate
from models.session import Session
from views.login import LoginModal
from utils.token_helper import get_user_key, get_user_id, is_valid_token
from topics import Topics
from loguru import logger


@callback(
    [
        Output(LoginModal.id, "is_open", allow_duplicate=True),
        Topics.Slots.token.get_output("data"),
    ],
    [
        Input("link-login", "n_clicks"),
    ],
    [
        Topics.Slots.token.get_state("data"),
    ],
    prevent_initial_call=True,
)
def toggle_login_modal_by_click(n_clicks, token):
    logger.info(f"toggle_login_modal_by_click {n_clicks} token {token}")
    if not n_clicks:
        return no_update, no_update
    update_token = no_update
    if (not token) or (not is_valid_token(token)):
        token = flask.request.cookies.get("sso-brmToken")
        logger.debug(f"token from cookies {token}")
        if (not token) or (not is_valid_token(token)):
            return True, no_update
        update_token = token
    return False, update_token


@callback(
    [
        Output(LoginModal.id, "is_open", allow_duplicate=True),
        Topics.Slots.token.get_output("data"),
    ],
    [
        Input("btn-run", "n_clicks"),
    ],
    [
        Topics.Slots.token.get_state("data"),
    ],
    prevent_initial_call=True,
)
def toggle_login_modal(n_clicks, token):
    logger.info(f"toggle_login_modal {n_clicks} token {token}")
    if not n_clicks:
        return no_update, no_update
    update_token = no_update
    if (not token) or (not is_valid_token(token)):
        token = flask.request.cookies.get("sso-brmToken")
        logger.debug(f"token from cookies {token}")
        if (not token) or (not is_valid_token(token)):
            return True, no_update
        update_token = token
    return False, update_token


@callback(
    [
        Output(LoginModal.id, "is_open", allow_duplicate=True),
        Topics.Slots.token.get_output("data"),
        Topics.Slots.username.get_output("data"),
        Output("span-username", "children", allow_duplicate=True),
        Topics.Slots.tour_shown.get_output("data", allow_duplicate=True),
    ],
    Input(LoginModal.modal_id, "message"),
    Topics.Slots.tour_shown.get_state("data"),
    prevent_initial_call="initial_duplicate",
)
def login(message, shown):
    logger.info(f"login message {message}")
    if message and "data" in message and "token" in message["data"]:
        token = message["data"]["token"]
    else:
        token = flask.request.cookies.get("sso-brmToken")
    token_info = is_valid_token(token)
    if token_info:
        user_id = get_user_id(token)

        user_key = get_user_key(token)
        logger.info(f"login {user_id} {user_key}")
        s: Session = Session.load(str(user_id))
        # s.updated_at = datetime.now().isoformat()
        # s.save()
        return (
            False,
            token,
            user_key,
            user_key,
            (s.tour_shown if s.tour_shown != shown else no_update),
        )
    if not message:
        logger.info(f"shown is {shown}")
        return no_update, no_update, no_update, no_update, shown
    return True, no_update, no_update, no_update, no_update


# 如果 topic tour_shown 为空且 session.tour_shown False 则设置 open 为 True
@callback(
    Output("tour", "open", allow_duplicate=True),
    Topics.Slots.tour_shown.get_input("data"),
    Topics.Slots.token.get_state("data"),
    prevent_initial_call=True,
)
def toggle_tour(shown, token):
    if token:
        user_id = get_user_id(token)
        if user_id:
            s: Session = Session.load(user_id)
            s.tour_shown = shown
            s.save()

    if not shown:
        return True
    return False


# 结束导览后记录 topic tour_shown True
@callback(
    Topics.Slots.tour_shown.get_output("data", allow_duplicate=True),
    Input("tour", "open"),
    Topics.Slots.token.get_state("data"),
    prevent_initial_call=True,
)
def save_tour_shown(current, token):
    logger.info(f"save_tour_shown {current}")
    if current == False:
        if token:
            user_id = get_user_id(token)
            if user_id:
                s: Session = Session.load(user_id)
                s.tour_shown = True
                s.save()
        return True
    return no_update


# tour_shown 为 true 后存储到 session

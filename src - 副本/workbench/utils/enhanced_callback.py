from dash import callback, State, no_update
from topics import Topics
from utils.metrics import log_metrics


def do_log_metrics(*args, **kwargs):
    if any(args[0]):
        log_metrics(
            args[1][0],
            "",
            kwargs.get("name"),
        )

    return no_update


def callback_with_metrics(*args, **kwargs):
    metrics_name = kwargs.pop("dp_metrics_name", "")
    endpoint = kwargs.pop("endpoint", "")

    def decorator(func):
        @callback(*args, **kwargs)
        def wrapper(*func_args):
            return func(*func_args)

        wrapper.__name__ = func.__name__

        @callback(
            [
                [
                    Topics.Slots.username.get_output("data"),
                ],
                args[1],
                [
                    Topics.Slots.username.get_state("data"),
                ],
            ],
            **kwargs,
        )
        def metrics(*func_args):
            return do_log_metrics(
                *func_args,
                **{
                    "name": metrics_name or func.__name__,
                    "endpoint": endpoint or func.__module__,
                },
            )

        return wrapper

    return decorator

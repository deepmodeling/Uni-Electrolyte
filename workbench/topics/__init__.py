from dash import html, dcc
from dash_id_utils import DashIDGenerator


class Topics:
    class Slots:
        # TODO add token input then get current exp_name
        token = DashIDGenerator(page="session", type="topics", name="token")
        username = DashIDGenerator(page="session", type="topics", name="username")
        exploration_name = DashIDGenerator(
            page="session", type="topics", name="exploration_name"
        )
        exploration_status = DashIDGenerator(
            page="session", type="topics", name="exploration_status"
        )
        target_molecule = DashIDGenerator(
            page="session", type="topics", name="target_molecule"
        )
        job_id = DashIDGenerator(page="session", type="topics", name="job_id")
        job_status = DashIDGenerator(page="session", type="topics", name="job_status")
        route_id = DashIDGenerator(page="session", type="topics", name="route_id")
        options = DashIDGenerator(page="session", type="topics", name="options")
        tour_shown = DashIDGenerator(page="session", type="topics", name="tour_shown")

    @classmethod
    def render(cls):
        res = []
        for slot in cls.Slots.__dict__.keys():
            if not slot.startswith("__"):
                id_generator: DashIDGenerator = getattr(cls.Slots, slot)
                res.append(dcc.Store(id=id_generator.get_identifier()))
        return html.Div(res, id="topic-placeholder")

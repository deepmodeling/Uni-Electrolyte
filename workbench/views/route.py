import dash_bootstrap_components as dbc
from dash import html
from models.session import Route
from typing import List


def render_candidate_routes(job_id: str, candidate_routes: List[Route]):
    header = [
        html.Thead(
            html.Tr(
                [
                    html.Th("Rank"),
                    html.Th("Name"),
                    html.Th("Steps"),
                    html.Th("Cost"),
                    html.Th("Probability"),
                    html.Th("Complete"),
                ]
            )
        )
    ]

    rows = []
    if not job_id or not candidate_routes:
        table_body = [html.Tbody(rows)]
        return header + table_body

    for i in range(0, len(candidate_routes)):
        route = candidate_routes[i]
        cost = route.properties.get("cost")
        probability = route.properties.get("probability")
        if cost:
            cost = int(cost)
        else:
            cost = "-"

        if probability:
            probability = round(probability, 3)
        else:
            probability = "-"
        rows.append(
            html.Tr(
                [
                    html.Td(
                        i,
                    ),
                    html.Td(route.route_name),
                    html.Td(route.properties.get("step")),
                    html.Td(cost),
                    html.Td(probability),
                    html.Td(f'{route.properties.get("complete")}'),
                ],
                id={
                    "view": "result",
                    "table": "table-candidate-routes",
                    "type": "tr",
                    "job": job_id,
                    "index": f"{i}",
                },
                n_clicks=0,
            )
        )

    table_body = [html.Tbody(rows)]
    return header + table_body


def route_view():
    table_header = [
        html.Thead(
            html.Tr(
                [
                    html.Th("Rank"),
                    html.Th("Name"),
                    html.Th("Steps"),
                    html.Th("Cost"),
                    html.Th("Probability"),
                    html.Th("Complete"),
                ]
            )
        )
    ]
    table_body = []

    table = dbc.Table(
        table_header + table_body,
        id="table-candidate-routes",
        bordered=True,
        hover=True,
        color="light",
    )
    res = html.Div(
        table,
        style={
            "maxHeight": "500px",
            # "overflowY": "auto",
        },
    )
    return res

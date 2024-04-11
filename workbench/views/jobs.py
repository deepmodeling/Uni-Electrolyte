import dash_bootstrap_components as dbc
from dash import html
from models.session import Job, JobStatus


table_header = [
    html.Thead(
        html.Tr(
            [
                html.Th("Exploration Id"),
                html.Th("Name"),
                html.Th("Description"),
                html.Th("Status"),
                html.Th("Created"),
            ]
        )
    )
]


def render_jobs(jobs: [Job]):
    rows = []
    for i in range(0, len(jobs)):
        job = jobs[i]
        # TODO add app ingress and replace domain
        job_url = f"https://app.bohrium.dp.tech/retro-synthesis-jobs/?request=GET%3A%2Fapplications%2Fretro-synthesis%2Fjobs%2F{job.name}"
        rows.append(
            html.Tr(
                [
                    html.Td(
                        i,
                    ),
                    html.Td(
                        html.A(job.name, href=job_url, target="_blank"),
                    ),
                    html.Td(job.descriptions),
                    html.Td(job.status),
                    html.Td(job.created_at),
                ],
                id={
                    "view": "jobs",
                    "table": "job",
                    "type": "tr",
                    "index": i,
                },
                n_clicks=0,
            )
        )

    table_body = [html.Tbody(rows)]
    return table_header + table_body


def jobs_view():
    table = dbc.Table(
        table_header,
        # table_header + table_body,
        id="table-jobs",
        bordered=True,
        responsive=True,
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

import dash_bootstrap_components as dbc
from dash import html
from views.helper import get_modalable_molecule


def render_backup_reactions(backup_reactions, viewport=None):
    header = [
        html.Thead(
            html.Tr(
                [
                    html.Th("Index"),
                    html.Th("SMILES"),
                    #html.Th("Reaction Type"),
                    html.Th("Probability"),
                    #html.Th("Confidence Score"),
                    html.Th("Reaction"),
                ]
            )
        )
    ]

    rows = []

    text_ellipsis = {
        "whiteSpace": "nowrap",
        "overflow": "hidden",
        "textOverflow": "ellipsis",
        "maxWidth": "10ch",
    }
    if not backup_reactions:
        table_body = [html.Tbody(rows)]
        return header + table_body

    for i in range(0, len(backup_reactions)):
        reaction = backup_reactions[i]
        rows.append(
            html.Tr(
                [
                    html.Td(
                        i,
                    ),
                    html.Td(
                        reaction["smiles"],
                        style=text_ellipsis,
                    ),
                    #html.Td(reaction.get("reaction_type")),
                    html.Td(reaction.get("probability")),
                    #html.Td(reaction.get("confidence_score")),
                    html.Td(
                        get_modalable_molecule(
                            f"backup-reaction-{i}",
                            reaction["smiles"],
                            500,
                            200,
                            viewport,
                            reaction=True,
                        ),
                        style={"width": "500px"},
                    ),
                ],
                # id=f"row-backup-{i}",
                id={
                    "view": "result",
                    "table": "table-backup-reactions",
                    "type": "tr",
                    "index": f"{i}",
                    "smiles": reaction["smiles"],
                },
                n_clicks=0,
            )
        )

    table_body = [html.Tbody(rows)]
    return header + table_body


def result_view():
    table_header = [
        html.Thead(
            html.Tr(
                [
                    html.Th("Index"),
                    html.Th("SMILES"),
                    #html.Th("Reaction Type"),
                    html.Th("Probability"),
                    #html.Th("Confidence Score"),
                    html.Th("Reaction", style={"width": "500px"}),
                ]
            )
        )
    ]
    table_body = []

    table = dbc.Table(
        table_header + table_body,
        id="table-backup-reactions",
        bordered=True,
        hover=True,
        color="light",
        # responsive=True,
    )
    res = html.Div(
        table,
        style={
            "maxHeight": "500px",
            # "overflowY": "auto",
            # "overflowX": "auto",
        },
    )
    return res

import dash_bootstrap_components as dbc
from loguru import logger
from dash import html
import dash_echarts
from fake_data.mindmap import DRY_RUN_DATA as graph


def summary_view():
    return html.Div()
    option = {
        "title": {"text": "Pipeline Mindmap", "top": "top", "left": "left"},
        "legend": {},
        "tooltip": {},
        "toolbox": {
            "show": True,
            "feature": {
                "mark": {"show": True},
                "dataView": {"show": True, "readOnly": False},
                "restore": {"show": True},
                "saveAsImage": {"show": True},
            },
        },
        "animationDuration": 1500,
        "animationEasingUpdate": "quinticInOut",
        "series": [
            {
                "name": "Les Miserables",
                "type": "graph",
                "layout": "none",
                "data": graph["nodes"],
                "links": graph["links"],
                "categories": graph["categories"],
                "roam": True,
                "label": {"position": "right", "formatter": "{b}"},
                "lineStyle": {"color": "source", "curveness": 0},
                "emphasis": {"focus": "adjacency", "lineStyle": {"width": 10}},
            }
        ],
    }
    chart = dash_echarts.DashECharts(
        option=option,
        id="chart-mindmap",
        style={
            "width": "80vh",
            "height": "30vh",
        },
    )
    # logger.debug(f"mindmap_view chart {chart}")
    return html.Div([chart])

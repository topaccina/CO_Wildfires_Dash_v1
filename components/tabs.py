from dash import Dash, html, dcc

import dash_bootstrap_components as dbc
from components.report import build_report
from components.guide import build_guide

report = build_report()
guide = build_guide()


def get_tabs():
    tab1_content = dbc.Card(
        dbc.CardBody(
            [
                report,
            ]
        ),
        className="m-4",
    )

    tab2_content = dbc.Card(
        dbc.CardBody([guide]),
        className="mt-3",
    )

    tabs = dbc.Tabs(
        [
            dbc.Tab(tab1_content, label="Report"),
            dbc.Tab(tab2_content, label="User Guide"),
            # dbc.Tab("This tab's content is never seen", label="Tab 3", disabled=True),
        ]
    )
    return tabs

from dash import Dash, html, dcc

import dash_bootstrap_components as dbc


def get_navbar():
    navbar = dbc.NavbarSimple(
        brand="Wildfires in Orinoco Top Parks",
        brand_href="#",
        color="primary",
        dark=True,
    )
    return navbar

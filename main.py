from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import geopandas as gpd
import dash_bootstrap_components as dbc

from components.navbar import get_navbar
from components.tabs import get_tabs


# fire = pd.read_csv("./data/fire_weather_address_subset.csv")
# parks = gpd.read_file("./data/parksSubset.geojson")


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# server = app.server

navbar = get_navbar()
tabs = get_tabs()


# filter and controls

main = dbc.Container([dbc.Row(dbc.Col(navbar)), html.Br(), dbc.Row(dbc.Col(tabs))])

app.layout = dbc.Container(main, fluid=True)


if __name__ == "__main__":
    app.run_server(debug=True)

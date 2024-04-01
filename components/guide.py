from dash import Dash, html, dcc, Input, Output, callback, dash_table

import dash_bootstrap_components as dbc
import pandas as pd
import geopandas as gpd
import plotly.express as px


def build_guide():

    guide = (
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    dcc.Markdown(
                                        "\n\n"
                                        "This application is intended for learning purpose only to explore the Plotly maps and test chained components.\n"
                                        'Dataset used in this app is a reduced version of the original dataset from this <dccLink href="https://github.com/oferreirap/wildfires_data_app/tree/main/Data" children="Github repository" />  \n '
                                        "\n"
                                        'Under development to join the <dccLink href="https://charming-data.circle.so/home " children="Charming Data Community" /> March Project initiative \n'
                                        "\n"
                                        "#### Data filtering and aggregation.\n"
                                        "- Data subset over 2019-2022 timeframe. \n"
                                        "- Daily data aggregation over 1x1 kmq tile by considering approx 1km=0.01 lat, 1km=0.01 lon.\n"
                                        "- Wildfires detected over with high confidence - MODIS data confindence >=80% \n"
                                        "- Points interesecting 3 of the top Orinoco Territory parks\n"
                                        "- Dataset enriched with: latitude, longitude reverse geocoding - added State and Town by usign Geopy package- and weather condition from open-meteo api \n"
                                        "\n "
                                        "\n\n\n",
                                        dangerously_allow_html=True,
                                    ),
                                ),
                                html.Hr(),
                                html.Div(
                                    dcc.Markdown("#### Data Preparation Hints.\n"),
                                ),
                                html.Div(
                                    dcc.Markdown("- Get Weather Information.\n"),
                                ),
                                dcc.Clipboard(
                                    target_id="copyable-markdown1",
                                    style={
                                        "display": "inline-block",
                                        "verticalAlign": "top",
                                    },
                                ),
                                html.Div(
                                    [
                                        dcc.Markdown(
                                            "import requests\n"
                                            "\n"
                                            "url=https://archive-api.open-meteo.com/v1/archive?latitude=54.52&longitude=31.41&start_date=2024-03-14&end_date=2024-03-28&daily=weathercode,wind_speed_10m_max,temperature_2m_mean,rain_sum&timezone=auto\n"
                                            "\n"
                                            "response = requests.get(url)\n"
                                            "\n"
                                            "response_json = response.json()",
                                            id="copyable-markdown1",
                                            style={
                                                "align": "left",
                                            },
                                        ),
                                    ],
                                    className="border me-3 mb-3 p-3 ",
                                ),
                                html.Div(
                                    dcc.Markdown("- Reverse geocoding \n"),
                                ),
                                dcc.Clipboard(
                                    target_id="copyable-markdown2",
                                    style={
                                        "display": "inline-block",
                                        "verticalAlign": "top",
                                    },
                                ),
                                html.Div(
                                    [
                                        dcc.Markdown(
                                            "from geopy.geocoders import Nominatim\n"
                                            "\n"
                                            'Latitude = "11.0912"\n\n'
                                            'Longitude = "-72.6625"\n'
                                            "\n"
                                            'geolocator = Nominatim(user_agent="your openstreet map id here!")\n'
                                            "\n"
                                            'location = geolocator.reverse(Latitude+","+Longitude)\n'
                                            "\n"
                                            'address = location.raw\["address"\]',
                                            id="copyable-markdown2",
                                            style={
                                                "align": "left",
                                            },
                                        ),
                                    ],
                                    className="border me-3 mb-3 p-3",
                                ),
                            ]
                        ),
                    ]
                )
            ],
        ),
    )
    return guide[0]

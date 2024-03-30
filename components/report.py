from dash import Dash, html, dcc, Input, Output, callback, dash_table

import dash_bootstrap_components as dbc
import pandas as pd
import geopandas as gpd
import plotly.express as px


def build_report():
    fire = pd.read_csv("./data/fire_weather_address_subset.csv")
    parks = gpd.read_file("./data/parksSubset.geojson")
    fire = fire.sort_values(by="acq_date")
    fire_group = (
        fire.groupby(by=["nombre", "year_month", "acq_year"])["rain"]
        .count()
        .reset_index()
    )
    fire_group.columns = ["Park", "Year_Month", "Year", "WildFires_Count"]

    radio = dbc.RadioItems(
        options=[{"label": "Yes", "value": 0}, {"label": "No", "value": 1}],
        value=1,
        id="map-radio",
    )

    animation = dbc.RadioItems(
        options=[{"label": "Yes", "value": 0}, {"label": "No", "value": 1}],
        value=1,
        id="map-animation-radio",
    )

    styleDrop = dcc.Dropdown(
        options=[
            "carto-darkmatter",
            "carto-positron",
            "white-bg",
            "open-street-map",
        ],
        value="open-street-map",
        id="map-dropdown",
        clearable=False,
    )
    fig = px.scatter_mapbox(
        fire,
        lat="lat_adj",
        lon="lon_adj",
        # center=dict(lat=fire.lat_adj.median(), lon=fire.lon_adj.median()),
        zoom=7,
        mapbox_style="open-street-map",
        custom_data=[
            "nombre",
            "acq_date",
            "state",
            "town",
            "T_mean",
            "rain",
            "wind_speed",
            "weather_code_description",
        ],
    )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.update_traces(hovertemplate="Park: %{customdata[0]} <br>Date: %{customdata[1]}")

    # fig3 = px.line(
    #     fire_group,
    #     x="Year_Month",
    #     y="WildFires_Count",
    #     color="Park",
    #     markers=True,
    # )

    fig3 = px.bar(
        fire_group,
        x="Year_Month",
        y="WildFires_Count",
        color="Park",
        barmode="group",
        height=500,
    )

    yearFilter = dcc.Dropdown(
        options=["all"] + [year for year in fire.acq_year.unique()],
        value="all",
        id="years-dropdown",
        clearable=False,
    )

    parkFilter = dcc.Dropdown(
        options=["all"] + [park for park in fire.nombre.unique()],
        value="all",
        id="parks-dropdown",
        clearable=False,
    )

    report = dbc.Container(
        [
            dbc.Row(
                [
                    html.H4("Wildfires Map Controls", className="card-text"),
                    dbc.Col([dbc.Label("Parks Borders"), radio]),
                    dbc.Col([dbc.Label("Animation"), animation]),
                    dbc.Col([dbc.Label("Style"), styleDrop], width=5),
                ],
                align="center",
                className="border rounded-3 p-3",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col([dcc.Graph(figure=fig, clickData=None, id="map")], width=9),
                    dbc.Col(
                        [
                            html.H4("WildFires Details", className="card-text"),
                            html.H6("click points on the map", className="card-text"),
                            html.Hr(),
                            html.Div(children="", id="clicked-data"),
                        ],
                        width=3,
                        className="border rounded-3 p-3",
                    ),
                ]
            ),
            dbc.Row(dbc.Spinner(html.Div(id="loading-output"))),
            html.Br(),
            dbc.Row(
                [
                    html.H4("Data Filters", className="card-text"),
                    dbc.Col([dbc.Label("Years"), yearFilter], width=3),
                    dbc.Col([dbc.Label("Parks"), parkFilter], width=4),
                    # dbc.Col([dbc.Label("Style"), styleDrop]),
                ],
                align="center",
                className="border rounded-3 p-3",
            ),
            html.Br(),
            dbc.Row(
                [
                    html.H4("Wildfires Trend", className="card-text"),
                    dbc.Col([dcc.Graph(figure=fig3, id="trend")]),
                ]
            ),
        ],
    )

    @callback(
        Output("map", "figure"),
        Output("loading-output", "children"),
        Output("trend", "figure"),
        Input("map-radio", "value"),
        Input("map-dropdown", "value"),
        Input("map-animation-radio", "value"),
        Input("years-dropdown", "value"),
        Input("parks-dropdown", "value"),
        prevent_initial_call=True,
    )
    def update_map(vizOption, vizStyle, animOptions, year, park):
        custom_data = [
            "nombre",
            "acq_date",
            "state",
            "town",
            "T_mean",
            "rain",
            "wind_speed",
            "weather_code_description",
        ]

        fire_ff = pd.DataFrame()
        parks_ff = pd.DataFrame()
        fire_group_ff = pd.DataFrame()
        fire_ff = fire
        parks_ff = parks
        fire_group_ff = fire_group
        if year != "all":
            fire_ff = fire_ff[fire_ff.acq_year == year]
            fire_group_ff = fire_group_ff[fire_group_ff.Year == year]

        if park != "all":
            fire_ff = fire_ff[fire_ff.nombre == park]
            parks_ff = parks_ff[parks_ff.nombre == park]
            fire_group_ff = fire_group_ff[fire_group_ff.Park == park]

        if (vizOption == 1) & (animOptions == 0):
            fig = px.scatter_mapbox(
                fire_ff,
                lat="lat_adj",
                lon="lon_adj",
                # center=dict(lat=fire.lat_adj.median(), lon=fire.lon_adj.median()),
                zoom=7,
                mapbox_style=vizStyle,  # "carto-positron",
                animation_frame="year_month",
                custom_data=custom_data,
            )
            fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
            fig.update_traces(
                hovertemplate="Park: %{customdata[0]} <br>Date: %{customdata[1]}"
            )
        elif (vizOption == 1) & (animOptions == 1):
            fig = px.scatter_mapbox(
                fire_ff,
                lat="lat_adj",
                lon="lon_adj",
                # center=dict(lat=fire.lat_adj.median(), lon=fire.lon_adj.median()),
                zoom=7,
                mapbox_style=vizStyle,  # "carto-positron",
                custom_data=custom_data,
            )
            fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
            fig.update_traces(
                hovertemplate="Park: %{customdata[0]} <br>Date: %{customdata[1]}"
            )
        elif (vizOption == 0) & (animOptions == 0):
            fig = px.scatter_mapbox(
                fire_ff,
                lat="lat_adj",
                lon="lon_adj",
                # center=dict(lat=fire.lat_adj.median(), lon=fire.lon_adj.median()),
                zoom=7,
                mapbox_style=vizStyle,  # "carto-positron",
                animation_frame="year_month",
                custom_data=custom_data,
            )
            fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
            fig.update_traces(
                hovertemplate="Park: %{customdata[0]} <br>Date: %{customdata[1]}"
            )
            fig2 = px.choropleth_mapbox(
                parks_ff,
                geojson=parks_ff.geometry,
                locations=parks_ff.index,
                color=parks_ff.nombre,
                color_continuous_scale="Viridis",
                range_color=(50, 100),
                mapbox_style=vizStyle,  # ""carto-positron",
                zoom=7,
                center={"lat": fire.lat_adj.median(), "lon": fire.lon_adj.median()},
                opacity=0.5,
            )
            trace0 = fig2
            for i in range(len(trace0.data)):
                fig.add_trace(trace0.data[i])
                trace0.layout.update(showlegend=False)
            print("update done ")
            fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
            fig.update_traces(
                hovertemplate="Park: %{customdata[0]} <br>Date: %{customdata[1]}"
            )
        else:
            fig = px.scatter_mapbox(
                fire_ff,
                lat="lat_adj",
                lon="lon_adj",
                center=dict(lat=fire.lat_adj.median(), lon=fire.lon_adj.median()),
                zoom=7,
                mapbox_style=vizStyle,
                custom_data=custom_data,  # ""carto-positron",
            )
            fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
            fig.update_traces(
                hovertemplate="Park: %{customdata[0]} <br>Date: %{customdata[1]}"
            )
            fig2 = px.choropleth_mapbox(
                parks_ff,
                geojson=parks_ff.geometry,
                locations=parks_ff.index,
                color=parks_ff.nombre,
                color_continuous_scale="Viridis",
                range_color=(50, 100),
                mapbox_style=vizStyle,  # ""carto-positron",
                zoom=7,
                center={"lat": fire.lat_adj.median(), "lon": fire.lon_adj.median()},
                opacity=0.5,
            )
            trace0 = fig2
            for i in range(len(trace0.data)):
                fig.add_trace(trace0.data[i])
                trace0.layout.update(showlegend=False)
            print("update done ")
            fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
            fig.update_traces(
                hovertemplate="Park: %{customdata[0]} <br>Date: %{customdata[1]}"
            )
        fig3 = px.bar(
            fire_group_ff,
            x="Year_Month",
            y="WildFires_Count",
            color="Park",
            barmode="group",
            height=500,
        )

        return fig, "", fig3

    @callback(
        Output("clicked-data", "children"),
        Input("map", "clickData"),
        prevent_initial_call=True,
    )
    def clickedData(clickData):
        if "customdata" in clickData["points"][0].keys():
            print(f"{clickData['points'][0]['customdata']}")
            parkInfo = f"Park: {clickData['points'][0]['customdata'][0]}"
            dateInfo = f"Date: {clickData['points'][0]['customdata'][1]}"
            stateInfo = f"State: {clickData['points'][0]['customdata'][2]}"
            townInfo = f"Town: {clickData['points'][0]['customdata'][3]}"
            temperatureInfo = (
                f"Avg Temperature: {clickData['points'][0]['customdata'][4]} Celsius"
            )
            rainInfo = f"Total Rain: {clickData['points'][0]['customdata'][5]} mm"
            windInfo = f"Wind Speed: {clickData['points'][0]['customdata'][6]} km/h"
            weatherInfo = f"Weather: {clickData['points'][0]['customdata'][7]} "
            # info = [parkInfo, dateInfo, temperatureInfo]
            # click = f"Park: {clickData['points'][0]['customdata'][0]}\n Date: {clickData['points'][0]['customdata'][1]}\n "
            click = [
                html.P(parkInfo),
                html.P(dateInfo),
                html.P(townInfo),
                html.P(stateInfo),
                html.P(temperatureInfo),
                html.P(rainInfo),
                html.P(windInfo),
                html.P(weatherInfo),
            ]
        else:
            click = (
                "Invalid selecton. Details on demand enabled w/o Parks Borders only!"
            )
        # if clickData["points"][0]["customdata"] == None:
        #     click = "No valid point selected"
        # else:
        #     click = f"{clickData}"
        # click = f"{clickData['points'][0]['customdata']}"
        return click

    return report

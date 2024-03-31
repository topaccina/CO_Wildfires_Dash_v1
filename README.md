#### App Purpose
This application explores the fires of recent years in some of Colombia's natural parks using data from NASA.This application is intended for learning purpose only to explore the Plotly maps and test chained components. 
#### Data Sources
Dataset used in this app is a reduced version of the original dataset from this <dccLink href="https://github.com/oferreirap/wildfires_data_app/tree/main/Data" children="Github repository" /> 

Under development to join the <dccLink href="https://charming-data.circle.so/home " children="Charming Data Community" /> March Project initiative

#### Notes for data Preparation-filtering and aggregation
- Data subset over 2019-2022 timeframe.
- Daily data aggregation over 1x1 kmq tile by considering approx 1km=0.01 lat, 1km=0.01 lon.
- Wildfires detected over with high confidence - MODIS data confindence >=80% 
- Points interesecting 3 of the top Orinoco Territory parks
- Dataset enriched with latitude, longitude reverse geocoding: added State and Town by usign Geopy package
- Dataset enriched with weather condition from <dccLink href="https://open-meteo.com/" children="open-meteo api" />
- This repository include only the app code. Notebook for data prep have not been added yet
#### Python version
- tested with 10.3 python version

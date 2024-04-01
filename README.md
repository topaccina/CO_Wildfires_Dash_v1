#### App Purpose
This application explores the fires of recent years in some of Colombia's natural parks using data from NASA.This application is intended for learning purpose only to explore the Plotly maps and test chained components. 
#### Data Sources
Dataset used in this app is a reduced version of the original dataset from this [Github repository](https://github.com/oferreirap/wildfires_data_app/tree/main/Data). Thanks to [Olger Ferreira Pacheco](linkedin.com/in/olgerfp)

Under development to join the [Charming Data Community](https://charming-data.circle.so/c/ai-python-projects/) March Project initiative 

#### Notes for data Preparation-filtering and aggregation
- Data subset over 2019-2022 timeframe.
- Daily data aggregation over 1x1 kmq tile by considering approx 1km=0.01 lat, 1km=0.01 lon.
- Wildfires detected over with high confidence - MODIS data confindence >=80% 
- Points interesecting 3 of the top Orinoco Territory parks
- Dataset enriched with latitude, longitude reverse geocoding: added State and Town by usign Geopy package
- Dataset enriched with weather condition from [open-meteo api](https://open-meteo.com/) 
- Added  notebook/data_prep.ipynb is to provide a sample of the main steps to simplify the original dataset.

#### Python version
- tested with 10.3 python version

# -*- coding: utf-8 -*-
"""atividade9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/199NtYjiisyA2NxHcoDhWXyYieZVkBXLC
"""

#importando as bibliotecas necessárias
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import random
import numpy as np
import plotly 
import plotly.offline as py
import plotly.graph_objs as go # criará de fato os gráficos
from plotly.offline import plot, iplot
import cufflinks as cf # para conectar o plotly ao pandas
cf.go_offline()
plotly.offline.init_notebook_mode(connected = True)
import plotly.io as pio
pio.renderers.default = 'colab'

dados = pd.read_excel("dados_atividade_9.xlsx")
print(dados.columns.ravel())

"""Questão 1.1"""
dados['REGISTROS'].describe()

"""Questão 1.2"""
dados['REGISTROS'].iplot(kind='hist')

"""questão 1.3"""
fig = px.density_mapbox(dados[0:200], lat='LATITUDE', lon='LONGITUDE', z='REGISTROS', radius=10,
                        center=dict(lat=-20, lon=-40), zoom=2,
                        mapbox_style="stamen-terrain")
fig.show()

"""Questão 1.4"""
fig = px.bar(dados[0:50], x='MUNICIPIO', y='REGISTROS')
fig.show()

"""Questão 2"""
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

fig = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 20),
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.8,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ])
fig.show()
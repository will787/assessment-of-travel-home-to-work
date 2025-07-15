# %%
import pandas as pd
import numpy as np
import sys
import json
import plotly.express as px
import plotly.io as pio

sys.path.append('../query')
from extract_data_cloud import database
sys.path.append('../geo')
from malhas_br import select_uf

siglas_uf = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 
    'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 
    'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
]

def plot_state(value):
    pio.renderers.default = 'vscode'
    if value not in siglas_uf:
        print(f"State {value} is not available in the dataset.")
        return
    
    select_uf(value)
    print(value.upper())
    state_data = database[database['sigla_uf'] == value]
    state_data = state_data[['id_municipio', 'id_municipio_nome', 'tempo_medio_deslocamento']] 

    select_uf(value)
    with open(f'../geo/json_states/municipios_{value.lower()}.geojson', 'r', encoding='utf-8') as f:
        geojson_state = json.load(f)

    fig = px.choropleth(
        state_data,
        geojson=geojson_state,
        locations='id_municipio',
        color='tempo_medio_deslocamento',
        color_continuous_scale='Viridis',
        featureidkey='properties.CD_MUN',
        projection='mercator',
        hover_name='id_municipio_nome',
        title=f'Average Commute Time in {value} State',
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.show()
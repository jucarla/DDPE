from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import sys

from app import *
from components import sidebar, car_data, feature, driver_data
import car_kpis

# =========  Layout  =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[

    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout], md=2, style={'background-color': '#da1818', 'height': '1080px'}),
            dbc.Col([
                content
            ], md = 10)

    ])


], fluid=True)
#Fluid -> o conteúdo da página vai se espalhar de acordo com o tamanho da tela

#Callback -> Função passada como parâmetro para outras funções
@app.callback(Output('page-content','children'), [Input('url', 'pathname')])
def render_page(pathname):
    if pathname == '/' or pathname =='/carkpis':
        return car_kpis.layout

    if pathname == '/cardata':
        return car_data.layout
        
    if pathname == '/features':
        return feature.layout
        
    if pathname == '/driverkpis' :
            return car_kpis.layout
    if pathname == '/driverdata' :
            return driver_data.layout
app.run_server(port=8051, debug=True)
from dash import html, dcc
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar
from globals import *
import sys
import joblib
from app import app
from components.utils import get_metrics_df, get_array_like_metrics


df_metrics = pd.read_csv('dashboard/data/Channel_rep_kpis_basic1.2.1.csv')





#df_metrics = add_na_before_ones(df_metrics, 'Lap')
opt = [{'label': i, 'value': i} for i in df_metrics.columns]
# ========== Components =========#
graph_1 = dcc.Graph(id='metric_chart_1')
graph_2 = dcc.Graph(id='metric_chart_2')
graph_3 = dcc.Graph(id='metric_chart_3')
graph_4 = dcc.Graph(id='metric_chart_4')
graph_5 = dcc.Graph(id='metric_chart_5')
graph_6 = dcc.Graph(id='metric_chart_6')

# =========  Layout  =========== #
layout = dbc.Col([
        #Headline
       dbc.Row([ 
        dbc.Row(
            html.H1("Car KPIs", className="text-primary", style={'font-family': 'arial', 'font-style': 'normal',
                'font-weight': '700',
                'font-size': '25px',
                'line-height': '38px',
                'color': '#FFFFFF'}),
        ),
        dbc.Row([
            dbc.Col(
                dcc.Checklist(
                options=opt[2:],
                id='checkbox'
                ), width=700),
            dbc.Col(
                html.Label("", id="max-metrics-alert"))
        ])
            
        
       ], style={'height': '100px'}),

       #First dashboard row
       dbc.Row([ 
            dbc.Col([
                graph_1
            ],style={'width': '400px'}),
            dbc.Col([
                graph_2
            ],style={'width': '400px'})
       ], style={'height': '420px'}),

       #Second dashboard row
       dbc.Row([ 
            dbc.Col([
                graph_3
            ],style={'width': '400px'}),
            dbc.Col([
                graph_4
            ],style={'width': '400px'})
       ], style={'height': '420px'}),

        #Third dashboard row
       dbc.Row([ 
            dbc.Col([
                graph_5
            ],style={'width': '400px'}),
            dbc.Col([
                graph_6
            ],style={'width': '400px'})
       ], style={'height': '420px'})

    ])

def filter_df_metric(df: pd.DataFrame, metrics):
    mask = list(set(df.columns) - set(metrics))
    filtered_df = df.drop(mask, axis=1)
    #filtered_df = pd.DataFrame(df.loc['mse',:])
    #final_df =pd.concat([df, filtered_df], axis=1)
    return filtered_df

# =========  Callbacks  =========== #
@app.callback(
    Output("metric_chart_1", "figure"),
    Output("metric_chart_2", "figure"),
    Output("metric_chart_3", "figure"),
    Output("metric_chart_4", "figure"),
    Output("metric_chart_5", "figure"),
    Output("metric_chart_6", "figure"),
    Output('max-metrics-alert', 'children'),
    Input("checkbox", "value"),
)
def update_metrics_charts(value):
    graph_1 = px.line()
    graph_2 = px.line()
    graph_3 = px.line()
    graph_4 = px.line()
    graph_5 = px.line()
    graph_6 = px.line()
    
    alert = html.Label('', id='max-metrics-alert')

    if value != None:
        n_metrics = len(value)
        
        df = filter_df_metric(df_metrics, value)
        if n_metrics==1:
            graph_1 = px.line(df, x = df.index, y = value[0], title=f'{value[0]}', color=df_metrics['Setup'])
        elif n_metrics==2:
            graph_1 = px.line(df, x = df.index, y = value[0], title=f'{value[0]}', color=df_metrics['Setup'])
            graph_2 = px.line(df, x = df.index, y = value[1], title=f'{value[1]}', color=df_metrics['Setup'])
        elif n_metrics==3:
            graph_1 = px.line(df, x = df.index, y = value[0], title=f'{value[0]}', color=df_metrics['Setup'])
            graph_2 = px.line(df, x = df.index, y = value[1], title=f'{value[1]}', color=df_metrics['Setup'])
            graph_3 = px.line(df, x = df.index, y = value[2], title=f'{value[2]}', color=df_metrics['Setup'])
        elif n_metrics==4:
            graph_1 = px.line(df, x = df.index, y = value[0], title=f'{value[0]}', color=df_metrics['Setup'])
            graph_2 = px.line(df, x = df.index, y = value[1], title=f'{value[1]}', color=df_metrics['Setup'])
            graph_3 = px.line(df, x = df.index, y = value[2], title=f'{value[2]}', color=df_metrics['Setup'])
            graph_4 = px.line(df, x = df.index, y = value[3], title=f'{value[3]}', color=df_metrics['Setup'])
        elif n_metrics==5:
            graph_1 = px.line(df, x = df.index, y = value[0], title=f'{value[0]}', color=df_metrics['Setup'])
            graph_2 = px.line(df, x = df.index, y = value[1], title=f'{value[1]}', color=df_metrics['Setup'])
            graph_3 = px.line(df, x = df.index, y = value[2], title=f'{value[2]}', color=df_metrics['Setup'])
            graph_4 = px.line(df, x = df.index, y = value[3], title=f'{value[3]}', color=df_metrics['Setup'])
            graph_5 = px.line(df, x = df.index, y = value[4], title=f'{value[4]}', color=df_metrics['Setup'])
        elif n_metrics==6:
            graph_1 = px.line(df, x = df.index, y = value[0], title=f'{value[0]}', color=df_metrics['Setup'])
            graph_2 = px.line(df, x = df.index, y = value[1], title=f'{value[1]}', color=df_metrics['Setup'])
            graph_3 = px.line(df, x = df.index, y = value[2], title=f'{value[2]}', color=df_metrics['Setup'])
            graph_4 = px.line(df, x = df.index, y = value[3], title=f'{value[3]}', color=df_metrics['Setup'])
            graph_5 = px.line(df, x = df.index, y = value[4], title=f'{value[4]}', color=df_metrics['Setup'])
            graph_6 = px.line(df, x = df.index, y = value[5], title=f'{value[5]}', color=df_metrics['Setup'])
        if n_metrics >6:
            alert = dbc.Alert("Maximum 6 metrics at a time!", color="danger", id = "max-metrics-alert", dismissable=True, style={"right-margin": "10px", 'left-margin':'10px'})
    
    
    return graph_1, graph_2, graph_3, graph_4,graph_5, graph_6, alert
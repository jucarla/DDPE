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


df_metrics = pd.read_csv('dashboard/data/car_kpi_exercises_S3.csv')

opt = [{'label': i, 'value': i} for i in df_metrics.columns]
# ========== Components =========#
graph_1 = dcc.Graph(id='channel_chart_1')
graph_2 = dcc.Graph(id='channel_chart_2')
graph_3 = dcc.Graph(id='channel_chart_3')
graph_4 = dcc.Graph(id='channel_chart_4')
graph_5 = dcc.Graph(id='channel_chart_5')
graph_6 = dcc.Graph(id='channel_chart_6')

# =========  Layout  =========== #
layout = dbc.Col([
        #Headline
       dbc.Row([ 
        dbc.Row(
            html.H1("Car Channel Data", className="text-primary", style={'font-family': 'arial', 'font-style': 'normal',
                'font-weight': '700',
                'font-size': '25px',
                'line-height': '38px',
                'color': '#FFFFFF'}),
        ),
        dbc.Row([
            dbc.Col(
                dcc.Checklist(
                options=opt,
                id='channel-checkbox'
                ), width=700),
            dbc.Col(
                html.Label("", id="channel-max-metrics-alert"))
        ])
            
        
       ]),

       #First dashboard row
       dbc.Row([graph_1], style={'height':'200px'}),
       dbc.Row([graph_2], style={'height':'200px'}),
       dbc.Row([graph_3], style={'height':'200px'}),
       dbc.Row([graph_4], style={'height':'200px'}),
       dbc.Row([graph_5], style={'height':'200px'}),
       dbc.Row([graph_6], style={'height':'200px'}),
       

    ])

def filter_df_metric(df: pd.DataFrame, metrics):
    mask = list(set(df.columns) - set(metrics))
    filtered_df = df.drop(mask, axis=1)
    #filtered_df = pd.DataFrame(df.loc['mse',:])
    #final_df =pd.concat([df, filtered_df], axis=1)
    return filtered_df

# =========  Callbacks  =========== #
@app.callback(
    Output("channel_chart_1", "figure"),
    Output("channel_chart_2", "figure"),
    Output("channel_chart_3", "figure"),
    Output("channel_chart_4", "figure"),
    Output("channel_chart_5", "figure"),
    Output("channel_chart_6", "figure"),
    Output('channel-max-metrics-alert', 'children'),
    Input("channel-checkbox", "value"),
)
def update_metrics_charts(value):
    graph_1 = px.line()
    graph_2 = px.line()
    graph_3 = px.line()
    graph_4 = px.line()
    graph_5 = px.line()
    graph_6 = px.line()
    
    alert = html.Label('', id='channel-max-metrics-alert')

    if value != None:
        n_metrics = len(value)
        
        df = filter_df_metric(df_metrics, value)
        
        if n_metrics==1:
            graph_1 = px.line(df, x = df_metrics['Time'], y = value[0])
        elif n_metrics==2:
            graph_1 = px.line(df, x = df_metrics['Time'], y = value[0])
            graph_2 = px.line(df, x = df_metrics['Time'], y = value[1])
        elif n_metrics==3:
            graph_1 = px.line(df, x = df_metrics['Time'], y = value[0])
            graph_2 = px.line(df, x = df_metrics['Time'], y = value[1])
            graph_3 = px.line(df, x = df_metrics['Time'], y = value[2])
        elif n_metrics==4:
            graph_1 = px.line(df, x = df_metrics['Time'], y = value[0])
            graph_2 = px.line(df, x = df_metrics['Time'], y = value[1])
            graph_3 = px.line(df, x = df_metrics['Time'], y = value[2])
            graph_4 = px.line(df, x = df_metrics['Time'], y = value[3])
        elif n_metrics==5:
            graph_1 = px.line(df, x = df_metrics['Time'], y = value[0])
            graph_2 = px.line(df, x = df_metrics['Time'], y = value[1])
            graph_3 = px.line(df, x = df_metrics['Time'], y = value[2])
            graph_4 = px.line(df, x = df_metrics['Time'], y = value[3])
            graph_5 = px.line(df, x = df_metrics['Time'], y = value[4])
        elif n_metrics==6:
            graph_1 = px.line(df, x = df_metrics['Time'], y = value[0])
            graph_2 = px.line(df, x = df_metrics['Time'], y = value[1])
            graph_3 = px.line(df, x = df_metrics['Time'], y = value[2])
            graph_4 = px.line(df, x = df_metrics['Time'], y = value[3])
            graph_5 = px.line(df, x = df_metrics['Time'], y = value[4])
            graph_6 = px.line(df, x = df_metrics['Time'], y = value[5])
        if n_metrics >6:
            alert = dbc.Alert("Maximum 6 metrics at a time!", color="danger", id = "channel-max-metrics-alert", dismissable=True, style={"right-margin": "10px", 'left-margin':'10px'})
    
    
    return graph_1, graph_2, graph_3, graph_4,graph_5, graph_6, alert
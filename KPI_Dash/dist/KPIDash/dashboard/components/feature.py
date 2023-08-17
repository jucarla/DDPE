from dash import html, dcc, callback
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar
from globals import *
from app import app
from dash.exceptions import PreventUpdate
import sys
import joblib
import seaborn as sb

sys.path.append('..')
df = pd.read_csv('dashboard/data/Channel_rep.csv')
opt = [{'label': i, 'value': i} for i in df.columns]

corr_graph = dcc.Graph(id = 'correlation-graph')
layout = dbc.Col([
    dbc.Row([
            dbc.Col(
                dcc.Checklist(
                options=opt,
                id='checkbox'
                ))
    ]),
    dbc.Row([
        dbc.Col(
            corr_graph
        )
    ])
])
def filter_df_metric(df: pd.DataFrame, metrics):
    mask = list(set(df.columns) - set(metrics))
    filtered_df = df.drop(mask, axis=1)
     
    return filtered_df

def filter_correlation(value,filter):
    if abs(value) >= filter:
        return value
    else:
        return np.nan

@app.callback(
    Output("correlation-graph", "figure"),
    Input("checkbox", "value"),
)
def update_metrics_charts(value):
    fig = px.line()
    if value != None and len(value) >=2:
        df_filtered = filter_df_metric(df, value)
        df_corr = df_filtered.corr()
        fig = go.Figure()
        fig.add_trace(
            go.Heatmap(
                x = df_corr.columns,
                y = df_corr.index,
                z = np.array(df_corr)
            )
        )


    return fig
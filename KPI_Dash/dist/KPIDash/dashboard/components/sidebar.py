import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import sys
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd
import sqlite3


# ========= Layout ========= #
layout = dbc.Col([
                html.H1("KPI Dash", className="text-primary", style={'font-family': 'arial', 'font-style': 'normal',
                'font-weight': '700',
                'font-size': '25px',
                'line-height': '38px',
                'color': 'white'}),
                html.Hr(),

                    
    # Seção NAV ------------------
    # href -> saber que pagina o programa irá ao clicar nos botões
    # pills -> botão em torno do menu quando ele é selecionado
                html.Hr(),
                dbc.Nav(
                    [
                        dbc.NavLink("Car KPIs", href="/carkpis", active="exact", style={'color': '#ffffff'}),
                        dbc.NavLink("Car Channels Data", href="/cardata", active = "exact", style={'color': '#ffffff'}),
                        dbc.NavLink("Feature Correlation", href="/features", active = "exact", style={'color': '#ffffff'}),
                        dbc.NavLink("Driver KPIs", href="/driverkpis", active="exact", style={'color': '#ffffff'}),
                        dbc.NavLink("Driver Channels Data", href="/driverdata", active = "exact", style={'color': '#ffffff'}),
                    ], vertical=True, pills=True, id='nav_buttons', style={'margin-bottom': "50px"}),
                
], id="sidebar-completa")





# =========  Callbacks  =========== #
# Pop-up receita
@app.callback(
    Output('modal-novo-receita', 'is_open'),
    Input('open-novo-projeto', 'n_clicks'),
    State('modal-novo-receita', 'is_open')
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open


    

'''@app.callback(
    [Output('project-name-label', 'children'), Output('popover-status','children')],
    Input('save-novo-projeto', 'n_clicks'),
    [State('project-name', 'value'), State('project-path', 'value')]
    )
def update_project(n_clicks, project_name, project_path):
    if n_clicks:
        try:
            if os.path.isfile(project_path):
                database = ReadSQL(project_path)
                
                popover_status = "Project Saved!"
            else: 
                popover_status = "Invalid Path"
        except:
            popover_status = "Invalid Path"
        
        return project_name, popover_status'''



    
if __name__ == '__main__':
    app.run_server(debug=True)
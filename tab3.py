# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:34:45 2023

@author: dokt.1
"""


import pandas as pd
import datetime as dt
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

def render_tab(df):


    grouped = pd.crosstab(df['day_of_week'],df['Store_type'],values=df['total_amt'],aggfunc=sum)
    
    traces = []
    for col in grouped.columns:
        traces.append(go.Bar(x=grouped.index,y=grouped[col],name=col,hoverinfo='text',
        hovertext=[f'{y/1e3:.2f}k' for y in grouped[col].values]))

    data = traces
    fig = go.Figure(data=data,layout=go.Layout(title='Przychody',barmode='stack',legend=dict(x=0,y=-0.5)))
    
    layout = html.Div([html.H1('Kanały Sprzedaży',style={'text-align':'center'}),
                        html.Div([html.Div([dcc.Graph(id='bar-stores',figure=fig)],style={'width':'50%'}),
                        html.Div([dcc.Dropdown(id='Store_type_dropd',
                                    options=[{'label':Store_type,'value':Store_type} for Store_type in df['Store_type'].unique()],
                                    value=df['Store_type'].unique()[0]),
                                    dcc.Graph(id='store_age')],style={'width':'50%'})],style={'display':'flex'}),
                                    html.Div(id='temp-out')
                        ])
    return layout   
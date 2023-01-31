# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:09:24 2023

@author: dokt.1
"""

import pandas as pd
import datetime as dt
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

def render_tab(df):

    layout = html.Div([html.H1('Sprzedaż globalna',style={'text-align':'center'}),
                        html.Div([dcc.DatePickerRange(id='sales-range',
                        start_date=df['tran_date'].min(),
                        end_date=df['tran_date'].max(),
                        display_format='YYYY-MM-DD')],style={'width':'100%','text-align':'center'}),
                        html.Div([html.Div([dcc.Graph(id='bar-sales')],style={'width':'50%'}),
                        html.Div([dcc.Graph(id='choropleth-sales')],style={'width':'50%'})],style={'display':'flex'})
                        ])

    return layout

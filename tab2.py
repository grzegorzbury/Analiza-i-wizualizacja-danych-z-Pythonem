# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:16:55 2023

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

    grouped = df[df['total_amt']>0].groupby('prod_cat')['total_amt'].sum()
    fig = go.Figure(data=[go.Pie(labels=grouped.index,values=grouped.values)],layout=go.Layout(title='Udział grup produktów w sprzedaży'))

    layout = html.Div([html.H1('Produkty',style={'text-align':'center'}),

                        html.Div([html.Div([dcc.Graph(id='pie-prod-cat',figure=fig)],style={'width':'50%'}),
                        html.Div([dcc.Dropdown(id='prod_dropdown',
                                    options=[{'label':prod_cat,'value':prod_cat} for prod_cat in df['prod_cat'].unique()],
                                    value=df['prod_cat'].unique()[0]),
                                    dcc.Graph(id='barh-prod-subcat')],style={'width':'50%'})],style={'display':'flex'}),
                                    html.Div(id='temp-out')
                        ])

    return layout
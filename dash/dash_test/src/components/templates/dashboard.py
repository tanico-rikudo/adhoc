
import dash
from dash import html
from dash import dcc
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import date

from ..organisms.content_header import content_header
from dash_builder import  logger
from ..data.btc import BTC

class Dashboard():
    def __init__(self, dash_app):
        self.dash_app = dash_app
        self.btc = BTC(dash_app)
        self.register_callbacks()

    def dashboard(self):
        self.btc.load_data()
        layout = html.Div([
            content_header(head_string="Dashboard"),
            html.Br(),
            self.table_component()
            ])
        return layout
    
    
    def register_callbacks(self):
    
        @self.dash_app.callback(
        Output('output-container-date-picker-range', 'children'),
        Input('my-date-picker-range', 'start_date'),
        Input('my-date-picker-range', 'end_date'))
        def update_output(start_date, end_date):
            string_prefix = 'You have selected: '
            if start_date is not None:
                start_date_object = date.fromisoformat(start_date)
                start_date_string = start_date_object.strftime('%B %d, %Y')
                string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '
            if end_date is not None:
                end_date_object = date.fromisoformat(end_date)
                end_date_string = end_date_object.strftime('%B %d, %Y')
                string_prefix = string_prefix + 'End Date: ' + end_date_string
            if len(string_prefix) == len('You have selected: '):
                return 'Select a date to see it displayed here'
            else:
                return string_prefix

    def table_component(self):
        component =  html.Div(
            [
                # Input
                dbc.CardBody([
                    
                    html.Div(
                            dcc.Dropdown(
                                id='symbol_drop_down',
                                options=["BTC","ETH","LTC","XRP","BCH","EOS","TRX","ETC","LINK","XLM","ADA","XMR","DASH","ZEC","XTZ","BNB","ATOM","ONT","IOTA","VET","NEO","QTUM","ZRX","OMG","BAT","LSK","NANO","ICX","WAVES","REP","NMR","BAL","CRV","YFI","UNI","AAVE","SNX","MKR","COMP","KNC","BNT","SUSHI","REN","LRC","GRT","1INCH","BAND","OCEAN"],
                                multi=True,
                                placeholder='Select symbol',
                                ),    
                            style={'width': '15%', 'display': 'inline-block',
                                    'margin-right': 10}
                            ),
                    html.Div(
                            dcc.Dropdown(id='side_drop_down',
                                        options=["BUY","SELL"],
                                        multi=False,
                                        placeholder='Select side',
                                        ),  
                            style={'width': '15%', 'display': 'inline-block',
                                    'margin-right': 10}
                            ),
                    html.Div(
                            dcc.DatePickerRange(
                                id='my-date-picker-range',
                                min_date_allowed=date(1995, 8, 5),
                                max_date_allowed=date(2034, 9, 19),
                                initial_visible_month=date(2017, 8, 5),
                                end_date=date(2017, 8, 25),
                            ),    
                            style={'width': '30%', 'display': 'inline-block',
                                    'margin-right': 10}
                            ),
                ]),
                html.Div(id='output-container-date-picker-range'),
                html.Div([
                    # output
                    dcc.Loading(id="ls-loading-1", children=[
                        html.Div(id='trade_table',
                                children=[],
                                style={'width': '50%', 'display': 'inline-block',
                                    'margin-right': 10}),]),
                    # output
                    dcc.Loading(children=[
                        dcc.Graph(id="trade_line_chart",
                            figure=[],
                            className='bg-dark',)],
                        type="default"),
                                
                ]
                )
        ]
        )
        return component

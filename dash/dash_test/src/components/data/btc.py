
import copy
import logging
import pandas as pd
import plotly.graph_objects as go
import dash as dcc
from dash import Dash, html, dcc, Input, Output
import dash_ag_grid as dag
from dash_builder import logger

# class DashboardInterface():
#     def __init__(self, selector_id, selector_value_name, ag_table_id, ag_table_value_name, line_chart_id, line_chart_value_name):
#         selector_id =  selector_id
#         selector_value_name =  selector_value_name
#         ag_table_id = ag_table_id 
#         ag_table_value_name = ag_table_value_name
#         line_chart_id = line_chart_id 
#         line_chart_value_name = line_chart_value_name
    

class BTC:
    
    def __init__(self, dash_app):
        self.df = None
        self.dash_app = dash_app
        logger.info(f"{type(dash_app)}")
        self.register_callbacks()
        
    
    def load_data(self):
        self.df = pd.read_csv('/app/data/20240229_BTC.csv.gz')
        logger.info("Load data")
        

    def display_ag_table(self, ddf):
        
        columnDefs = [
            {
                    "headerName": "Symbol",
                    "field": "symbol",
                    "filter": True,
            },
            {
                    "headerName": "Side",
                    "field": "side",
                    "filter": True,
            },
            {
                    "headerName": "Size",
                    "field": "size",
                    "filter": True,
            },
            {
                    "headerName": "Time",
                    "field": "timestamp",
                    "filter": True,
            }
        ]
        
        defaultColDef = {
            "filter": "agNumberColumnFilter",
            "resizable": True,
            "sortable": True,
            "editable": False,
            "floatingFilter": True,
        }
        
        table = dag.AgGrid(
            id="portfolio-grid",
            className="ag-theme-alpine-dark",
            style={"width": "100%"},
            columnDefs=columnDefs,
            rowData=ddf.to_dict("records"),
            columnSize="autoSize",
            defaultColDef=defaultColDef,
            dashGridOptions={"undoRedoCellEditing": True, 
                            "rowSelection": "single",
                            "rowHeight": 20,},
        )
        return table
    
    
    def display_figure(self, ddf):
        fig_line = go.Figure(
            data=go.Scatter(
                x=ddf['timestamp'],
                y=ddf['price'],
                name='Trajectory',
                line=dict(color='firebrick', width=4)
            )
        )
        fig_line.update_layout(
            title=dict(text='<b>Time Series of Stock Prices',
                        font=dict(size=26)),
            template='plotly_dark',
            legend=dict(xanchor='left',
                        yanchor='bottom',
                        x=0.02,
                        y=0.9,
                        orientation='h',
                        borderwidth=1)
        )
        return fig_line
    
    def register_callbacks(self):
        @self.dash_app.callback(
            Output("trade_table","children"),
            Output("trade_line_chart","figure"),
            Input("side_drop_down","value"))
        def update_dashboad_objects(side=None):
            logger.info(f"Update dashboard objects:{self.df.head()}")
            if side is None:
                dff = copy.copy(self.df)
            else:
                dff = self.df[self.df['side'] == side]
            ag_table =  self.display_ag_table(dff)
            line_chart =  self.display_figure(dff)
            return ag_table, line_chart
        
        
        
        logger.info(f"Registered")

    

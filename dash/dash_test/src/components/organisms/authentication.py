
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
from flask import Flask, redirect, url_for,request
from dash_builder import  logger
from flask_login import current_user

# sampl;e users
users = {'test': {'password': 'test'}}

class User(UserMixin):
    def __init__(self,user_id):
        self.id = user_id
        self.password = None

# https://dev.to/naderelshehabi/securing-plotly-dash-using-flask-login-4ia2
class Authentication():
    def __init__(self, dash_app, dash_login_manager):
        self.dash_app = dash_app
        self.dash_login_manager = dash_login_manager
        # logger.info(f"{type(dash_app)}")
        self.register_user_loader()
        self.register_callbacks()
    
    def register_user_loader(self):
        @self.dash_login_manager.user_loader
        def load_user(user_id):
            return User(user_id)
        
    def register_callbacks(self):
        @self.dash_app.callback(
            [Output('url_login', 'pathname'),
             Output('output-state', 'children')],
            [Input('login-button', 'n_clicks')],
            [State('username', 'value'),
             State('password', 'value')])
        def login(n_clicks, username, password):
            if n_clicks > 0:
                if current_user.is_authenticated:
                    return '/success', ''
                else:
                    if username == 'test' and password == 'test':
                        user = User(username)
                        login_user(user)
                        return '/success', ''
                    else:
                        return '/login', 'Incorrect username or password'

            return dash.no_update, dash.no_update 
                
        @self.dash_app.callback(
            Output('user-status-link', 'href'),
            Output('user-status-message', 'children'),
            Output('login-status', 'data'), 
            [Input('url', 'pathname')])
        def login_status(url):
            ''' callback to display login/logout link in the header '''
            if hasattr(current_user, 'is_authenticated') and current_user.is_authenticated \
                    and url != '/logout':  # If the URL is /logout, then the user is about to be logged out anyways
                return '/logout', current_user.get_id() , current_user.get_id()
            else:
                return '/login', 'Log in','loggedout'
        

    def login_view(self):
        
        login = dbc.Container([
            dcc.Location(id='url_login', refresh=True),
            dbc.Row([
                dbc.Col([
                    html.H2('''Please log in to continue:''', id='h1'),
                    dbc.Input(placeholder='Enter your username', type='text', id='username'),
                    dbc.Input(placeholder='Enter your password', type='password', id='password'),
                    dbc.Button('Login', id='login-button', type="submit", color="primary", className="mr-2", n_clicks=0),
                    html.Div(children='', id='output-state'),
                    html.Br(),
                ])
            ])
        ])
        return login

    def logout_view(self):
        logout = dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2('You have been logged out - Please login'),
                    html.Br(),
                    dcc.Link('Home', href='/')
                ])
            ])
        ])
        return logout

    def success_view(self):
        success = dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2('Login successful.'),
                    html.Br(),
                ])
            ])
        ])
        return success

    def failed_view(self):
        failed = dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H2('Log in Failed. Please try again.'),
                    html.Br(),
                    self.login_view(),
                    dcc.Link('Home', href='/')
                ])
            ])
        ])
        return failed
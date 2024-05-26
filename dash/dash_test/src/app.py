import os
import dash
from dotenv import load_dotenv
from dash import dcc
from dash import Input
from dash import Output
from dash import html
from flask_login import current_user
import dash_bootstrap_components as dbc
from flask_login import logout_user
from dash_builder import dash_app, logger, server, login_manager
from utils.config import ConfigManager
from components.templates import base_layout
from components.templates.dashboard import Dashboard
from components.templates.about import About
from components.data.btc import BTC
from components.organisms.authentication import Authentication

# Load configuration
load_dotenv(".env.development")
PORT = os.environ.get("PORT")
DEBUG = os.environ.get("DEBUG")
MULTITHREADING = bool(os.environ.get("MULTITHREADING"))
RELOAD_MODE = bool(os.environ.get("RELOAD_MODE"))

config_manager = ConfigManager()
config_manager.read_config()
config = config_manager.get_config()
logger.info(f"==============")
logger.info(f"debug: {DEBUG}")
logger.info(f"port: {PORT}")
logger.info(f"multithreading: {MULTITHREADING}")
logger.info(f"use_reloader: {RELOAD_MODE}")
logger.info(f"==============")



logger.info(f"Init layout...")



# Layout
dash_app.layout = base_layout.layout()

# Autehntication
global authentication_obj
authentication_obj= Authentication(dash_app, login_manager)

# init templates
global dashboard_obj
dashboard_obj = Dashboard(dash_app)

global about_obj
about_obj = About()

@dash_app.callback(Output("page-content", "children"), 
                   [Input("url", "pathname")])
def render_page_content(pathname):
    logger.info(f"pathname: {pathname}")
    if pathname == "/":
        if current_user.is_authenticated:
            logger.info(f"current_user: {current_user}")
            return dashboard_obj.dashboard()
        else:
            logger.info(f"go to login")
            return authentication_obj.login_view()
    elif pathname == '/success':
        if current_user.is_authenticated:
            logger.info(f"current_user: {current_user}")
            return authentication_obj.success_view()
        else:
            logger.info("failed to login")  
            return failed
    elif pathname == '/logout':
        if current_user.is_authenticated:
            logger.info(f"current_user: {current_user}. logging out... ")
            logout_user()
            return authentication_obj.logout_view()
        else:
            logger.info("failed to logout. login first.")
            return authentication_obj.login_view()
    elif pathname == '/login':
        logger.info("login view")  
        return authentication_obj.login_view()
    elif pathname == "/about":
        logger.info("about view")   
        return about_obj.about()

    return dbc.Container(
        children=[
            html.H1(
                "404 Error: Page Not found",
                style={"textAlign": "center", "color": "#082446"},
            ),
            html.Br(),
            html.P(
                f"Oh no! The pathname '{pathname}' was not recognised...",
                style={"textAlign": "center"},
            ),
            # image
            html.Div(
                style={"display": "flex", "justifyContent": "center"},
                children=[
                    html.Img(
                        src="https://elephant.art/wp-content/uploads/2020/02/gu_announcement_01-1.jpg",
                        alt="hokie",
                        style={"width": "400px"},
                    ),
                ],
            ),
        ]
    )
logger.info(f"DONE setup ...")


if __name__ == '__main__':
    try:
        # Ignite the app
        dash_app.run_server(debug=DEBUG,
                        port=PORT,
                        threaded=MULTITHREADING,
                        use_reloader=RELOAD_MODE)

    except Exception as e:
        logger.exception(e)
        
        
# https://plotly.com/examples/generative-ai-chatgpt/
# https://qiita.com/Yusuke_Pipipi/items/b74f269d112f180d2131

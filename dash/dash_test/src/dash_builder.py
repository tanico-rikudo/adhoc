

import logging
import dash
import dash_bootstrap_components as dbc
from flask import Flask
from flask_login import LoginManager
from flask.logging import default_handler


# Init app
server = Flask(__name__)
dash_app = dash.Dash(
    __name__,
    server=server,
    pages_folder=False,    # turn on Dash pages
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME,
        dbc.themes.DARKLY
    ],  # fetch the proper css items we want
    meta_tags=[
        {   # check if device is a mobile device. This is a must if you do any mobile styling
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1'
        }
    ],
    suppress_callback_exceptions=True,
    title='Dash Board Preview'
)

# Register configs


# Init logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('../log/app.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.removeHandler(default_handler)

logger.info(f"Init server...")

# Deligate
server = dash_app.server
server.config['SECRET_KEY'] = 'supersecret'

# Init authentication
login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = '/login'


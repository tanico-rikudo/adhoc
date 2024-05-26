import dash
from dash import html
from dash import dcc
from components.organisms import sidebar

CONTENT_STYLE = {
    "transition": "margin-left .1s",
    "padding": "1rem 1rem",
}

theme = {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}

def layout():
    base_layout = html.Div(
        id='dark-theme-components',
        className="dash-bootstrap",
        children=[
            dcc.Location(id='url', refresh=False),
            # dcc.Location(id='redirect', refresh=True),
            dcc.Store(id='login-status', storage_type='session'),
            sidebar.sidebar(),
            html.Div([
                dash.page_container,
                ],
            className="content",
            style=CONTENT_STYLE,
            id="page-content")
        ])
    
    return base_layout
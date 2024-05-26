import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
# from components.authentication import login_info


def sidebar():
    sidebar = html.Div(
        [
            html.Div(
                [
                    html.H2("Test BTC", style={"color": "white"}),
                ],
                className="sidebar-header",
            ),
            html.Br(),
            html.Div(style={"border-top": "2px solid white"}),
            html.Br(),
            # nav component
            dbc.Nav(
                [
                    dbc.NavLink(
                        [
                            html.I(className="fas fa-solid fa-star me-2"),
                            html.Span("Overview"),
                        ],
                        href="/",
                        active="exact",
                    ),
                    dbc.NavLink(
                        [
                            html.I(className="fas fa-home me-2"),
                            html.Span("Apartments Listing"),
                        ],
                        href="/listing",
                        active="exact",
                    ),
                    dbc.NavLink(
                        [
                            html.I(className="fas fa-solid fa-code me-2"),
                            html.Span("About"),
                        ],
                        href="/about",
                        active="exact",
                    ),
                    dbc.NavLink(
                        [
                            html.I(className="fas fa-solid fa-gear me-2"),
                            html.Span(id='user-status-message'),
                        ],
                        id='user-status-link',
                        href="",
                        active="exact",
                    ),
                ],
                vertical=True,
                pills=True,
            ),
        ],
        className="sidebar",
    )
    return sidebar

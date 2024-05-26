import requests
import dash
from dash import html
from dash import Input
from dash import Output
from dash import dcc
import dash_bootstrap_components as dbc
from ..organisms.content_header import content_header

class About():
    def __init__(self):
        pass
    
    def get_profile_img(self):
        # GitHubからプロフィール画像のURLを取得
        github_api_url = 'https://api.github.com/users/tanico-rikudo'
        response = requests.get(github_api_url)
        github_data = response.json()
        profile_image_url = github_data['avatar_url']
        return profile_image_url
    
    def about(self):
        layout = html.Div([
            content_header(head_string="About"),
            html.Br(),
            self.my_card()
            ])
        return layout
        
    def my_card(self):
        card = dbc.Card(
            [
                dbc.CardImg(src=self.get_profile_img(), 
                            top=True,
                            style={'width': '150px', 'height': '150px',"display": "inline-block", "margin-left": "auto", "margin-right": "auto"}),
                dbc.CardBody([
                    html.H5("Name:", className="card-title"),
                    html.P("otakazuy", className="card-text"),
                    html.H5("Web Page:", className="card-title"),
                    html.A("https://tanico-kazuyo.net/", href="https://tanico-kazuyo.net/", className="card-link"),
                    html.H5("GitHub:", className="card-title"),
                    html.A("https://github.com/tanico-rikudo", href="https://github.com/tanico-rikudo", className="card-link"),
                ])
            ],
            className="mb-3"
        )
        
        return card
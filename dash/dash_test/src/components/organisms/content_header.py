

from dash import html            

def content_header(head_string):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src="https://images.unsplash.com/photo-1557683316-973673baf926?q=80&w=1129&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                        style={
                            "width": "100%",
                            "height": "auto",
                            "position": "relative",
                        },
                    ),
                ],
                style={
                    "height": "50px",
                    "overflow": "hidden",
                    "position": "relative",
                },
            ),
            html.H1(
                head_string,
                style={
                    "position": "absolute",
                    "top": "0%",
                    "left": "0%",
                    "color": "white",
                    "text-align": "center",
                    "width": "100%",
                },
            ),
        ],
        style={
            "position": "relative",
            "text-align": "center",
            "color": "white",
        },
    )
    
    return header
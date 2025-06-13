from dash import html, dcc

def v6_layout():
    return html.Div([
        html.H2("Visualization 6: Playlist Genre vs Average Popularity"),

        dcc.Graph(id='v6-bar-graph')
    ])

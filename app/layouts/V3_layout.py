from dash import html, dcc

GENRES = ['pop', 'rap', 'r&b', 'rock', 'latin', 'edm']

def v3_layout():
    return html.Div([
        html.H2("Visualization 3: Radar Chart - Audio Profiles by Genre"),

        html.Label("Select Genres:"),
        dcc.Dropdown(
            id='v3-genre-dropdown',
            options=[{'label': genre.capitalize(), 'value': genre} for genre in GENRES],
            value=GENRES,
            multi=True
        ),

        dcc.Graph(id='v3-radar-graph')
    ])

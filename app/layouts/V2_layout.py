from dash import html, dcc

# Same genres as before
GENRES = ['pop', 'rap', 'r&b', 'rock', 'latin', 'edm']

def v2_layout():
    return html.Div([
        html.H2("Visualization 2: Stacked Area Chart (Genre Diversity Over Time)"),

        html.Label("Select Genres:"),
        dcc.Dropdown(
            id='v2-genre-dropdown',
            options=[{'label': genre.capitalize(), 'value': genre} for genre in GENRES],
            value=GENRES,
            multi=True
        ),

        dcc.Graph(id='v2-stacked-area-graph')
    ])

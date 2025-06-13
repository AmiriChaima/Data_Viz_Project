from dash import html, dcc
import pandas as pd

# Audio features we allow the user to select
AUDIO_FEATURES = [
    'track_popularity',
    'energy',
    'danceability',
    'valence',
    'instrumentalness',
    'acousticness',
    'loudness',
    'tempo',
    'duration_ms',
    'speechiness'
]

# Genres — You can dynamically load them if you want, but for now we hard-code
GENRES = ['pop', 'rap', 'r&b', 'rock', 'latin', 'edm']

def v1_layout():
    return html.Div([
        html.H2("Visualization 1: Time Series by Feature and Genre"),

        html.Label("Select Feature:"),
        dcc.Dropdown(
            id='v1-feature-dropdown',
            options=[{'label': feat.capitalize(), 'value': feat} for feat in AUDIO_FEATURES],
            value='track_popularity'
        ),

        html.Label("Select Genres:"),
        dcc.Dropdown(
            id='v1-genre-dropdown',
            options=[{'label': genre.capitalize(), 'value': genre} for genre in GENRES],
            value=GENRES,
            multi=True
        ),

        dcc.Graph(id='v1-timeseries-graph')
    ])

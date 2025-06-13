from dash import html, dcc
def v5_layout():
    return html.Div([
        html.H2("Visualization 5: Violin Plots - Popularity vs Audio Features"),

        dcc.Graph(id='v5-violin-graph')
    ])
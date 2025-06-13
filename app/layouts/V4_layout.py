from dash import html, dcc

def v4_layout():
    return html.Div([
        html.H2("Visualization 4: Scatter Plot (Energy vs Valence)"),

        dcc.Graph(id='v4-scatter-graph')
    ])

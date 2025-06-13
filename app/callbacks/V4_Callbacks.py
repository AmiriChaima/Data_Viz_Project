from dash import Output, Input
import plotly.express as px

def register_v4_callbacks(app, scatter_df):

    @app.callback(
        Output('v4-scatter-graph', 'figure'),
        Input('v4-scatter-graph', 'id')  # dummy input just to trigger initial render
    )
    def update_v4_scatter(_):
        fig = px.scatter(
            scatter_df,
            x='energy',
            y='valence',
            size='danceability',
            color='track_popularity',
            hover_data=['track_name', 'track_artist'],
            color_continuous_scale='Viridis',
            size_max=20
        )

        fig.update_layout(
            title="Energy vs Valence (Color: Popularity, Size: Danceability)",
            xaxis_title="Energy",
            yaxis_title="Valence",
            template="plotly_white"
        )

        return fig

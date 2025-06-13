from dash import Output, Input
import plotly.express as px

def register_v6_callbacks(app, bar_df):

    @app.callback(
        Output('v6-bar-graph', 'figure'),
        Input('v6-bar-graph', 'id')
    )
    def update_v6_bar(_):

        fig = px.bar(
            bar_df,
            x='playlist_genre',
            y='avg_popularity',
            color='playlist_genre',
            text=bar_df['avg_popularity'].round(1),
            title='Average Popularity by Playlist Genre'
        )

        fig.update_layout(
            xaxis_title="Playlist Genre",
            yaxis_title="Average Popularity",
            template="plotly_white",
            showlegend=False
        )

        return fig

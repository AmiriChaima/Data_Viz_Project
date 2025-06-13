from dash import Input, Output
import plotly.express as px

def register_v2_callbacks(app, count_df):
    
    @app.callback(
        Output('v2-stacked-area-graph', 'figure'),
        Input('v2-genre-dropdown', 'value')
    )
    def update_v2_area(selected_genres):
        filtered_df = count_df[count_df['playlist_genre'].isin(selected_genres)]

        fig = px.area(
            filtered_df,
            x='release_year',
            y='song_count',
            color='playlist_genre',
            groupnorm='',
            markers=False
        )

        fig.update_layout(
            title="Genre Diversity Over Time",
            xaxis_title="Year",
            yaxis_title="Number of Songs",
            template="plotly_white"
        )

        return fig

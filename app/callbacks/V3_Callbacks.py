from dash import Input, Output
import plotly.graph_objects as go

def register_v3_callbacks(app, radar_df):
    
    @app.callback(
        Output('v3-radar-graph', 'figure'),
        Input('v3-genre-dropdown', 'value')
    )
    def update_v3_radar(selected_genres):
        features = ['danceability', 'energy', 'valence', 'acousticness', 'speechiness']

        fig = go.Figure()

        for genre in selected_genres:
            genre_data = radar_df[radar_df['playlist_genre'] == genre].iloc[0]
            values = [genre_data[feature] for feature in features]
            # Close the radar loop
            values += [values[0]]

            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=features + [features[0]],
                fill='toself',
                name=genre.capitalize()
            ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 1])
            ),
            showlegend=True,
            title="Audio Feature Profiles by Genre",
            template="plotly_white"
        )

        return fig

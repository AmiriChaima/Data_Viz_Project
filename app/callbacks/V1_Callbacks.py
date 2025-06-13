from dash import Input, Output
import plotly.express as px

def register_v1_callbacks(app, agg_df):
    
    @app.callback(
        Output('v1-timeseries-graph', 'figure'),
        Input('v1-feature-dropdown', 'value'),
        Input('v1-genre-dropdown', 'value')
    )
    def update_v1_timeseries(selected_feature, selected_genres):
        filtered_df = agg_df[agg_df['playlist_genre'].isin(selected_genres)]
        
        fig = px.line(
            filtered_df, 
            x='release_year', 
            y=selected_feature, 
            color='playlist_genre',
            markers=True
        )

        fig.update_layout(
            title=f"Evolution of {selected_feature.capitalize()} Over Time",
            xaxis_title="Year",
            yaxis_title=selected_feature.capitalize(),
            template="plotly_white"
        )

        return fig

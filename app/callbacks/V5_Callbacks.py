from dash import Output, Input
import plotly.subplots as sp
import plotly.graph_objects as go

def register_v5_callbacks(app, violin_df):

    @app.callback(
        Output('v5-violin-graph', 'figure'),
        Input('v5-violin-graph', 'id')
    )
    def update_v5_violin(_):

        # All features & bins
        features_bins = [
            ('danceability_bin', 'Danceability'),
            ('acoustic_bin', 'Acousticness'),
            ('instrumental_bin', 'Instrumentalness'),
            ('mode_bin', 'Mode'),
            ('duration_bin', 'Duration'),
            ('tempo_bin', 'Tempo')
        ]

        rows, cols = 2, 3
        fig = sp.make_subplots(rows=rows, cols=cols, subplot_titles=[f[1] for f in features_bins])

        for i, (bin_col, title) in enumerate(features_bins):
            row = i // cols + 1
            col = i % cols + 1

            # Get sorted categories to keep same order always
            categories = violin_df[bin_col].dropna().unique()
            categories = sorted(categories)

            for group in categories:
                filtered = violin_df[violin_df[bin_col] == group]
                fig.add_trace(go.Violin(
                    y=filtered['track_popularity'],
                    name=str(group),
                    box_visible=True,
                    meanline_visible=True,
                    spanmode='hard',
                    legendgroup=str(group),
                    showlegend=(i == 0)  # Only show legend once globally
                ), row=row, col=col)

        fig.update_layout(
            height=800,
            width=1300,
            template="plotly_white",
            title_text="Popularity vs Audio Features (Violin Distribution)",
            violingap=0.3
        )

        return fig

import dash
from dash import html, dcc, Output, Input
from utils.data_loader import load_spotify_data
from utils.preprocessing import prepare_v1_timeseries, prepare_v2_stacked_area, prepare_v3_radar, prepare_v4_scatter, prepare_v5_violin, prepare_v6_bar
from app.layouts.V1_layout import v1_layout
from app.layouts.V2_layout import v2_layout
from app.layouts.V3_layout import v3_layout
from app.callbacks.V1_Callbacks import register_v1_callbacks
from app.callbacks.V2_Callbacks import register_v2_callbacks
from app.callbacks.V3_Callbacks import register_v3_callbacks
from app.layouts.V4_layout import v4_layout
from app.callbacks.V4_Callbacks import register_v4_callbacks
from app.layouts.V5_layout import v5_layout
from app.callbacks.V5_Callbacks import register_v5_callbacks
from app.layouts.V6_layout import v6_layout
from app.callbacks.V6_callbacks import register_v6_callbacks
# Load & preprocess data
df = load_spotify_data('data/raw/spotify_songs.csv')
agg_df = prepare_v1_timeseries(df)
count_df = prepare_v2_stacked_area(df)
radar_df = prepare_v3_radar(df)
scatter_df = prepare_v4_scatter(df)
violin_df = prepare_v5_violin(df)
bar_df = prepare_v6_bar(df)



# Build app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Spotify Dashboard"

# Tabs for multi-page
app.layout = html.Div([
    html.H1("Spotify Trends Dashboard"),

    dcc.Tabs(id='tabs', value='v1', children=[
        dcc.Tab(label='V1 - Time Series', value='v1'),
        dcc.Tab(label='V2 - Stacked Area', value='v2'),
        dcc.Tab(label='V3 - Radar Chart', value='v3'),
        dcc.Tab(label='V4 - Scatter Plot', value='v4'),
        dcc.Tab(label='V5 - Violin Plot', value='v5'),
        dcc.Tab(label='V6 - Bar Chart', value='v6')
    ]),

    html.Div(id='tab-content')
])

@app.callback(
    Output('tab-content', 'children'),
    Input('tabs', 'value')
)
def render_content(tab):
    if tab == 'v1':
        return v1_layout()
    elif tab == 'v2':
        return v2_layout()
    elif tab == 'v3':
        return v3_layout()
    elif tab == 'v4':
        return v4_layout()
    elif tab == 'v5':
        return v5_layout()
    elif tab == 'v6':
        return v6_layout()


# Register callbacks
register_v1_callbacks(app, agg_df)
register_v2_callbacks(app, count_df)
register_v3_callbacks(app, radar_df)
register_v4_callbacks(app, scatter_df)
register_v5_callbacks(app, violin_df)
register_v6_callbacks(app, bar_df)


if __name__ == '__main__':
    app.run(debug=True)

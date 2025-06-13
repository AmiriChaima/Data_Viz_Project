import pandas as pd
import numpy as np
def prepare_v1_timeseries(df):
    """
    Aggregate data to prepare for time series visualization (V1).
    We compute mean values of audio features per year and genre.
    """
    # Group and aggregate
    agg_df = df.groupby(['release_year', 'playlist_genre']).agg({
        'track_popularity': 'mean',
        'energy': 'mean',
        'danceability': 'mean',
        'valence': 'mean',
        'instrumentalness': 'mean',
        'acousticness': 'mean',
        'loudness': 'mean',
        'tempo': 'mean',
        'duration_ms': 'mean',
        'speechiness': 'mean'
    }).reset_index()

    return agg_df

def prepare_v2_stacked_area(df):
    """
    Prepare data for stacked area chart showing number of songs per genre and year.
    """
    # Group by year and genre, count number of songs
    count_df = df.groupby(['release_year', 'playlist_genre']).size().reset_index(name='song_count')
    
    return count_df

def prepare_v3_radar(df):
    """
    Prepare data for radar chart: average audio features per genre.
    """
    features = ['danceability', 'energy', 'valence', 'acousticness', 'speechiness']

    radar_df = df.groupby('playlist_genre')[features].mean().reset_index()

    return radar_df


def prepare_v4_scatter(df):
    """
    Prepare data for scatter plot: energy vs valence, colored by popularity.
    """
    # We keep only necessary columns for efficiency
    scatter_df = df[['track_name', 'track_artist', 'energy', 'valence', 'track_popularity', 'danceability']].dropna()

    return scatter_df

def prepare_v5_violin(df):
    """
    Prepare data for violin plots: binning audio features.
    """

    df = df.copy()

    # Danceability bins
    df['danceability_bin'] = pd.cut(df['danceability'], 
                                     bins=[0, 0.4, 0.7, 1], 
                                     labels=['Low', 'Medium', 'High'])

    # Acousticness binary
    df['acoustic_bin'] = np.where(df['acousticness'] > 0.5, 'Acoustic', 'Non-Acoustic')

    # Instrumentalness binary
    df['instrumental_bin'] = np.where(df['instrumentalness'] > 0.5, 'Instrumental', 'Non-Instrumental')

    # Mode binary
    df['mode_bin'] = np.where(df['mode'] == 1, 'Major', 'Minor')

    # Duration bins (convert ms to min)
    df['duration_min'] = df['duration_ms'] / 60000
    df['duration_bin'] = pd.cut(df['duration_min'], 
                                 bins=[0, 3, 4, 20], 
                                 labels=['Short (<3min)', 'Medium (3-4min)', 'Long (>4min)'])

    # Tempo bins
    df['tempo_bin'] = pd.cut(df['tempo'], 
                              bins=[0, 90, 120, 300], 
                              labels=['Slow (<90 BPM)', 'Medium (90-120 BPM)', 'Fast (>120 BPM)'])

    return df

def prepare_v6_bar(df):
    """
    Prepare data for bar chart: average popularity per playlist genre.
    """
    bar_df = df.groupby('playlist_genre')['track_popularity'].mean().reset_index()
    bar_df.rename(columns={'track_popularity': 'avg_popularity'}, inplace=True)

    return bar_df

import pandas as pd

def load_spotify_data(filepath):
    """
    Load the Spotify dataset from CSV and do initial processing.
    """
    df = pd.read_csv(filepath)

    # Handle release date parsing
    df['track_album_release_date'] = pd.to_datetime(df['track_album_release_date'], errors='coerce')
    df['release_year'] = df['track_album_release_date'].dt.year

    # Filter out rows with no release year if needed
    df = df[df['release_year'].notnull()]

    return df

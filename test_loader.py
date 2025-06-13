## Test script for loading Spotify dataset

# from utils.data_loader import load_spotify_data

# # Load dataset
# df = load_spotify_data('data/raw/spotify_songs.csv')

# # Display basic info
# print(df.head())
# print(df.info())


# Test script for loading and preparing Spotify dataset for V1 visualization

from utils.data_loader import load_spotify_data
from utils.preprocessing import prepare_v1_timeseries

# Load data
df = load_spotify_data('data/raw/spotify_songs.csv')

# Prepare for V1
agg_df = prepare_v1_timeseries(df)

# Check output
print(agg_df.head())




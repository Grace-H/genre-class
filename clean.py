# Script to clean music genre dataset
#
# date: 17 February 2023

import pandas as pd
import numpy as np

# Create dataframe
df = pd.read_csv('uncleaned_data.csv')

# Drop columns & rows with NaNs
to_drop = ['key',
           'instrumentalness']
df.drop(to_drop, inplace=True, axis=1)
df = df.dropna(axis='index')

# Grab rows with correct genres
acoustic_folk = df.loc[df["Class"] == 0] # Acoustic/Folk
alt = df.loc[df["Class"] == 1]
blues = df.loc[df["Class"] == 2]
bollywood = df.loc[df["Class"] == 3]
country = df.loc[df["Class"] == 4]
hiphop = df.loc[df["Class"] == 5]
indie_alt = df.loc[df["Class"] == 6]
instrumental = df.loc[df["Class"] == 7]
metal = df.loc[df["Class"] == 8]
pop = df.loc[df["Class"] == 9]
rock = df.loc[df["Class"] == 10]

dfs = [blues, hiphop, metal]
df = pd.concat(dfs)

# Drop rows with duplicate songs
df.drop_duplicates(subset=["Artist Name", "Track Name"], inplace=True)

df.to_csv(path_or_buf="music.csv")

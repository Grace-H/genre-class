import pandas as pd
import numpy as np

# Create dataframe
df = pd.read_csv('train.csv')

# Drop columns
to_drop = ['key',
           'instrumentalness']
df.drop(to_drop, inplace=True, axis=1)

# Grab rows with correct genres
five = df.loc[df["Class"] == 5]
six = df.loc[df["Class"] == 6]
eight = df.loc[df["Class"] == 8]
nine = df.loc[df["Class"] == 9]
ten = df.loc[df["Class"] == 10]

dfs = [five, six, eight, nine, ten]
df = pd.concat(dfs)

# Drop rows with duplicate songs
df.drop_duplicates(subset=["Artist Name", "Track Name"], inplace=True)

df.to_csv(path_or_buf="music.csv")

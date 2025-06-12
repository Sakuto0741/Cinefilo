import numpy as np
import pandas as pd
 
df = pd.read_csv('data/archive/movie_metadata.csv')

print(df.head())
print(df.info())
print(df.describe())
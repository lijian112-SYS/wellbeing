import pandas as pd
df = pd.read_csv('data/derived_constructs.csv')
corr = df.corr()
corr.to_csv('results/tables/correlation_matrix.csv')

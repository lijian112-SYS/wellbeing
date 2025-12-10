import pandas as pd
df = pd.read_csv('data/derived_constructs.csv')
df.describe().to_csv('results/tables/descriptive_stats.csv')

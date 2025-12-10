import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('data/derived_constructs.csv')
X = df[['Identity_Construction','Validation','Comparison','Daily_Usage_Time','Age']]
X = sm.add_constant(X)
y = df['Wellbeing_Score']

model = sm.OLS(y, X, missing='drop').fit()
with open('results/tables/regression_results.txt','w') as f:
    f.write(model.summary().as_text())

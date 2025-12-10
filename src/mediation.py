import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('data/derived_constructs.csv')

def reg(y, X_cols):
    X = sm.add_constant(df[X_cols])
    return sm.OLS(df[y], X, missing='drop').fit()

a = reg('Comparison',['Identity_Construction','Daily_Usage_Time','Age'])
b = reg('Wellbeing_Score',['Identity_Construction','Comparison','Daily_Usage_Time','Age'])
a2 = reg('Validation',['Identity_Construction','Daily_Usage_Time','Age'])
b2 = reg('Wellbeing_Score',['Identity_Construction','Validation','Daily_Usage_Time','Age'])

with open('results/tables/mediation_results.txt','w') as f:
    f.write(a.summary().as_text()+"
"+b.summary().as_text()+"
"+a2.summary().as_text()+"
"+b2.summary().as_text())

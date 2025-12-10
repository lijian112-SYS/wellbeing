import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('data/derived_constructs.csv')

def std_coef(y,X_cols):
    X = sm.add_constant(df[X_cols])
    return sm.OLS(df[y], X, missing='drop').fit().params

coef = {
'Identity->Validation': std_coef('Validation',['Identity_Construction','Daily_Usage_Time','Age']),
'Validation->Wellbeing': std_coef('Wellbeing_Score',['Identity_Construction','Validation','Daily_Usage_Time','Age'])
}

import json
with open('results/tables/sem_coeff.json','w') as f:
    f.write(json.dumps({k:v.tolist() if hasattr(v,'tolist') else float(v) for k,v in coef.items()}))

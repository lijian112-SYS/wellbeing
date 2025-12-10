import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('data/derived_constructs.csv')

df['Age_centered'] = df['Age'] - df['Age'].mean()
df['ICxAge'] = df['Identity_Construction'] * df['Age_centered']

X_age = sm.add_constant(df[['Identity_Construction','Age_centered','ICxAge']])
mod_age = sm.OLS(df['Wellbeing_Score'], X_age, missing='drop').fit()

df['Gender_binary'] = (df['Gender']=='Female').astype(int)
df['ICxGender'] = df['Identity_Construction'] * df['Gender_binary']

X_gender = sm.add_constant(df[['Identity_Construction','Gender_binary','ICxGender']])
mod_gender = sm.OLS(df['Wellbeing_Score'], X_gender, missing='drop').fit()

with open('results/tables/moderation.txt','w') as f:
    f.write(mod_age.summary().as_text()+"
"+mod_gender.summary().as_text())

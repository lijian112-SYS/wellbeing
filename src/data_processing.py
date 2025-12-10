import pandas as pd
import numpy as np

def load_and_clean():
    df_train = pd.read_csv('data/train_cleaned.csv')
    df_test = pd.read_csv('data/test_cleaned.csv')
    df_val = pd.read_csv('data/val_cleaned.csv')
    df = pd.concat([df_train, df_test, df_val], ignore_index=True)
    df = df[pd.to_numeric(df['Age'], errors='coerce').notnull()]
    df['Age'] = df['Age'].astype(int)
    df = df[df['Gender'].isin(['Male','Female','Non-binary'])]
    if 'Daily_Usage_Time (minutes)' in df.columns:
        df.rename(columns={'Daily_Usage_Time (minutes)':'Daily_Usage_Time'}, inplace=True)
    num_cols = ['Daily_Usage_Time','Posts_Per_Day','Likes_Received_Per_Day','Comments_Received_Per_Day','Messages_Sent_Per_Day']
    for col in num_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df.to_csv('data/merged_cleaned.csv', index=False)

if __name__=='__main__':
    load_and_clean()

import pandas as pd
import numpy as np

df = pd.read_csv('data/merged_cleaned.csv')

df['Identity_Construction'] = df['Posts_Per_Day'] + df['Messages_Sent_Per_Day']
df['Validation'] = df['Likes_Received_Per_Day'] + df['Comments_Received_Per_Day']
df['Comparison'] = df['Likes_Received_Per_Day'] / df['Posts_Per_Day'].replace(0, np.nan)

emotion_map = {'Happiness':1,'Neutral':0,'Boredom':0,'Anger':-1,'Sadness':-1,'Anxiety':-1}
df['Wellbeing_Score'] = df['Dominant_Emotion'].map(emotion_map)

df.to_csv('data/derived_constructs.csv', index=False)

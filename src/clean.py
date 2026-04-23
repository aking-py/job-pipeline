import pandas as pd 
import numpy as np 

df = pd.read_csv("raw/postings.csv")

df.head(10)

print(df.shape)
print(df.columns)
print(df.isnull().sum())

df = df [['title', 'company_name', 'location', 'formatted_work_type', 'remote_allowed', 'formatted_experience_level', 'min_salary', 'max_salary', 'normalized_salary', 'views', 'applies', 'listed_time']]
print(df.shape)
df.dtypes

df = df.fillna(0).astype({'min_salary':'int','max_salary':'int','normalized_salary':'int','views':'int','applies':'int'})

df['listed_time'] = pd.to_datetime(df['listed_time'], unit = 'ms')
df['listed_time']

print(sum(df.duplicated()))
df = df.drop_duplicates()
df.shape

df

df['company_name'] = df['company_name'].replace(0,'Unknown')
df['location'] = df['location'].replace(0,'Unknown')
df['formatted_experience_level'] = df['formatted_experience_level'].replace(0,'Unknown')
df['remote_allowed'] = df['remote_allowed'].astype('bool')
df["remote_allowed"].dtype

df.head(10)
print(df.shape)
print(df.dtypes)
df.head()

df.to_csv("processed/cleaned_postings.csv", index=False)                
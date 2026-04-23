import pandas as pd
import numpy as np 

df = pd.read_csv("processed/cleaned_postings.csv")
print(df['title'].value_counts().head(10))
print(df["location"].value_counts().head(10))
print("Average salary =", np.mean(df['normalized_salary']))
print("Median salary =", np.median(df['normalized_salary']))
print("Highest salary =", np.max(df['normalized_salary']))
print("Lowest salary =", np.min(df['normalized_salary']))
df_salaries = df[(df['normalized_salary'] > 20000) & (df['normalized_salary'] < 200000)] 
print(df_salaries.shape)
print((df['normalized_salary'] == 0).sum())
print("Average salary =", np.mean(df_salaries["normalized_salary"]))
print("Median salary =", np.median(df_salaries["normalized_salary"]))
print("Highest salary =", np.max(df_salaries["normalized_salary"]))
print("Lowest salary =", np.min(df_salaries["normalized_salary"]))
print(df.columns)
print(df["remote_allowed"].value_counts())
filtered_df = df[df["company_name"] != "Unknown"]
print(filtered_df["company_name"].value_counts().head(10))
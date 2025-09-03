"""
From people.csv, select all rows where:

Age > 25, AND

City = "Chicago".
"""
import pandas as pd

df = pd.read_csv('C:\\Users\\JIYA\\Downloads\\people_with_duplicates.csv')
print("Original DataFrame:")
print(df)
filtered_df = df[(df['Age'] > 25) & (df['City'] == 'Chicago')]
print(filtered_df)  
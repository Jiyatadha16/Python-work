"""
Create a DataFrame with some duplicate rows.

Drop duplicates and keep only unique rows.
"""
import pandas as pd
df=pd.read_csv('C:\\Users\\JIYA\\Downloads\\people_with_duplicates.csv')
print("Original DataFrame with duplicates:")
print(df)

df_unique = df.drop_duplicates()
print("\nDataFrame after dropping duplicates:") 
print(df_unique)
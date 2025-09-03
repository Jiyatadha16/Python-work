"""
Load the famous Iris dataset using pd.read_csv().

Display column names and shape.

Show first 10 and last 5 rows.
"""
import pandas as pd

df=pd.read_csv('C:\\Users\\JIYA\\Downloads\\sales_data_sample.csv')
print(df)

print(f'Shape: {df.shape}')
print(f'Columns: {df.columns}')

print(df.head(3))
print(df.tail(3))
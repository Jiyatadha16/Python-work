"""
Select all subjects where marks > 85.
"""
import pandas as pd

df=pd.read_json('D:\\Python work\\myenv\\Pandas\\student.json')
print(df)

df_filtered= df[df['marks'] > 85]
print(df_filtered)
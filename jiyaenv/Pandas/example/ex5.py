"""
Select all rows where total_bill > 30 and sex == "Male".

Find the average tip given by each gender.
"""

import pandas as pd
df = pd.read_csv('C:\\Users\\JIYA\\Downloads\\tips.csv')
print(df)

filtered_df = df[(df['total_bill'] > 30) & (df['sex'] == "Male")]
print("New:",filtered_df)

avg_tip=df['tip'].mean()
print("Average Tip:",avg_tip)
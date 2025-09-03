"""
vertically(row wise) concatenate karva mate
horizontally(column wise) concatenate karva mate

pd.concate([df1,df2], axis=0/1, ignore_index=True/False)

[df1, df2] = dataframes to concatenate
axis=0 -> row wise
axis=1 -> column wise

ignore_index=True -> new index assign kare
ignore_index=False -> original index maintain kare
"""

import pandas as pd

#region1 data

df_region1 = pd.DataFrame({
    'customerID': [1,2],
    'Name': ['Ram', 'Shyam'],
})

#region2 data

df_region2 = pd.DataFrame({
    'customerID': [3,4],
    'Name': ['Ghanshyam', 'Mohan'],
})
#concatenate
df_concat = pd.concat([df_region1, df_region2], axis=0, ignore_index=True)
print(df_concat)
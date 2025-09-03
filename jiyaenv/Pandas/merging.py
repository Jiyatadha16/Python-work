#df.merge(df1,df2, on='Column_name', how='inner/outer/left/right')
import pandas as pd

#customer data
df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'CustomerName': ['Anil', 'Sunil', 'Kenil']
})

#order data
df_orders = pd.DataFrame({
    'CustomerID': [1, 2, 4],
    'OrderAmount': [250, 450, 300]
})

#merge

df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='inner')
print("Inner Join:")
print(df_merged)
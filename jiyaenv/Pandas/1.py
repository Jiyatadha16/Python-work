import pandas as pd

#read data from csv file into a DataFrame
df = pd.read_csv('data.csv')
df1=pd.read_excel('data.xlsx')
df2=pd.read_json('data.json')
print(df)
print(df1)
print(df2)
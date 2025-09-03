import pandas as pd

data={
    "Name":['Ram','Shyam','Ghanshyam'],
    "Age":[23,45,34],   
    "City":['Delhi','Mumbai','Chennai']
}
df=pd.DataFrame(data)
print(df)

df.to_csv('data.csv',index=False)
df.to_excel('data.xlsx',index=False)
df.to_json('data.json',index=False)
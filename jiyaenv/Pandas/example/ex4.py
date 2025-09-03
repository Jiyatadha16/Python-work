"""
Create a DataFrame with some NaN values.

Fill missing values with mean.

Drop rows with missing values.
"""
import pandas as pd

data={
    "Name": ['jiya', None, 'Esha', 'Mansi','Anjali','Riya'],
    "Age": [22, 21, 20, None,18,17],
    "City": ['Delhi', 'Mumbai', 'Chennai', None,'Bangalore','Hyderabad']
}

df=pd.DataFrame(data)
print("Original DataFrame:")
print(df)


df['Name'].fillna('Unknown', inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['City'].fillna('Unknown', inplace=True)
print(df)

df.dropna(inplace=True)
print("DataFrame after dropping rows with missing values:") 
print(df)
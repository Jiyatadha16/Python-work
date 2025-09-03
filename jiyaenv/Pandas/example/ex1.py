"""
Create a DataFrame

Make a DataFrame from a Python dictionary with columns: Name, Age, City.

Print the first 5 rows.
"""
import pandas as pd

data={
    "Name": ['jiya', 'Mishri', 'Esha', 'Mansi','Anjali','Riya'],
    "Age": [22, 21, 20, 19,18,17],
    "City": ['Delhi', 'Mumbai', 'Chennai', 'Kolkata','Bangalore','Hyderabad']
}

df=pd.DataFrame(data)
print(df.head())
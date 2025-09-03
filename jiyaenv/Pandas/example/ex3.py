""""
Select only the Age column.

Select rows where Age > 25.

Select Name and City columns.
"""

import pandas as pd


data={
    "Name": ['jiya', 'Mishri', 'Esha', 'Mansi','Anjali','Riya'],
    "Age": [22, 21, 20, 19,18,17],
    "City": ['Delhi', 'Mumbai', 'Chennai', 'Kolkata','Bangalore','Hyderabad']
}

df=pd.DataFrame(data)
print(df)

print(df["Age"])

age=df[df["Age"]>20]
print(age)

print(df[["Age","City"]])
"""
1. How big is your dataset?
2. What are the names of the columns?

Shape and Columns
"""

import pandas as pd

data={
    "Name":['Ram','Shyam','Ghanshyam','Mohan','Sohan','Ramesh','Mahesh','Rajesh','Vijay','Ajay'],
    "Age":[23,45,34,22,25,29,31,28,30,27],
    "City":['Delhi','Mumbai','Chennai','Kolkata','Bangalore','Hyderabad','Pune','Ahmedabad','Surat','Jaipur'],
    "Salary":[50000,60000,55000,52000,58000,62000,59000,61000,57000,53000],
    "PerformanceScore":[3,4,5,2,4,5,3,4,5,3]

}
df=pd.DataFrame(data)
print(df)
print(f'Shape: {df.shape}')
print(f'Columns: {df.columns}')
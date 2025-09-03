#dropna()= Rows ya to Columns ni missing values ne remove kare
# df.dropna(axis=0,inplace=True) #axis=0 means rows
# df.dropna(axis=1,inplace=True) #axis=1 means columns

import pandas as pd

data={
    "Name":['Ram',None,'Ghanshyam','Mohan','Sohan','Ramesh','Mahesh','Rajesh','Vijay','Ajay'],
    "Age":[23,None,34,22,25,29,31,28,30,27],
    "City":['Delhi',None,'Chennai','Kolkata','Bangalore','Hyderabad','Pune','Ahmedabad','Surat','Jaipur'],
    "Salary":[50000,None,55000,52000,58000,62000,59000,61000,57000,53000],
    "PerformanceScore":[3,None,5,2,4,5,3,4,5,3]

}
df=pd.DataFrame(data)
print(df)

df.dropna(inplace=True)
print(df)
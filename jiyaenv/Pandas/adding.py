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

# square brackets for adding new column df["column_name"]=data

df['Bonus'] = df['Salary'] * 0.1  # 10% bonus
print(df)

# using insert method to add new column at specific position
# df.insert(position, "column_name", data)

df.insert(0,"ID",[101,102,103,104,105,106,107,108,109,110])
print(df)

#OR

#df.insert(0,"ID",range(101,111))
#print(df)
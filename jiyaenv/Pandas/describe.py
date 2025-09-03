import pandas as pd

data={
    "Name":['Ram','Shyam','Ghanshyam','Mohan','Sohan','Ramesh','Mahesh','Rajesh','Vijay','Ajay'],
    "Age":[23,45,34,22,25,29,31,28,30,27],
    "City":['Delhi','Mumbai','Chennai','Kolkata','Bangalore','Hyderabad','Pune','Ahmedabad','Surat','Jaipur']
}
df=pd.DataFrame(data)
print("Sample DataFrame:")
print(df)
print("\nDescriptive Statistics:")
print(df.describe())
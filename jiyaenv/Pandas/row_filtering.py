import pandas as pd

data={
    "Name":['Ram','Shyam','Ghanshyam','Mohan','Sohan','Ramesh','Mahesh','Rajesh','Vijay','Ajay'],
    "Age":[23,45,34,22,25,29,31,28,30,27],
    "City":['Delhi','Mumbai','Chennai','Kolkata','Bangalore','Hyderabad','Pune','Ahmedabad','Surat','Jaipur'],
    "Salary":[50000,60000,55000,52000,58000,62000,59000,61000,57000,53000],
    "PerformanceScore":[3,4,5,2,4,5,3,4,5,3]

}
df=pd.DataFrame(data)

high_salary=df[df['Salary']>50000]
print("Employees with salary greater than 50000:")
print(high_salary)

#filtering rows salary>50000 and age>30
filtered= df[(df['Salary']>5000) & (df['Age']>30)]
print("\nEmployees with salary greater than 50000 and age greater than 30:")
print(filtered)

#using or condition
filtered_or= df[(df['performanceScore'] > 90) | (df['Age']>30)]
print("\nEmployees with performance score greater than 90 or age greater than 30:")
print(filtered_or)
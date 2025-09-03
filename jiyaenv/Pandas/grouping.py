import pandas as pd

data={
    "Name": ['Arun', 'Tarun', 'Varun','Karun','Sarun'],
    "Age": [28, 22, 25,28,22],
    "Salary": [50000, 60000, 55000, 40000, 70000]
}
df = pd.DataFrame(data)
grouped=df.groupby("Age")["Salary"].sum()
print(grouped)

#grouped=df.groupby(["Age","Name"])["Salary"].sum()
#print(grouped)
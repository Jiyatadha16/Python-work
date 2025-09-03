"""df["Column_name"].mean()
df["Column_name"].median()
df["Column_name"].sum()
df["Column_name"].min()
df["Column_name"].max()"""

import pandas as pd

data={
    "Name": ['Arun', 'Tarun', 'Varun'],
    "Age": [28, 22, 25],
    "Salary": [50000, 60000, 55000]
}
df = pd.DataFrame(data)

avg_salary = df["Salary"].mean()
print("Average Salary:", avg_salary)
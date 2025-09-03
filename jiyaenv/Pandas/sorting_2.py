#df.sort_values(by=['Column_name','Column2_name'], True/False,inplace=True)

import pandas as pd

data={
    "Name": ['Arun', 'Tarun', 'Varun'],
    "Age": [28, 22, 25],
    "Salary": [50000, 60000, 55000]
}
df = pd.DataFrame(data)

df.sort_values(by=['Age','Salary'], ascending=[True,False], inplace=True)
print("DataFrame sorted by Age (asc) and Salary (desc):")
print(df)
"""
Load a dataset of students (id, name, age, city).

Add a new column age_after_5_years.
"""
import pandas as pd

data ={
    "id": [1, 2, 3, 4],
    "Name": ['Ram', 'Shyam', 'Ghanshyam', 'Mohan'],
    "Age": [23, 45, 34, 22],    
    "City": ['Delhi', 'Mumbai', 'Chennai', 'Kolkata']
}

df=pd.DataFrame(data)
df['age_after_5_years'] = df['Age'] + 5
print(df)
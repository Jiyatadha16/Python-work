"""
GroupBy with Multiple Aggregations

From marks.csv, find per student:

Highest marks

Lowest marks

Average marks
"""
import pandas as pd

df = pd.read_csv('C:\\Users\\JIYA\\Downloads\\marks.csv')
print("Original DataFrame:")    
print(df)

# Highest marks per student
max_marks = df.groupby('student')['marks'].max()

# Lowest marks per student
min_marks = df.groupby('student')['marks'].min()

# Average marks per student
mean_marks = df.groupby('student')['marks'].mean()

# Combine results into a single DataFrame
result = pd.DataFrame({
    'Highest': max_marks,
    'Lowest': min_marks,
    'Average': mean_marks
}).reset_index()

print(result)
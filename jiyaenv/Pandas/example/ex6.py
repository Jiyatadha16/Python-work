"""
Merge them on id.

Find the highest marks per student.
"""
import pandas as pd

# Load CSV files
students = pd.read_csv('C:\\Users\\JIYA\\Downloads\\students.csv')
marks = pd.read_csv('C:\\Users\\JIYA\\Downloads\\marks.csv')

# Merge the two DataFrames on 'id'
df = pd.merge(students, marks, on='id')

# Get the row with the highest marks for each student
highest_marks = df.loc[df.groupby('id')['marks'].idxmax()]

# Rename columns for clarity
highest_marks = highest_marks.rename(columns={
    'marks': 'highest_marks',
    'subject': 'subject_with_highest_marks'
})

# Sort by highest marks (topper first)
highest_marks = highest_marks.sort_values('highest_marks', ascending=False).reset_index(drop=True)

# Show the final result
print("\nHighest Marks per Student (Topper First):")
print(highest_marks)

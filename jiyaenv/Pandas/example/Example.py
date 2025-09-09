#create a dataset of students with their marks, calculate totals, averages, grades, and generate a report.
#Student Result Report to include:1. Overall class topper, 2. Subject-wise toppers, 3. pass/fail statistics, 4. Average marks per subject

import pandas as pd
import numpy as np

students =['Heer','Riya','Anaya','Maya','Sara']

marks =([
    [85, 92, 78, 88, 90],
    [76, 85, 83, 80, 79],
    [90, 91, 92, 89, 95],
    [65, 70, 72, 68, 74],
    [88, 84, 86, 90, 92]
])

df=pd.DataFrame(marks, index=students, columns=['Math','Science','English','History','Art'])

df['Total'] = df.sum(axis=1)
df['Average']= df.mean(axis=1)

def calculate_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'
df['Grade'] = np.vectorize(calculate_grade)(df['Average'])

topper = df['Total'].idxmax()
topper_marks = df.loc[topper, 'Total']

subject_toppers ={}
for subject in ['Math','Science','English','History','Art']:
    max_score = df[subject].max()
    topper_name = df[df[subject] == max_score].index.tolist()
    subject_toppers[subject] = (topper_name, max_score)

df['Result'] = np.where(df['Average'] >= 40, 'Pass', 'Fail')

print("Student Result Report")
print(df)

print(f"\nOverall Class Topper: {topper} with {topper_marks} marks")

print("\nSubject-wise Toppers:")
for subject, (names, score) in subject_toppers.items():
    print(f"{subject}: {', '.join(names)} with {score} marks")
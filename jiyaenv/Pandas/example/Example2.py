
import pandas as pd

df=pd.read_csv('C:\\Users\\JIYA\\Downloads\\student_report_data.csv')

df['Total']=df[['Math','Science','English']].sum(axis=1)
df['Average']=df[['Math','Science','English']].mean(axis=1)

def get_grade(avg):
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

df['Grade']=df['Average'].apply(get_grade)

topper=df.loc[df['Total'].idxmax()]
topper_name=topper['Name']
topper_marks=topper['Total']
print(f"Overall Class Topper: {topper_name} with {topper_marks} marks")

subjects = ['Math','Science','English']
print("\nSubject-wise Toppers:")
for subject in subjects:
    max_score=df[subject].max()
    toppers=df[df[subject]==max_score]['Name'].tolist()
    print(f"{subject}: {', '.join(toppers)} with {max_score} marks")

print("\nFinal Student Report:")
print(df.head(10))


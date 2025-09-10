import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import numpy as np
import random

# Set style
plt.style.use('seaborn-v0_8')

# -------------------------
# Create Sample Student Data
# -------------------------
students = ["Alice", "Bob", "Charlie", "David", "Eva"]
subjects = ["Math", "Science", "English", "History"]
exams = [f"Exam {i}" for i in range(1, 11)]  # 10 exams

data = []
for exam in exams:
    for student in students:
        for subject in subjects:
            marks = random.randint(40, 100)  # marks between 40–100
            data.append({"Exam": exam, "Student": student, "Subject": subject, "Marks": marks})

df = pd.DataFrame(data)
df.to_csv("student_data.csv", index=False)
print("Sample student data created!")

# -------------------------
# 4. Pie Chart Animation – Subject distribution for a student
# -------------------------
def pie_animation():
    df = pd.read_csv("student_data.csv")
    exams = sorted(df["Exam"].unique())
    student = "Alice"

    fig, ax = plt.subplots()

    def animate(frame):
        ax.clear()
        exam = exams[frame]
        data = df[(df["Exam"] == exam) & (df["Student"] == student)]

        ax.pie(data["Marks"], labels=data["Subject"], autopct="%1.1f%%", startangle=90)
        ax.set_title(f"{student}'s Marks - {exam}")

    anim = animation.FuncAnimation(fig, animate, frames=len(exams),
                                   interval=1000, repeat=True)
    plt.show()


# -------------------------
# Run New Animations
# -------------------------

pie_anim = pie_animation()
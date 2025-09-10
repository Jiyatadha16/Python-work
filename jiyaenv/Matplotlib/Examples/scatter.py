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


def scatter_animation():
    df = pd.read_csv("student_data.csv")
    scatter_df = df[df["Subject"].isin(["Math", "Science"])]
    pivot_df = scatter_df.pivot_table(index=["Exam", "Student"], 
                                      columns="Subject", 
                                      values="Marks").reset_index()

    exams = sorted(pivot_df["Exam"].unique())
    students = pivot_df["Student"].unique()

    fig, ax = plt.subplots()

    def animate(frame):
        ax.clear()
        exam = exams[frame]
        data = pivot_df[pivot_df["Exam"] == exam]

        for student in students:
            s_data = data[data["Student"] == student]
            if not s_data.empty:
                ax.scatter(s_data["Math"], s_data["Science"], label=student)
                ax.text(s_data["Math"]+0.5, s_data["Science"]+0.5, student)

        ax.set_title(f"Math vs Science - {exam}")
        ax.set_xlabel("Math Marks")
        ax.set_ylabel("Science Marks")
        ax.set_xlim(30, 100)
        ax.set_ylim(30, 100)
        ax.legend()

    anim = animation.FuncAnimation(fig, animate, frames=len(exams),
                                   interval=1000, repeat=True)
    plt.show()
scatter_anim = scatter_animation()
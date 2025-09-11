import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import random
import numpy as np

# -------------------------
# Create Sample Data
# -------------------------
students = ["Alice", "Bob", "Charlie", "David", "Eva"]
subjects = ["Math", "Science", "English", "History"]
exams = [f"Exam {i}" for i in range(1, 6)]  # 5 exams (small for 3D view)

data = []
for exam in exams:
    for student in students:
        for subject in subjects:
            marks = random.randint(40, 100)
            data.append({"Exam": exam, "Student": student, "Subject": subject, "Marks": marks})

df = pd.DataFrame(data)
df.to_csv("student_data.csv", index=False)

def line_3d_animation():
    df = pd.read_csv("student_data.csv")
    avg_scores = df.groupby(["Exam", "Student"])["Marks"].mean().reset_index()

    exams = sorted(avg_scores["Exam"].unique())
    students = avg_scores["Student"].unique()
    exam_nums = {exam: i for i, exam in enumerate(exams)}

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    def animate(frame):
        ax.clear()
        for s, student in enumerate(students):
            data = avg_scores[(avg_scores["Student"] == student) &
                              (avg_scores["Exam"].isin(exams[:frame+1]))]
            xs = [exam_nums[e] for e in data["Exam"]]
            ys = [s]*len(xs)  # student index
            zs = data["Marks"]

            ax.plot(xs, ys, zs, marker="o", label=student)

        ax.set_title(f"3D Progress (up to {exams[frame]})")
        ax.set_xlabel("Exam")
        ax.set_ylabel("Student")
        ax.set_zlabel("Marks")
        ax.set_yticks(range(len(students)))
        ax.set_yticklabels(students)
        ax.set_xticks(range(len(exams)))
        ax.set_xticklabels(exams)
        ax.set_zlim(30, 100)
        ax.legend()

    anim = animation.FuncAnimation(fig, animate, frames=len(exams),
                                   interval=1000, repeat=True)
    plt.show()
line_3d_animation()
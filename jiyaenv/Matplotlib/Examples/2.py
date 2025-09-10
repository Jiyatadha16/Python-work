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
# 1. Line Chart Animation – Progress of each student
# -------------------------
def animate_student_progress():
    df = pd.read_csv("student_data.csv")

    # Average marks per student per exam
    avg_scores = df.groupby(["Exam", "Student"])["Marks"].mean().reset_index()

    exams = sorted(avg_scores["Exam"].unique())
    students = avg_scores["Student"].unique()

    fig, ax = plt.subplots(figsize=(10, 6))

    colors = plt.cm.Set1(np.linspace(0, 1, len(students)))
    color_map = dict(zip(students, colors))

    def animate(frame):
        ax.clear()
        current_exam = exams[frame]
        current_data = avg_scores[avg_scores["Exam"] <= current_exam]

        for student in students:
            student_data = current_data[current_data["Student"] == student]
            ax.plot(student_data["Exam"], student_data["Marks"],
                    label=student, marker="o", color=color_map[student])

        ax.set_title(f"Average Marks Progress - Up to {current_exam}",
                     fontsize=14, fontweight="bold")
        ax.set_xlabel("Exams")
        ax.set_ylabel("Average Marks")
        ax.set_ylim(30, 100)
        ax.legend(loc="upper left")
        ax.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()

    anim = animation.FuncAnimation(fig, animate, frames=len(exams),
                                   interval=600, repeat=True)
    plt.show()
    return anim


# -------------------------
# Run Animations
# -------------------------
line_anim = animate_student_progress()


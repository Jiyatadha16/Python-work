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
# 2. Bar Chart Animation – Toppers per exam
# -------------------------
def animate_toppers():
    df = pd.read_csv("student_data.csv")

    exams = sorted(df["Exam"].unique())
    students = df["Student"].unique()

    fig, ax = plt.subplots(figsize=(10, 6))
    colors = plt.cm.viridis(np.linspace(0, 1, len(students)))

    def animate(frame):
        ax.clear()
        current_exam = exams[frame]
        current_data = df[df["Exam"] == current_exam].groupby("Student")["Marks"].mean().reset_index()

        bars = ax.bar(current_data["Student"], current_data["Marks"],
                      color=colors, alpha=0.8, edgecolor="black")

        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                    f"{height:.1f}", ha="center", va="bottom", fontsize=9, fontweight="bold")

        ax.set_title(f"Average Marks by Student - {current_exam}",
                     fontsize=14, fontweight="bold")
        ax.set_xlabel("Students")
        ax.set_ylabel("Average Marks")
        ax.set_ylim(30, 100)
        ax.grid(True, axis="y", alpha=0.3)

    anim = animation.FuncAnimation(fig, animate, frames=len(exams),
                                   interval=800, repeat=True)
    plt.show()
    return anim
# -------------------------
# Run Animations
# -------------------------

bar_anim = animate_toppers()
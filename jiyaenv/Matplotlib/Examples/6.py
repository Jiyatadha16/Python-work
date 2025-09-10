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
# 5. Histogram Animation – Distribution of marks
# -------------------------
def animate_histogram():
    df = pd.read_csv("student_data.csv")

    exams = sorted(df["Exam"].unique())

    fig, ax = plt.subplots(figsize=(10, 6))

    def animate(frame):
        ax.clear()
        current_exam = exams[frame]
        current_data = df[df["Exam"] <= current_exam]

        n, bins, patches = ax.hist(current_data["Marks"], bins=10,
                                   alpha=0.7, color="skyblue",
                                   edgecolor="black", linewidth=1)

        # Color intensity based on frequency
        if len(n) > 0 and max(n) > 0:
            for patch, count in zip(patches, n):
                patch.set_facecolor(plt.cm.viridis(count / max(n)))

        mean_marks = current_data["Marks"].mean()
        ax.axvline(mean_marks, color="red", linestyle="--", linewidth=2, label=f"Mean: {mean_marks:.1f}")

        ax.set_title(f"Marks Distribution - Up to {current_exam}",
                     fontsize=14, fontweight="bold")
        ax.set_xlabel("Marks")
        ax.set_ylabel("Frequency")
        ax.set_xlim(30, 100)
        ax.legend()
        ax.grid(True, alpha=0.3)

    anim = animation.FuncAnimation(fig, animate, frames=len(exams),
                                   interval=900, repeat=True)
    plt.show()
    return anim

# -------------------------
# Run New Animations
# -------------------------

hist_anim = animate_histogram()
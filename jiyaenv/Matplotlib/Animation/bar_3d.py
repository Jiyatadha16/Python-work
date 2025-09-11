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
exams = [f"Exam {i}" for i in range(1, 6)]  # 5 exams
data = []
for exam in exams:
    for student in students:
        for subject in subjects:
            marks = random.randint(40, 100)
            data.append({"Exam": exam, "Student": student, "Subject": subject, "Marks": marks})
df = pd.DataFrame(data)

def bar_3d_animation():
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")

    exams = sorted(df["Exam"].unique())
    subjects = sorted(df["Subject"].unique())
    subject_idx = {s: i for i, s in enumerate(subjects)}

    def animate(frame):
        ax.clear()
        exam = exams[frame // 20]  # Slow down exam change (20 sub-frames per exam)
        subframe = frame % 20      # Sub-frame for up-down animation
        data = df[df["Exam"] == exam].groupby("Subject")["Marks"].mean().reset_index()

        xs = [frame // 20] * len(data)
        ys = [subject_idx[s] for s in data["Subject"]]
        zs = np.zeros(len(data))
        dx = 0.6
        dy = 0.6
        # Animate height from 0 to full marks
        dz = [min(marks, marks * subframe / 19) for marks in data["Marks"]]

        ax.bar3d(xs, ys, zs, dx, dy, dz, color="skyblue", alpha=0.7, edgecolor="black")

        ax.set_title(f"3D Bar Chart - {exam}")
        ax.set_xlabel("Exam")
        ax.set_ylabel("Subject")
        ax.set_zlabel("Marks")
        ax.set_yticks(range(len(subjects)))
        ax.set_yticklabels(subjects)
        ax.set_xticks(range(len(exams)))
        ax.set_xticklabels(exams)
        ax.set_zlim(0, 100)
        ax.view_init(elev=30, azim=45)

    # Total frames = number of exams * sub-frames per exam
    anim = animation.FuncAnimation(fig, animate, frames=len(exams)*20, interval=50, repeat=True)
    plt.tight_layout()
    return anim

anim = bar_3d_animation()
plt.show()

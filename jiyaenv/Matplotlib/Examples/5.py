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
def animate_pie_chart():
    df = pd.read_csv("student_data.csv")

    exams = sorted(df["Exam"].unique())
    student = "Alice"  # Example: animate for Alice

    fig, ax = plt.subplots(figsize=(8, 8))
    colors = plt.cm.Set3(np.linspace(0, 1, len(subjects)))

    def animate(frame):
        ax.clear()
        current_exam = exams[frame]
        current_data = df[(df["Exam"] == current_exam) & (df["Student"] == student)]

        wedges, texts, autotexts = ax.pie(current_data["Marks"],
                                          labels=current_data["Subject"],
                                          colors=colors,
                                          autopct="%1.1f%%",
                                          startangle=90,
                                          explode=[0.05] * len(current_data))

        for autotext in autotexts:
            autotext.set_color("white")
            autotext.set_fontweight("bold")

        ax.set_title(f"{student}'s Marks Distribution - {current_exam}",
                     fontsize=16, fontweight="bold")
        ax.axis("equal")

    anim = animation.FuncAnimation(fig, animate, frames=len(exams),
                                   interval=1000, repeat=True)
    plt.show()
    return anim

# -------------------------
# Run New Animations
# -------------------------

pie_anim = animate_pie_chart()
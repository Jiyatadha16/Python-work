import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import random

# -------------------------
# Create Sample Data
# -------------------------
students = ["Alice", "Bob", "Charlie", "David", "Eva"]
subjects = ["Math", "Science", "English", "History"]
exams = [f"Exam {i}" for i in range(1, 11)]

data = []
for exam in exams:
    for student in students:
        for subject in subjects:
            marks = random.randint(40, 100)
            data.append({"Exam": exam, "Student": student, "Subject": subject, "Marks": marks})

df = pd.DataFrame(data)
df.to_csv("student_data.csv", index=False)
print("Sample student data created!")

def line_animation():
    df = pd.read_csv("student_data.csv")
    avg_scores = df.groupby(["Exam", "Student"])["Marks"].mean().reset_index()

    exams = sorted(avg_scores["Exam"].unique())
    students = avg_scores["Student"].unique()

    fig, ax = plt.subplots()

    def animate(frame):
        ax.clear()
        exam = exams[frame]
        data = avg_scores[avg_scores["Exam"] <= exam]

        for student in students:
            s_data = data[data["Student"] == student]
            ax.plot(s_data["Exam"], s_data["Marks"], marker="o", label=student)

        ax.set_title(f"Progress up to {exam}")
        ax.set_xlabel("Exams")
        ax.set_ylabel("Average Marks")
        ax.set_ylim(30, 100)
        ax.legend()

    anim = animation.FuncAnimation(fig, animate, frames=len(exams),
                                   interval=1000, repeat=True)
    plt.show()

line_animation()
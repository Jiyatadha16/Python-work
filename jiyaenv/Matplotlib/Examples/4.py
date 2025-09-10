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
# 3. Scatter Plot Animation – Math vs Science
# -------------------------
def animate_scatter_math_science():
    df = pd.read_csv("student_data.csv")

    # Filter only Math & Science
    scatter_df = df[df["Subject"].isin(["Math", "Science"])]

    # Pivot so we have columns: Exam | Student | Math | Science
    scatter_pivot = scatter_df.pivot_table(index=["Exam", "Student"],
                                           columns="Subject",
                                           values="Marks").reset_index()

    exams = sorted(scatter_pivot["Exam"].unique())
    students = scatter_pivot["Student"].unique()

    fig, ax = plt.subplots(figsize=(10, 6))

    colors = plt.cm.tab10(np.linspace(0, 1, len(students)))
    color_map = dict(zip(students, colors))

    def animate(frame):
        ax.clear()
        current_exam = exams[frame]
        current_data = scatter_pivot[scatter_pivot["Exam"] == current_exam]

        # Scatter plot: Math (x) vs Science (y)
        for student in students:
            student_data = current_data[current_data["Student"] == student]
            if not student_data.empty:
                ax.scatter(student_data["Math"], student_data["Science"],
                           c=[color_map[student]], label=student,
                           s=120, alpha=0.8, edgecolor="black")

                # Label with student name
                for _, row in student_data.iterrows():
                    ax.text(row["Math"] + 0.5, row["Science"] + 0.5, student,
                            fontsize=9, weight="bold")

        ax.set_title(f"Math vs Science Performance - {current_exam}",
                     fontsize=14, fontweight="bold")
        ax.set_xlabel("Math Marks")
        ax.set_ylabel("Science Marks")
        ax.set_xlim(30, 100)
        ax.set_ylim(30, 100)
        ax.grid(True, alpha=0.3)

        # Avoid duplicate legend
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys(), loc="upper left")

        plt.tight_layout()

    anim = animation.FuncAnimation(fig, animate, frames=len(exams),
                                   interval=800, repeat=True)
    plt.show()
    return anim

# -------------------------
# Run New Animations
# -------------------------

scatter_anim = animate_scatter_math_science()
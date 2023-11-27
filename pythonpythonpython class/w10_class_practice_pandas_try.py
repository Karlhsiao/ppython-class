import pandas as pd
import matplotlib as plt

filename = "student_score.csv"
df = pd.read_csv(filename)
df_sorted = df.sort_values(by="ID")

new_row1 = ["S008", "Tina", 90, 87, 96]
new_row2 = ["S009", "Wayne", 79, 83, 86]
new_student = pd.DataFrame([new_row1, new_row2], 
                           columns=df_sorted.columns)

selected_cols = ["Exam1", "Exam2", "Exam3"]

new_df = pd.concat([df_sorted, new_student])
new_df["Sum"] = new_df[selected_cols].sum(axis="columns")
new_df["Mean"] = new_df[selected_cols].mean(axis="columns")

new_df.plot(kind="bar", x="ID")

plt.pyplot.show()
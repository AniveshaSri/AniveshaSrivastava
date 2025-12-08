
# Student Performance Data Analysis Project

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic dataset
np.random.seed(42)
n = 200

data = pd.DataFrame({
    "Hours_Studied": np.random.normal(5, 2, n).clip(0),
    "Attendance": np.random.normal(85, 10, n).clip(50, 100),
    "Assignments_Completed": np.random.randint(5, 11, n),
})

# Create Exam Score with a weighted formula + noise
data["Exam_Score"] = (
    5 * data["Hours_Studied"] +
    0.4 * data["Attendance"] +
    3 * data["Assignments_Completed"] +
    np.random.normal(0, 10, n)
).clip(0, 100)

# Show first few rows
print("=== Sample of Dataset ===")
print(data.head())



#Chart 1 — Hours Studied vs Exam Score (Scatter)

plt.figure(figsize=(7,5))
plt.scatter(data["Hours_Studied"], data["Exam_Score"])
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Relationship Between Hours Studied and Exam Score")
plt.tight_layout()
plt.show()



#Chart 2 — Attendance Distribution (Histogram)

plt.figure(figsize=(7,5))
plt.hist(data["Attendance"], bins=10)
plt.xlabel("Attendance (%)")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Attendance")
plt.tight_layout()
plt.show()



#Basic Insights

print("\n=== Insights ===")

# Correlation
print("\nCorrelation Matrix:")
print(data.corr())

avg_study = data["Hours_Studied"].mean()
avg_attendance = data["Attendance"].mean()
avg_score = data["Exam_Score"].mean()

print(f"\nAverage Hours Studied: {avg_study:.2f}")
print(f"Average Attendance: {avg_attendance:.2f}%")
print(f"Average Exam Score: {avg_score:.2f}")

import pandas as pd
import matplotlib.pyplot as plt

""" 
# Visualizing the distribution of exam scores

You are provided with a dataset containing exam scores for a group of students. Create a bar 
chart that represents the distribution of scores across different grade bands (e.g., A, B, C, D, F). 
The goal is to practice the principles of clarity, accuracy, and simplicity in visualization.
"""

# Sample dataset: Exam scores
data = {'Grade': ['A', 'B', 'C', 'D', 'F'],
        'Number of Students': [20, 35, 40, 10, 5]}
df = pd.DataFrame(data)


# Data preparation
grades = df['Grade']
students = df['Number of Students']

# Create a bar chart
plt.barh(grades, students, color='skyblue')
plt.title("Distribution of Exam Scores")
plt.ylabel("Grade")
plt.xlabel("Number of Students")
plt.show()


"""
Why a Bar Chart?

Bar charts are excellent for categorical data, where we want to compare quantities across discrete 
categories (in this case, grade bands). This is the simplest and most accurate way to convey the distribution of students across grades.
"""

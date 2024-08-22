import pandas as pd
import plotly.express as px

""" 
# Visualizing the relationship between Age and Income

You are given a dataset that contains the ages and annual incomes of a group of individuals. 
Your task is to create a scatter plot to explore the relationship between age and income.
"""

# Sample dataset: Age and income
data = {'Age': [22, 25, 47, 52, 46, 56, 55, 38],
        'Income': [35000, 42000, 79000, 85000, 76000, 90000, 94000, 62000]}
df = pd.DataFrame(data)

# Create a scatter plot
fig = px.scatter(df, x="Age", y="Income", title="Age vs Income")
fig.show()

"""
Why a Scatter Plot?

A scatter plot is the most appropriate choice when visualizing the relationship 
between two continuous variables. It helps in identifying trends, correlations, and potential outliers.
"""

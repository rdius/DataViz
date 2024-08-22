import seaborn as sns
import pandas as pd


"""
# Learn how to visualize multiple variables simultaneously to uncover deeper insights.

You have a dataset containing information about different cars, including horsepower, weight, and fuel efficiency. 
Visualize the relationship between these variables using a scatterplot matrix to uncover potential correlations.
"""

# Sample dataset: Car attributes
data = {'Horsepower': [130, 250, 190, 300, 210],
        'Weight': [3500, 4500, 3800, 4700, 4000],
        'MPG': [25, 15, 20, 12, 18]}
df = pd.DataFrame(data)


import matplotlib.pyplot as plt

# Create a pairplot (scatterplot matrix)
sns.pairplot(df)
plt.show()



"""
Why a Scatterplot Matrix?

This type of visualization is useful when you have more than two continuous variables 
and you want to explore pairwise relationships across the dataset. 
It gives a comprehensive view of the correlations between multiple variables in one chart.
"""

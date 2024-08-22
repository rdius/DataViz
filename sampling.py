import pandas as pd
import numpy as np

"""
# Data sampling

You have a dataset containing millions of financial transactions. Your goal is to create a visualization of transaction amounts over time, 
but the dataset is too large to plot directly. Use a sampling technique to reduce the data size and visualize trends.
"""

# Simulate large financial transactions dataset
np.random.seed(42)
data = {'Date': pd.date_range(start='2023-01-01', periods=1000000, freq='T'),
        'Transaction_Amount': np.random.normal(100, 20, 1000000)}
df = pd.DataFrame(data)


# Sample 1% of the data
sampled_data = df.sample(frac=0.01, random_state=42)

# Plot sampled data
import matplotlib.pyplot as plt

plt.plot(sampled_data['Date'], sampled_data['Transaction_Amount'], linestyle='', marker='.', alpha=0.5)
plt.title("Sampled Financial Transactions Over Time")
plt.xlabel("Date")
plt.ylabel("Transaction Amount")
plt.show()



"""
Why Sampling?

Sampling is a practical approach when working with very large datasets that cannot be visualized directly. 
By randomly selecting a smaller subset of the data, we can still observe overall trends without overwhelming computational resources.
"""

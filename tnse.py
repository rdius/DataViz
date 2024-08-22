from sklearn.datasets import load_digits
import pandas as pd

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt



"""
#Visualizing high-dimensional data

You are given the famous Digits dataset from scikit-learn, 
which contains 64 features for each handwritten digit (8x8 pixel values). 
Use t-SNE to reduce the data to 2 dimensions and visualize the different digit clusters.

"""

# Load the digits dataset
digits = load_digits()
df = pd.DataFrame(digits.data)


# Apply t-SNE to reduce dimensions to 2
tsne = TSNE(n_components=2, random_state=42)
reduced_data = tsne.fit_transform(df)

# Create a scatter plot of the t-SNE results, color by digit labels
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=digits.target, cmap='viridis', alpha=0.7)
plt.colorbar(label='Digit Label')
plt.title("t-SNE Visualization of Handwritten Digits")
plt.xlabel("t-SNE Dimension 1")
plt.ylabel("t-SNE Dimension 2")
plt.show()



"""
Why t-SNE?

t-SNE is ideal for visualizing high-dimensional data, especially when the data forms complex, 
non-linear patterns. It excels in revealing clusters that might not be visible with linear dimensionality reduction techniques like PCA.
"""

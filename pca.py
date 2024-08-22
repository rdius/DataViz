import pandas as pd
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Simulate customer behavior dataset with 10 features
#np.random.seed(42)
#data = np.random.rand(1000, 10)  # 1000 customers, 10 features
#df = pd.DataFrame(data, columns=[f'Feature_{i+1}' for i in range(10)])

# Load the digits dataset
digits = load_digits()
df = pd.DataFrame(digits.data)
print(len(df))

# Apply PCA to reduce dimensions to 2
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(df)

# Create a scatter plot of the PCA results
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], alpha=0.5, color='blue')
plt.title("Customer Segments Visualization (PCA)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()

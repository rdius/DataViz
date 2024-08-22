import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Charger les donnees
data = load_iris()
print(data)
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
X = data.data
y = data.target # ['setosa', 'versicolor', 'virginica']

# Standardiser les données (features engineering)
X_std = StandardScaler().fit_transform(X)

# Appliquer la PCA, ici avec deux composantes principales
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_std)

# Visualiser les resultats
plt.figure(figsize=(8,6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', edgecolor='k', s=50)
plt.xlabel('Composante Principale 1')
plt.ylabel('Composante Principale 2')
plt.title('Projection des données avec PCA')
plt.show()


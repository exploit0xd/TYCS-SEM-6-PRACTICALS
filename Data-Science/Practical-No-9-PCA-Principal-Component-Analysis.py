import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# ------------------- Load Iris Dataset -------------------
data = load_iris()
X = data.data
y = data.target

# ------------------- Apply PCA -------------------
pca = PCA()
X_pca = pca.fit_transform(X)

# ------------------- Explained Variance Analysis -------------------
explained_variance_ratio = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance_ratio)

# ------------------- Plot Explained and Cumulative Variance -------------------
plt.figure(figsize=(10, 6))
plt.bar(range(1, len(explained_variance_ratio) + 1), explained_variance_ratio, alpha=0.7,
        align='center', label='Explained Variance Ratio')
plt.step(range(1, len(cumulative_variance) + 1), cumulative_variance, where='mid',
         label='Cumulative Explained Variance', color='red')
plt.xlabel('Principal Components')
plt.ylabel('Explained Variance Ratio')
plt.title('Explained Variance Ratio and Cumulative Explained Variance')
plt.legend()
plt.grid()
plt.show()

# ------------------- Determine Number of Components for 95% Variance -------------------
n_components = np.argmax(cumulative_variance >= 0.95) + 1
print("Number of principal components to retain:", n_components)

# ------------------- Visualize Data in 2D PCA Space -------------------
plt.figure(figsize=(8, 6))
for target in np.unique(y):
    plt.scatter(X_pca[y == target, 0], X_pca[y == target, 1], label=f'Class {target}')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA - Iris Dataset (First 2 Principal Components)')
plt.legend()
plt.grid()
plt.show()

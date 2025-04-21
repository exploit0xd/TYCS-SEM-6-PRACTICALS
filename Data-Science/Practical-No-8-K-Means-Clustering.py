import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# ------------------- Generate synthetic data -------------------
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# ------------------- Apply K-Means for various cluster counts -------------------
wcss = []  # Within-cluster sum of squares
silhouette_scores = []

for i in range(2, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X, kmeans.labels_))

# ------------------- Elbow Method & Silhouette Analysis -------------------
plt.figure(figsize=(12, 5))

# Elbow Method Plot
plt.subplot(1, 2, 1)
plt.plot(range(2, 11), wcss, marker='o', linestyle='--', color='blue')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')

# Silhouette Analysis Plot
plt.subplot(1, 2, 2)
plt.plot(range(2, 11), silhouette_scores, marker='o', linestyle='--', color='green')
plt.title('Silhouette Analysis')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')

plt.tight_layout()
plt.show()

# ------------------- Determine Optimal Clusters -------------------
optimal_num_clusters = np.argmax(silhouette_scores) + 2  # +2 because range starts from 2
print("Optimal number of clusters:", optimal_num_clusters)

# ------------------- Apply Final K-Means Clustering -------------------
kmeans = KMeans(n_clusters=optimal_num_clusters, init='k-means++', max_iter=300,
                n_init=10, random_state=0)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# ------------------- Cluster Visualization -------------------
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')
plt.title('K-Means Clustering Result')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

# ------------------- Final Output -------------------
print("Cluster Centers:\n", centers)

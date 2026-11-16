'''
AIM=Program to demonstrate DBSCAN clustering algorithm

REL. THEORY=
DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is an unsupervised machine learning algorithm that groups data points based on their density. It identifies clusters of closely packed points and detects outliers or noise without requiring the number of clusters in advance.

CODE=                                                                '''
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
# Load dataset
iris = load_iris()
X = iris.data
# Standardize
X_scaled = StandardScaler().fit_transform(X)
# DBSCAN
model = DBSCAN(eps=0.8, min_samples=5)
labels = model.fit_predict(X_scaled)
print("Cluster Labels:")
print(labels)
print("\nNumber of clusters:",
 len(set(labels)) - (1 if -1 in labels else 0))
print("Number of noise points:",
 list(labels).count(-1))
# Plot using first two features
plt.figure(figsize=(8, 5))
plt.scatter(
 X_scaled[:, 0],
 X_scaled[:, 1],
 c=labels,
 cmap="rainbow"
)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("DBSCAN Clustering")
plt.show()

'''
LO=
1. Understand the working of the DBSCAN algorithm.
2. Perform density-based clustering on datasets.
3. Identify clusters and detect noise or outliers.
'''
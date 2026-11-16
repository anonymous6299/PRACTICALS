'''
AIM=Program to demonstrate K-Medoid clustering algorithm

REL. THEORY=
K-Medoids is an unsupervised machine learning algorithm used for clustering. It partitions data into K clusters by selecting actual data points as cluster centers (medoids). It assigns each point to its nearest medoid and minimizes the total distance within clusters.

CODE=                                                                '''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import pairwise_distances

# Load and standardize data
iris = load_iris()
X = StandardScaler().fit_transform(iris.data[:, :2])

# Initialize medoids
k = 3
medoids = np.array([0, 50, 100])

def assign_clusters(X, medoids):
    return np.argmin(pairwise_distances(X, X[medoids]), axis=1)

def calculate_cost(X, medoids):
    distances = pairwise_distances(X, X[medoids])
    return np.sum(np.min(distances, axis=1))

# Optimize medoids
current_cost = calculate_cost(X, medoids)
improved = True

while improved:
    improved = False
    for i in range(k):
        for candidate in range(len(X)):
            if candidate in medoids:
                continue
            new_medoids = medoids.copy()
            new_medoids[i] = candidate
            new_cost = calculate_cost(X, new_medoids)
            if new_cost < current_cost:
                medoids = new_medoids
                current_cost = new_cost
                improved = True

# Display results
labels = assign_clusters(X, medoids)
print("Final Medoids:", medoids)
print("Final Cost:", current_cost)
print("Cluster Labels:", labels)

# Plot clusters
plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="rainbow")
plt.scatter(X[medoids, 0], X[medoids, 1], color="black",
            marker="X", s=200, label="Medoids")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("K-Medoids Clustering")
plt.legend()
plt.show()

'''
LO=
1. Understand the working of the K-Medoids algorithm.
2. Perform clustering using selected medoids.
3. Analyze clusters and identify representative data points.
'''
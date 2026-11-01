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
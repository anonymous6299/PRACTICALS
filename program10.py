import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
# Load handwritten digits dataset
digits = load_digits()
X = digits.data
y = digits.target
print("Dataset Shape:", X.shape)
# K-Means
kmeans = KMeans(
 n_clusters=10,
 random_state=42,
 n_init=10
)
clusters = kmeans.fit_predict(X)
print("\nCluster Labels:")
print(clusters[:30])
print("\nInertia:")
print(kmeans.inertia_)
# Reduce dimensions using PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
# Plot clusters
plt.figure(figsize=(10, 6))
plt.scatter(
 X_pca[:, 0],
 X_pca[:, 1],
 c=clusters,
 cmap="tab10",
 s=10
)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("K-Means Clustering of Handwritten Digits")
plt.colorbar(label="Cluster")
plt.show()
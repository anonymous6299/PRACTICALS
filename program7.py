import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Standardize data
X_scaled = StandardScaler().fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Original shape:", X.shape)
print("PCA shape:", X_pca.shape)
print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

# Apply LDA
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X_scaled, y)

print("\nLDA shape:", X_lda.shape)

# Plot PCA and LDA
plt.figure(figsize=(12, 5))

# PCA Plot
plt.subplot(1, 2, 1)
for i in range(3):
    plt.scatter(
        X_pca[y == i, 0],
        X_pca[y == i, 1],
        label=iris.target_names[i]
    )
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA on Iris Dataset")
plt.legend()

# LDA Plot
plt.subplot(1, 2, 2)
for i in range(3):
    plt.scatter(
        X_lda[y == i, 0],
        X_lda[y == i, 1],
        label=iris.target_names[i]
    )
plt.xlabel("LD1")
plt.ylabel("LD2")
plt.title("LDA on Iris Dataset")
plt.legend()

plt.tight_layout()
plt.show()
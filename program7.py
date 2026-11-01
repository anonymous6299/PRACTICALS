
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
data = {
    'Maths': [80, 90, 70, 85, 95],
    'Science': [85, 95, 75, 80, 90],
    'English': [78, 88, 65, 82, 92]
}
df = pd.DataFrame(data)
print("Original Dataset:")
print(df)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
pca = PCA(n_components=2)
pca_data = pca.fit_transform(scaled_data)
result = pd.DataFrame(pca_data, columns=['PC1', 'PC2'])
print("\nDataset After PCA:")
print(result.round(3))
print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_.round(3))
print("\nTotal Variance Explained:")
print(round(sum(pca.explained_variance_ratio_), 3))

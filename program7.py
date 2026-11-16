'''
AIM=To perform Principal Component Analysis on datasets.

REL. THEORY=
Principal Component Analysis (PCA) is a dimensionality reduction technique that transforms correlated variables into a smaller set of uncorrelated variables called principal components. These components capture maximum possible variance in the data. PCA reduces complexity, removes redundancy, and supports visualization. Python's Scikit-learn library provides tools for implementing PCA on datasets.

CODE=                                                                '''
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


'''
LO=
1. Understand the concept and importance of Principal Component Analysis.
2. Learn to reduce dataset dimensionality while retaining important information.
3. Apply PCA using Python to simplify and visualize complex datasets.
'''

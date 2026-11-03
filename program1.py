import pandas as pd
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add dependent variable
df['target'] = iris.target

# Display dataset
print("First Five Records:")
print(df.head())

# Independent parameters
X = df.drop('target', axis=1)

# Dependent parameter
Y = df['target']

# Display independent parameters
print("\nIndependent Parameters (X):")
print(X.head())

# Display dependent parameter
print("\nDependent Parameter (Y):")
print(Y.head())

# Display shapes
print("\nShape of Independent Parameters:", X.shape)
print("Shape of Dependent Parameter:", Y.shape)
'''
AIM=Loading and Distinguishing Dependent and Independent parameters

REL. THEORY=
Data visualization begins with loading and understanding datasets. Independent parameters are input variables used for analysis, while dependent parameters are output variables influenced by them. Python libraries like Pandas and Scikit-learn help load, organize, and distinguish these variables.

CODE=                                                                '''

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


'''
LO=
1.	Learned to load datasets using Python.
2.	Identified dependent and independent variables.
3.	Understood basic dataset structure.
'''
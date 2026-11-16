'''
AIM=Introduction to JUPYTER IDE and its libraries Pandas and NumPy

REL. THEORY=
Jupyter Notebook is an interactive IDE used for writing and executing Python code. It supports libraries like NumPy and Pandas. NumPy is used for numerical computations and handling multidimensional arrays, while Pandas is used for data manipulation, analysis, and handling structured datasets using Series and DataFrames.

CODE=                                                                '''
import numpy as np
import pandas as pd
# NumPy array
arr = np.array([10, 20, 30, 40, 50])
print("NumPy Array:")
print(arr)
print("\nSum =", np.sum(arr))
print("Mean =", np.mean(arr))
print("Maximum =", np.max(arr))
print("Minimum =", np.min(arr))
# Pandas DataFrame
data = {
 "Name": ["Aman", "Riya", "Rahul", "Neha"],
 "Marks": [85, 92, 78, 88],
 "Age": [20, 21, 20, 22]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)
print("\nFirst two rows:")
print(df.head(2))
print("\nStatistical Summary:")
print(df.describe())

'''
LO=
1. Understand the Jupyter Notebook environment.
2. Learn basic operations using NumPy arrays.
3. Perform data manipulation using Pandas.
'''
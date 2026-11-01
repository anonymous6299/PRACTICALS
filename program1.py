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

import numpy as np
import pandas as pd
data = [10, 20, 30, 40, 50]
arr = np.array(data)
print("NumPy Array:")
print(arr)
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
student_data = {
    'Name': ['Amit', 'Neha', 'Raj', 'Priya'],
    'Age': [21, 22, 20, 23],
    'Marks': [85, 90, 78, 95]
}
df = pd.DataFrame(student_data)
print("\nDataFrame:")
print(df)
print("\nData Description:")
print(df.describe())
print("\nStudents Scoring Above 85:")
print(df[df['Marks'] > 85])
print("\nSorted by Marks:")
print(df.sort_values(by='Marks', ascending=False))

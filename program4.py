'''
AIM=To use Python as a programming tool for the analysis of data structures.

REL. THEORY=
Python is a versatile programming language widely used in data science for storing, processing, and analyzing data. It supports data structures such as lists, tuples, dictionaries, and sets. Libraries like NumPy and Pandas simplify numerical computations and structured data analysis, enabling efficient data handling, transformation, and interpretation.

CODE=                                                                '''
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
'''
LO=
1. Understand Python data structures such as lists, tuples, dictionaries, and sets.
2. Learn to store, access, and manipulate data using Python.
3. Apply Python libraries for efficient data analysis and processing.
'''
'''
AIM=To perform Data Aggregation and GroupWise Operations.

REL. THEORY=
Data aggregation combines multiple data values into summarized results using operations such as sum, mean, count, minimum, and maximum. GroupWise operations divide datasets into groups based on common attributes and perform calculations on each group. Python's Pandas library provides the groupby() function for efficient grouping, aggregation, and analysis of structured datasets.

CODE=                                                                '''
import pandas as pd
data = {
    'Department': ['IT', 'HR', 'IT', 'HR', 'Sales', 'Sales'],
    'Employee': ['Amit', 'Neha', 'Raj', 'Priya', 'Karan', 'Riya'],
    'Salary': [50000, 40000, 60000, 45000, 35000, 55000]
}
df = pd.DataFrame(data)
print("Original Dataset:")
print(df)
print("\nGroupWise Salary Sum:")
print(df.groupby('Department')['Salary'].sum())
print("\nGroupWise Salary Mean:")
print(df.groupby('Department')['Salary'].mean())
print("\nGroupWise Aggregation:")
print(df.groupby('Department')['Salary'].agg(['sum', 'mean', 'max', 'min', 'count']))
print("\nEmployee Count per Department:")
print(df.groupby('Department')['Employee'].count())
'''
LO=
1. Understand the concepts of data aggregation and group-wise operations.
2. Learn to group datasets based on common attributes.
3. Perform summary calculations such as sum, mean, count, minimum, and maximum using Pandas.
'''
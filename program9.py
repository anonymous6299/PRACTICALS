
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

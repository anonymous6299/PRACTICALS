import pandas as pd
data = {
    'Name': ['Amit', 'Neha', 'Raj', 'Priya', 'Karan'],
    'Age': [21, 22, 20, 23, 21],
    'Marks': [85, 90, 78, 95, 88]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)
print("\nFirst 3 Rows:")
print(df.head(3))
print("\nStatistical Description:")
print(df.describe())
print("\nColumn Names:")
print(df.columns)
print("\nShape of Data:")
print(df.shape)
print("\nViewing Marks Column:")
print(df['Marks'])
df['Marks'] = df['Marks'] + 5
print("\nUpdated Data:")
print(df)
df = df[df['Age'] > 21]
print("\nStudents Older Than 21:")
print(df)
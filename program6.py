
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Name': ['Amit', 'Neha', 'Raj', 'Priya', 'Karan'],
    'Marks': [85, 90, 78, 95, 88],
    'Age': [21, 22, 20, 23, 21]
}
df = pd.DataFrame(data)
print("Dataset:")
print(df)
print("\nDescriptive Statistics:")
print(df.describe())
print("\nMean Marks:", df['Marks'].mean())
print("Median Marks:", df['Marks'].median())
print("Mode Marks:", df['Marks'].mode()[0])
print("Standard Deviation:", round(df['Marks'].std(), 2))
print("Variance:", round(df['Marks'].var(), 2))
print("Minimum Marks:", df['Marks'].min())
print("Maximum Marks:", df['Marks'].max())
plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Marks'])
plt.title('Student Marks')
plt.xlabel('Student')
plt.ylabel('Marks')
plt.grid(axis='y')
plt.show()
plt.figure(figsize=(8, 5))
plt.hist(df['Marks'], bins=5, edgecolor='black')
plt.title('Distribution of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()
plt.figure(figsize=(6, 5))
plt.boxplot(df['Marks'])
plt.title('Box Plot of Marks')
plt.ylabel('Marks')
plt.show()

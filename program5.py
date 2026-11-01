
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [120, 150, 100, 180, 200],
    'Profit': [20, 30, 15, 40, 50]
}
df = pd.DataFrame(data)
df.to_csv('sales_data.csv', index=False)
print("Data Stored Successfully")
print("\nSales Data:")
print(df)
print("\nStatistical Analysis:")
print(df.describe())
print("\nTotal Sales:", df['Sales'].sum())
print("Average Sales:", df['Sales'].mean())
print("Total Profit:", df['Profit'].sum())
plt.figure(figsize=(8, 5))
plt.bar(df['Month'], df['Sales'])
plt.title('Monthly Sales Analysis')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(axis='y')
plt.show()
plt.figure(figsize=(8, 5))
plt.plot(df['Month'], df['Profit'], marker='o')
plt.title('Monthly Profit Analysis')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.grid(True)
plt.show()

'''
AIM=Creating Scatter Plot maps

REL. THEORY=
Scatter plots represent relationships between two numerical variables using individual data points. They help identify patterns, trends, clusters, and correlations. Python Matplotlib provides scatter plot functions that support different colors, sizes, and markers for effective visualization.

CODE=                                                                '''
import matplotlib.pyplot as plt
import pandas as pd

# Create sample dataset
data = {
    'Study_Hours': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'Marks': [40, 45, 50, 55, 60, 65, 75, 80, 85, 95],
    'Attendance': [60, 65, 70, 72, 75, 80, 85, 88, 90, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display dataset
print("Student Performance Dataset:")
print(df)

# Create scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(df['Study_Hours'], df['Marks'],
            c=df['Attendance'],
            s=100,
            cmap='viridis',
            edgecolor='black')

# Add labels and title
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

# Display color bar
plt.colorbar(label="Attendance (%)")

# Display grid
plt.grid(True)

plt.show()

# Create another scatter plot
plt.figure(figsize=(8, 5))

plt.scatter(df['Attendance'], df['Marks'],
            color='red',
            marker='o',
            s=80)

plt.title("Attendance vs Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")

plt.grid(True)
plt.show()

'''
LO=
1.	Learned to create scatter plots.
2.	Understood relationships between numerical variables.
3.	Identified patterns and trends in data.
'''
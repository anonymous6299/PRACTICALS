'''
AIM= Exploring Data Visualization tools 

REL. THEORY=
Data visualization tools help represent data graphically for better understanding and analysis. Python provides libraries such as Matplotlib, Seaborn, and Pandas to create charts, graphs, and statistical visualizations. These tools make complex data easier to interpret.

CODE=                                                                '''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create sample dataset
data = {
    'Student': ['A', 'B', 'C', 'D', 'E'],
    'Marks': [85, 70, 90, 65, 80],
    'Attendance': [90, 75, 95, 60, 85]
}

df = pd.DataFrame(data)

# Display dataset
print("Student Dataset:")
print(df)

# 1. Bar Chart
plt.figure(figsize=(7, 4))
plt.bar(df['Student'], df['Marks'])
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 2. Line Chart
plt.figure(figsize=(7, 4))
plt.plot(df['Student'], df['Attendance'], marker='o')
plt.title("Student Attendance - Line Chart")
plt.xlabel("Students")
plt.ylabel("Attendance (%)")
plt.show()

# 3. Scatter Plot
plt.figure(figsize=(7, 4))
plt.scatter(df['Attendance'], df['Marks'])
plt.title("Marks vs Attendance")
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")
plt.show()

# 4. Histogram
plt.figure(figsize=(7, 4))
plt.hist(df['Marks'], bins=5, edgecolor='black')
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 5. Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df[['Marks', 'Attendance']].corr(),
            annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()


'''
LO=
1.	Explored different visualization libraries.
2.	Learned to create basic visualizations.
3.	Understood graphical data representation.
'''
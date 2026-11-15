'''
AIM=Understanding Data Visualization frameworks

REL. THEORY=
Data visualization frameworks provide tools for representing and analyzing information graphically. Python offers frameworks such as Matplotlib, Seaborn, and Plotly for creating static, statistical, and interactive visualizations. These frameworks make data analysis more effective and understandable.

CODE=                                                                '''
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd

# Create sample dataset
data = {
    'Student': ['A', 'B', 'C', 'D', 'E'],
    'Marks': [85, 70, 90, 65, 80],
    'Attendance': [90, 75, 95, 60, 85]
}

df = pd.DataFrame(data)

# Display dataset
print("Student Performance Dataset:")
print(df)

# 1. Using Matplotlib
plt.figure(figsize=(7, 4))
plt.bar(df['Student'], df['Marks'],
        color='skyblue', edgecolor='black')
plt.title("Matplotlib - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 2. Using Seaborn
plt.figure(figsize=(7, 4))
sns.scatterplot(data=df, x='Attendance',
                y='Marks', hue='Student', s=100)
plt.title("Seaborn - Scatter Plot")
plt.show()

# 3. Using Plotly
fig = px.line(
    df,
    x='Student',
    y='Marks',
    title='Plotly - Interactive Line Chart',
    markers=True
)

fig.show()

# 4. Using Seaborn Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(
    df[['Marks', 'Attendance']].corr(),
    annot=True,
    cmap='coolwarm'
)
plt.title("Seaborn - Correlation Heatmap")
plt.show()



'''
LO=
1.	Explored different Python visualization frameworks.
2.	Created static and interactive visualizations.
3.	Understood the applications of visualization libraries.
'''
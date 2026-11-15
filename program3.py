'''
AIM=Drawing Charts

REL. THEORY=
Charts are graphical representations of data used to compare values and identify patterns. Different charts, such as bar charts, pie charts, line charts, histograms, and scatter plots, serve different purposes. Python Matplotlib provides functions to create and customize these charts.

CODE=                                                                '''

import matplotlib.pyplot as plt

# Sample data
subjects = ['Python', 'Java', 'C++', 'DBMS', 'OS']
marks = [85, 75, 90, 80, 70]

# 1. Bar Chart
plt.figure(figsize=(7, 5))
plt.bar(subjects, marks, color='skyblue', edgecolor='black')
plt.title("Subject-wise Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 2. Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(marks, labels=subjects, autopct='%1.1f%%',
        startangle=90)
plt.title("Marks Distribution")
plt.show()

# 3. Line Chart
plt.figure(figsize=(7, 5))
plt.plot(subjects, marks, marker='o',
         linestyle='-', color='green')
plt.title("Line Chart of Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# 4. Histogram
plt.figure(figsize=(7, 5))
plt.hist(marks, bins=5, color='orange',
         edgecolor='black')
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot
plt.figure(figsize=(7, 5))
plt.scatter(subjects, marks, color='red',
            marker='o', s=100)
plt.title("Scatter Plot of Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()


'''
LO=
1.Learned to create different types of charts.
2.Understood chart customization techniques.
3.Improved data comparison and interpretation skills.


'''
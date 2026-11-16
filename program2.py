'''
AIM=To plot the probability distribution curve.

REL. THEORY=
A probability distribution describes the possible values of a random variable and their associated probabilities. A probability distribution curve represents this relationship graphically. Normal distribution is a common example, characterized by its bell-shaped curve. Python libraries such as NumPy, SciPy, and Matplotlib help calculate probabilities and visualize distribution curves.

CODE=                                                                '''
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, 0, 1)
plt.plot(x, y, label='Normal Distribution')
plt.title('Probability Distribution Curve')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()
plt.show()

'''
LO=
1. Understand the concept of probability distributions.
2. Learn to calculate and analyze probability distributions.
3. Develop skills in plotting distribution curves using Python libraries.
'''

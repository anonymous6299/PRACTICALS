'''
AIM= Write a MATLAB/Python function that computes the value of the Gaussian distribution N(m,s) at given vector
X and plot the effect of varying mean and variance to the normal distribution.

REL. TH.=Gaussian distribution, also known as normal distribution, is a continuous probability distribution that represents data around a central mean value. It is defined by two parameters: mean and variance. The mean determines the centre of the curve, while variance controls its spread. Python libraries such as NumPy and Matplotlib are used to calculate and visualize Gaussian distributions with different parameters.

CODE=
'''
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate Gaussian distribution
def gaussian(X, m, s):
    return (1 / np.sqrt(2 * np.pi * s)) * np.exp(
        -((X - m) ** 2) / (2 * s)
    )

# Generate values of X
X = np.linspace(-10, 10, 500)

# Plot effect of varying mean
plt.figure(figsize=(10, 5))

for m in [-3, 0, 3]:
    Y = gaussian(X, m, 1)
    plt.plot(X, Y, label=f'Mean = {m}')

plt.title("Effect of Varying Mean")
plt.xlabel("X")
plt.ylabel("Probability Density")
plt.legend()
plt.grid()
plt.show()

# Plot effect of varying variance
plt.figure(figsize=(10, 5))

for s in [0.5, 1, 2, 4]:
    Y = gaussian(X, 0, s)
    plt.plot(X, Y, label=f'Variance = {s}')

plt.title("Effect of Varying Variance")
plt.xlabel("X")
plt.ylabel("Probability Density")
plt.legend()
plt.grid()
plt.show()
'''
LO=
1. Understand the concept of Gaussian distribution.
2. Explore the effects of mean and variance.
3. Visualize normal distribution using Python.
'''
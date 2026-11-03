
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

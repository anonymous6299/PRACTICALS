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

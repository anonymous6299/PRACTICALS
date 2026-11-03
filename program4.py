import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 10, 100)
y1 = x
y2 = x ** 2
y3 = np.sin(x)
y4 = np.cos(x)

# 1. Linear Graph
plt.figure(figsize=(7, 5))
plt.plot(x, y1, label='y = x')
plt.title("Linear Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# 2. Quadratic Graph
plt.figure(figsize=(7, 5))
plt.plot(x, y2, color='red', label='y = x²')
plt.title("Quadratic Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# 3. Sine Graph
plt.figure(figsize=(7, 5))
plt.plot(x, y3, color='green', label='y = sin(x)')
plt.title("Sine Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# 4. Cosine Graph
plt.figure(figsize=(7, 5))
plt.plot(x, y4, color='orange', label='y = cos(x)')
plt.title("Cosine Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# 5. Multiple Graphs
plt.figure(figsize=(8, 5))
plt.plot(x, y1, label='Linear')
plt.plot(x, y2, label='Quadratic')
plt.plot(x, y3, label='Sine')
plt.plot(x, y4, label='Cosine')
plt.title("Combined Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Define the cost function
def cost_function(x):
    return x**2

# Define the gradient (derivative)
def gradient(x):
    return 2*x

# Initialize parameters
x = 10
learning_rate = 0.1
iterations = 50

# Store values for plotting
x_values = []
cost_values = []

# Gradient Descent Algorithm
for i in range(iterations):
    x_values.append(x)
    cost_values.append(cost_function(x))

    x = x - learning_rate * gradient(x)

    print(f"Iteration {i+1}: x = {x:.4f}, Cost = {cost_function(x):.4f}")

# Display final result
print("\nMinimum value of x:", round(x, 4))
print("Minimum cost:", round(cost_function(x), 4))

# Plot cost function
X = np.linspace(-10, 10, 200)
Y = cost_function(X)

plt.figure(figsize=(10, 5))
plt.plot(X, Y, label="Cost Function")
plt.scatter(x_values, cost_values, color='red',
            label="Gradient Descent Steps")
plt.title("Gradient Descent Optimization")
plt.xlabel("x")
plt.ylabel("Cost")
plt.legend()
plt.grid()
plt.show()

# Plot convergence
plt.figure(figsize=(10, 5))
plt.plot(range(iterations), cost_values, marker='o')
plt.title("Gradient Descent Convergence")
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.grid()
plt.show()

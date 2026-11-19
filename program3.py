'''
AIM=Implementation of Linear Regression using Gradient descent. 

REL. TH.=Linear Regression is a supervised machine learning algorithm used to establish a relationship between independent and dependent variables. It represents this relationship using a straight-line equation. Gradient descent is used to optimize the model parameters by minimizing the mean squared error. The trained model can predict continuous numerical values from input data.

CODE=
'''
import numpy as np
import matplotlib.pyplot as plt

# Generate sample dataset
X = np.array([1, 2, 3, 4, 5, 6, 7, 8])
Y = np.array([2, 4, 5, 4, 5, 7, 8, 9])

# Initialize parameters
m = 0
b = 0
learning_rate = 0.01
iterations = 1000
n = len(X)

# Gradient Descent
for i in range(iterations):
    Y_pred = m * X + b

    # Calculate gradients
    dm = (-2/n) * np.sum(X * (Y - Y_pred))
    db = (-2/n) * np.sum(Y - Y_pred)

    # Update parameters
    m = m - learning_rate * dm
    b = b - learning_rate * db

    # Calculate cost
    cost = np.mean((Y - Y_pred) ** 2)

    if (i + 1) % 100 == 0:
        print(f"Iteration {i+1}: Cost = {cost:.4f}")

# Display final parameters
print("\nSlope (m):", round(m, 4))
print("Intercept (b):", round(b, 4))

# Predict values
Y_pred = m * X + b

# Plot original data and regression line
plt.figure(figsize=(8, 5))
plt.scatter(X, Y, color='blue', label='Actual Data')
plt.plot(X, Y_pred, color='red', label='Regression Line')

plt.title("Linear Regression using Gradient Descent")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.grid()
plt.show()
'''
LO=
1. Understand the concept of linear regression.
2. Implement gradient descent for model training.
3. Predict continuous values using a trained model.
'''
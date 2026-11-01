import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
# Dataset
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([30, 35, 40, 45, 50, 55, 60, 65, 70, 75])
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size=0.2, random_state=42
)
# Create model
model = LinearRegression()
# Train model
model.fit(X_train, y_train)
# Prediction
y_pred = model.predict(X_test)
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("\nActual values:")
print(y_test)
print("\nPredicted values:")
print(y_pred)
print("\nMean Squared Error:",
 mean_squared_error(y_test, y_pred))
print("R2 Score:",
 r2_score(y_test, y_pred))
# Plot
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Simple Linear Regression")
plt.legend()
plt.show()

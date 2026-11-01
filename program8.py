
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 5, 4, 5])
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
print("Slope:", round(model.coef_[0], 2))
print("Intercept:", round(model.intercept_, 2))
print("Predicted Values:", np.round(y_pred, 2))
print("R-squared Score:", round(model.score(X, y), 2))
print("Prediction for X = 6:", round(model.predict([[6]])[0], 2))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, y_pred, color='red', label='Regression Line')
plt.title('Linear Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()

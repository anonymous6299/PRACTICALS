'''
AIM=To perform linear regression on datasets.

REL. THEORY=
Linear regression is a supervised machine learning technique used to model the relationship between a dependent variable and one or more independent variables. It fits a linear equation to observed data and predicts numerical outcomes. Model performance can be evaluated using metrics such as R-squared and mean squared error. Python's Scikit-learn library supports implementation.

CODE=                                                                '''
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
'''
LO=
1. Understand the concept of linear regression and its applications.
2. Learn to establish relationships between dependent and independent variables.
3. Develop skills in building and evaluating linear regression models using Python.
'''
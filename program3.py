'''
AIM=Program to demonstrate Logistic Regression 

REL. THEORY=
Logistic Regression is a supervised machine learning algorithm used for classification problems. It predicts the probability of an outcome using the logistic (sigmoid) function and classifies data into categories, usually binary classes such as 0 and 1.

CODE=                                                                '''
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
# Use two classes for binary classification
X = X[y != 2]
y = y[y != 2]
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size=0.2, random_state=42
)
# Create model
model = LogisticRegression(max_iter=200)
# Train
model.fit(X_train, y_train)
# Prediction
y_pred = model.predict(X_test)
print("Actual values:")
print(y_test)
print("\nPredicted values:")
print(y_pred)
print("\nAccuracy:",
 accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

'''
LO=
1. Understand the concept of Logistic Regression.
2. Implement a classification model using Python.
3. Predict and evaluate categorical outcomes.

'''
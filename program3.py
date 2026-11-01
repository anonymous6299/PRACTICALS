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
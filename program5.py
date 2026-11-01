from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
# Split data
X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size=0.2, random_state=42
)
# Create KNN model
k = 5
model = KNeighborsClassifier(n_neighbors=k)
# Train
model.fit(X_train, y_train)
# Prediction
y_pred = model.predict(X_test)
print("K =", k)
print("\nActual values:")
print(y_test)
print("\nPredicted values:")
print(y_pred)
print("\nAccuracy:",
 accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
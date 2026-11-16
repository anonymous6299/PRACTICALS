'''
AIM=Program to demonstrate k-Nearest Neighbor flowers classification 

REL. THEORY=
K-Nearest Neighbor (KNN) is a supervised machine learning algorithm used for classification. It classifies a new data point based on the majority class of its K nearest neighbors. In flower classification, it uses flower features such as petal and sepal length to predict the flower species.

CODE=                                                                '''
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

'''
LO=
1. Understand the working of the KNN algorithm.
2. Classify flowers based on their features.
3. Evaluate classification accuracy using Python.
'''
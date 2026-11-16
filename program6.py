'''
AIM=Program to demonstrate Naïve- Bayes Classifier 

REL. THEORY=
Naïve Bayes is a supervised machine learning algorithm used for classification based on Bayes' theorem. It assumes that all features are independent of each other. It calculates the probability of different classes and assigns a data point to the class with the highest probability.

CODE=                                                                '''
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size=0.2, random_state=42
)
# Create Gaussian Naive Bayes model
model = GaussianNB()
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
1. Understand the working of the Naïve Bayes classifier.
2. Learn the application of Bayes' theorem in classification.
3. Perform classification and evaluate model accuracy.
'''
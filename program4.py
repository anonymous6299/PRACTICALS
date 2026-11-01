from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt
# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size=0.2, random_state=42
)
# ID3 uses entropy as criterion
model = DecisionTreeClassifier(
 criterion="entropy",
 random_state=42
)
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
# Display tree
plt.figure(figsize=(12, 8))
tree.plot_tree(
 model,
 feature_names=iris.feature_names,
 class_names=iris.target_names,
 filled=True
)
plt.show()
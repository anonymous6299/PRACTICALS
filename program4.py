
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense

# Load handwritten digits dataset
digits = load_digits()
X = digits.images
Y = digits.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42, stratify=Y
)

# ---------------- SVM CLASSIFIER ----------------

# Flatten images for SVM
X_train_svm = X_train.reshape(len(X_train), -1)
X_test_svm = X_test.reshape(len(X_test), -1)

# Standardize data
scaler = StandardScaler()
X_train_svm = scaler.fit_transform(X_train_svm)
X_test_svm = scaler.transform(X_test_svm)

# Train SVM model
svm = SVC(kernel='rbf')
svm.fit(X_train_svm, y_train)

# SVM prediction
svm_pred = svm.predict(X_test_svm)
svm_accuracy = accuracy_score(y_test, svm_pred)

print("SVM Accuracy:", round(svm_accuracy * 100, 2), "%")

# ---------------- CNN CLASSIFIER ----------------

# Normalize and reshape images
X_train_cnn = X_train.reshape(-1, 8, 8, 1) / 16.0
X_test_cnn = X_test.reshape(-1, 8, 8, 1) / 16.0

# Build CNN model
cnn = Sequential([
    Conv2D(32, (3, 3), activation='relu',
           input_shape=(8, 8, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile model
cnn.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

# Train CNN model
cnn.fit(X_train_cnn, y_train,
        epochs=20, batch_size=32, verbose=0)

# Evaluate CNN model
loss, cnn_accuracy = cnn.evaluate(
    X_test_cnn, y_test, verbose=0
)

print("CNN Accuracy:", round(cnn_accuracy * 100, 2), "%")

# ---------------- COMPARISON ----------------

models = ['SVM', 'CNN']
accuracies = [svm_accuracy * 100, cnn_accuracy * 100]

plt.figure(figsize=(8, 5))
plt.bar(models, accuracies, width=0.5)

plt.title("SVM vs CNN Classification Accuracy")
plt.xlabel("Classification Models")
plt.ylabel("Accuracy (%)")
plt.ylim(0, 100)

for i, value in enumerate(accuracies):
    plt.text(i, value + 1, f'{value:.2f}%',
             ha='center')

plt.grid(axis='y')
plt.show()

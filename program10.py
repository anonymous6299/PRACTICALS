
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pickle
import os

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense, Dropout

# Dataset folder path
DATASET_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "cifar-10-batches-py"
)

# Function to load CIFAR-10 batch
def load_batch(file_path):
    with open(file_path, "rb") as file:
        batch = pickle.load(file, encoding="bytes")

    images = batch[b"data"].reshape(-1, 3, 32, 32)
    images = images.transpose(0, 2, 3, 1)
    labels = np.array(batch[b"labels"])

    return images, labels

# Load training dataset
X_train_list = []
y_train_list = []

for i in range(1, 6):
    X, y = load_batch(
        os.path.join(DATASET_PATH, f"data_batch_{i}")
    )
    X_train_list.append(X)
    y_train_list.append(y)

X_train = np.concatenate(X_train_list)
y_train = np.concatenate(y_train_list)

# Load testing dataset
X_test, y_test = load_batch(
    os.path.join(DATASET_PATH, "test_batch")
)

# Reshape labels
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)

print("CIFAR-10 Dataset Loaded Successfully!")
print("Training Images:", X_train.shape)
print("Testing Images:", X_test.shape)

# Define class names
class_names = [
    'Airplane', 'Automobile', 'Bird', 'Cat', 'Deer',
    'Dog', 'Frog', 'Horse', 'Ship', 'Truck'
]

# Normalize image data
X_train = X_train / 255.0
X_test = X_test / 255.0

# Build CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu',
           input_shape=(32, 32, 3)),
    MaxPooling2D((2, 2)),

    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),

    Conv2D(128, (3, 3), activation='relu'),
    Flatten(),

    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Display model summary
model.summary()

# Train CNN model
model.fit(
    X_train, y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.1
)

# Evaluate model
loss, accuracy = model.evaluate(X_test, y_test)

print("\nTest Accuracy:", accuracy * 100, "%")
print("Test Loss:", loss)

# Predict sample images
predictions = model.predict(X_test[:5])

print("\nImage Classification Results:")

for i in range(5):
    predicted_class = np.argmax(predictions[i])
    actual_class = y_test[i][0]

    print("Predicted:", class_names[predicted_class])
    print("Actual:", class_names[actual_class])
    print()

# Display sample images
plt.figure(figsize=(10, 5))

for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(X_test[i])
    plt.title(class_names[np.argmax(predictions[i])])
    plt.axis('off')

plt.tight_layout()
plt.show()

print("CNN Computer Vision Program Completed!")

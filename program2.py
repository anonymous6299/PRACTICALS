# Import required libraries
import tensorflow as tf
import keras
import torch

# Display library versions
print("TensorFlow Version:", tf.__version__)
print("Keras Version:", keras.__version__)
print("PyTorch Version:", torch.__version__)

# TensorFlow example
print("\n--- TensorFlow ---")
a = tf.constant(10)
b = tf.constant(20)
print("Addition:", tf.add(a, b).numpy())

# Keras example
print("\n--- Keras ---")
model = keras.Sequential([
    keras.layers.Dense(8, activation='relu', input_shape=(4,)),
    keras.layers.Dense(1, activation='sigmoid')
])

model.summary()

# PyTorch example
print("\n--- PyTorch ---")
x = torch.tensor([10, 20, 30])
y = torch.tensor([1, 2, 3])

result = x + y

print("Tensor:", x)
print("Addition:", result)
print("Multiplication:", x * y)

print("\nAll libraries executed successfully!")
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

# Sample text dataset
sentences = [
    "I love machine learning",
    "Deep learning is very interesting",
    "Python is easy to learn",
    "I enjoy artificial intelligence",
    "This is a great experience",
    "I hate wasting my time",
    "The movie was very boring",
    "This is a bad experience",
    "I dislike this program",
    "The service is very poor"
]

# Labels: 1 = Positive, 0 = Negative
labels = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])

# Initialize tokenizer
tokenizer = Tokenizer(num_words=1000)
tokenizer.fit_on_texts(sentences)

# Convert text into sequences
sequences = tokenizer.texts_to_sequences(sentences)

# Apply padding
max_length = 6
X = pad_sequences(
    sequences, maxlen=max_length, padding='post'
)

# Build LSTM model
model = Sequential([
    Embedding(input_dim=1000, output_dim=32),
    LSTM(32),
    Dropout(0.3),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train model
model.fit(X, labels, epochs=100, verbose=1)

# Display model summary
model.summary()

# Test new sentences
test_sentences = [
    "I love deep learning",
    "This program is boring",
    "Python is interesting",
    "I hate this experience"
]

# Convert test sentences
test_sequences = tokenizer.texts_to_sequences(test_sentences)
test_data = pad_sequences(
    test_sequences, maxlen=max_length, padding='post'
)

# Predict results
predictions = model.predict(test_data)

print("\nNLP Text Classification Results:")

for i in range(len(test_sentences)):
    result = "Positive" if predictions[i][0] >= 0.5 else "Negative"
    print(test_sentences[i], ":", result)

print("\nNLP Model Execution Completed!")
''' 
AIM= Train a sentiment analysis model on IMDB dataset, use RNN layers with LSTM/GRU   

REL. THEORY=
Sentiment Analysis is a Natural Language Processing technique used to identify opinions and emotions expressed in text. Recurrent Neural Networks process sequential data, while LSTM and GRU networks help capture long-term dependencies. The IMDB dataset contains movie reviews labelled as positive or negative. Deep learning models can use this dataset to classify the sentiment of reviews.



CODE=                                     '''
import tensorflow as tf
import numpy as np
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, GRU, Dense, Dropout
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Set parameters
vocab_size = 10000
max_length = 200

# Load IMDB dataset
(X_train, y_train), (X_test, y_test) = imdb.load_data(
    num_words=vocab_size
)

# Pad sequences
X_train = pad_sequences(
    X_train, maxlen=max_length, padding='post'
)

X_test = pad_sequences(
    X_test, maxlen=max_length, padding='post'
)

# Build RNN model using LSTM and GRU
model = Sequential([
    Embedding(vocab_size, 64),
    LSTM(64, return_sequences=True),
    Dropout(0.3),
    GRU(32),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Display model summary
model.summary()

# Train model
history = model.fit(
    X_train,
    y_train,
    epochs=3,
    batch_size=64,
    validation_split=0.2
)

# Evaluate model
loss, accuracy = model.evaluate(X_test, y_test)

print("\nTest Loss:", loss)
print("Test Accuracy:", accuracy * 100, "%")

# Predict sentiment
predictions = model.predict(X_test[:5])

print("\nSentiment Predictions:")

for i in range(5):
    sentiment = "Positive" if predictions[i][0] >= 0.5 else "Negative"

    print("Review", i + 1, ":", sentiment)
    print("Actual:", "Positive" if y_test[i] == 1 else "Negative")

print("\nSentiment Analysis Completed!")


'''
LO=
1. Understood sentiment analysis using NLP.
2. Implemented LSTM and GRU layers.
3. Classified movie reviews as positive or negative.
'''
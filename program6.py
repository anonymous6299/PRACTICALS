import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Bidirectional, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Training data
questions = [
    "hello", "hi", "how are you",
    "what is your name", "what can you do",
    "good morning", "bye", "thank you",
    "what is machine learning", "what is AI"
]

answers = [
    "hello how can I help you",
    "hi nice to meet you",
    "I am fine thank you",
    "I am a chatbot",
    "I can answer your questions",
    "good morning",
    "goodbye have a nice day",
    "you are welcome",
    "machine learning helps computers learn",
    "AI stands for artificial intelligence"
]

# Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(questions + answers)

input_seq = tokenizer.texts_to_sequences(questions)
output_seq = tokenizer.texts_to_sequences(answers)

# Padding sequences
max_len = max(max(map(len, input_seq)),
              max(map(len, output_seq)))

X = pad_sequences(input_seq, maxlen=max_len, padding='post')
Y = pad_sequences(output_seq, maxlen=max_len, padding='post')

# Prepare target output
vocab_size = len(tokenizer.word_index) + 1

# Convert output into categorical format
Y = tf.keras.utils.to_categorical(Y, num_classes=vocab_size)

# Build Bi-LSTM model
model = Sequential([
    Embedding(vocab_size, 64, input_length=max_len),
    Bidirectional(LSTM(64)),
    Dense(max_len * vocab_size, activation='softmax'),
    tf.keras.layers.Reshape((max_len, vocab_size))
])

# Compile model
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train model
model.fit(X, Y, epochs=200, verbose=1)

print("\nChatbot Training Completed!")

# Chatbot response function
def chatbot_response(text):
    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=max_len, padding='post')

    prediction = model.predict(padded, verbose=0)
    predicted_words = np.argmax(prediction[0], axis=1)

    response = []
    for word_id in predicted_words:
        word = tokenizer.index_word.get(word_id)
        if word is not None:
            response.append(word)

    return " ".join(response)

# Interact with chatbot
print("\nChatbot is ready! Type 'exit' to stop.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = chatbot_response(user_input)
    print("Chatbot:", response)
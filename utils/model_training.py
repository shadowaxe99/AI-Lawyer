
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read().replace('\n', '')
    return data

def create_tokenizer(data):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts([data])
    return tokenizer

def create_model(tokenizer):
    total_words = len(tokenizer.word_index) + 1

    model = Sequential()
    model.add(Embedding(total_words, 100, input_length=20, trainable=True))
    model.add(LSTM(150, return_sequences=True))
    model.add(LSTM(100))
    model.add(Dense(total_words, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def train_model(model, predictors, label, epochs=100):
    model.fit(predictors, label, epochs=epochs, verbose=1)

def save_model(model, model_path):
    model.save(model_path)

if __name__ == "__main__":
    data = load_data("../data/contracts/contract1.txt")
    tokenizer = create_tokenizer(data)
    model = create_model(tokenizer)
    predictors, label = prepare_sequences(data, tokenizer)
    train_model(model, predictors, label)
    save_model(model, "../models/contract_model.h5")

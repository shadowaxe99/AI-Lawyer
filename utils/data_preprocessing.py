
import os
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def load_data(directory):
    data = ""
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as f:
            data += f.read()
    return data

def preprocess_data(data, vocab_size=10000, oov_token="<OOV>", max_length=100, trunc_type='post', padding_type='post'):
    tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_token)
    tokenizer.fit_on_texts([data])

    total_words = len(tokenizer.word_index) + 1

    input_sequences = []
    for line in data.split('\n'):
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i+1]
            input_sequences.append(n_gram_sequence)

    input_sequences = pad_sequences(input_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

    predictors, label = input_sequences[:,:-1],input_sequences[:,-1]
    label = tf.keras.utils.to_categorical(label, num_classes=total_words)

    return predictors, label, total_words, tokenizer

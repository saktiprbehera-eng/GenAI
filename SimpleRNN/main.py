# step 1 - Import libraries and load models
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model

# Load the IMDB dataset for word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# Load the trained model
model = load_model('simple_rnn_imdb.h5')

# step 2 - Define a function to preprocess the input text
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in encoded_review])

#Function to process user input
def process_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]  # 2 is for unknown words
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

### step 3 - Define prediction function
def predict_sentiment(review):
    # Preprocess the input review
    preprocessed_review = process_text(review)

    # Make prediction
    prediction = model.predict(preprocessed_review)

    # Interpret the prediction
    sentiment = 'Positive' if prediction[0][0] > 0.5 else 'Negative'
    return sentiment, prediction[0][0]


import streamlit as st
## streamlit app
st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a Movie review to classify it as Positive or Negative')

# User input
user_input = st.text_area('Enter your review here:')

if st.button('Classify'):
    preprocess_input=process_text(user_input)

    ## Make prediction
    prediction=model.predict(preprocess_input)

    sentiment='Positive' if prediction[0][0] > 0.5 else 'Negative'
    st.write(f'The sentiment of the review is: {sentiment} (Confidence: {prediction[0][0]:.2f})')
else:
    st.write('Please enter a review and click "Classify" to see the sentiment.')
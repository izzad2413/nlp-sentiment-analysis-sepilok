import streamlit as st
import pickle
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re

nltk.download('stopwords')
nltk.download('wordnet')

STOPWORDS = set(stopwords.words("english"))

def load_model():
    # Get the saved models
    try:
        predictor = pickle.load(open("models/model_rf.pkl", "rb"))
        scaler = pickle.load(open("models/scaler.pkl", "rb"))
        cv = pickle.load(open("models/cv.pkl", "rb"))
        return predictor, scaler, cv
    except FileNotFoundError:
        st.error("Model files are missing. Ensure 'model_rf.pkl', 'scaler.pkl', and 'cv.pkl' are in the 'models/' directory.")
        return None, None, None


def predict(predictor, scaler, cv, text_input):
    # Clean and preprocess the text input
    corpus = []
    lemmatizer = WordNetLemmatizer()
    review = re.sub('[^a-zA-Z]', ' ', text_input)
    review = review.lower().split()
    review = [lemmatizer.lemmatize(word) for word in review if not word in STOPWORDS]
    review = ' '.join(review)
    corpus.append(review)
    
    # Vectorize and scale the text
    x_pred = cv.transform(corpus).toarray()
    x_pred_scaled = scaler.transform(x_pred)
    
    # Get the probabilities for each class
    y_pred = predictor.predict_proba(x_pred_scaled)
    y_pred_class = y_pred.argmax(axis=1)[0]
    
    # Map the output to the corresponding sentiment
    sentiment_mapping = {
        0: "Negative",
        1: "Neutral",
        2: "Positive"
    }
    
    return y_pred_class, sentiment_mapping[y_pred_class]
    
    
def show_predict_page():
     
     st.title('Sentiment Analyzer at Sepilok Orangutan Sanctuary')
     st.write('The Sepilok Sentiment Analyzer is a cutting-edge application designed to evaluate visitor reviews of the Sepilok Orangutan Sanctuary. Using advanced natural language processing (NLP), it classifies reviews as positive or negative, enabling sanctuary staff to quickly assess visitor feedback. This tool ensures actionable insights, supporting enhanced visitor experiences and sanctuary management.')
     st.image('screenshot/project_design_thumbnail-modified.png')
     
     text_input = st.text_area('Enter a review:')
     
     if st.button('Predict Sentiment', key='predict_button'):
         predictor, scaler, cv = load_model()
         if predictor and scaler and cv:
             sentiment_class, sentiment_label = predict(predictor, scaler, cv, text_input)
             st.success(f"The predicted sentiment is: {sentiment_label} (Class {sentiment_class})")
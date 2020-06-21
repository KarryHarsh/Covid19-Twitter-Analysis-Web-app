import streamlit as st
import pandas as pd
import pickle

# title
import TweetNormalizer

st.title("Covid twitter analyzer")

# Header
st.header("header")
# sub header
st.subheader("subheader")

# text
st.text("text")

# Markdown
st.title("Tweet Analyzer 🔥")

def load_data():
    return pd.read_excel("dataset/predictv1.1.xlsx")

def data_precosess():
    df = load_data()
    df["clean_tweets"] = df["tweet"].apply(lambda x: TweetNormalizer.tweet_preprocessing(x))
    df.dropna(subset=['clean_tweets'], inplace=True)
    pred_texts = df['clean_tweets']
    return pred_texts

model = st.sidebar.selectbox("Select Classifier",("SVM","LSTM","Bertweet"))

if model == "SVM":
    model = pickle.load(open("Models/SVM_model.pkl", 'rb'))
    text = data_precosess()
    prediction = model.predict(text)
    st.write(len(prediction))






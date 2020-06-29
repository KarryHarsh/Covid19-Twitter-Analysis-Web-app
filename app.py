# -*- coding: utf-8 -*-

import sqlite3

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st
from wordcloud import WordCloud, STOPWORDS

import settings
from utiliy import get_file_content_as_string

st.header("Twitter Sentiment and Intent Analysis on Covid19 🦠 😷🔬")
st.sidebar.header("Twitter Sentiment and Intent Analysis on Covid19 🦠 😷🔬")

st.markdown(
    "This application is a Streamlit dashboard to analyze the Tweets on Covid19 🦠 😷🔬"
)

# Loading Dataset from Sqlite Database.
@st.cache(persist=True)
def load_data():
    db_connection = sqlite3.connect("TwitterDB")
    data = pd.read_sql_query(
        "SELECT * FROM {}".format("Twitter_covid19"), db_connection
    )
    data["created_at"] = pd.to_datetime(data["created_at"])
    return data


data = load_data()  # data loaded as dataframe

# Define The selection fields.
select = st.sidebar.selectbox(
    "Choice",
    [
        "Show Instructions",
        "Sentiment Analysis",
        "Intent Analysis",
        "Source Code",
        "About",
    ],
    key="main_select",
)
# Displays the Instructions and features of the application.
if select == "Show Instructions":
    st.markdown(get_file_content_as_string("Instructions.md"))

elif select == "Sentiment Analysis":
    # ******************Show Random Tweet by Sentiment***********************#
    st.sidebar.subheader("Show Random Tweet by Sentiment")
    random_tweet = st.sidebar.radio("Sentiment", ("positive", "negative", "neutral"))
    st.sidebar.markdown(
        data.query("sentiment == @random_tweet")[["text"]].sample(n=1).iat[0, 0]
    )
    # ******************Visualize No. of tweets by sentiment***********************#
    st.sidebar.markdown("### Visualize No. of tweets by sentiment")
    select = st.sidebar.selectbox(
        "Visualization type", ["Histogram", "Pie chart"], key="sentiviz"
    )
    sentiment_count = data["sentiment"].value_counts()
    sentiment_count = pd.DataFrame(
        {"Sentiment": sentiment_count.index, "Tweets": sentiment_count.values}
    )
    # Check box to hide the visualization until unchecked.
    if not st.sidebar.checkbox("Hide", True):
        st.markdown("### Visualize No. of tweets by sentiment")
        if select == "Histogram":
            fig = px.bar(sentiment_count, x="Sentiment", y="Tweets", height=500)
            st.plotly_chart(fig)

        elif select == "Pie chart":
            fig = px.pie(
                sentiment_count, values="Tweets", names="Sentiment", height=500
            )
            st.plotly_chart(fig)

    # ******************When and where are users tweeting from?***********************#
    st.sidebar.subheader("When and where are users tweeting from?")
    hour = st.sidebar.slider("Hour of day", 0, 23)
    modified_data = data[data["created_at"].dt.hour == hour]
    if not st.sidebar.checkbox("Close", True, key="tweettime"):
        st.markdown("### Tweets locations based on the time of day")
        st.markdown(
            "%i tweets between %i:00 and %i:00"
            % (len(modified_data), hour, (hour + 1) % 24)
        )
        st.map(modified_data)
        if st.sidebar.checkbox("Show raw data", False, key="time_df"):
            st.dataframe(modified_data)

    # ******************Dataset based on sentiment***********************#
    st.sidebar.subheader("Dataset based on sentiment")
    sentiment_choice = st.sidebar.selectbox(
        "select", data.sentiment.unique(), key="sentiment_df"
    )
    sentiment_df = data[data["sentiment"] == sentiment_choice]
    if st.sidebar.checkbox("Show raw data", False):
        st.dataframe(sentiment_df)

    # ******************Breakdown Country tweets by sentiment***********************#
    st.sidebar.subheader("Breakdown Country tweets by sentiment")
    choice = st.sidebar.multiselect(
        "Pick Country", data.user_location.unique(), key="0"
    )

    if len(choice) > 0:
        choice_data = data[data.user_location.isin(choice)]
        fig_choice = px.histogram(
            choice_data,
            x="user_location",
            y="sentiment",
            histfunc="count",
            color="sentiment",
            facet_col="sentiment",
            labels={"sentiment": "tweets"},
            height=600,
            width=800,
        )
        st.plotly_chart(fig_choice)

    # ******************Word Cloud***********************#
    st.sidebar.header("Word Cloud")
    word_sentiment = st.sidebar.radio(
        "Display word cloud for what sentiment?", data.sentiment.unique()
    )
    if not st.sidebar.checkbox("Close", True, key="senti_wordcloud"):
        st.subheader("word cloud for %s sentiment" % (word_sentiment))
        df1 = data[data["sentiment"] == word_sentiment]
        words = " ".join(df1["text"])
        processed_words = " ".join(
            [
                word
                for word in words.split()
                if "http" not in word and not word.startswith("@") and word != "RT"
            ]
        )
        wordcloud = WordCloud(
            stopwords=STOPWORDS, background_color="white", height=640, width=800
        ).generate(processed_words)
        plt.imshow(wordcloud)
        plt.xticks([])
        plt.yticks([])
        st.pyplot()

elif select == "Intent Analysis":
    # ******************SShow Random Tweet by Intent***********************#
    st.sidebar.subheader("Show Random Tweet by Intent")
    random_tweet = st.sidebar.radio("Intent", data.label.unique())
    st.sidebar.markdown(
        data.query("label == @random_tweet")[["text"]].sample(n=1).iat[0, 0]
    )

    # ******************SVisualize No. of tweets by Intent***********************#
    st.sidebar.markdown("### Visualize No. of tweets by Intent")
    select = st.sidebar.selectbox(
        "Visualization type", ["Histogram", "Pie chart"], key="intent_viz"
    )
    intent_count = data["label"].value_counts()
    intent_count = pd.DataFrame(
        {"Intent": intent_count.index, "Tweets": intent_count.values}
    )

    if not st.sidebar.checkbox("Hide", True, key="intent_checkbox"):
        st.markdown("### Visualize No. of tweets by Intent")
        if select == "Histogram":
            fig = px.bar(intent_count, x="Intent", y="Tweets", height=500)
            st.plotly_chart(fig)

        elif select == "Pie chart":
            fig = px.pie(intent_count, values="Tweets", names="Intent", height=500)
            st.plotly_chart(fig)

    # ******************Dataset filtered based on intent***********************#
    st.sidebar.subheader("Dataset filtered based on intent")
    Intent = st.sidebar.selectbox(
        "Select any", data.label.unique(), key="dataset_filter"
    )
    if not st.sidebar.checkbox("Close", True, key="dataset_filter_checkbox"):
        st.subheader("Data for %s" % (Intent))
        modified_data = data[data["label"] == Intent]
        st.dataframe(modified_data)

    # ******************Breakdown Country tweets by Intent***********************#
    st.sidebar.subheader("Breakdown Country tweets by Intent")
    choice = st.sidebar.multiselect(
        "Pick Country", data.user_location.unique(), key="0"
    )

    if len(choice) > 0:
        choice_data = data[data.user_location.isin(choice)]
        fig_choice = px.histogram(
            choice_data,
            x="user_location",
            y="label",
            histfunc="count",
            color="label",
            facet_col="label",
            labels={"label": "Intent"},
            height=600,
            width=2000,
        )
        st.plotly_chart(fig_choice)

    # ******************Word Cloud***********************#
    st.sidebar.header("Word Cloud")
    word_sentiment = st.sidebar.radio(
        "Display word cloud for what Intent?", data.label.unique()
    )
    if not st.sidebar.checkbox("Close", True, key="intent_wordcloud"):
        st.subheader("word cloud for %s Intent" % (word_sentiment))
        df1 = data[data["label"] == word_sentiment]
        words = " ".join(df1["text"])
        processed_words = " ".join(
            [
                word
                for word in words.split()
                if "http" not in word and not word.startswith("@") and word != "RT"
            ]
        )
        wordcloud = WordCloud(
            stopwords=STOPWORDS, background_color="white", height=640, width=800
        ).generate(processed_words)
        plt.imshow(wordcloud)
        plt.xticks([])
        plt.yticks([])
        st.pyplot()

elif select == "Source Code":
    # ******************Display Source Code***********************#
    st.info("---------------------------------------------Source Code-------------------------------------------")
    st.code(get_file_content_as_string("app.py"))

elif select == "About":
    # ******************About Developer***********************#
    st.subheader("About:Twitter Sentiment & Intent Analysis App on Coronavirus 🦠 😷🔬")
    st.info("Built with Streamlit,Textblob, LSTM based Intent recognizer & tweepy")
    st.markdown("### **Karry Harsh**")
    st.markdown("Gmail: [✉](karryharsh@gmail.com) ⬅ click")
    st.markdown("Linkedin: [🧑‍💼](https://www.linkedin.com/in/karryharsh/) ⬅ click")
    st.markdown("Github: [😺](https://karryharsh.github.io/)⬅ click")

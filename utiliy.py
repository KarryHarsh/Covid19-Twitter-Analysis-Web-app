import urllib
import streamlit as st
import googlemaps
import re
import settings


def clean_tweets(tweet):
    """
    Clean the tweet for sentiment prediction
    :param tweet: Single tweet
    :return: clean tweet
    """
    tweet = re.sub("RT @[\w]*:", "<user>", tweet)
    tweet = re.sub(r"@\w+", "<user>", tweet)
    tweet = re.sub(r"[-+]?[.\d]*[\d]+[:,.\d]*", "<number>", tweet)
    tweet = re.sub(r"https?:\/\/\S+\b|www\.(\w+\.)+\S*", "<url>", tweet)
    tweet = re.sub("#[\w]*:", "", tweet)
    tweet = re.sub(r"\W", " ", tweet)
    tweet = re.sub("â", "a", tweet)
    tweet = tweet.lower()
    return tweet


# Configuring Google api key
gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)


def lat_long(location):
    """
    Used to determine country Name and its latitude and longitude using Google Maps API.
    :param location:location of the user.
    :return: latitude, longitude and country
    """
    try:
        country = gmaps.geocode(location)[0]["formatted_address"].split(",")[-1].strip()
    except:
        country = None
    if country is not None:
        latitude = gmaps.geocode(location)[0]["geometry"]["location"]["lat"]
        longitude = gmaps.geocode(location)[0]["geometry"]["location"]["lng"]
    else:
        latitude = None
        longitude = None
    return latitude, longitude, country


def sentiment_val(value):
    """
    Label Sentiment based on ots sentiment polarity
    :param value: sentiment polarity Float
    :return: Sentiment: negative, positive or neutral
    """
    if value < float(0.0):
        return "negative"
    elif value == float(0.0):
        return "neutral"
    else:
        return "positive"


def deEmojify(text):
    """
    Strip all non-ASCII characters to remove Emoji characters
    """
    if text:
        return text.encode("ascii", "ignore").decode("ascii")
    else:
        return None


# Download a single file and make its content available as a string.
@st.cache(show_spinner=False)
def get_file_content_as_string(path):
    """
    Gets the respective file from Github to display in the web app.
    :param path: file name
    :return: display the file in webapp
    """
    url = "https://raw.githubusercontent.com/streamlit/demo-self-driving/master/" + path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")

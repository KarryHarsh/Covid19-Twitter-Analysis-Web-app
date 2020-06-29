import sqlite3

import nltk
import tweepy
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from utiliy import clean_tweets, lat_long, deEmojify, sentiment_val

try:
    nltk.data.find("vader_lexicon")
except LookupError:
    nltk.download("vader_lexicon")
import prediction
import settings


class MyStreamListener(tweepy.StreamListener):
    """
    Tweets are known as “status updates”. So the Status class in tweepy has properties describing the tweet.
    https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object.html
    """

    def on_status(self, status):
        """
        Extract info from tweets
        """

        if status.retweeted:
            # Avoid re-tweeted info, and only original tweets will be received
            return True
        # Extract attributes from each tweet
        id_str = status.id_str
        created_at = status.created_at
        text = deEmojify(status.text)  # Pre-processing the text
        label = prediction.predict(text)
        sentiment = sentiment_val(sia.polarity_scores(clean_tweets(text))["compound"])
        latitude, longitude, user_location = lat_long(deEmojify(status.user.location))

        # Store all data in Sqlite DB
        mycursor = mydb.cursor()
        if label[0] != "Not related or irrelevant" and user_location is not None:
            print(status.text)
            print("sentiment: {}".format(sentiment))
            print(
                "latitude {} longitude {} and user_location {}".format(
                    latitude, longitude, user_location
                )
            )
            print("label {}".format(label[0]))
            sql = (
                "INSERT INTO {} (id_str, created_at, text, user_location,longitude,"
                " latitude, sentiment, label) VALUES (?,?,?,?,?,?,?,?)".format(
                    settings.TABLE_NAME
                )
            )
            val = (
                id_str,
                created_at,
                text,
                user_location,
                longitude,
                latitude,
                sentiment,
                label[0],
            )
            mycursor.execute(sql, val)
            mydb.commit()

    def on_error(self, status_code):
        """
        Since Twitter API has rate limits, stop scraping data as it exceed to the threshold.
        """
        if status_code == 420:
            # return False to disconnect the stream
            return False


sia = SentimentIntensityAnalyzer()

mydb = sqlite3.connect("TwitterDB")
mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS {} ({})".format(
        settings.TABLE_NAME, settings.TABLE_ATTRIBUTES
    )
)
mydb.commit()
mycursor.close()

# Configuring twitter api key
auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET_KEY)
auth.set_access_token(settings.ACCESS_TOEKN, settings.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Create an Object for streaming twitter data
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener, verify=False)
myStream.filter(languages=["en"], track=settings.TRACK_WORDS)
# Close the Sqlite3 connection as it finished
# However, this won't be reached as the stream listener won't stop automatically
# Press STOP button to finish the process.
mydb.close()

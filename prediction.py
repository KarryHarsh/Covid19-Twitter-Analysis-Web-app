import pickle
import re

import settings

with open(settings.Model, "rb") as handle:
    model = pickle.load(handle)


def clean_tweet(tweet):
    """
    Clean the tweets before prediction
    :param tweet: Single tweet value
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
    return [tweet]


def predict(tweet):
    """
    predict the Intent of the text.
    :param text: tweet
    :return: Intent label
    """
    tweet = clean_tweet(tweet)
    tweet = model.predict(tweet)
    label = list(map(get_value, tweet))
    return label


# Key: code of intent and value: Intent label.
dict_labels = {
    0: "Disease signs or symptoms",
    1: "Disease transmission",
    2: "Prevention",
    3: "Treatment",
    4: "Deaths reports",
    5: "Affected people",
    6: "Other useful information",
    7: "Not related or irrelevant",
}


def get_value(x):
    """
    maps Intent label based on code.
    :param x: Intent code
    :return: Intent label
    """
    return list(dict_labels.values())[list(dict_labels.keys()).index(x)]

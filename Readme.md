# Covid19 Twitter Sentiment & Intent Analysis

## Table of contents
* [General info](#general-info)
* [Illustration](#illustration)
* [Run demo](#run-demo)
* [Package](#package)
* [Setup](#setup)
* [Feature](#feature)
* [Source](#source)

## General info
The project web application is used for Analysis of tweets **Sentiment** and **Intent** for **Covid19**.

## Illustration

## Run demo
```
pip install streamlit plotly wordcloud matplotlib
streamlit run https://raw.githubusercontent.com/KarryHarsh/Twitter-Covid19-Analysis-Web-app/master/app.py
```

## Project Package
Project is created with:
* Python = 3.7
* streamlit = 0.62.1
* plotly = 4.8.2
* matplotlib = 3.2.2
* wordcloud = 1.7.0
* nltk = 3.5
* tweepy = 3.8.0
* googlemaps = 4.4.1
* scikit-learn = 0.20.3

## Setup
#### Streamlit app
To run this project, install it locally using Conda environment:

```
$ mkdir <folder_name>
$ cd <folder_name>
$ git clone <URL>
$ conda create -n myenv python=3.7
$ conda activate myenv
$ pip install -r requirements.txt
$ streamlit run app.py
```

#### Tweepy and Googlemap API 
* Create an [twitter Developer](https://developer.twitter.com/en/apps) Account and generate API key and token. [refer](https://www.youtube.com/watch?v=vlvtqp44xoQ) 
* Sign-In [Google Cloud platform](https://cloud.google.com/) and genrate API key. [refer](https://www.youtube.com/watch?v=1JNwpp5L4vM)
* Provide The API token and key details in **settings.py**

```
ACCESS_TOEKN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
ACCESS_TOKEN_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
API_SECRET_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
GOOGLE_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```
**Note:**
Settings.py is the configuration setting file of the whole project Changing anything may break the code.

## Feature
* Get Graphical Insights of Covid19 tweets based on its sentiment and Intent.
* Analysis Tweets based on its time and Location.
* Create word clouds.
* Breakdown and visualize Country tweets based on its sentiment and Intent.

#### Future Scope
* Train the Intent Recognition model to predict Intent more accurately.
* More Analytical feature to visualize the social media trend on Covid19.

## Source
This app is inspired by various open-source contributors in the field of data science.
* Snehan Kekre: "Create Interactive Dashboards with Streamlit and Python" course in coursera.
* Srivatsan Srinivasan: [AIEngineering](https://www.youtube.com/channel/UCwBs8TLOogwyGd0GxHCp-Dw) YouTube
* Krish Naik: [Krish Naik](https://www.youtube.com/user/krishnaik06) YouTube
* JCharisTech & J-Secur1ty: [JCharisTech & J-Secur1ty](https://www.youtube.com/channel/UC2wMHF4HBkTMGLsvZAIWzRg) YouTube
* Chulong-Li: [Chulong-Li](https://medium.com/@ChulongLi) Medium

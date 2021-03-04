# twitter_sentimental_analysis

Python code to crawler and analyze tweeter data

## Getting started
 We will use tweepy to access and save tweeter data. In order to access the twitter api it is necessary to create an developer account and generate access tolkens
 
 Reference tutorial:
 https://realpython.com/twitter-bot-python-tweepy/
## Code Overview

### query_tweets.py
Initialize the credentials, query data on twitter and save as csv file

### analyze.py
We read the csv data into a Pandas dataset.

- The split_date() function splits the time stamp.

- generate_graphs() generates daily and hourly time stamped graphs of the number of tweets.

- In preprocess_tweets() we use Natural Language Toolkit NLTK (https://www.nltk.org/) to generate stop words which are passed into the tweet_processing() function which removes stop words, signs and lemmatizes the tweets.

- sentiment_graphs() generates daily and hourly time stamped graphs of the polarity and subjectivity of the tweets.

## Test Results
We tested the code on the hashtag #ImpeachmentBolsonaroUrgente for the date spam between 2021/02/23 and 2021/03/03 (yyyy/mm/dd).
On the tweet number we observe a spike of tweets on 02/27:

![impeachment_graphs](https://user-images.githubusercontent.com/68067140/109921221-d9a5ef00-7cfe-11eb-942a-a499e9f2cb9f.png)

A similar behaviour was observed on the average subjectivity of the tweets, but the same behaviours is not observed on the polarity of the tweets:

![sentiment](https://user-images.githubusercontent.com/68067140/109921317-078b3380-7cff-11eb-8a5a-419dab9f256f.png)


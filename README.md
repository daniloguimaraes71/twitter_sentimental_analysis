# twitter_sentimental_analysis

Python code to crawler and analyze tweeter data

## Getting started
 We will use tweepy to access and save tweeter data. In order to access the twitter api it is necessary to create an developer account and generate access tolkens
 
 Reference tutorial:
 https://realpython.com/twitter-bot-python-tweepy/

### query_tweets.py
Initialize the credentials, query data on twitter and save as csv file

### analyze.py
We read the csv data into a Pandas dataset.

- The split_date() function splits the time stamp.

- generate_graphs() generates daily and hourly time stamped graphs of the number of tweets.

- In preprocess_tweets() we use Natural Language Toolkit NLTK (https://www.nltk.org/) to generate stop words which are passed into the tweet_processing() function which removes stop words, signs and lemmatizes the tweets.

- sentiment_graphs() generates daily and hourly time stamped graphs of the polarity and subjectivity of the tweets.

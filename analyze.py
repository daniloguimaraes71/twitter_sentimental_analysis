import pandas as pd
from matplotlib import pyplot as plt
import nltk
from nltk.corpus import stopwords
from textblob import Word, TextBlob
import stanza
import numpy as np

def split_date(tweets):
    tweets.Time = pd.to_datetime(tweets.Time,format="%Y-%m-%d %H:%M:%S")
    
    tweets['year'] = tweets['Time'].dt.year
    tweets['day'] = tweets['Time'].dt.day
    tweets['month'] = tweets['Time'].dt.month
    tweets['hour'] = tweets['Time'].dt.hour
    tweets['minute'] = tweets['Time'].dt.minute
    tweets['second'] = tweets['Time'].dt.second

    return tweets

def number_tweets_graphs(tweets):
    # get day count of tweets
    daily_numbers = tweets.groupby(['month','day']).size().reset_index()
    daily_numbers = daily_numbers.rename(columns={0:'tweet_num'})
    daily_numbers['time'] = daily_numbers['month'].astype(str) +'/'+ daily_numbers['day'].astype(str)

    # get hourly count of tweets
    hourly_numbers = tweets.groupby(['month','day','hour']).size().reset_index()
    hourly_numbers = hourly_numbers.rename(columns={0:'tweet_num'})
    hourly_numbers['time'] = hourly_numbers['month'].astype(str) +'/'+ hourly_numbers['day'].astype(str) +':'+hourly_numbers['hour'].astype(str) + 'h'

    
    fig, axes = plt.subplots(2,1, figsize=(13,10))

    # plot daily values
    axes[0].plot(daily_numbers['time'],daily_numbers['tweet_num'])
    axes[0].set_title('\n'.join(['Daily tweet numbers']))
    # plot hourly values
    axes[1].plot(range(hourly_numbers['time'].shape[0]),hourly_numbers['tweet_num'], color='orange')
    indexes = [0]
    for i in range(0,hourly_numbers['time'].shape[0],25):
        indexes.append(i)
        
    axes[1].set_xticklabels(hourly_numbers['time'][indexes])
    axes[1].set_title('\n'.join(['Hourly tweet numbers']))
    fig.suptitle('\n'.join(['Tweet Number Data']))
    plt.savefig('graphs/tweet_num_graphs.png')
    plt.close()
def tweet_processing(tweet, stop_words, custom_stopwords,nlp):
    preprocessed = tweet
    preprocessed.replace('[^\w\s]','')
    preprocessed = ' '.join(word for word in preprocessed.split() if word not in stop_words)
    preprocessed = ' '.join(word for word in preprocessed.split() if word not in custom_stopwords)
    #preprocessed = ' '.join(Word(word).lemmatize() for word in preprocessed.split()) #use for English
    preprocessed = ' '.join(nlp(word).sentences[0].words[0].lemma for word in preprocessed.split()) #use for Portuguese

    return preprocessed

def preprocess_tweets(tweets):
    nltk.download('stopwords')
    nltk.download('wordnet')
    stanza.download('pt')
    nlp = stanza.Pipeline('pt')

    stop_words = stopwords.words('portuguese')
    custom_stopwords = ['RT', '#ImpeachmentBolsonaroUrgente']
    
    tweets['processed_tweets'] = tweets['Text'].apply(lambda x: tweet_processing(x, stop_words, custom_stopwords,nlp))

    tweets['polarity'] = tweets['processed_tweets'].apply(lambda x: TextBlob(x).sentiment[0])
    tweets['subjectivity'] = tweets['processed_tweets'].apply(lambda x: TextBlob(x).sentiment[1])

    #tweets.to_csv('lemmatized.csv')
    
    return tweets

def sentiment_graphs(tweets):
    # plot daily sentiment data
    tweets1 = tweets.groupby('day', sort=False)[['polarity','subjectivity']].agg(np.mean)
    tweets1 = tweets1.reset_index()

    fig,axes= plt.subplots(2,1, figsize=(8,8))

    indexes = [0]
    for i in range(tweets1.shape[0]):
        indexes.append(i)

    axes[0].plot(tweets1['polarity'])
    axes[0].set_xticklabels(tweets1['day'][indexes])
    axes[0].set_title('\n'.join(['Daily average polarity']))

    axes[1].plot(tweets1['subjectivity'], color='orange')
    axes[1].set_xticklabels(tweets1['day'][indexes])
    axes[1].set_title('\n'.join(['Daily average subjectivity']))
    fig.suptitle('\n'.join(['Tweet Daily Sentiment Data']))
    plt.savefig('graphs/sentiment_daily.png')
    #plt.show()
    plt.close()

    # plot hourly sentiment data
    tweets2 = tweets.groupby(['hour','day'], sort=False)[['polarity','subjectivity']].agg(np.mean)
    tweets2 = tweets2.reset_index()
    tweets2['time'] = tweets2['day'].astype(str)+':'+tweets2['hour'].astype(str)+'h'

    indexes = [0]
    for i in range(0,tweets2.shape[0],25):
        indexes.append(i)
    
    fig,axes= plt.subplots(2,1, figsize=(8,8))

    axes[0].plot(tweets2['polarity'])
    axes[0].set_xticklabels(tweets2['time'][indexes])
    axes[0].set_title('\n'.join(['Hourly average polarity']))

    axes[1].plot(tweets2['subjectivity'], color='orange')
    axes[1].set_xticklabels(tweets2['time'][indexes])
    axes[1].set_title('\n'.join(['Hourly average subjectivity']))
    fig.suptitle('\n'.join(['Tweet Hourly Sentiment Data']))
    plt.savefig('graphs/sentiment_hourly.png')
    #plt.show()
    plt.close()

# load csv with tweet data
tweets = pd.read_csv('csv_path')

# treat time data
tweets = split_date(tweets)

# generated graphs of tweets over time
number_tweets_graphs(tweets)

# preprocess tweets
preprocess_tweets(tweets)

# plot sentiment graphs
sentiment_graphs(tweets)


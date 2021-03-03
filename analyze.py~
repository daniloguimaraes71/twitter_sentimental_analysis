import pandas as pd
from matplotlib import pyplot as plt
import nltk
from nltk.corpus import stopwords
from textblob import Word, TextBlob
import stanza

def split_date(tweets):
    #tweets.Time = pd.to_datetime(tweets.Time,format="%Y-%m-%d %H:%M:%S")
    tweets.Time = pd.to_datetime(tweets.Time,format="%Y/%m/%d %H:%M")
    
    #tweets['year'] = tweets['Time'].dt.year
    tweets['day'] = tweets['Time'].dt.day
    tweets['month'] = tweets['Time'].dt.month
    tweets['hour'] = tweets['Time'].dt.hour
    #tweets['minute'] = tweets['Time'].dt.minute
    #tweets['second'] = tweets['Time'].dt.second

    return tweets

def generate_graphs(tweets):
    # get day count of tweets
    print('daily report')
    daily_numbers = tweets.groupby(['month','day']).size().reset_index()
    daily_numbers = daily_numbers.rename(columns={0:'tweet_num'})
    daily_numbers['time'] = daily_numbers['month'].astype(str) +'/'+ daily_numbers['day'].astype(str)
    
    # get hourly count of tweets
    print('hourly report')
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
    fig.suptitle('\n'.join(['Impeachment Hashtag Tweet Data Analysis']))
    plt.savefig('impeachment_graphs.png')

def preprocess_tweets(tweet, stop_words, custom_stopwords):
    stanza.download('pt')
    nlp = stanza.Pipeline('pt')
    
    preprocessed = tweet
    preprocessed.replace('[^\w\s]','')
    preprocessed = ' '.join(word for word in preprocessed.split() if word not in stop_words)
    preprocessed = ' '.join(word for word in preprocessed.split() if word not in custom_stopwords)
    #preprocessed = ' '.join(Word(word).lemmatize() for word in preprocessed.split())
    preprocessed = ' '.join(nlp(word).sentences[0].words[0].lemma for word in preprocessed.split())

    return preprocessed

def sentiment(tweets):
    nltk.download('stopwords')
    nltk.download('wordnet')
    stop_words = stopwords.words('portuguese')
    custom_stopwords = ['RT', '#ImpeachmentBolsonaroUrgente']

    tweets['processed_tweets'] = tweets['Text'].apply(lambda x: preprocess_tweets(x, stop_words, custom_stopwords))

    print(tweets['Text'][20])
    print(tweets['processed_tweets'][20])

# load csv with tweet data
tweets = pd.read_csv('impeachment_tweets.csv')

# treat time data
tweets = split_date(tweets)
generate_graphs(tweets)


sentiment(tweets)

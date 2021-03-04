import tweepy as tw
import numpy as np
import csv

#initialize twitter app credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Authenticate

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# tweet query and save csv
csvFile = open('output_path', 'a', encoding='utf-8-sig')
csvWriter = csv.writer(csvFile)

# set headers for each column
csvWriter.writerow(['Time','Text'])

# query hashtag and time spam
hashtag = ''

# save tweets to csv file
for tweet in tw.Cursor(api.search,q=hashtag, lang='pt', count=5000).items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text])

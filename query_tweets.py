import tweepy as tw
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import csv

#initialize twittter app credentials
consumer_key = 'HFYB89RBwdthbpEmyYHTESjEc'
consumer_secret = '2qP3SRd5XZpeQjUfWI8Wo3VE9WtXo15AiESkBflu61naYNoXVV'
access_token = '1170632448-JkrPEbz57K5Ifj8ZvqFShiNFFu5pLINwzkjpBcp'
access_token_secret = 'eDOFB6PalTHv1dW2NOX6KP3oDHwVlVkVmsGoVdtXo7qRa'

# Authenticate

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# tweet query and save csv
csvFile = open('impeachment_tweets3.csv', 'a', encoding='utf-8-sig')
csvWriter = csv.writer(csvFile)
# set headers for each column
#csvWriter.writerow(['Time','Text'])

# query hashtag and time spam
hashtag = '#ImpeachmentBolsonaroUrgente since:2021-02-23 until:2021-02-24'

# save tweets to csv file
for tweet in tw.Cursor(api.search,q=hashtag, lang='pt', count=5000).items():
    print(tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text])

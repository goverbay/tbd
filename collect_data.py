import json
import snscrape.modules.twitter as snttwitter
import tweepy
from pymongo import MongoClient
from key import *

#mongo
client = MongoClient('localhost', 27017)
db = client['tbdtubes']
collection = db['kematian_kurama_tweepy']

#api key
#imported from another file

#auth ke twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#key search
keysSearch = ['kematian kurama', 'kurama mati', 'kurama meninggal']

maxTweets = 1000000

# Collect tweets
# tweets = tweepy.Cursor(api.search_tweets,
#               q=keysSearch[0])

for tweet in api.search_tweets(q="kurama mati", since="2021-01-01"):
    print(tweet.text)
    collection.insert_one(tweet._json)
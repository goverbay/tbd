import json
import snscrape.modules.twitter as snttwitter
import tweepy
from pymongo import MongoClient
from key import *

#mongo
client = MongoClient('localhost', 27017)
db = client['tbdtubes']
collection = db['kurama_20_11']

#api key
#imported from another file

#auth ke twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#key search
keysSearch = ['kematian kurama', 'kurama mati', 'kurama meninggal','kurama', 'kyubi-kacau', 'kurama death', 'kyubi death', 'kyuubi death', 'death kyubi']

maxTweets = 1000000

for i, tweet in enumerate(snttwitter.TwitterSearchScraper('boruto chapter 56 + since:2021-01-01 until:2021-12-16').get_items()):
    print("=======================")
    print("sns scrape: ", tweet.id, tweet.date, tweet.content)
    try:
        tweepyTweet = api.get_status(tweet.id, tweet_mode="extended")
    except Exception as e:
        continue
    #print(tweepyTweet.created_at, tweepyTweet.full_text)
    json_str = json.dumps(tweepyTweet._json)
    print(json_str)
    collection.insert_one(tweepyTweet._json)

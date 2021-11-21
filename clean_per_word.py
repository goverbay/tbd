from httpcore._sync.base import ConnectionState
from pymongo import MongoClient
from googletrans import Translator
import nltk


client = MongoClient('localhost', 27017)
db = client['tbdtubes']
perWordCollection=db["kurama_per_word"]
translatedCollection=db["kurama_english"]

tweetKurama = translatedCollection.find()
for document in tweetKurama:
    print(document["tweet"])
    tokens = nltk.word_tokenize(document["tweet"]);        
    perWordCollection.insert_one({"created_at": document["created_at"], "tweet": tokens})
    print(tokens)


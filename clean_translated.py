from pymongo import MongoClient
from googletrans import Translator

client = MongoClient('localhost', 27017)
db = client['tbdtubes']
cleanCollection=db["kurama_clean"]
translatedCollection=db["kurama_english"]

# init the Google API translator
translator = Translator()

translatedCollection.drop()
tweetKurama = cleanCollection.find()
for document in tweetKurama:
    try:
        translation = translator.translate(document["tweet"])
        print(translation.text)
        translatedCollection.insert_one({"created_at": document["created_at"], "tweet": translation.text})
    except Exception as e:
        continue


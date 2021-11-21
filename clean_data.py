import re
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['tbdtubes']
allCollection=db["kurama_20_11"]
cleanCollection=db["kurama_clean"]

#proses cleansing
# cleanCollection.drop()
tweetkurama = allCollection.find()
for document in tweetkurama:
    document_properties = {}
    document_properties["created_at"] = document["created_at"]
    document_properties["tweet"] = document["full_text"]

    document_clean = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(https?:\/\/\S+)",
                     " ",document["full_text"]).split())

    print('=================================')
    print('created_at:',document["created_at"])
    print(document_clean)

    dataClean = {"created_at": document_properties["created_at"],"tweet":document_clean}
    cleanCollection.insert_one(dataClean)
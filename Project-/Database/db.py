from pymongo import MongoClient
from urllib.parse import quote_plus

password = quote_plus("951753!@")

uri = f"mongodb+srv://admin_hung:{password}@hung-c4e26-0zkua.mongodb.net/test?retryWrites=true"

#1.Connect
client = MongoClient(uri)

#2.Get database
db = client.test

#3. get collection
datahome_collection = db["data_luxhome"]

#4. create new document
# new_data = {}

#5. Insert new documnet into collection
# datahome_collection.insert_one(new_data)

#6. Close connection
def close():
    client.close()
client.close()
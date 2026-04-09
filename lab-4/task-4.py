from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["library"]

authors = db["authors"]

authors.insert_one({"name": "Tolstoi", "country": "Russia"})

for a in authors.find():
    print(a)
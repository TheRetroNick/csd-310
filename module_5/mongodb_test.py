# Assignment 5.2

from pyMongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.cbez6.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url);
db = client.pyTech;

print(db.list_collections_names)

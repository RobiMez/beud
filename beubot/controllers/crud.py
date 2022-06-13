from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.beubot
# database definitions
users = db['users']
rests = db['restaurants']
orders = db['orders']
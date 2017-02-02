import datetime
from pymongo import MongoClient

class MongoStore(object):
    def __init__(self,connectionStr):
        self.client=MongoClient(connectionStr)
        self.db=self.client['blog']
        self.collection=self.db['articles']
    
    def insert(self,obj):
        return self.collection.insert_one(obj).inserted_id

    def insert_all(self,objs):
        result=self.collection.insert_many(objs)
        return result.inserted_ids


store=MongoStore('mongodb://super:super@localhost:27017/')

post={"author": "Mike",
      "text": "My first blog post!",
      "tags": ["mongodb", "python", "pymongo"],
      "date": datetime.datetime.utcnow()}

posts = [{"author": "Mike",
               "text": "Another post!",
               "tags": ["bulk", "insert"],
               "date": datetime.datetime(2009, 11, 12, 11, 14)},
              {"author": "Eliot",
               "title": "MongoDB is fun",
               "text": "and pretty easy too!",
               "date": datetime.datetime(2009, 11, 10, 10, 45)}]

store.insert(post)

store.insert_all(posts)
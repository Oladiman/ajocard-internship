from pymongo import MongoClient
from config.environment import config
from bson.objectid import ObjectId

class MongoHelper:
  
  def __init__(self, coll):
    url = config['mongo']['url']
    db_name = config['mongo']['db']
    print('Mongodb url', url)
    client = MongoClient(url)
    db = client[db_name]
    self.collection = db[coll]

  def insert(self, data):
    data_id = self.collection.insert_one(data).inserted_id
    return data_id

  def find_one_by_id(self, id):
    data = self.collection.find_one({'_id': ObjectId(id)})
    return data

  def find_all(self):
    data =  self.collection.find({})
    returned = []
    for d in data:
      d['_id'] = str(d['_id'])
      returned.append(d)
    print(returned)
    return returned

  def find_one(self, condition):
    data = self.collection.find_one(condition)
    return data

  def update_by_id(self, id, data):
    result = self.collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    return result

  def increment_by_id(self, id, data):
    result = self.collection.update_one({'_id': ObjectId(id)}, {'$inc': data})
    return result



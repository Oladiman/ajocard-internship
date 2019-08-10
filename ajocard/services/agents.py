from helpers.mongo_helper import MongoHelper
import bcrypt

class AgentsService:
  
  def __init__(self):
    print('Agents service initialized')
    collection_name = 'agents'
    self.db = MongoHelper(collection_name)

  def create_agent(self, data):
    '''
    data: name, pin, phone
    '''
    hashed = bcrypt.hashpw(data['pin'].encode(), bcrypt.gensalt())
    data['pin'] = hashed.decode()
    self.db.insert(data)

  def validate_agent(self, phone, pin):
    agent = self.db.find_one({'phone': phone})
    return bcrypt.checkpw(pin.encode(), agent['pin'].encode())

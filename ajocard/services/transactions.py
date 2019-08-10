from helpers.mongo_helper import MongoHelper

class TransactionsService:
  def __init__(self):
    print('Transactions service initialized')
    collection_name = 'transactions'
    self.db = MongoHelper(collection_name)

  def create_transaction(self, data):
    '''
    data: agent_phone, wallet_id, amount, type
    '''
    return self.db.insert(data)

  def get_transactions(self):
    return self.db.find_all()

  
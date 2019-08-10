from helpers.mongo_helper import MongoHelper

class WalletService:

  def __init__(self):
    print('Wallet service initialized')
    collection_name = 'wallet'
    self.db = MongoHelper(collection_name)

  def create_wallet(self, name):
    '''
    data: name
    '''
    data = {
      'name': name,
      'amount': 10000 # initial amount
    }
    wallet_id = self.db.insert(data)
    return wallet_id

  def deposit_in_wallet(self, wallet_id, amount):
    wallet_data = self.db.increment_by_id(wallet_id, {'amount': amount})
    return wallet_data

  def withdraw_from_wallet(self, wallet_id, amount):
    amount = int(amount)
    amount = -amount
    return self.deposit_in_wallet(wallet_id, amount)

    
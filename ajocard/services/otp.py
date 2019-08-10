from helpers.mongo_helper import MongoHelper
from random import randint

class OtpService:
  
  def __init__(self):
    print('OTP service initialized')
    collection_name = 'otp'
    self.db = MongoHelper(collection_name)

  def generate_code(self):
    n = 4
    code = ''.join(["%s" % randint(0, 9) for num in range(0, n)])
    return code


  def create_otp(self, phone):
    otp = self.generate_code()
    self.db.insert({'otp': otp, 'used': False, 'phone': phone})
    return otp

  def validate_otp(self, code):
    otp_data = self.db.find_one({'otp': code, 'used': False})
    print('Otp data', otp_data, 'code', code)
    if otp_data:
      self.db.update_by_id(otp_data['_id'], {'used': True})
      return True, otp_data['phone']
    else:
      return False, None

    

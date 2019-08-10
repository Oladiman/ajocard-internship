from sanic.views import HTTPMethodView
from sanic.response import json

from config.environment import config

from services.agents import AgentsService
from services.transactions import TransactionsService
from services.otp import OtpService
from services.wallets import WalletService

class TransactionsController(HTTPMethodView):
  
  def __init__(self):
    self.agents = AgentsService()
    self.transactions = TransactionsService()
    self.otp = OtpService()
    self.wallets = WalletService()

  async def post(self, request):
    '''
    data: amount, wallet_id, pin, otp
    '''
    data = request.json
    if 'amount' not in data or 'wallet_id' not in data or 'pin' not in data or 'otp' not in data:
      return json({'error': True, 'message': 'amount, wallet_id, pin and otp are required'})
    
    otp_is_valid, phone = self.otp.validate_otp(data['otp'])
    if not otp_is_valid:
      return json({'error': True, 'message': 'Invalid otp'})
      
    if not self.agents.validate_agent(phone, data['pin']):
      return json({'error': True, 'message': 'Invalid PIN'})
    
    self.wallets.withdraw_from_wallet(data['wallet_id'], data['amount'])

    self.transactions.create_transaction(
      {'agent_phone': phone, 'wallet_id': data['wallet_id'], 'amount': data['amount'], 'type': 'Withdrawal'}
    )

    return json({'error': False, 'message': 'Transaction successful'})

  async def get(self, request):
    transactions = self.transactions.get_transactions()
    return json({
      'error': False,
      'transactions': transactions
    })

from sanic.views import HTTPMethodView
from sanic.response import json

from services.wallets import WalletService

class WalletsController(HTTPMethodView):

  def __init__(self):
    self.wallets= WalletService()

  async def post(self, request):
    '''
    data: name
    '''
    data = request.json
    if 'name' not in data:
      return json({'error': True, 'message': 'name is required'})
    wallet_id = self.wallets.create_wallet(data['name'])
    return json({
      'error': False,
      'wallet_id': str(wallet_id)
    })
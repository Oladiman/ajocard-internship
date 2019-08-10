from sanic.views import HTTPMethodView
from sanic.response import json

from services.otp import OtpService

class OtpController(HTTPMethodView):

  def __init__(self):
    self.otp = OtpService()

  async def post(self, request):
    '''
    data: phone
    '''
    data = request.json
    if 'phone' not in data:
      return json({'error': True, 'message': 'phone is required'})
    otp = self.otp.create_otp(data['phone'])
    return json({
      'error': False,
      'otp': otp
    })
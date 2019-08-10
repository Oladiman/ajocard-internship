from sanic.views import HTTPMethodView
from sanic.response import json

from services.agents import AgentsService

class AgentsController(HTTPMethodView):

  def __init__(self):
    self.agents = AgentsService()

  async def post(self, request):
    '''
    data: name, pin, phone
    '''
    data = request.json
    # print(request)
    if 'name' not in data or 'pin' not in data or 'phone' not in data:
      return json({'error': True, 'message': 'name, pin and phone are required'})
    self.agents.create_agent(data)
    return json({
      'error': False,
      'message': 'Agent created successfully'
    })
from sanic import Sanic

from config.environment import config

from controllers.agentsController import AgentsController
from controllers.otpController import OtpController
from controllers.transactionsController import TransactionsController
from controllers.walletsController import WalletsController


app = Sanic('ajocard')

app.add_route(AgentsController.as_view(), '/agents')
app.add_route(OtpController.as_view(), '/otp')
app.add_route(WalletsController.as_view(), '/wallets')
app.add_route(TransactionsController.as_view(), '/transactions')

if __name__ == '__main__':
  app.run(
    host=config['api']['host'],
    port=config['api']['port']
  )
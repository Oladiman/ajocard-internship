import os

mongo_username = os.getenv('MONGO_USERNAME')
mongo_password = os.getenv('MONGO_PASSWORD')
mongo_host = os.getenv('MONGO_HOST')
mongo_port = os.getenv('MONGO_PORT')
db_name = os.getenv('DB_NAME')

mongo_url = 'mongodb://{}/{}'.format(mongo_host, db_name)

config = {
  'api': {
    'host': '0.0.0.0',
    'port': os.getenv('API_PORT')
  },
  'mongo': {
    'url': mongo_url,
    'db': db_name
  },
  'jwt': {
    'secret': os.getenv('JWT_SECRET')
  }
}
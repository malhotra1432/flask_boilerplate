import os
from flask import Flask
from flask_restful import Api
import pymongo
from log4mongo.handlers import MongoHandler
import logging
from log.RequestFormatter import RequestFormatter

from web import home
from apis.home_api import Home

app = Flask(__name__)
config = app.config
config.from_object('config')
api = Api(app)

try:
    app.logger.info('mongodb get_db request complete')
    environment = config['ACTIVE_ENV']
    handler = MongoHandler(host=config['ENVS'][environment]['DB_HOST'],
                           port=config['ENVS'][environment]['DB_PORT'],
                           database_name=config['ENVS'][environment]['DB_NAME'])
    formatter = RequestFormatter()
    handler.setFormatter(formatter)
    logger = logging.getLogger(config["APP_NAME"])
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    app.logger = logger
except pymongo.errors.ServerSelectionTimeoutError as e:
    message = "Could not connect to database"
    status = 403
    app.logger.error('Could not connect to database',e)
except Exception as e:
    message = "database connection error"
    status = 400
    app.logger.error('database error',e)

# APIs
api.add_resource(Home, '/home')

# Web URLs
app.register_blueprint(home.bp)

if __name__ == '__main__':
    app.run(debug=True)

from sys import stderr
import pymongo
from pymongo import MongoClient
from flask import current_app as app
import pymongo


class Database(object):
    database = None
    database_name = ''

    def __init__(self, db_name='', **kwargs):
        app.logger.info('mongodb init started')
        args = app.config
        environment = args['ACTIVE_ENV']
        args = args['ENVS'][environment]
        mongo_client = MongoClient(host=args['DB_HOST'], port=args['DB_PORT'])
        if db_name == '':
            self.database_name = args['DB_NAME']
        else:
            self.database_name = db_name
        self.database = mongo_client[str(self.database_name)]
        app.logger.info('mongodb init finished')

    @staticmethod
    def database_error(error, message, status_code):
        return {'error': error, 'message': message, 'status_code': status_code}

    def get_db(self):
        app.logger.info('mongodb get_db request')
        try:
            self.database.command("serverStatus")
            app.logger.info('mongodb get_db request complete')
            return {"database": self.database, "status": 200}
        except pymongo.errors.ServerSelectionTimeoutError as e:
            message = "Could not connect to database"
            status = 403
            self.database_error(e, message, status)
            app.logger.error('Could not connect to database')
            return {"status": status}
        except Exception as e:
            message = "database connection error"
            status = 400
            self.database_error(e, message, status)
            app.logger.error('database error')
            return {"status": 400}

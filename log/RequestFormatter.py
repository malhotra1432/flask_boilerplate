import logging
from flask import request
from log4mongo.handlers import MongoFormatter


class RequestFormatter(MongoFormatter):
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        #print("++++++++++++++++", record)
        return super().format(record)

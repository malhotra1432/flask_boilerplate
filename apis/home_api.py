from flask_restful import Resource
from flask import jsonify, make_response, request
from log.RequestFormatter import RequestFormatter
from db.mongo import Database

database = None


class Home(Resource, RequestFormatter):
    def __init__(self):
        super().__init__()
        self.global_db = Database().get_db()["database"]
        database = Database()
        self.database = database.get_db()

    def get(self):
        data_list = list()
        if self.database["status"] == 200:
            data = self.database["database"].get_collection('inventory').find({}, {"_id": 0})
            for i in data:
                data_list.append(i)
        else:
            data_list = {}
        return make_response(jsonify(data_list))

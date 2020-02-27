import json
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    """ fonction to jsonify ObjectId """
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class MongoConnection(object):
    """ MongoDb information """
    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 27017
        self.login = 'rhr'
        self.password = 'admin'
        self.name = 'cookbook'
        self.collection_ingredient = 'ingredient'
        self.collection_recipe = 'recipe'
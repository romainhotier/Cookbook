import json
import sys

from bson import ObjectId
from pymongo import MongoClient, errors

import utils


class JSONEncoder(json.JSONEncoder):
    """ fonction to jsonify ObjectId """
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class Mongo(object):
    """ MongoDb information """
    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 27017
        self.login = 'rhr'
        self.password = 'admin'
        self.name = 'cookbook'
        self.collection_user = 'user'
        self.collection_ingredient = 'ingredient'
        self.collection_ingredient_recipe = "ingredient_recipe"
        self.collection_recipe = 'recipe'
        self.collection_fs_files = 'fs.files'
        self.collection_fs_chunks = 'fs.chunks'

    def select_collection(self, kind):
        if kind == "ingredient":
            return self.collection_ingredient
        elif kind == "recipe":
            return self.collection_recipe

    @staticmethod
    def format_json(data):
        return json.loads(JSONEncoder().encode(data))

    def check_mongodb_up(self):
        try:
            client = MongoClient(self.ip, self.port, serverSelectionTimeoutMS=2000)
            client.server_info()
            client.close()
        except errors.ServerSelectionTimeoutError:
            utils.Server.logger.critical("Connexion to MongoDB Failed !!!")
            sys.exit()


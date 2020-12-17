import json
import sys
from bson import ObjectId
from pymongo import MongoClient, errors

import utils

server = utils.Server()


class JSONEncoder(json.JSONEncoder):
    """ Return the same dict with stringify ObjectId.
    """

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class Mongo(object):

    def __init__(self):
        """ MongoDB information.
        """
        self.ip = '127.0.0.1'
        self.port = 27017
        self.login = 'rhr'
        self.password = 'admin'
        self.name = 'cookbook'
        self.collection_user = 'user'
        self.collection_ingredient = 'ingredient'
        self.collection_recipe = 'recipe'
        self.collection_link = "link"
        self.collection_step = 'step'
        self.collection_fs_files = 'fs.files'
        self.collection_fs_chunks = 'fs.chunks'

    def select_collection(self, kind):
        """ Return a collection's name for given type.

        Parameters
        ----------
        kind : str
            Can be in ["ingredient", "recipe"].

        Returns
        -------
        str
            Collection's name.
        """
        if kind == "ingredient":
            return self.collection_ingredient
        elif kind == "recipe":
            return self.collection_recipe

    @staticmethod
    def to_json(data):
        """ Format data in a json without ObjectId.

        Parameters
        ----------
        data : Any
            MongoDB result.

        Returns
        -------
        dict
            Json.
        """
        return json.loads(JSONEncoder().encode(data))

    def check_mongodb_up(self):
        """ Check if MongoDB is UP.

        Returns
        -------
        Any
            Close app if there is no connection.
        """
        try:
            client = MongoClient(self.ip, self.port, serverSelectionTimeoutMS=2000)
            client.server_info()
            client.close()
        except errors.ServerSelectionTimeoutError:
            server.logger.critical("Connexion to MongoDB Failed !!!")
            sys.exit()

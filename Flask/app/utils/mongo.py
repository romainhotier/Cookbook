import json
import sys
from bson import ObjectId
from pymongo import MongoClient, errors
from app.utils.logger import logger


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
        self.ip = "127.0.0.1"
        self.port = 27017
        self.login = "rhr"
        self.password = "admin"
        self.name = 'cookbook'
        self.collection_user = 'user'
        self.collection_ingredient = 'ingredient'
        self.collection_recipe = 'recipe'

    def check_mongodb_up(self):
        """ Check if MongoDB is UP.

        Returns
        -------
        Any
            Close app if there is no connection.
        """
        try:
            with MongoClient(self.ip, self.port, serverSelectionTimeoutMS=2000) as client:
                client.server_info()
        except errors.ServerSelectionTimeoutError:
            logger.critical("Connexion to MongoDB Failed !!!")
            sys.exit()

    @staticmethod
    def convert_object_id_to_str(data):
        """ Format data in a json without ObjectId.

        Parameters
        ----------
        data : Any

        Returns
        -------
        Dict
            Json
        """
        return json.loads(JSONEncoder().encode(data))

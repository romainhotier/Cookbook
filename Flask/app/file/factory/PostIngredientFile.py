from pymongo import MongoClient
from bson import ObjectId


from server import mongo_config as mongo_conf
import app.file.model as file_model

mongo = mongo_conf.MongoConnection()
list_param_file = file_model.File().list_param


class Factory(object):

    def clean_body(self, data):
        cleaned = self.remove_foreign_key(data)
        return cleaned

    @staticmethod
    def remove_foreign_key(data):
        clean_data = {}
        for i, j in data.items():
            if i in list_param_file:
                clean_data[i] = j
        return clean_data

    @staticmethod
    def enrich_ingredient(_id_ingredient, _id_file, metadata):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        db.update_one({"_id": ObjectId(_id_ingredient)},
                      {'$push': {"files": {"$each": [{"_id": _id_file, "is_main": metadata["is_main"]}]}}})
        """ return result """
        result = db.find({"_id": ObjectId(_id_ingredient)})
        client.close()
        return result

    @staticmethod
    def detail_information(_id_file):
        return "added file ObjectId: {0}".format(str(_id_file))

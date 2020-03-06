from pymongo import MongoClient
from bson import ObjectId

from server import mongo_config as mongo_conf

mongo = mongo_conf.MongoConnection()
json_format = mongo_conf.JSONEncoder()


class Steps(object):

    def __init__(self):
        self.list_param = ["step", "position"]

    @staticmethod
    def get_steps_length(_id, mode):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        if result is None:
            return 0
        else:
            steps_length = len(result["steps"])
            if mode == "insert":
                return steps_length
            elif mode == "delete":
                return steps_length - 1

    @staticmethod
    def insert(_id, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        new_step = data["step"]
        if "position" in data.keys():
            position = data["position"]
            db.update_one({"_id": ObjectId(_id)}, {'$push': {"steps": {"$each": [new_step], "$position": position}}})
        else:
            db.update_one({"_id": ObjectId(_id)}, {'$push': {"steps": {"$each": [new_step]}}})
        """ return result """
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        result_json = json_format.encode(result)
        return result_json

    @staticmethod
    def delete(_id, position):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.update_one({"_id": ObjectId(_id)}, {'$unset': {"steps.{}".format(position): 1}})
        db.update_one({"_id": ObjectId(_id)}, {'$pull': {"steps": None}})
        """ return result """
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        result_json = json_format.encode(result)
        return result_json

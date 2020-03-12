from pymongo import MongoClient
from bson import ObjectId

from server import mongo_config as mongo_conf
import app.recipe.recipe.model as recipe_model

mongo = mongo_conf.MongoConnection()
json_format = mongo_conf.JSONEncoder()
recipe = recipe_model.Recipe()


class Steps(object):

    def __init__(self):
        self.list_param = ["step"]
        self.result = ""

    @staticmethod
    def get_steps_length(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        if result is None:
            return 0
        else:
            steps_length = len(result["steps"])
            return steps_length

    def insert(self, _id, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        new_step = {"_id": ObjectId(), "step": data["step"]}
        if "position" in data.keys():
            position = data["position"]
            db.update_one({"_id": ObjectId(_id)}, {'$push': {"steps": {"$each": [new_step], "$position": position}}})
        else:
            db.update_one({"_id": ObjectId(_id)}, {'$push': {"steps": {"$each": [new_step]}}})
        client.close()
        """ return result """
        self.result = recipe.select_one(_id=_id)
        return self

    def update(self, _id_recipe, _id_step, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        position = Steps.get_step_index(_id_recipe=_id_recipe, _id_step=_id_step)
        db.update_one({"_id": ObjectId(_id_recipe)}, {'$set': {"steps.{0}.step".format(position): data["step"]}})
        client.close()
        """ return result """
        self.result = recipe.select_one(_id=_id_recipe)
        return self

    def delete(self, _id_recipe, _id_step):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.update_one({"_id": ObjectId(_id_recipe)}, {'$pull': {"steps": {"_id": ObjectId(_id_step)}}})
        client.close()
        """ return result """
        self.result = recipe.select_one(_id=_id_recipe)
        return self

    @staticmethod
    def get_step_index(_id_recipe, _id_step):
        steps = recipe.select_one(_id=_id_recipe).get_result()["steps"]
        i = 0
        for step in steps:
            if step["_id"] == _id_step:
                return i
            else:
                i += 1

    @staticmethod
    def get_result():
        return recipe.get_result()

    @staticmethod
    def add_enrichment_file():
        return recipe.add_enrichment_file()

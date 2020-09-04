from pymongo import MongoClient
from bson import ObjectId

import utils
import app.file as file_model

mongo = utils.Mongo


class Recipe(object):

    def __init__(self):
        self.result = {}

    def select_all(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        cursor = db.find({})
        client.close()
        self.result = mongo.format_json([recipe for recipe in cursor])
        return self

    def select_one(self, _id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.result = mongo.format_json(result)
        return self

    @staticmethod
    def check_recipe_is_unique(title):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.count_documents({"title": title})
        client.close()
        return result

    def insert(self, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        query = db.insert_one(data)
        result = db.find_one({"_id": ObjectId(query.inserted_id)})
        client.close()
        self.result = mongo.format_json(result)
        return self

    def update(self, _id, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.update_one({"_id": ObjectId(_id)}, {'$set': data})
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.result = mongo.format_json(result)
        return self

    @staticmethod
    def delete(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.delete_one({"_id": ObjectId(_id)})
        client.close()
        return

    def add_enrichment_file_for_all(self):
        for recipe in self.result:
            recipe["files"] = []
            """ get files for recipe """
            files_recipe = file_model.FileModel.get_all_file_by_id_parent(_id_parent=recipe["_id"]).json
            for file in files_recipe:
                file_enrichment = {"_id": str(file["_id"]), "is_main": file["metadata"]["is_main"]}
                recipe["files"].append(file_enrichment)
            """ get files for steps """
            for step in recipe["steps"]:
                step["files"] = []
                files_step = file_model.FileModel.get_all_file_by_id_parent(_id_parent=step["_id"]).json
                for file in files_step:
                    file_enrichment = {"_id": str(file["_id"]), "is_main": file["metadata"]["is_main"]}
                    step["files"].append(file_enrichment)
        return self

    def add_enrichment_file_for_one(self):
        self.result["files"] = []
        """ get files for recipe """
        files_recipe = file_model.FileModel.get_all_file_by_id_parent(_id_parent=self.result["_id"]).json
        for file in files_recipe:
            file_enrichment = {"_id": str(file["_id"]), "is_main": file["metadata"]["is_main"]}
            self.result["files"].append(file_enrichment)
        """ get files for steps """
        for step in self.result["steps"]:
            step["files"] = []
            files_step = file_model.FileModel.get_all_file_by_id_parent(_id_parent=step["_id"]).json
            for file in files_step:
                file_enrichment = {"_id": str(file["_id"]), "is_main": file["metadata"]["is_main"]}
                step["files"].append(file_enrichment)
        return self

    @staticmethod
    def get_all_step_id(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find_one({"_id": ObjectId(_id)})
        steps_ids = [step["_id"] for step in result["steps"]]
        client.close()
        return steps_ids

    @staticmethod
    def get_title_by_id(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        return result["title"]


class Step(object):

    def __init__(self):
        self.result = {}

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
        self.result = Recipe().select_one(_id=_id).result
        return self

    def update(self, _id_recipe, _id_step, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        position = Step.get_step_index(_id_recipe=_id_recipe, _id_step=_id_step)
        db.update_one({"_id": ObjectId(_id_recipe)}, {'$set': {"steps.{0}.step".format(position): data["step"]}})
        client.close()
        """ return result """
        self.result = Recipe().select_one(_id=_id_recipe).result
        return self

    def delete(self, _id_recipe, _id_step):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.update_one({"_id": ObjectId(_id_recipe)}, {'$pull': {"steps": {"_id": ObjectId(_id_step)}}})
        client.close()
        """ return result """
        self.result = Recipe().select_one(_id=_id_recipe).result
        return self

    @staticmethod
    def get_step_index(_id_recipe, _id_step):
        steps = Recipe().select_one(_id=_id_recipe).result["steps"]
        i = 0
        for step in steps:
            if step["_id"] == _id_step:
                return i
            else:
                i += 1

    def add_enrichment_file_for_one(self):
        self.result["files"] = []
        """ get files for recipe """
        files_recipe = file_model.FileModel.get_all_file_by_id_parent(_id_parent=self.result["_id"]).json
        for file in files_recipe:
            file_enrichment = {"_id": str(file["_id"]), "is_main": file["metadata"]["is_main"]}
            self.result["files"].append(file_enrichment)
        """ get files for steps """
        for step in self.result["steps"]:
            step["files"] = []
            files_step = file_model.FileModel.get_all_file_by_id_parent(_id_parent=step["_id"]).json
            for file in files_step:
                file_enrichment = {"_id": str(file["_id"]), "is_main": file["metadata"]["is_main"]}
                step["files"].append(file_enrichment)
        return self

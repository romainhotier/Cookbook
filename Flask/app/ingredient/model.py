from pymongo import MongoClient
from bson import ObjectId

import utils
import app.file as file_model
import app.recipe as recipe_model

mongo = utils.Mongo


class Ingredient(object):

    def __init__(self):
        self.json = {}

    def select_all(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        cursor = db.find({})
        client.close()
        self.json = mongo.format_json([ingredient for ingredient in cursor])
        return self

    def select_one(self, _id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.json = mongo.format_json(result)
        return self

    @staticmethod
    def check_ingredient_is_unique(name):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.count_documents({"name": name})
        client.close()
        return result

    def insert(self, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        query = db.insert_one(data)
        result = db.find_one({"_id": ObjectId(query.inserted_id)})
        client.close()
        self.json = mongo.format_json(result)
        return self

    def update(self, _id, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        db.update_one({"_id": ObjectId(_id)}, {'$set': data})
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.json = mongo.format_json(result)
        return self

    @staticmethod
    def delete(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        db.delete_one({"_id": ObjectId(_id)})
        client.close()
        return

    def add_enrichment_file_for_all(self):
        for ingredient in self.json:
            ingredient["files"] = []
            """ get files """
            files = file_model.FileModel.get_all_file_by_id_parent(_id_parent=ingredient["_id"]).json
            for file in files:
                file_enrichment = {"_id": str(file["_id"]), "is_main": file["metadata"]["is_main"]}
                ingredient["files"].append(file_enrichment)
        return self

    def add_enrichment_file_for_one(self):
        self.json["files"] = []
        """ get files """
        files = file_model.FileModel.get_all_file_by_id_parent(_id_parent=self.json["_id"]).json
        for file in files:
            file_enrichment = {"_id": str(file["_id"]), "is_main": file["metadata"]["is_main"]}
            self.json["files"].append(file_enrichment)
        return self

    @staticmethod
    def get_name_by_id(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        return result["name"]


class IngredientRecipe(object):

    def __init__(self):
        self.json = {}

    def insert(self, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        query = db.insert_one(data)
        result = db.find_one({"_id": ObjectId(query.inserted_id)})
        client.close()
        self.json = mongo.format_json(result)
        return self

    def select_all_by_id_recipe(self, _id_recipe):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        cursor = db.find({"_id_recipe": ObjectId(_id_recipe)})
        client.close()
        self.json = mongo.format_json([ingredient for ingredient in cursor])
        return self

    def select_all_by_id_ingredient(self, _id_ingredient):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        cursor = db.find({"_id_ingredient": ObjectId(_id_ingredient)})
        client.close()
        self.json = mongo.format_json([recipe for recipe in cursor])
        return self

    def update(self, _id, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        db.update_one({"_id": ObjectId(_id)}, {'$set': data})
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.json = mongo.format_json(result)
        return self

    @staticmethod
    def delete(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        db.delete_one({"_id": ObjectId(_id)})
        client.close()
        return

    @staticmethod
    def clean_link_by_id_ingredient(_id_ingredient):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        db.delete_many({"_id_ingredient": ObjectId(_id_ingredient)})
        client.close()
        return

    @staticmethod
    def clean_link_by_id_recipe(_id_recipe):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        db.delete_many({"_id_recipe": ObjectId(_id_recipe)})
        client.close()
        return

    @staticmethod
    def check_link_is_unique(_id_ingredient, _id_recipe):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        result = db.count_documents({'$and': [{"_id_ingredient": ObjectId(_id_ingredient)},
                                              {"_id_recipe": ObjectId(_id_recipe)}]})
        client.close()
        """ return result """
        return result

    def add_enrichment_name_for_all(self):
        for link in self.json:
            link["name"] = Ingredient().get_name_by_id(_id=link["_id_ingredient"])
        return self

    def add_enrichment_title_for_all(self):
        for link in self.json:
            link["title"] = recipe_model.RecipeModel.get_title_by_id(_id=link["_id_recipe"])
        return self

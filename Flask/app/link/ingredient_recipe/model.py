from pymongo import MongoClient
from bson import ObjectId
import json
import copy
import re

from server import mongo_config as mongo_conf
import app.ingredient.ingredient.model as ingredient_model
import app.recipe.recipe.model as recipe_model

mongo = mongo_conf.MongoConnection()
json_format = mongo_conf.JSONEncoder()
ingredient = ingredient_model.Ingredient()
recipe = recipe_model.Recipe()


class LinkIngredientRecipe(object):

    def __init__(self):
        self.list_param = ["quantity", "unit", "_id_ingredient", "_id_recipe"]
        self.result = {}

    def insert(self, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_link_ingr_recip]
        query = db.insert_one(data)
        result = db.find_one({"_id": ObjectId(query.inserted_id)})
        client.close()
        """ return result """
        self.result = result
        return self

    def select_all_by_id_recipe(self, _id_recipe):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_link_ingr_recip]
        result = db.find({"_id_recipe": ObjectId(_id_recipe)})
        client.close()
        self.result = [ingr for ingr in result]
        return self

    def select_all_by_id_ingredient(self, _id_ingredient):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_link_ingr_recip]
        result = db.find({"_id_ingredient": ObjectId(_id_ingredient)})
        client.close()
        self.result = [recip for recip in result]
        return self

    def update(self, _id, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_link_ingr_recip]
        db.update_one({"_id": ObjectId(_id)}, {'$set': data})
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.result = result
        return self

    @staticmethod
    def delete(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_link_ingr_recip]
        db.delete_one({"_id": ObjectId(_id)})
        client.close()
        return

    @staticmethod
    def clean_link_by_id_ingredient(_id_ingredient):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_link_ingr_recip]
        db.delete_many({"_id_ingredient": ObjectId(_id_ingredient)})
        client.close()
        return

    @staticmethod
    def clean_link_by_id_recipe(_id_recipe):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_link_ingr_recip]
        db.delete_many({"_id_recipe": ObjectId(_id_recipe)})
        client.close()
        return

    @staticmethod
    def check_link_is_unique(_id_ingredient, _id_recipe):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_link_ingr_recip]
        result = db.find_one({'$and': [{"_id_ingredient": ObjectId(_id_ingredient)},
                                       {"_id_recipe": ObjectId(_id_recipe)}]})
        client.close()
        """ return result """
        return result

    def add_enrichment_name_for_all(self):
        for link in self.result:
            link["name"] = ingredient.get_name_by_id(_id=link["_id_ingredient"])
        return self

    def add_enrichment_title_for_all(self):
        for link in self.result:
            link["title"] = recipe.get_title_by_id(_id=link["_id_recipe"])
        return self

    def get_result(self):
        return json.loads(json_format.encode(self.result))


class LinkIngredientRecipeTest(object):

    def __init__(self):
        self.data = {"_id": "",
                     "quantity": 0,
                     "unit": "qa_rhr_unit",
                     "_id_ingredient": ObjectId(),
                     "_id_recipe": ObjectId()
                     }

    def display(self):
        print(self.data)

    def set_id(self, _id):
        self.data["_id"] = _id

    def delete_id(self):
        self.data.pop("_id")

    def get_id(self):
        return str(self.data["_id"])

    def get_data(self):
        return self.data

    def get_data_stringify_object_id(self):
        return json.loads(json_format.encode(self.data))

    def get_data_without_id(self):
        data_without_id = copy.deepcopy(self.get_data())
        data_without_id.pop("_id")
        return json.loads(json_format.encode(data_without_id))

    def custom(self, data):
        for i, j in data.items():
            if i in LinkIngredientRecipe().list_param or i == "_id":
                self.data[i] = j
        return self

    def custom_test(self, data):
        for i, j in data.items():
            if i in LinkIngredientRecipe().list_param or i == "_id":
                self.data[i] = j
        self.data["unit"] = self.data["unit"] + "_qa_rhr"
        return self

    def select_ok(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_link_ingr_recip]
        result = db.find({"_id": ObjectId(self.get_id())})
        client.close()
        assert result.count() == 1
        assert isinstance(result[0]["_id"], ObjectId)
        for value in result[0]:
            if value not in ["_id"]:
                assert result[0][value] == self.data[value]

    def select_nok(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_link_ingr_recip]
        result = db.count_documents({"_id": ObjectId(self.get_id())})
        client.close()
        assert result == 0

    def select_nok_by_unit(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_link_ingr_recip]
        result = db.count_documents({"unit": self.data["unit"]})
        client.close()
        assert result == 0

    def select_nok_by_linked(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_link_ingr_recip]
        result = db.count_documents({'$and': [{"_id_ingredient": ObjectId(self.data["_id_ingredient"])},
                                              {"_id_recipe": ObjectId(self.data["_id_recipe"])}]})
        client.close()
        assert result == 0

    def insert(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_link_ingr_recip]
        self.delete_id()
        query = db.insert_one(self.get_data())
        client.close()
        self.set_id(query.inserted_id)
        return self

    def delete(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_link_ingr_recip]
        db.delete_one({"_id": ObjectId(self.get_id())})
        client.close()
        return

    @staticmethod
    def clean():
        rgx = re.compile('.*qa_rhr.*', re.IGNORECASE)
        rgx2 = re.compile('.*invalid.*', re.IGNORECASE)
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_link_ingr_recip]
        db.delete_many({"unit": rgx})
        db.delete_many({"unit": rgx2})
        client.close()

    def add_name(self):
        self.data["name"] = ingredient.get_name_by_id(self.data["_id_ingredient"])
        return self

    def add_title(self):
        self.data["title"] = recipe.get_title_by_id(self.data["_id_recipe"])
        return self

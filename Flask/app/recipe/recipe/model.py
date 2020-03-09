from pymongo import MongoClient
from bson import ObjectId
import copy
import re
import json

from server import mongo_config as mongo_conf

mongo = mongo_conf.MongoConnection()
json_format = mongo_conf.JSONEncoder()


class Recipe(object):

    def __init__(self):
        self.list_param = ["title", "level", "resume", "cooking_time", "preparation_time", "nb_people", "note", "steps"]

    @staticmethod
    def select_all():
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find({})
        client.close()
        results = []
        for recipe in result:
            results.append(recipe)
        result_json = json_format.encode(results)
        return result_json

    @staticmethod
    def select_one(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        result_json = json_format.encode(result)
        return result_json

    @staticmethod
    def select_one_by_title(title):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find({"title": title})
        client.close()
        return result

    @staticmethod
    def select_one_with_enrichment(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db_recipe = client[mongo.name][mongo.collection_recipe]
        db_file = client[mongo.name][mongo.collection_fs_files]
        """ get recipe """
        result = db_recipe.find_one({"_id": ObjectId(_id)})
        result["files"] = []
        """ get files """
        files = db_file.find({"metadata._id": ObjectId(_id)})
        for file in files:
            file_enrichment = {"_id": file["_id"], "is_main": file["metadata"]["is_main"]}
            result["files"].append(file_enrichment)
        client.close()
        result_json = json_format.encode(result)
        return result_json

    @staticmethod
    def insert(data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        query = db.insert_one(data)
        result = db.find_one({"_id": ObjectId(query.inserted_id)})
        client.close()
        result_json = json_format.encode(result)
        return result_json

    @staticmethod
    def update(_id, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.update_one({"_id": ObjectId(_id)}, {'$set': data})
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        result_json = json_format.encode(result)
        return result_json

    @staticmethod
    def delete(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.delete_one({"_id": ObjectId(_id)})
        client.close()
        return


class RecipeTest(object):

    def __init__(self):
        self.data = {"_id": "",
                     "title": "",
                     "level": "",
                     "resume": "",
                     "cooking_time": "",
                     "preparation_time": "",
                     "nb_people": "",
                     "note": "",
                     "steps": []
                     }

    def display(self):
        print(self.data)

    def get_data(self):
        return self.data

    def get_data_stringify_object_id(self):
        return json.loads(json_format.encode(self.data))

    def get_data_without_id(self):
        data_without_id = copy.deepcopy(self.get_data())
        data_without_id.pop("_id")
        return data_without_id

    def get_id(self):
        return str(self.data["_id"])

    def set_id(self, _id):
        self.data["_id"] = _id

    def delete_id(self):
        self.data.pop("_id")

    def get_data_value(self, value):
        return self.data[value]

    def custom(self, data):
        for i, j in data.items():
            if i in Recipe().list_param or i == "_id":
                self.data[i] = j
        return self

    def custom_test(self, data):
        for i, j in data.items():
            if i in Recipe().list_param or i == "_id":
                self.data[i] = j
        self.data["title"] = self.data["title"] + "qa_rhr"
        return self

    def select_ok(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find({"_id": ObjectId(self.get_id())})
        client.close()
        assert result.count() == 1
        assert isinstance(result[0]["_id"], ObjectId)
        for value in result[0]:
            if value not in ["_id"]:
                assert result[0][value] == self.data[value]

    def select_ok_by_title(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find({"title": self.data['title']})
        client.close()
        assert result.count() == 1
        assert isinstance(result[0]["_id"], ObjectId)
        for value in result[0]:
            if value not in ["_id"]:
                assert result[0][value] == self.data[value]

    def select_nok(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.count_documents({"_id": ObjectId(self.get_id())})
        client.close()
        assert result == 0

    def select_nok_by_title(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.count_documents({"title": self.data['title']})
        client.close()
        assert result == 0

    def insert(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        self.delete_id()
        query = db.insert_one(self.get_data())
        client.close()
        self.set_id(query.inserted_id)
        return self

    def delete(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.delete_one({"_id": ObjectId(self.get_id())})
        client.close()
        return

    @staticmethod
    def clean():
        rgx = re.compile('.*qa_rhr.*', re.IGNORECASE)
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.delete_many({"title": rgx})
        client.close()
        return

from pymongo import MongoClient
from bson import ObjectId
import re
import copy
import json

from server import mongo_config as mongo_conf

mongo = mongo_conf.MongoConnection()
json_format = mongo_conf.JSONEncoder()


class Ingredient(object):

    def __init__(self):
        self.list_param = ["name", "files"]

    @staticmethod
    def select_all():
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find({})
        client.close()
        results = []
        for ingredient in result:
            results.append(ingredient)
        result_json = json_format.encode(results)
        return result_json

    @staticmethod
    def select_one(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        result_json = json_format.encode(result)
        return result_json

    @staticmethod
    def select_one_by_name(name):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find({"name": name})
        client.close()
        return result

    @staticmethod
    def select_one_with_enrichment(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db_ingredient = client[mongo.name][mongo.collection_ingredient]
        db_file = client[mongo.name][mongo.collection_fs_files]
        """ get ingredient """
        result = db_ingredient.find_one({"_id": ObjectId(_id)})
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
        db = client[mongo.name][mongo.collection_ingredient]
        query = db.insert_one(data)
        result = db.find_one({"_id": ObjectId(query.inserted_id)})
        client.close()
        result_json = json_format.encode(result)
        return result_json

    @staticmethod
    def update(_id, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        db.update_one({"_id": ObjectId(_id)}, {'$set': data})
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        result_json = json_format.encode(result)
        return result_json

    @staticmethod
    def delete(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        db.delete_one({"_id": ObjectId(_id)})
        client.close()
        return


class IngredientTest(object):

    def __init__(self):
        self.data = {"_id": "",
                     "name": ""
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

    def get_data_with_enrichment(self):
        client = MongoClient(mongo.ip, mongo.port)
        db_file = client[mongo.name][mongo.collection_fs_files]
        data = copy.deepcopy(self.get_data())
        data["files"] = []
        """ get files """
        files = db_file.find({"metadata._id": ObjectId(self.get_id())})
        for file in files:
            file_enrichment = {"_id": file["_id"], "is_main": file["metadata"]["is_main"]}
            data['files'].append(file_enrichment)
        client.close()
        return json.loads(json_format.encode(data))

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
            if i in ["_id", "name"]:
                self.data[i] = j
        return self

    def custom_test(self, data):
        for i, j in data.items():
            if i in ["_id", "name"]:
                self.data[i] = j
        self.data["name"] = self.data["name"] + "qa_rhr"
        return self

    def select_ok(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find({"_id": ObjectId(self.get_id())})
        client.close()
        assert result.count() == 1
        assert isinstance(result[0]["_id"], ObjectId)
        for value in result[0]:
            if value not in ["_id"]:
                assert result[0][value] == self.data[value]

    def select_ok_by_name(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find({"name": self.data['name']})
        client.close()
        assert result.count() == 1
        assert isinstance(result[0]["_id"], ObjectId)
        for value in result[0]:
            if value not in ["_id"]:
                assert result[0][value] == self.data[value]

    def select_nok(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.count_documents({"_id": ObjectId(self.get_id())})
        client.close()
        assert result == 0

    def select_nok_by_name(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.count_documents({"name": self.data['name']})
        client.close()
        assert result == 0

    def insert(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        self.delete_id()
        query = db.insert_one(self.get_data())
        client.close()
        self.set_id(query.inserted_id)
        return self

    def delete(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        db.delete_one({"_id": ObjectId(self.get_id())})
        client.close()
        return

    @staticmethod
    def clean():
        rgx = re.compile('.*qa_rhr.*', re.IGNORECASE)
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        db.delete_many({"name": rgx})
        client.close()
        return

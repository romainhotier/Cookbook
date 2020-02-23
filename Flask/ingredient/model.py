from pymongo import MongoClient
from bson import ObjectId
import re
import copy
import json

import mongo_config as mongo_conf

mongo = mongo_conf.MongoConnection()
json_format = mongo_conf.JSONEncoder()


class Ingredient(object):

    def __init__(self):
        self.list_param = ["name"]

    @staticmethod
    def select_all():
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find({})
        client.close()
        return result

    @staticmethod
    def select_one(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find({"_id": ObjectId(_id)})
        client.close()
        return result

    @staticmethod
    def select_one_by_name(name):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find({"name": name})
        client.close()
        return result

    @staticmethod
    def insert(data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        query = db.insert_one(data)
        result = db.find({"_id": ObjectId(query.inserted_id)})
        client.close()
        return result

    @staticmethod
    def update(_id, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        db.update_one({"_id": ObjectId(_id)}, {'$set': data})
        result = db.find({"_id": ObjectId(_id)})
        client.close()
        return result

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

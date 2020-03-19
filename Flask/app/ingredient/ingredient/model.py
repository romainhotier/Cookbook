from pymongo import MongoClient
from bson import ObjectId
import re
import copy
import json

from server import mongo_config as mongo_conf
import app.file.file.model as file_model

mongo = mongo_conf.MongoConnection()
json_format = mongo_conf.JSONEncoder()


class Ingredient(object):

    def __init__(self):
        self.list_param = ["name", "files"]
        self.result = {}

    def select_all(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find({})
        client.close()
        self.result = []
        for ingredient in result:
            self.result.append(ingredient)
        return self

    def select_one(self, _id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.result = result
        return self

    @staticmethod
    def select_one_by_name(name):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find({"name": name})
        client.close()
        return result

    def insert(self, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        query = db.insert_one(data)
        result = db.find_one({"_id": ObjectId(query.inserted_id)})
        client.close()
        self.result = result
        return self

    def update(self, _id, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        db.update_one({"_id": ObjectId(_id)}, {'$set': data})
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.result = result
        return self

    @staticmethod
    def delete(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        db.delete_one({"_id": ObjectId(_id)})
        client.close()
        return

    def add_enrichment_file_for_all(self):
        client = MongoClient(mongo.ip, mongo.port)
        db_file = client[mongo.name][mongo.collection_fs_files]
        for ingredient in self.result:
            ingredient["files"] = []
            """ get files """
            files = db_file.find({"metadata._id": ObjectId(ingredient["_id"])})
            for file in files:
                file_enrichment = {"_id": file["_id"], "is_main": file["metadata"]["is_main"]}
                ingredient["files"].append(file_enrichment)
        client.close()
        return self

    def add_enrichment_file_for_one(self):
        client = MongoClient(mongo.ip, mongo.port)
        db_file = client[mongo.name][mongo.collection_fs_files]
        self.result["files"] = []
        """ get files """
        files = db_file.find({"metadata._id": ObjectId(self.result["_id"])})
        for file in files:
            file_enrichment = {"_id": file["_id"], "is_main": file["metadata"]["is_main"]}
            self.result["files"].append(file_enrichment)
        client.close()
        return self

    @staticmethod
    def get_name_by_id(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        return result["name"]

    def get_result(self):
        return json.loads(json_format.encode(self.result))


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

    def get_data_with_file(self, files):
        self.data["files"] = []
        for file in files:
            self.data["files"].append(file.get_data_for_enrichment())
        return json.loads(json_format.encode(self.data))

    def get_id(self):
        return str(self.data["_id"])

    def get_id_objectId(self):
        return self.data["_id"]

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
        self.data["name"] = self.data["name"] + "_qa_rhr"
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

    def add_file(self, filename, is_main):
        return file_model.FileTest().custom_filename(filename).\
            custom_metadata({"kind": "ingredient",
                             "_id": ObjectId(self.data["_id"]),
                             "is_main": is_main}).insert()

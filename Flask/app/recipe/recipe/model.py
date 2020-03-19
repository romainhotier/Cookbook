from pymongo import MongoClient
from bson import ObjectId
import copy
import re
import json

from server import mongo_config as mongo_conf
import app.file.file.model as file_model

mongo = mongo_conf.MongoConnection()
json_format = mongo_conf.JSONEncoder()


class Recipe(object):

    def __init__(self):
        self.list_param = ["title", "slug", "level", "resume", "cooking_time", "preparation_time", "nb_people",
                           "note", "steps", "categories"]
        self.result = {}

    def select_all(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find({})
        client.close()
        self.result = []
        for recipe in result:
            self.result.append(recipe)
        return self

    def select_one(self, _id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.result = result
        return self

    @staticmethod
    def select_one_by_title(title):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find({"title": title})
        client.close()
        return result

    def insert(self, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        query = db.insert_one(data)
        result = db.find_one({"_id": ObjectId(query.inserted_id)})
        client.close()
        self.result = result
        return self

    def update(self, _id, data):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.update_one({"_id": ObjectId(_id)}, {'$set': data})
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.result = result
        return self

    @staticmethod
    def delete(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.delete_one({"_id": ObjectId(_id)})
        client.close()
        return

    def add_enrichment_file_for_all(self):
        client = MongoClient(mongo.ip, mongo.port)
        db_file = client[mongo.name][mongo.collection_fs_files]
        for recipe in self.result:
            recipe["files"] = []
            """ get files for recipe """
            files_recipe = db_file.find({"metadata._id": ObjectId(recipe["_id"])})
            for file in files_recipe:
                file_enrichment = {"_id": file["_id"], "is_main": file["metadata"]["is_main"]}
                recipe["files"].append(file_enrichment)
            """ get files for steps """
            for step in recipe["steps"]:
                step["files"] = []
                files_step = db_file.find({"metadata._id": ObjectId(step["_id"])})
                for file in files_step:
                    file_enrichment = {"_id": file["_id"], "is_main": file["metadata"]["is_main"]}
                    step["files"].append(file_enrichment)
        client.close()
        return self

    def add_enrichment_file_for_one(self):
        client = MongoClient(mongo.ip, mongo.port)
        db_file = client[mongo.name][mongo.collection_fs_files]
        self.result["files"] = []
        """ get files for recipe """
        files_recipe = db_file.find({"metadata._id": ObjectId(self.result["_id"])})
        for file in files_recipe:
            file_enrichment = {"_id": file["_id"], "is_main": file["metadata"]["is_main"]}
            self.result["files"].append(file_enrichment)
        """ get files for steps """
        for step in self.result["steps"]:
            step["files"] = []
            files_step = db_file.find({"metadata._id": ObjectId(step["_id"])})
            for file in files_step:
                file_enrichment = {"_id": file["_id"], "is_main": file["metadata"]["is_main"]}
                step["files"].append(file_enrichment)
        client.close()
        return self

    @staticmethod
    def get_all_step_id(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        steps_ids = []
        result = db.find_one({"_id": ObjectId(_id)})
        for step in result["steps"]:
            steps_ids.append(step["_id"])
        client.close()
        return steps_ids

    @staticmethod
    def get_title_by_id(_id):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        return result["title"]

    def get_result(self):
        return json.loads(json_format.encode(self.result))


class RecipeTest(object):

    def __init__(self):
        self.data = {"_id": "",
                     "title": "",
                     "slug": "",
                     "level": 0,
                     "resume": "",
                     "cooking_time": 0,
                     "preparation_time": 0,
                     "nb_people": 0,
                     "note": "",
                     "categories": [],
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

    def get_data_with_file(self, files_recipe, files_steps):
        tmp_data = copy.deepcopy(self)
        tmp_data.data["files"] = []
        for recipe_file in files_recipe:
            tmp_data.data["files"].append(recipe_file.get_data_for_enrichment())
        if len(files_steps) != 0:
            for i, j in files_steps.items():
                for step in tmp_data.data["steps"]:
                    if str(step["_id"]) == i:
                        step["files"] = []
                        for step_file in j:
                            step["files"].append(step_file.get_data_for_enrichment())
        return json.loads(json_format.encode(tmp_data.data))

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
            if i in Recipe().list_param or i == "_id":
                self.data[i] = j
        return self

    def custom_test(self, data):
        for i, j in data.items():
            if i in Recipe().list_param or i == "_id":
                self.data[i] = j
        self.data["title"] = self.data["title"] + "_qa_rhr"
        return self

    def select_ok(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find({"_id": ObjectId(self.get_id())})
        client.close()
        assert result.count() == 1
        assert isinstance(result[0]["_id"], ObjectId)
        for value in result[0]:
            if value not in ["_id", "files"]:
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

    def add_step(self, _id_step, step):
        self.data["steps"].append({"_id": ObjectId(_id_step), "step": step})

    def custom_step(self, position, data):
        self.data["steps"][position]["step"]=data

    def remove_step(self, position):
        del self.data["steps"][position]

    def add_file_recipe(self, filename, is_main):
        return file_model.FileTest().custom_filename(filename).\
            custom_metadata({"kind": "recipe",
                             "_id": ObjectId(self.data["_id"]),
                             "is_main": is_main}).insert()

    @staticmethod
    def add_file_step(_id_step, filename, is_main):
        return file_model.FileTest().custom_filename(filename).\
            custom_metadata({"kind": "step",
                             "_id": ObjectId(_id_step),
                             "is_main": is_main}).insert()

from pymongo import MongoClient
from bson import ObjectId
import copy
import re


import utils

import tests.file.model as file_model

mongo = utils.Mongo


class RecipeTest(object):

    def __init__(self):
        self._id = ObjectId()
        self.title = "qa_rhr_title"
        self.slug = "qa_rhr_slug"
        self.level = 1
        self.resume = "qa_rhr_resume"
        self.cooking_time = 10
        self.preparation_time = 5
        self.nb_people = 2
        self.note = "qa_rhr_note"
        self.categories = ["qa_rhr_category"]
        self.steps = []

    def display(self):
        print(self.__dict__)

    def get_param(self):
        return [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

    def get_id(self):
        return str(self._id)

    def get(self):
        return copy.deepcopy(self.__dict__)

    def get_without_id(self):
        data = self.get()
        data.pop("_id")
        return data

    def get_stringify(self):
        return mongo.format_json(self.get())

    def get_stringify_with_file(self, files_recipe, files_steps):
        data = mongo.format_json(self.get())
        data["files"] = []
        for recipe_file in files_recipe:
            data["files"].append(recipe_file.get_for_enrichment())
        if len(files_steps) != 0:
            for i, j in files_steps.items():
                for step in data["steps"]:
                    if str(step["_id"]) == i:
                        step["files"] = []
                        for step_file in j:
                            step["files"].append(step_file.get_for_enrichment())
        return mongo.format_json(data)

    def custom(self, data):
        for i, j in data.items():
            if i in self.get_param():
                if i == '_id':
                    self.__setattr__(i, ObjectId(j))
                else:
                    self.__setattr__(i, j)
        return self

    def select_ok(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        recipe = db.find_one({"_id": ObjectId(self.get_id())})
        client.close()
        assert recipe is not None
        for value in recipe:
            if value not in ["_id", "files"]:
                assert recipe[value] == self.__getattribute__(value)

    def select_ok_by_title(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        recipe = db.find_one({"title": self.title})
        client.close()
        assert recipe is not None
        for value in recipe:
            if value not in ["_id", "files"]:
                assert recipe[value] == self.__getattribute__(value)

    def select_nok(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.count_documents({"_id": ObjectId(self.get_id())})
        client.close()
        assert result == 0

    def select_nok_by_title(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.count_documents({"title": self.title})
        client.close()
        assert result == 0

    def insert(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        query = db.insert_one(self.get_without_id())
        client.close()
        self.__setattr__("_id", query.inserted_id)
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
        self.steps.append({"_id": ObjectId(_id_step), "step": step})

    def custom_step(self, position, data):
        self.steps[position]["step"] = data

    def remove_step(self, position):
        del self.steps[position]

    def add_file_recipe(self, filename, is_main, **kwargs):
        file = file_model.FileTest().custom({"filename": filename,
                                             "metadata": {"kind": "recipe",
                                                          "_id": ObjectId(self._id),
                                                          "is_main": is_main}}).insert()
        if "identifier" in kwargs.keys():
            file.custom({"_id": kwargs["identifier"]})
        return file

    @staticmethod
    def add_file_step(_id_step, filename, is_main, **kwargs):
        file = file_model.FileTest().custom({"filename": filename,
                                             "metadata": {"kind": "step",
                                                          "_id": ObjectId(_id_step),
                                                          "is_main": is_main}}).insert()
        if "identifier" in kwargs.keys():
            file.custom({"_id": kwargs["identifier"]})
        return file

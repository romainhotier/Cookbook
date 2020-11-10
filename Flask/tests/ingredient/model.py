from pymongo import MongoClient
from bson import ObjectId
import copy
import re

import utils
import app.ingredient.model as ingredient_model
import app.recipe.model as recipe_model

import tests.file.model as file_model

mongo = utils.Mongo()


class IngredientTest(object):

    def __init__(self):
        self._id = ObjectId()
        self.name = "qa_rhr_name"
        self.slug = "qa_rhr_slug"
        self.categories = ["qa_rhr_category"]
        self.nutriments = {"calories_per_100g": {"quantity": 60, "unit": "g"},
                           "carbohydrates_per_100g": {"quantity": 20, "unit": "g"},
                           "fats_per_100g": {"quantity": 10, "unit": "g"},
                           "proteins_per_100g": {"quantity": 30, "unit": "g"}}

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
        return mongo.to_json(self.get())

    def get_stringify_with_files(self, files):
        data = mongo.to_json(self.get())
        data["files"] = []
        for file in files:
            data["files"].append(file.get_for_enrichment())
        return mongo.to_json(data)

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
        db = client[mongo.name][mongo.collection_ingredient]
        ingredient = db.find_one({"_id": ObjectId(self.get_id())})
        client.close()
        assert ingredient is not None
        for value in ingredient:
            if value not in ["_id"]:
                assert ingredient[value] == self.__getattribute__(value)

    def select_ok_by_name(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        ingredient = db.find_one({"name": self.name})
        client.close()
        assert ingredient is not None
        for value in ingredient:
            if value not in ["_id"]:
                assert ingredient[value] == self.__getattribute__(value)

    def select_nok(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.count_documents({"_id": ObjectId(self.get_id())})
        client.close()
        assert result == 0

    def select_nok_by_name(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.count_documents({"name": self.name})
        client.close()
        assert result == 0

    def insert(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        query = db.insert_one(self.get_without_id())
        client.close()
        self.__setattr__("_id", query.inserted_id)
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
        db.delete_many({"name": {"$regex": rgx}})
        client.close()
        return

    def add_file(self, filename, is_main, **kwargs):
        file = file_model.FileTest().custom({"filename": filename,
                                             "metadata": {"kind": "ingredient",
                                                          "_id": ObjectId(self._id),
                                                          "is_main": is_main}}).insert()
        if "identifier" in kwargs.keys():
            file.custom({"_id": kwargs["identifier"]})
        return file


class IngredientRecipeTest(object):

    def __init__(self):
        self._id = ObjectId()
        self.quantity = 0
        self.unit = "qa_rhr_unit"
        self._id_ingredient = ObjectId()
        self._id_recipe = ObjectId()

    def display(self):
        print(self.__dict__)

    def get_param(self):
        return [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

    def get_id(self):
        return str(self._id)

    def get_id_ingredient(self):
        return str(self._id_ingredient)

    def get_id_recipe(self):
        return str(self._id_recipe)

    def get(self):
        return copy.deepcopy(self.__dict__)

    def get_without_id(self):
        data = self.get()
        data.pop("_id")
        return data

    def get_stringify(self):
        return mongo.to_json(self.get())

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
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        ingredient_recipe = db.find_one({"_id": ObjectId(self.get_id())})
        client.close()
        assert ingredient_recipe is not None
        for value in ingredient_recipe:
            if value not in ["_id"]:
                assert ingredient_recipe[value] == self.__getattribute__(value)

    def select_nok(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        result = db.count_documents({"_id": ObjectId(self.get_id())})
        client.close()
        assert result == 0

    def select_nok_by_unit(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        result = db.count_documents({"unit": self.unit})
        client.close()
        assert result == 0

    def select_nok_by_linked(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        result = db.count_documents({'$and': [{"_id_ingredient": self._id_ingredient},
                                              {"_id_recipe": self._id_recipe}]})
        client.close()
        assert result == 0

    def insert(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        query = db.insert_one(self.get_without_id())
        client.close()
        self.__setattr__("_id", query.inserted_id)
        return self

    def delete(self):
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        db.delete_one({"_id": ObjectId(self.get_id())})
        client.close()
        return

    @staticmethod
    def clean():
        rgx = re.compile('.*qa_rhr.*', re.IGNORECASE)
        rgx2 = re.compile('.*invalid.*', re.IGNORECASE)
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        db.delete_many({"unit": {"$regex": rgx}})
        db.delete_many({"unit": {"$regex": rgx2}})
        client.close()

    # def add_name(self):
    #     self.__setattr__("name", ingredient_model.Ingredient().get_name_by_id(self._id_ingredient))
    #     return self

    def add_title(self):
        self.__setattr__("title", recipe_model.Recipe().get_title_by_id(self._id_recipe))
        return self

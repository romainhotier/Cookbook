from pymongo import MongoClient
from bson import ObjectId
import copy
import re


import utils

import tests.file.model as file_model

mongo = utils.Mongo()


class RecipeTest(object):

    def __init__(self):
        """ RecipeTest model.

        - _id = ObjectId in mongo
        - title = Recipe's name (Unique)
        - slug = Recipe's slug (Unique)
        - level = Recipe's level
        - resume = Recipe's resume
        - cooking_time = Recipe's cooking_time
        - preparation_time = Recipe's preparation_time
        - nb_people = Recipe's nb_people
        - note = Recipe's note
        - categories = Recipe's categories
        - steps = Recipe's steps
        - status = Recipe's status
        """
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
        self.status = "in_progress"

    def display(self):
        """ Print RecipeTest model.

        Returns
        -------
        Any
            Display RecipeTest.
        """
        print(self.__dict__)

    def get_param(self):
        """ Get RecipeTest parameters.

        Returns
        -------
        list
            RecipeTest parameters.
        """
        return [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

    def get_id(self):
        """ Get _id of RecipeTest.

        Returns
        -------
        str
            RecipeTest's _id.
        """
        return str(self._id)

    def get(self):
        """ Get RecipeTest.

        Returns
        -------
        dict
            Copy of RecipeTest.
        """
        return copy.deepcopy(self.__dict__)

    def get_without_id(self):
        """ Get RecipeTest without _id attribute.

        Returns
        -------
        dict
            Copy of RecipeTest without _id.
        """
        data = self.get()
        data.pop("_id")
        return data

    def get_stringify(self):
        """ Get RecipeTest with ObjectId stringify.

        Returns
        -------
        dict
            Copy of RecipeTest with ObjectId stringify.
        """
        return mongo.to_json(self.get())

    def get_stringify_with_file(self, files_recipe, files_steps):
        """ Get RecipeTest with ObjectId stringify and files.

        Returns
        -------
        dict
            Copy of RecipeTest with ObjectId stringify with files.
        """
        data = mongo.to_json(self.get())
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
        return mongo.to_json(data)

    def custom(self, data):
        """ Update RecipeTest.

        Parameters
        ----------
        data : dict
            Data to be updated for RecipeTest.

        Returns
        -------
        Any
            Self
        """
        for i, j in data.items():
            if i in self.get_param():
                if i == '_id':
                    self.__setattr__(i, ObjectId(j))
                else:
                    self.__setattr__(i, j)
        return self

    def select_ok(self):
        """ Check if RecipeTest is correct.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        recipe = db.find_one({"_id": ObjectId(self.get_id())})
        client.close()
        assert recipe is not None
        for value in recipe:
            if value not in ["_id", "files"]:
                assert recipe[value] == self.__getattribute__(value)

    def select_ok_by_title(self):
        """ Check if RecipeTest is correct by title.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        recipe = db.find_one({"title": self.title})
        client.close()
        assert recipe is not None
        for value in recipe:
            if value not in ["_id", "files"]:
                assert recipe[value] == self.__getattribute__(value)

    def select_nok(self):
        """ Check if RecipeTest doesn't exist.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.count_documents({"_id": ObjectId(self.get_id())})
        client.close()
        assert result == 0

    def select_nok_by_title(self):
        """ Check if RecipeTest doesn't exist by title.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.count_documents({"title": self.title})
        client.close()
        assert result == 0

    def insert(self):
        """ Insert RecipeTest.

        Returns
        -------
        Any
            Self
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        query = db.insert_one(self.get_without_id())
        client.close()
        self.__setattr__("_id", query.inserted_id)
        return self

    def delete(self):
        """ Delete RecipeTest.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.delete_one({"_id": ObjectId(self.get_id())})
        client.close()
        return

    @staticmethod
    def clean():
        """ Clean RecipeTest by title and slug.
        """
        rgx = re.compile('.*qa_rhr.*', re.IGNORECASE)
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.delete_many({"title": {"$regex": rgx}})
        db.delete_many({"slug": {"$regex": rgx}})
        client.close()
        return

    def add_step(self, _id_step, description):
        """ Insert a Step.

        Parameters
        ----------
        _id_step : str
            Step's ObjectId.
        description : str
            Step's description.
        """
        self.steps.append({"_id": ObjectId(_id_step), "description": description})

    def custom_step(self, position, data):
        """ Custom a Step.

        Parameters
        ----------
        position : int
            Step's position in array.
        data : str
            Step's data.
        """
        self.steps[position]["description"] = data

    def remove_step(self, position):
        """ Delete a Step.

        Parameters
        ----------
        position : int
            Step's position in array.
        """
        del self.steps[position]

    def add_file_recipe(self, filename, is_main, **kwargs):
        """ Add a file to RecipeTest.

        Parameters
        ----------
        filename : str
            Name of File.
        is_main : bool
            Is primary or not.
        kwargs : Any
            identifier : force ObjectId

        Returns
        -------
        Any
            FileTest added.
        """
        file = file_model.FileTest().custom({"filename": filename,
                                             "metadata": {"kind": "recipe",
                                                          "_id_parent": ObjectId(self._id),
                                                          "is_main": is_main}}).insert()
        if "identifier" in kwargs.keys():
            file.custom({"_id": kwargs["identifier"]})
        return file

    @staticmethod
    def add_file_step(_id_step, filename, is_main, **kwargs):
        """ Add a file to RecipeTest's step.

        Parameters
        ----------
        _id_step : str
            Step's ObjectId
        filename : str
            Name of File.
        is_main : bool
            Is primary or not.
        kwargs : Any
            identifier : force ObjectId

        Returns
        -------
        Any
            FileTest added.
        """
        file = file_model.FileTest().custom({"filename": filename,
                                             "metadata": {"kind": "step",
                                                          "_id_parent": ObjectId(_id_step),
                                                          "is_main": is_main}}).insert()
        if "identifier" in kwargs.keys():
            file.custom({"_id": kwargs["identifier"]})
        return file

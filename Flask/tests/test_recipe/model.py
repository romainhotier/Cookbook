from pymongo import MongoClient
from bson import ObjectId
import copy
import re

import utils

import tests.test_file_mongo.model as filemongotest_model
FileMongoTest = filemongotest_model.FileMongoTest()

mongo = utils.Mongo()


class RecipeTest(object):

    def __init__(self):
        """ RecipeTest model.

        - _id = ObjectId in mongo
        - categories = Recipe's categories
        - cooking_time = Recipe's cooking_time
        - ingredients = Recipe's ingredients
        - level = Recipe's level
        - nb_people = Recipe's nb_people
        - note = Recipe's note
        - preparation_time = Recipe's preparation_time
        - resume = Recipe's resume
        - slug = Recipe's slug (Unique)
        - status = Recipe's status
        - steps = Recipe's steps
        - title = Recipe's name (Unique)
        """
        self._id = ObjectId()
        self.categories = ["qa_rhr_category"]
        self.cooking_time = 10
        self.ingredients = []
        self.level = 1
        self.nb_people = 2
        self.note = "qa_rhr_note"
        self.preparation_time = 5
        self.resume = "qa_rhr_resume"
        self.slug = "qa_rhr_slug"
        self.status = "in_progress"
        self.steps = []
        self.title = "qa_rhr_title"

    """ recipe """
    def display(self):
        """ Print RecipeTest model.

        Returns
        -------
        dict
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

    def get_stringify(self):
        """ Get RecipeTest with ObjectId stringify.

        Returns
        -------
        dict
            Copy of RecipeTest with ObjectId stringify.
        """
        return mongo.to_json(self.get())

    def insert(self):
        """ Insert RecipeTest.

        Returns
        -------
        RecipeTest
            Self
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        data = self.get()
        data.pop("_id")
        query = db.insert_one(data)
        client.close()
        self.__setattr__("_id", query.inserted_id)
        return self

    def custom(self, data):
        """ Update RecipeTest.

        Parameters
        ----------
        data : dict
            Data to be updated for RecipeTest.

        Returns
        -------
        RecipeTest
            Self
        """
        for i, j in data.items():
            if i in self.get_param():
                if i == '_id':
                    self.__setattr__(i, ObjectId(j))
                else:
                    self.__setattr__(i, j)
        return self

    def custom_id_from_body(self, data):
        """ Update RecipeTest's _id from PostRecipe's body.

        Parameters
        ----------
        data : dict
            PostRecipe's body.

        Returns
        -------
        RecipeTest
            Self
        """
        self.__setattr__("_id", ObjectId(data["data"]["_id"]))
        return self

    def delete(self):
        """ Delete RecipeTest.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.delete_one({"_id": ObjectId(self.get_id())})
        client.close()
        return

    def check_bdd_data(self):
        """ Check if RecipeTest is correct.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        recipe = db.find_one({"_id": ObjectId(self.get_id())})
        client.close()
        assert recipe is not None
        for value in recipe:
            if value in ["steps"]:  # check for steps
                for i, step in enumerate(recipe["steps"]):
                    if "_id" not in self.__getattribute__(value)[i]:  # new step
                        assert step["description"] == self.__getattribute__(value)[i]["description"]
                    else:  # old step
                        assert mongo.to_json(step) == mongo.to_json(self.__getattribute__(value)[i])
            elif value not in ["_id"]:
                assert recipe[value] == self.__getattribute__(value)

    def check_doesnt_exist_by_id(self):
        """ Check if RecipeTest doesn't exist.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.count_documents({"_id": ObjectId(self.get_id())})
        client.close()
        assert result == 0

    def check_doesnt_exist_by_title(self):
        """ Check if RecipeTest doesn't exist by title.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.count_documents({"title": self.title})
        client.close()
        assert result == 0

    def check_doesnt_exist_by_slug(self):
        """ Check if RecipeTest doesn't exist by slug.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.count_documents({"slug": self.slug})
        client.close()
        assert result == 0

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

    """ steps """
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

    """ ingredients """
    def add_ingredient(self, _id, quantity, unit):
        """ Add a IngredientTest to RecipeTest.

        Parameters
        ----------
        _id : str
            IngredientTest's ObjectId.
        quantity : int
            IngredientTest's quantity.
        unit : str
            IngredientTest's unit

        Returns
        -------
        RecipeTest
            RecipeTest.
        """
        self.ingredients.append({"_id": _id, "quantity": quantity, "unit": unit})
        return self

    def delete_ingredient(self, _id):
        """ Delete a IngredientTest to RecipeTest.

        Parameters
        ----------
        _id : str
            IngredientTest's ObjectId.

        Returns
        -------
        RecipeTest
            RecipeTest.
        """
        for ingredient in self.ingredients:
            if ingredient["_id"] == _id:
                self.ingredients.remove(ingredient)
                break
        return self

    """ files mongo """
    def add_file_mongo_recipe(self, filename, is_main, **kwargs):
        """ Add a Mongo file to RecipeTest.

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
        FileTest
            FileTest added.
        """
        file = filemongotest_model.FileMongoTest().custom({"filename": filename,
                                                           "metadata": {"kind": "recipe",
                                                                        "_id_parent": ObjectId(self._id),
                                                                        "is_main": is_main}}).insert()
        if "identifier" in kwargs.keys():
            file.custom({"_id": kwargs["identifier"]})
        return file

    @staticmethod
    def add_file_mongo_step(_id_step, filename, is_main, **kwargs):
        """ Add a Mongo file to RecipeTest's step.

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
        FileTest
            FileTest added.
        """
        file = filemongotest_model.FileMongoTest().custom({"filename": filename,
                                                           "metadata": {"kind": "step",
                                                                        "_id_parent": ObjectId(_id_step),
                                                                        "is_main": is_main}}).insert()
        if "identifier" in kwargs.keys():
            file.custom({"_id": kwargs["identifier"]})
        return file

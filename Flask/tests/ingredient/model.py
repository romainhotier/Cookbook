from pymongo import MongoClient
from bson import ObjectId
import copy
import re

import utils
import app.ingredient.model as ingredient_model
import app.recipe.model as recipe_model

import tests.file.model as filetest_model
FileTest = filetest_model.FileTest()

mongo = utils.Mongo()
ingredient = ingredient_model.Ingredient()
recipe = recipe_model.Recipe()


class IngredientTest(object):

    def __init__(self):
        """ IngredientTest model.

        - _id = ObjectId in mongo
        - categories = Ingredient's categories
        - name = Ingredient's name (Unique)
        - nutriments = Ingredient's nutriments
        - slug = Ingredient's slug (Unique)
        """
        self._id = ObjectId()
        self.name = "qa_rhr_name"
        self.slug = "qa_rhr_slug"
        self.categories = ["qa_rhr_category"]
        self.nutriments = {"calories": 60,
                           "carbohydrates": 40,
                           "fats": 10,
                           "proteins": 30,
                           "portion": 1}

    def display(self):
        """ Print IngredientTest model.

        Returns
        -------
        Any
            Display IngredientTest.
        """
        print(self.__dict__)

    def get_param(self):
        """ Get IngredientTest parameters.

        Returns
        -------
        list
            IngredientTest parameters.
        """
        return [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

    def get_id(self):
        """ Get _id of IngredientTest.

        Returns
        -------
        str
            IngredientTest's _id.
        """
        return str(self._id)

    def get(self):
        """ Get IngredientTest.

        Returns
        -------
        dict
            Copy of IngredientTest.
        """
        return copy.deepcopy(self.__dict__)

    def get_stringify(self):
        """ Get IngredientTest with ObjectId stringify.

        Returns
        -------
        dict
            Copy of IngredientTest with ObjectId stringify.
        """
        return mongo.to_json(self.get())

    def insert(self):
        """ Insert IngredientTest.

        Returns
        -------
        IngredientTest
            Self
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        data = self.get()
        data.pop("_id")
        query = db.insert_one(data)
        client.close()
        self.__setattr__("_id", query.inserted_id)
        return self

    def custom(self, data):
        """ Update IngredientTest.

        Parameters
        ----------
        data : dict
            Data to be updated for IngredientTest.

        Returns
        -------
        IngredientTest
            Self
        """
        for i, j in data.items():
            if i in self.get_param():
                if i == '_id':
                    self.__setattr__(i, ObjectId(j))
                if i == "nutriments":
                    try:
                        for k, v in data[i].items():
                            if k in ["calories", "carbohydrates", "fats", "proteins", "portion"]:
                                self.nutriments[k] = v
                    except AttributeError:
                        pass
                else:
                    self.__setattr__(i, j)
        return self

    def custom_id_from_body(self, data):
        """ Update IngredientTest's _id from PostIngredient's body.

        Parameters
        ----------
        data : dict
            PostIngredient's body.

        Returns
        -------
        IngredientTest
            Self
        """
        self.__setattr__("_id", ObjectId(data["data"]["_id"]))
        return self

    def delete(self):
        """ Delete IngredientTest.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        db.delete_one({"_id": ObjectId(self.get_id())})
        client.close()
        return

    def check_bdd_data(self):
        """ Check if IngredientTest is correct.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find_one({"_id": ObjectId(self.get_id())})
        client.close()
        assert result is not None
        for value in result:
            if value not in ["_id"]:
                assert result[value] == self.__getattribute__(value)

    def check_doesnt_exist_by_id(self):
        """ Check if IngredientTest doesn't exist.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.count_documents({"_id": ObjectId(self.get_id())})
        client.close()
        assert result == 0

    def check_doesnt_exist_by_name(self):
        """ Check if IngredientTest doesn't exist by name.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.count_documents({"name": self.name})
        client.close()
        assert result == 0

    @staticmethod
    def clean():
        """ Clean IngredientTest by name.
        """
        rgx = re.compile('.*qa_rhr.*', re.IGNORECASE)
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        db.delete_many({"name": {"$regex": rgx}})
        client.close()
        return

    """ files """
    def add_file(self, filename, is_main, **kwargs):
        """ Add a file to IngredientTest.

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
            Response server if validation failed, True otherwise.

        """
        file = FileTest.custom({"filename": filename,
                                "metadata": {"kind": "ingredient",
                                             "_id_parent": ObjectId(self._id),
                                             "is_main": is_main}}).insert()
        if "identifier" in kwargs.keys():
            file.custom({"_id": kwargs["identifier"]})
        return file

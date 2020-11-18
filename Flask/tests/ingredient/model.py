from pymongo import MongoClient
from bson import ObjectId
import copy
import re

import utils
import app.ingredient.model as ingredient_model
import app.recipe.model as recipe_model

import tests.file.model as file_model

mongo = utils.Mongo()
ingredient = ingredient_model.Ingredient()
recipe = recipe_model.Recipe()


class IngredientTest(object):

    def __init__(self):
        """ IngredientTest model.

        - _id = ObjectId in mongo
        - name = Ingredient's name (Unique)
        - slug = Ingredient's slug (Unique)
        - categories = Ingredient's categories
        - nutriments = Ingredient's nutriments
        """
        self._id = ObjectId()
        self.name = "qa_rhr_name"
        self.slug = "qa_rhr_slug"
        self.categories = ["qa_rhr_category"]
        self.nutriments = {"calories": 60,
                           "carbohydrates": 40,
                           "fats": 10,
                           "proteins": 30,
                           "info": "per 100g"}

    def display(self):
        """ Print IngredientTest model.

        Returns
        -------
        Any
            Display IngredientTest
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

    def get_without_id(self):
        """ Get IngredientTest without _id attribute.

        Returns
        -------
        dict
            Copy of IngredientTest without _id.
        """
        data = self.get()
        data.pop("_id")
        return data

    def get_stringify(self):
        """ Get IngredientTest with ObjectId stringify.

        Returns
        -------
        dict
            Copy of IngredientTest with ObjectId stringify.
        """
        return mongo.to_json(self.get())

    def get_stringify_with_files(self, files):
        """ Get IngredientTest with ObjectId stringify and files.

        Returns
        -------
        dict
            Copy of IngredientTest with ObjectId stringify with files.
        """
        data = mongo.to_json(self.get())
        data["files"] = [file.get_for_enrichment() for file in files]
        return mongo.to_json(data)

    def custom(self, data):
        """ Update IngredientTest.

        Parameters
        ----------
        data : dict
            Data to be updated for IngredientTest.

        Returns
        -------
        Any
            Self
        """
        for i, j in data.items():
            if i in self.get_param():
                if i == '_id':
                    self.__setattr__(i, ObjectId(j))
                if i == "nutriments":
                    try:
                        for k, v in data[i].items():
                            if k in ["calories", "carbohydrates", "fats", "proteins", "info"]:
                                self.nutriments[k] = v
                    except AttributeError:
                        pass
                else:
                    self.__setattr__(i, j)
        return self

    def select_ok(self):
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

    def select_ok_by_name(self):
        """ Check if IngredientTest is correct by name.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find_one({"name": self.name})
        client.close()
        assert result is not None
        for value in result:
            if value not in ["_id"]:
                assert result[value] == self.__getattribute__(value)

    def select_nok(self):
        """ Check if IngredientTest doesn't exist.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.count_documents({"_id": ObjectId(self.get_id())})
        client.close()
        assert result == 0

    def select_nok_by_name(self):
        """ Check if IngredientTest doesn't exist by name.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.count_documents({"name": self.name})
        client.close()
        assert result == 0

    def insert(self):
        """ Insert IngredientTest.

        Returns
        -------
        Any
            Self
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        query = db.insert_one(self.get_without_id())
        client.close()
        self.__setattr__("_id", query.inserted_id)
        return self

    def delete(self):
        """ Delete IngredientTest.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        db.delete_one({"_id": ObjectId(self.get_id())})
        client.close()
        return

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
        Any
            Response server if validation failed, True otherwise.

        """
        file = file_model.FileTest().custom({"filename": filename,
                                             "metadata": {"kind": "ingredient",
                                                          "_id_parent": ObjectId(self._id),
                                                          "is_main": is_main}}).insert()
        if "identifier" in kwargs.keys():
            file.custom({"_id": kwargs["identifier"]})
        return file


class IngredientRecipeTest(object):

    def __init__(self):
        """ IngredientTest model.

        - _id = ObjectId in mongo
        - _id_recipe = Recipe's ObjectId (Unique)
        - _id_ingredient = Ingredient's ObjectId (Unique)
        - quantity = Quantity of the ingredient in this recipe.
        - unit = Unit of the quantity.
        """
        self._id = ObjectId()
        self.quantity = 0
        self.unit = "qa_rhr_unit"
        self._id_ingredient = ObjectId()
        self._id_recipe = ObjectId()

    def display(self):
        """ Print IngredientRecipeTest model.

        Returns
        -------
        Any
            Display IngredientRecipeTest
        """
        print(self.__dict__)

    def get_param(self):
        """ Get IngredientRecipeTest parameters.

        Returns
        -------
        list
            IngredientRecipeTest parameters.
        """
        return [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

    def get_id(self):
        """ Get _id of IngredientRecipeTest.

        Returns
        -------
        str
            IngredientRecipeTest's _id.
        """
        return str(self._id)

    def get_id_ingredient(self):
        """ Get _id_ingredient of IngredientRecipeTest.

        Returns
        -------
        str
            IngredientRecipeTest's _id_ingredient.
        """
        return str(self._id_ingredient)

    def get_id_recipe(self):
        """ Get _id_recipe of IngredientRecipeTest.

        Returns
        -------
        str
            IngredientRecipeTest's _id_recipe.
        """
        return str(self._id_recipe)

    def get(self):
        """ Get IngredientRecipeTest.

        Returns
        -------
        dict
            Copy of IngredientRecipeTest.
        """
        return copy.deepcopy(self.__dict__)

    def get_without_id(self):
        """ Get IngredientRecipeTest without _id attribute.

        Returns
        -------
        dict
            Copy of IngredientRecipeTest without _id.
        """
        data = self.get()
        data.pop("_id")
        return data

    def get_stringify(self):
        """ Get IngredientRecipeTest with ObjectId stringify.

        Returns
        -------
        dict
            Copy of IngredientRecipeTest with ObjectId stringify.
        """
        return mongo.to_json(self.get())

    def custom(self, data):
        """ Update IngredientRecipeTest.

        Parameters
        ----------
        data : dict
            Data to be updated for IngredientRecipeTest.

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
        """ Check if IngredientRecipeTest is correct.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        ingredient_recipe = db.find_one({"_id": ObjectId(self.get_id())})
        client.close()
        assert ingredient_recipe is not None
        for value in ingredient_recipe:
            if value not in ["_id"]:
                assert ingredient_recipe[value] == self.__getattribute__(value)

    def select_nok(self):
        """ Check if IngredientRecipeTest doesn't exist.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        result = db.count_documents({"_id": ObjectId(self.get_id())})
        client.close()
        assert result == 0

    def select_nok_by_unit(self):
        """ Check if IngredientRecipeTest doesn't exist by unit.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        result = db.count_documents({"unit": self.unit})
        client.close()
        assert result == 0

    def select_nok_by_linked(self):
        """ Check if IngredientRecipeTest doesn't exist by both parent _ids.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        result = db.count_documents({'$and': [{"_id_ingredient": self._id_ingredient},
                                              {"_id_recipe": self._id_recipe}]})
        client.close()
        assert result == 0

    def insert(self):
        """ Insert IngredientRecipeTest.

        Returns
        -------
        Any
            Self
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        query = db.insert_one(self.get_without_id())
        client.close()
        self.__setattr__("_id", query.inserted_id)
        return self

    def delete(self):
        """ Delete IngredientRecipeTest.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        db.delete_one({"_id": ObjectId(self.get_id())})
        client.close()
        return

    @staticmethod
    def clean():
        """ Clean IngredientRecipeTest by unit.
        """
        rgx = re.compile('.*qa_rhr.*', re.IGNORECASE)
        rgx2 = re.compile('.*invalid.*', re.IGNORECASE)
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        db.delete_many({"unit": {"$regex": rgx}})
        db.delete_many({"unit": {"$regex": rgx2}})
        client.close()

    def add_name(self):
        self.__setattr__("name", ingredient.get_name_by_id(str(self._id_ingredient)))
        return self

    def add_title(self):
        self.__setattr__("title", recipe.get_title_by_id(str(self._id_recipe)))
        return self

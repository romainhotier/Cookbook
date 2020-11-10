from pymongo import MongoClient
from bson import ObjectId
import re

import utils
import app.file.model as file_model
import app.recipe.model as recipe_model

mongo = utils.Mongo()


class Ingredient(object):

    def __init__(self):
        """ Ingredient model.

        - _id = ObjectId in mongo
        - name = Ingredient's name (Unique)
        - slug = Ingredient's slug (Unique)
        - categories = Ingredient's categories
        - nutriments = Ingredient's nutriments
        """
        self.result = {}

    def select_all(self):
        """ Get all existing ingredient.

        Returns
        -------
        Any
            List of all ingredients.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        cursor = db.find({})
        client.close()
        self.result = mongo.to_json([ingredient for ingredient in cursor])
        return self

    def select_one(self, _id):
        """ Get one ingredient by it's ObjectId.

        Parameters
        ----------
        _id : str
            ObjectId of the ingredient.

        Returns
        -------
        Any
            One ingredient
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.result = mongo.to_json(result)
        return self

    def search(self, data):
        """ Search ingredients with matching keys.

        Parameters
        ----------
        data : dict
            Keys and values to match.

        Returns
        -------
        Any
            List of matched ingredients.
        """
        search = {}
        for i, j in data.items():
            if i == "categories":
                search[i] = {"$in": [re.compile('.*{0}.*'.format(j), re.IGNORECASE)]}
            else:
                search[i] = {"$regex": re.compile('.*{0}.*'.format(j), re.IGNORECASE)}
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        cursor = db.find(search)
        client.close()
        self.result = mongo.to_json([ingredient for ingredient in cursor])
        return self

    @staticmethod
    def check_ingredient_is_unique(key, value):
        """ Check if an ingredient already exist with a specific key.

        Parameters
        ----------
        key : str
            Key to be tested.
        value : str
            Value of the tested key.

        Returns
        -------
        bool
            True if key/value doesn't exist in mongo.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.count_documents({key: value})
        client.close()
        if result == 0:
            return True
        else:
            return False

    def insert(self, data):
        """ Insert an Ingredient.

        Parameters
        ----------
        data : dict
            Information of the ingredient.

        Returns
        -------
        Any
            Inserted ingredient.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        query = db.insert_one(data)
        result = db.find_one({"_id": ObjectId(query.inserted_id)})
        client.close()
        self.result = mongo.to_json(result)
        return self

    def update(self, _id, data):
        """ Update an Ingredient.

        Parameters
        ----------
        _id : str
            ObjectId of the ingredient.
        data : dict
            Information of the ingredient.

        Returns
        -------
        Any
            Updated ingredient.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        db.update_one({"_id": ObjectId(_id)}, {'$set': data})
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.result = mongo.to_json(result)
        return self

    @staticmethod
    def delete(_id):
        """ Delete an Ingredient.

        Parameters
        ----------
        _id : str
            ObjectId of the ingredient.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        db.delete_one({"_id": ObjectId(_id)})
        client.close()
        return

    def add_enrichment_file_for_all(self):
        """ Add files informations for all ingredient.

        Returns
        -------
        Any
            List of ingredient with files informations.
        """
        for ingredient in self.result:
            ingredient["files"] = []
            """ get files """
            files = file_model.File().get_all_file_by_id_parent(_id_parent=ingredient["_id"]).result
            for file in files:
                file_enrichment = {"_id": str(file["_id"]), "is_main": file["metadata"]["is_main"]}
                ingredient["files"].append(file_enrichment)
        return self

    def add_enrichment_file_for_one(self):
        """ Add files informations for one ingredient.

        Returns
        -------
        Any
            One ingredient with files informations.
        """
        self.result["files"] = []
        """ get files """
        files = file_model.File().get_all_file_by_id_parent(_id_parent=self.result["_id"]).result
        for file in files:
            file_enrichment = {"_id": str(file["_id"]), "is_main": file["metadata"]["is_main"]}
            self.result["files"].append(file_enrichment)
        return self

    @staticmethod
    def get_name_by_id(_id):
        """ Get ingredient's name associated with a ObjectId.

        Parameters
        ----------
        _id : str
            ObjectId of the ingredient.

        Returns
        -------
        str
            Name of the ingredient.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        return result["name"]


class IngredientRecipe(object):

    def __init__(self):
        """ Link between Ingredient and Recipe model.

        - _id_ingredient = Ingredient's ObjectId in mongo (Unique)
        - _id_recipe = Recipe's ObjectId in mongo (Unique)
        - quantity = Quantity of the ingredient for this recipe
        - unit = Unit of the quantity
        """
        self.result = {}

    def insert(self, data):
        """ Associate an Ingredient to a Recipe.

        Parameters
        ----------
        data : dict
            Information of the link.

        Returns
        -------
        Any
            Association Ingredient and Recipe.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        query = db.insert_one(data)
        result = db.find_one({"_id": ObjectId(query.inserted_id)})
        client.close()
        self.result = mongo.to_json(result)
        return self

    def select_all_by_id_recipe(self, _id_recipe):
        """ Get all Ingredients for a Recipe.

        Parameters
        ----------
        _id_recipe : str
            ObjectId of the recipe.

        Returns
        -------
        Any
            List of Ingredient's Recipe.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        cursor = db.find({"_id_recipe": ObjectId(_id_recipe)})
        client.close()
        self.result = mongo.to_json([ingredient for ingredient in cursor])
        return self

    def select_all_by_id_ingredient(self, _id_ingredient):
        """ Get all Recipe associated to an Ingredient.

        Parameters
        ----------
        _id_ingredient : str
            ObjectId of the ingredient.

        Returns
        -------
        Any
            List of Recipe's with this Ingredient.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        cursor = db.find({"_id_ingredient": ObjectId(_id_ingredient)})
        client.close()
        self.result = mongo.to_json([recipe for recipe in cursor])
        return self

    def update(self, _id, data):
        """ Update an association Ingredient Recipe.

        Parameters
        ----------
        _id : str
            ObjectId of the association.
        data : dict
            Information of the association.

        Returns
        -------
        Any
            Updated association.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        db.update_one({"_id": ObjectId(_id)}, {'$set': data})
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.result = mongo.to_json(result)
        return self

    @staticmethod
    def delete(_id):
        """ Delete an association Ingredient Recipe.

        Parameters
        ----------
        _id : str
            ObjectId of the association.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        db.delete_one({"_id": ObjectId(_id)})
        client.close()
        return

    @staticmethod
    def clean_link_by_id_ingredient(_id_ingredient):
        """ Delete all association with a specific Ingredient.

        Parameters
        ----------
        _id_ingredient : str
            ObjectId of the Ingredient.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        db.delete_many({"_id_ingredient": ObjectId(_id_ingredient)})
        client.close()
        return

    @staticmethod
    def clean_link_by_id_recipe(_id_recipe):
        """ Delete all association with a specific Recipe.

        Parameters
        ----------
        _id_recipe : str
            ObjectId of the Recipe.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        db.delete_many({"_id_recipe": ObjectId(_id_recipe)})
        client.close()
        return

    @staticmethod
    def check_link_is_unique(_id_ingredient, _id_recipe):
        """ Check if an association Ingredient Recipe exist.

        Parameters
        ----------
        _id_ingredient : str
            ObjectId of the Ingredient.
        _id_recipe : str
            ObjectId of the Recipe.

        Returns
        -------
        bool
            True if assocaition doesn't exist in mongo.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient_recipe]
        result = db.count_documents({'$and': [{"_id_ingredient": ObjectId(_id_ingredient)},
                                              {"_id_recipe": ObjectId(_id_recipe)}]})
        client.close()
        if result == 0:
            return True
        else:
            return False

    def add_enrichment_name_for_all(self):
        """ Add Ingredient's name for all association.

        Returns
        -------
        Any
            List of Ingredient Recipe with Ingredient's Name.
        """
        for link in self.result:
            link["name"] = Ingredient().get_name_by_id(_id=link["_id_ingredient"])
        return self

    def add_enrichment_title_for_all(self):
        """ Add Recipe's title for all association.

        Returns
        -------
        Any
            List of Ingredient Recipe with Recipe's Title.
        """
        for link in self.result:
            link["title"] = recipe_model.Recipe().get_title_by_id(_id=link["_id_recipe"])
        return self

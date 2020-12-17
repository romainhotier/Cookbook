from pymongo import MongoClient
from bson import ObjectId
import re

import utils

mongo = utils.Mongo()


class Recipe(object):

    def __init__(self):
        """ Recipe model.

        - _id = ObjectId in mongo
        - categories = Recipe's categories
        - cooking_time = Recipe's cooking_time
        - ingredients = Recipe's Ingredients
        - ingredients._id = Ingredient's ObjectId
        - ingredients.quantity = Ingredient's quantity
        - ingredients.unit = Ingredient's unit
        - level = Recipe's level (0-3)
        - nb_people = Recipe's nb_people
        - note = Recipe's note
        - preparation_time = Recipe's preparation_time
        - resume = Recipe's resume
        - slug = Recipe's slug (Unique)
        - status = Recipe's status
        - steps = Recipe's steps
        - steps.description = Step's description
        - title = Recipe's name (Unique)
        """
        self.result = {}

    def select_all(self):
        """ Get all existing Recipe.

        Returns
        -------
        Recipe
            List of all Recipes.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        cursor = db.find({})
        client.close()
        self.result = mongo.to_json([recipe for recipe in cursor])
        return self

    def select_one(self, _id):
        """ Get one Recipe by it's OjectId.

        Parameters
        ----------
        _id : str
            Recipe's ObjectId.

        Returns
        -------
        Recipe
            One Recipe.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.result = mongo.to_json(result)
        return self

    def select_one_by_slug(self, slug):
        """ Get one Recipe by it's slug.

        Parameters
        ----------
        slug : str
            Recipe's slug.

        Returns
        -------
        Recipe
            One Recipe.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find_one({"slug": slug})
        client.close()
        self.result = mongo.to_json(result)
        return self

    def search(self, data):
        """ Search Recipe with matching keys.

        Parameters
        ----------
        data : dict
            Keys and values to match.

        Returns
        -------
        Recipe
            List of matched Recipes.
        """
        search = {}
        for i, j in data.items():
            if i == "categories":
                search[i] = {"$in": [re.compile('.*{0}.*'.format(j), re.IGNORECASE)]}
            elif i in ["level", "cooking_time", "preparation_time", "nb_people"]:
                search[i] = int(j)
            else:
                search[i] = {"$regex": re.compile('.*{0}.*'.format(j), re.IGNORECASE)}
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        cursor = db.find(search)
        client.close()
        self.result = mongo.to_json([recipe for recipe in cursor])
        return self

    @staticmethod
    def check_recipe_is_unique(key, value):
        """ Check if a Recipe already exist with a specific key.

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
        db = client[mongo.name][mongo.collection_recipe]
        result = db.count_documents({key: value})
        client.close()
        if result == 0:
            return True
        else:
            return False

    def insert(self, data):
        """ Insert an Recipe.

        Parameters
        ----------
        data : dict
            Recipe's data.

        Returns
        -------
        Recipe
            Inserted Recipe.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        query = db.insert_one(data)
        result = db.find_one({"_id": ObjectId(query.inserted_id)})
        client.close()
        self.result = mongo.to_json(result)
        return self

    def update(self, _id, data):
        """ Update an Recipe.

        Parameters
        ----------
        _id : str
            Recipe's ObjectId.
        data : dict
            Recipe's data.

        Returns
        -------
        Recipe
            Updated Recipe.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.update_one({"_id": ObjectId(_id)}, {'$set': data})
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.result = mongo.to_json(result)
        return self

    @staticmethod
    def delete(_id):
        """ Delete an Recipe.

        Parameters
        ----------
        _id : str
            Recipe's ObjectId.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.delete_one({"_id": ObjectId(_id)})
        client.close()
        return

    @staticmethod
    def clean_ingredients_by_id(_id_ingredient):
        """ Remove Ingredient for Recipes by ObjectId.

        Parameters
        ----------
        _id_ingredient : str
            Ingredient's ObjectId.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.update({}, {'$pull': {"ingredients": {"_id": _id_ingredient}}})
        client.close()

    @staticmethod
    def get_all_step_id(_id_recipe):
        """ Get all Step's _ids for a Recipe.

        Parameters
        ----------
        _id_recipe : str
            Recipe's ObjectId.

        Returns
        -------
        list
            All Step's _id.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find_one({"_id": ObjectId(_id_recipe)})
        steps_ids = [step["_id"] for step in result["steps"]]
        client.close()
        return steps_ids

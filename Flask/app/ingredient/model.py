from pymongo import MongoClient, errors
from bson import ObjectId
import re

import utils

mongo = utils.Mongo()


class Ingredient(object):

    def __init__(self):
        """ Ingredient model.

        - _id = ObjectId in mongo
        - categories = Ingredient's categories
        - name = Ingredient's name (Unique)
        - nutriments = Ingredient's nutriments
        - nutriments.calories = Ingredient's calories
        - nutriments.carbohydrates = Ingredient's carbohydrates
        - nutriments.fats = Ingredient's fats
        - nutriments.proteins = Ingredient's proteins
        - nutriments.portion  = nutriments' portion
        - slug = Ingredient's slug (Unique)
        - unit = Ingredient's unit (Unique)
        """
        self.result = {}

    def select_all(self):
        """ Get all existing Ingredients.

        Returns
        -------
        Ingredient
            List of all Ingredients.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        cursor = db.find({})
        client.close()
        self.result = mongo.to_json([ingredient for ingredient in cursor])
        return self

    def select_one(self, _id):
        """ Get one Ingredient by it's ObjectId.

        Parameters
        ----------
        _id : str
            Ingredient's ObjectId.

        Returns
        -------
        Ingredient
            One Ingredient
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.result = mongo.to_json(result)
        return self

    def search(self, data):
        """ Search Ingredients with matching keys.

        Parameters
        ----------
        data : dict
            Keys and values to match.

        Returns
        -------
        Ingredient
            List of matched Ingredients.
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

    def insert(self, data):
        """ Insert an Ingredient.

        Parameters
        ----------
        data : dict
            Ingredient's data.

        Returns
        -------
        Ingredient
            Inserted Ingredient.
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
            Ingredient's ObjectId.
        data : dict
            Ingredient's data.

        Returns
        -------
        Ingredient
            Updated Ingredient.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        """ update nutriments if exist """
        try:
            data_nutriments = data.pop("nutriments")
            for i, j in data_nutriments.items():
                db.update_one({"_id": ObjectId(_id)}, {'$set': {"nutriments.{}".format(i): j}})
        except KeyError:
            pass
        """ update ingredient others keys"""
        try:
            db.update_one({"_id": ObjectId(_id)}, {'$set': data})
        except errors.WriteError:
            pass
        """ return result """
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
            Ingredient ObjectId.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        db.delete_one({"_id": ObjectId(_id)})
        client.close()
        return

    @staticmethod
    def check_ingredient_is_unique(key, value):
        """ Check if an Ingredient already exist with a specific key.

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

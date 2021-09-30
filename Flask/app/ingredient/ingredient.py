from pymongo import MongoClient, errors
from bson import ObjectId
import re
import json
import jsonpickle

from app import utils
from app.ingredient.nutriments import Nutriments

mongo = utils.Mongo()


class Ingredient(object):

    def __init__(self, **kwargs):
        """ Ingredient model

        - _id = ObjectId in mongo
        - categories = Ingredient's categories. ex:['plat', 'dessert']
        - name = Ingredient's name (Unique)
        - nutriments = Ingredient's nutriments
        - slug = Ingredient's slug for url (Unique)
        - unit = Ingredient's unit. Must be in ['g', 'ml']

        Returns
        -------
        Ingredient
        """
        self._id = None
        self.categories = []
        self.name = None
        self.nutriments = Nutriments()
        self.slug = None
        self.unit = "g"
        if "serialize" in kwargs:
            self.set_attributes(kwargs["serialize"])

    def get_attributes(self):
        """ Get Ingredient attributes.

        Returns
        -------
        list
            Ingredient attributes.
        """
        return [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

    def set_attributes(self, data):
        """ Set Ingredient attributes.

        Parameters
        ----------
        data : dict
            Json.

        """
        try:
            for key, value in data.items():
                if key in self.get_attributes():
                    if key == "nutriments":
                        self.nutriments = Nutriments(serialize=value)
                    else:
                        self.__setattr__(key, value)
        except AttributeError:
            pass

    def get_as_json(self):
        """ Return Ingredient as a dict.

        Return
        ----------
        dict
            Ingredient as Json.

        """
        return json.loads(jsonpickle.encode(self, unpicklable=False))

    @staticmethod
    def select_all():
        """ Get all existing Ingredients.

        Returns
        -------
        list of Ingredient
            List of all Ingredients.
        """
        with MongoClient(mongo.ip, mongo.port) as client:
            db = client[mongo.name][mongo.collection_ingredient]
            cursor = db.find({})
        return [Ingredient(serialize=mongo.convert_object_id_to_str(data)) for data in cursor]

    @staticmethod
    def select_one(_id):
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
        with MongoClient(mongo.ip, mongo.port) as client:
            db = client[mongo.name][mongo.collection_ingredient]
            result = db.find_one({"_id": ObjectId(_id)})
        return Ingredient(serialize=mongo.convert_object_id_to_str(result))

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
        self.result = mongo.convert_to_json([ingredient for ingredient in cursor])
        return self

    def insert(self):
        """ Insert an Ingredient.

        Returns
        -------
        Ingredient
            Inserted Ingredient.
        """
        with MongoClient(mongo.ip, mongo.port) as client:
            db = client[mongo.name][mongo.collection_ingredient]
            payload = self.get_as_json()
            payload.pop("_id")
            query = db.insert_one(payload)
            result = db.find_one({"_id": ObjectId(query.inserted_id)})
        return Ingredient(serialize=mongo.convert_object_id_to_str(result))

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
        self.result = mongo.convert_to_json(result)
        return self

    @staticmethod
    def delete(_id):
        """ Delete an Ingredient.

        Parameters
        ----------
        _id : str
            Ingredient ObjectId.
        """
        with MongoClient(mongo.ip, mongo.port) as client:
            db = client[mongo.name][mongo.collection_ingredient]
            db.delete_one({"_id": ObjectId(_id)})
        return

    """ recipe calories """
    @staticmethod
    def get_nutriments(_id):
        """ Get nutriments for one Ingredient by ObjectId.

        Parameters
        ----------
        _id : str
            Ingredient's ObjectId.

        Returns
        -------
        dict
            Ingredient's nutriment
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_ingredient]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        return result["nutriments"]

from pymongo import MongoClient
from bson import ObjectId
import re

import utils
import app.file.model as file_model

mongo = utils.Mongo()
file = file_model.File()


class Recipe(object):

    def __init__(self):
        """ Recipe model.

        - _id = ObjectId in mongo
        - title = Recipe's name (Unique)
        - slug = Recipe's slug (Unique)
        - level = Recipe's level (0-3)
        - resume = Recipe's resume
        - cooking_time = Recipe's cooking_time
        - preparation_time = Recipe's preparation_time
        - nb_people = Recipe's nb_people
        - note = Recipe's note
        - steps = Recipe's steps
        - categories = Recipe's categories
        - status = Recipe's status
        """
        self.result = {}

    def select_all(self):
        """ Get all existing Recipe.

        Returns
        -------
        Any
            List of all Recipes.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        cursor = db.find({})
        client.close()
        self.result = mongo.to_json([recipe for recipe in cursor])
        return self

    def select_one(self, _id):
        """ Get one Recipe by it's ObjectId.

        Parameters
        ----------
        _id : str
            Recipe's ObjectId.

        Returns
        -------
        Any
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
        Any
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
        Any
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
        Any
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
        Any
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

    def add_enrichment_file_for_all(self):
        """ Add Files information for all Recipes.

        Returns
        -------
        Any
            List of Recipes with Files information.
        """
        for recipe in self.result:
            recipe["files"] = []
            """ get files for recipe """
            files_recipe = file.get_all_file_by_id_parent(_id_parent=recipe["_id"]).result
            for f in files_recipe:
                file_enrichment = {"_id": str(f["_id"]), "is_main": f["metadata"]["is_main"]}
                recipe["files"].append(file_enrichment)
            """ get files for steps """
            for step in recipe["steps"]:
                step["files"] = []
                files_step = file.get_all_file_by_id_parent(_id_parent=step["_id"]).result
                for f in files_step:
                    file_enrichment = {"_id": str(f["_id"]), "is_main": f["metadata"]["is_main"]}
                    step["files"].append(file_enrichment)
        return self

    def add_enrichment_file_for_one(self):
        """ Add Files information for one Recipe.

        Returns
        -------
        Any
            One Recipe with Files information.
        """
        self.result["files"] = []
        """ get files for recipe """
        files_recipe = file.get_all_file_by_id_parent(_id_parent=self.result["_id"]).result
        for f in files_recipe:
            file_enrichment = {"_id": str(f["_id"]), "is_main": f["metadata"]["is_main"]}
            self.result["files"].append(file_enrichment)
        """ get files for steps """
        for step in self.result["steps"]:
            step["files"] = []
            files_step = file.get_all_file_by_id_parent(_id_parent=step["_id"]).result
            for f in files_step:
                file_enrichment = {"_id": str(f["_id"]), "is_main": f["metadata"]["is_main"]}
                step["files"].append(file_enrichment)
        return self

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

    @staticmethod
    def get_title_by_id(_id):
        """ Get Recipe's title associated with a ObjectId.

        Parameters
        ----------
        _id : str
            Recipe's ObjectId.

        Returns
        -------
        str
            Recipe's title.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        return result["title"]


class Step(object):

    def __init__(self):
        """ Step model.

        - _id = ObjectId in mongo
        - description = Recipe's description
        """
        self.result = {}

    @staticmethod
    def get_steps_length(_id_recipe):
        """ Get number of Steps for a Recipe.

        Parameters
        ----------
        _id_recipe : str
            Recipe's ObjectId.

        Returns
        -------
        int
            Number of Steps.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find_one({"_id": ObjectId(_id_recipe)})
        client.close()
        if result is None:
            return 0
        else:
            steps_length = len(result["steps"])
            return steps_length

    def insert(self, _id, data):
        """ Insert a Step for a Recipe.

        Parameters
        ----------
        _id : str
            Recipe's ObjectId.
        data : dict
            Step's data.

        Returns
        -------
        Any
            Recipe with Steps.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        new_step = {"_id": ObjectId(), "description": data["description"]}
        if "position" in data:
            position = data["position"]
            db.update_one({"_id": ObjectId(_id)}, {'$push': {"steps": {"$each": [new_step], "$position": position}}})
        else:
            db.update_one({"_id": ObjectId(_id)}, {'$push': {"steps": {"$each": [new_step]}}})
        client.close()
        """ return result """
        self.result = Recipe().select_one(_id=_id).result
        return self

    def update(self, _id_recipe, _id_step, data):
        """ Update a Step for a Recipe.

        Parameters
        ----------
        _id_recipe : str
            Recipe's ObjectId.
        _id_step : str
            Step's ObjectId.
        data : dict
            Step's data.

        Returns
        -------
        Any
            Recipe with Steps.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        position = Step.get_step_index(_id_recipe=_id_recipe, _id_step=_id_step)
        db.update_one({"_id": ObjectId(_id_recipe)},
                      {'$set': {"steps.{0}.description".format(position): data["description"]}})
        client.close()
        """ return result """
        self.result = Recipe().select_one(_id=_id_recipe).result
        return self

    def delete(self, _id_recipe, _id_step):
        """ Delete a Step for a Recipe.

        Parameters
        ----------
        _id_recipe : str
            Recipe's ObjectId.
        _id_step : str
            Step's ObjectId.

        Returns
        -------
        Any
            Recipe with Steps.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.update_one({"_id": ObjectId(_id_recipe)}, {'$pull': {"steps": {"_id": ObjectId(_id_step)}}})
        client.close()
        """ return result """
        self.result = Recipe().select_one(_id=_id_recipe).result
        return self

    @staticmethod
    def get_step_index(_id_recipe, _id_step):
        """ Get position in the list.

        Parameters
        ----------
        _id_recipe : str
            Recipe's ObjectId.
        _id_step : str
            Step's ObjectId.

        Returns
        -------
        Any
            Position.
        """
        steps = Recipe().select_one(_id=_id_recipe).result["steps"]
        i = 0
        for step in steps:
            if step["_id"] == _id_step:
                return i
            else:
                i += 1

    def add_enrichment_file_for_one(self):
        """ Add Files information for one Recipe.

        Returns
        -------
        Any
            One Recipe with Files information.
        """
        self.result["files"] = []
        """ get files for recipe """
        files_recipe = file.get_all_file_by_id_parent(_id_parent=self.result["_id"]).result
        for f in files_recipe:
            file_enrichment = {"_id": str(f["_id"]), "is_main": f["metadata"]["is_main"]}
            self.result["files"].append(file_enrichment)
        """ get files for steps """
        for step in self.result["steps"]:
            step["files"] = []
            files_step = file.get_all_file_by_id_parent(_id_parent=step["_id"]).result
            for f in files_step:
                file_enrichment = {"_id": str(f["_id"]), "is_main": f["metadata"]["is_main"]}
                step["files"].append(file_enrichment)
        return self

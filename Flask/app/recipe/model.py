from pymongo import MongoClient, ASCENDING, DESCENDING
from bson import ObjectId
import re

from app import utils, backend
from app.ingredient import Ingredient

mongo = utils.Mongo()
converter = utils.PathExplorer()


class Recipe(object):

    def __init__(self):
        """ Recipe model.

        - _id = ObjectId in mongo
        - categories = Recipe's categories
        - cooking_time = Recipe's cooking_time
        - files = Recipe's files
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
        self.result = mongo.convert_to_json([recipe for recipe in cursor])
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
        self.result = mongo.convert_to_json(result)
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
        self.result = mongo.convert_to_json(result)
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
        order_by = ""
        direction = ""
        for i, j in data.items():
            if i == "categories":
                search[i] = {"$in": [re.compile('.*{0}.*'.format(j), re.IGNORECASE)]}
            elif i in ["level", "cooking_time", "preparation_time", "nb_people"]:
                search[i] = int(j)
            elif i in ["title", "slug", "status"]:
                search[i] = {"$regex": re.compile('.*{0}.*'.format(j), re.IGNORECASE)}
            elif i == "order":
                direction = j
            elif i == "orderBy":
                order_by = j
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        """ search ordered """
        cursor = db.find(search)
        if order_by != "":
            if direction == "":
                cursor.sort(order_by)
            else:
                if direction == "asc":
                    cursor.sort(order_by, ASCENDING)
                elif direction == "desc":
                    cursor.sort(order_by, DESCENDING)
        client.close()
        self.result = mongo.convert_to_json([recipe for recipe in cursor])
        return self

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
        self.result = mongo.convert_to_json(result)
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
        self.result = mongo.convert_to_json(result)
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

    """ steps """
    @staticmethod
    def get_step_position(_id_recipe, _id_step):
        """ Get step position by id.

        Parameters
        ----------
        _id_recipe : str
            Recipe's ObjectId.
        _id_step : str
            Step's ObjectId.

        Returns
        -------
        int
            Step's position.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        recipe = db.find_one({"_id": ObjectId(_id_recipe)})
        client.close()
        list_steps = mongo.convert_to_json([steps["_id"] for steps in recipe["steps"]])
        return list_steps.index(_id_step)

    """ files """
    def add_files_recipe(self, _id, data):
        """ add files to a recipe.

        Parameters
        ----------
        _id : str
            Recipe's ObjectId.
        data : list
            Files's urls.

        Returns
        -------
        Recipe
            Updated Recipe.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        for url in data:
            db.update_one({"_id": ObjectId(_id)}, {'$push': {"files": url}})
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        self.result = mongo.convert_to_json(result)
        return self

    def add_files_step(self, _id_recipe, _id_step, data):
        """ add files to a recipe.

        Parameters
        ----------
        _id_recipe : str
            Recipe's ObjectId.
        _id_step : str
            Step's ObjectId.
        data : list
            Files's urls.

        Returns
        -------
        Recipe
            Updated Recipe.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        self.get_step_position(_id_recipe=_id_recipe, _id_step=_id_step)
        index = self.get_step_position(_id_recipe=_id_recipe, _id_step=_id_step)
        for url in data:
            db.update_one({"_id": ObjectId(_id_recipe)}, {'$push': {"steps.{0}.files".format(index): url}})
        result = db.find_one({"_id": ObjectId(_id_recipe)})
        client.close()
        self.result = mongo.convert_to_json(result)
        return self

    @staticmethod
    def get_files(_id):
        """ get Recipe's files.

        Parameters
        ----------
        _id : str
            Recipe's ObjectId.

        Returns
        -------
        list
            Recipe's Files.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find_one({"_id": ObjectId(_id)})["files"]
        client.close()
        return result

    @staticmethod
    def get_steps_files(_id):
        """ get Recipe's Steps files.

        Parameters
        ----------
        _id : str
            Recipe's ObjectId.

        Returns
        -------
        list
            Recipe's Files.
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.find_one({"_id": ObjectId(_id)})
        client.close()
        steps_files = {}
        try:
            for steps in result["steps"]:
                try:
                    steps_files[str(steps["_id"])] = steps["files"]
                except TypeError:
                    pass
        except TypeError:
            pass
        return mongo.convert_to_json(steps_files)

    def delete_file(self, path):
        """ delete files.

        Parameters
        ----------
        path : str
            Files's short_path.

        Returns
        -------
        Recipe
            Updated Recipe.
        """
        if len(path.split("/")) == 3:
            self.delete_file_recipe(path=path)
        elif len(path.split("/")) == 5:
            self.delete_file_step(path=path)
        return self

    # use in delete_file
    def delete_file_recipe(self, path):
        """ delete files to a recipe.

        Parameters
        ----------
        path : str
            Files's short_path.

        Returns
        -------
        Recipe
            Updated Recipe.
        """
        _id_recipe = path.split("/")[1]
        s_path = path
        if backend.config["SYSTEM"] == "Windows":
            s_path = converter.convert_path(target="Windows", path=path)
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.update_one({"_id": ObjectId(_id_recipe)}, {'$pull': {"files": s_path}})
        result = db.find_one({"_id": ObjectId(_id_recipe)})
        client.close()
        self.result = mongo.convert_to_json(result)
        return self

    # use in delete_file
    def delete_file_step(self, path):
        """ delete files to a step.

        Parameters
        ----------
        path : str
            Files's short_path.

        Returns
        -------
        Recipe
            Updated Recipe.
        """
        _id_recipe = path.split("/")[1]
        _id_step = path.split("/")[3]
        s_path = path
        if backend.config["SYSTEM"] == "Windows":
            s_path = converter.convert_path(target="Windows", path=path)
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        index = self.get_step_position(_id_recipe=_id_recipe, _id_step=_id_step)
        db.update_one({"_id": ObjectId(_id_recipe)}, {'$pull': {"steps.{0}.files".format(index): s_path}})
        result = db.find_one({"_id": ObjectId(_id_recipe)})
        client.close()
        self.result = mongo.convert_to_json(result)
        return self

    """ calories """
    def add_enrichment_calories(self):
        """ calculate calories with ingredient's recipe.

        Returns
        -------
        int
            Recipe's calories
        """
        if isinstance(self.result, dict):
            self.calculate_recipe_calories(recipe=self.result)
        elif isinstance(self.result, list):
            for recipe in self.result:
                self.calculate_recipe_calories(recipe=recipe)
            return self

    # use in add_enrichment_calories
    def calculate_recipe_calories(self, recipe):
        recipe_calories = 0
        ingredients = recipe["ingredients"]
        for ing in ingredients:
            nutri = Ingredient().get_nutriments(_id=ing["_id"])
            if ing["unit"] == "portion":
                ing_calories = ((float(nutri["calories"]) / 100) * float(nutri["portion"])) * float(ing["quantity"])
                recipe_calories += ing_calories
            else:
                ing_calories = (float(nutri["calories"]) / 100) * float(ing["quantity"])
                recipe_calories += ing_calories
        recipe["calories"] = recipe_calories
        return self

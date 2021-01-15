from pymongo import MongoClient
from bson import ObjectId
import copy
import re

from app import utils
from app.ingredient import Ingredient

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
        - files = Recipe's files
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
        self.files = []

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
        return mongo.convert_to_json(self.get())

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
                elif i == "ingredients":
                    try:
                        for ingr in data["ingredients"]:
                            for key in list(ingr):
                                if key not in ["_id", "quantity", "unit"]:
                                    ingr.pop(key)
                    except (TypeError, AttributeError):
                        pass
                    self.__setattr__(i, j)
                elif i == "steps":
                    try:
                        for step in data["steps"]:
                            for key in list(step):
                                if key not in ["_id", "description"]:
                                    step.pop(key)
                    except (TypeError, AttributeError):
                        pass
                    self.__setattr__(i, j)
                else:
                    self.__setattr__(i, j)
        return self

    def custom_from_body(self, data):
        """ Update RecipeTest from PostRecipe.

        Parameters
        ----------
        data : dict
            Body's value.

        Returns
        -------
        IngredientTest
        """
        """ default value """
        optional_parameter = ["categories", "cooking_time", "ingredient", "level", "nb_people", "note",
                              "preparation_time", "resume", "status", "steps"]
        for param in optional_parameter:
            if param not in data:
                if param in ["categories", "ingredients", "steps", "files"]:
                    self.__setattr__(param, [])
                elif param in ["cooking_time", "level", "nb_people", "preparation_time"]:
                    self.__setattr__(param, 0)
                elif param in ["note", "resume"]:
                    self.__setattr__(param, "")
                elif param in ["status"]:
                    self.__setattr__(param, "in_progress")
        self.custom(data)
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
            """ check steps """
            if value in ["steps"]:  # check for steps
                for i, step in enumerate(recipe["steps"]):
                    if "_id" not in self.__getattribute__(value)[i]:  # new step
                        assert step["description"] == self.__getattribute__(value)[i]["description"]
                    else:  # old step
                        assert mongo.convert_to_json(step) == mongo.convert_to_json(self.__getattribute__(value)[i])
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
        data = {"_id": ObjectId(_id_step), "description": description}
        """ add in model """
        self.steps.append(data)
        """ add in mongo """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.update_one({"_id": ObjectId(self._id)}, {'$push': {"steps": data}})
        client.close()
        return self

    """ ingredients """
    def add_ingredient(self, ingredient, quantity, unit):
        """ Add a IngredientTest to RecipeTest.

        Parameters
        ----------
        ingredient : IngredientTest
            IngredientTest to be added.
        quantity : int
            IngredientTest's quantity.
        unit : str
            IngredientTest's unit

        Returns
        -------
        RecipeTest
            RecipeTest.
        """
        data = {"_id": ingredient.get_id(), "quantity": quantity, "unit": unit}
        """ add in model """
        self.ingredients.append(data)
        """ add in mongo """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        db.update_one({"_id": ObjectId(self._id)}, {'$push': {"ingredients": data}})
        client.close()
        return self

    def delete_ingredient(self, ingredient):
        """ Delete a IngredientTest to RecipeTest.

        Parameters
        ----------
        ingredient : IngredientTest
            IngredientTest.

        Returns
        -------
        RecipeTest
            RecipeTest.
        """
        """ delete in model """
        for ingr in self.ingredients:
            if ingr["_id"] == ingredient.get_id():
                self.ingredients.remove(ingr)
                break
        return self

    """ files """
    def add_files_recipe(self, files, **kwargs):
        """ Add a  FileTest to RecipeTest's step.

        Parameters
        ----------
        files : list
            FileTest to be added
        kwargs: Any
            'add_in_mongo'

        Returns
        -------
        RecipeTest
            RecipeTest.
        """
        for f in files:
            self.files.append(f.short_path)
        if "add_in_mongo" in kwargs:
            client = MongoClient(mongo.ip, mongo.port)
            db = client[mongo.name][mongo.collection_recipe]
            for f in files:
                db.update_one({"_id": ObjectId(self.get_id())}, {'$push': {"files": f.short_path}})
            client.close()
        return self

    def delete_files_recipe(self, files):
        """ Delete a FileTest to RecipeTest's step.

        Parameters
        ----------
        files : list
            FileTest to be deleted

        Returns
        -------
        RecipeTest
            RecipeTest.
        """
        for f in files:
            self.files.remove(f.short_path)
        return self

    """ calories """
    def add_enrichment_calories(self):
        """ calculate calories with ingredient's recipe.

        Parameters
        ----------

        Returns
        -------
        int
            Recipe's calories
        """
        recipe_calories = 0
        for ing in self.ingredients:
            nutri = Ingredient().get_nutriments(_id=ing["_id"])
            if ing["unit"] == "portion":
                ing_calories = ((nutri["calories"] / 100) * nutri["portion"]) * ing["quantity"]
                recipe_calories += ing_calories
            else:
                ing_calories = (nutri["calories"] / 100) * ing["quantity"]
                recipe_calories += ing_calories
        self.__setattr__("calories", recipe_calories)
        return self

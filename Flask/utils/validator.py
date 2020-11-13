from flask import abort
from pymongo import MongoClient
from bson import ObjectId
from os import path
import jsonschema

import utils
import app.ingredient.model as ingredient_model
import app.recipe.model as recipe_model
import app.user.model as user_model

server = utils.Server()
mongo = utils.Mongo()
ingredient = ingredient_model.Ingredient()
ingredient_recipe = ingredient_model.IngredientRecipe()
recipe = recipe_model.Recipe()
user = user_model.User()


class Validator(object):
    """ All generic validator for the project.
    """

    @staticmethod
    def is_object_id(param, value):
        """ Check if the value is a correct ObjectId.

        Parameters
        ----------
        param : str
            Name of the tested parameter.
        value : Any
            Value of the tested parameter.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed..
        """
        if value is None or len(value) != 24:
            detail = server.format_detail(param=param, msg=server.detail_must_be_an_object_id, value=value)
            return abort(status=400, description=detail)
        else:
            return True

    @staticmethod
    def is_object_id_in_collection(param, value, collection):
        """ Check if the ObjectId is present in a collection.

        Parameters
        ----------
        param : str
            Name of the tested parameter.
        value : str
            Value of the tested parameter.
        collection : str
            Name of the mongodb collection to be checked in.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed..
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][collection]
        result = db.count_documents({"_id": ObjectId(value)})
        client.close()
        if result == 0:
            detail = server.format_detail(param=param, msg=server.detail_doesnot_exist, value=value)
            return abort(status=400, description=detail)
        else:
            return True

    @staticmethod
    def is_slug_in_collection(param, value, collection):
        """ Check if the slug is present in a collection.

        Parameters
        ----------
        param : str
            Name of the tested parameter.
        value : str
            Value of the tested parameter.
        collection : str
            Name of the mongodb collection to be checked in.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed..
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][collection]
        result = db.count_documents({"slug": value})
        client.close()
        if result == 0:
            detail = server.format_detail(param=param, msg=server.detail_doesnot_exist, value=value)
            return abort(status=400, description=detail)
        else:
            return True

    @staticmethod
    def is_object_id_in_recipe_steps(param, _id_recipe, _id_step):
        """ Check if the ObjectId is present in a recipe steps.

        Parameters
        ----------
        param : str
            Name of the tested parameter.
        _id_recipe : str
            ObjectId of the recipe.
        _id_step : str
            ObjectId of the step.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed..
        """
        client = MongoClient(mongo.ip, mongo.port)
        db = client[mongo.name][mongo.collection_recipe]
        result = db.count_documents({"$and": [{"_id": ObjectId(_id_recipe)},
                                              {"steps": {"$elemMatch": {"_id": ObjectId(_id_step)}}}]})
        client.close()
        if result == 0:
            detail = server.format_detail(param=param, msg=server.detail_doesnot_exist, value=_id_step)
            return abort(status=400, description=detail)
        else:
            return True

    @staticmethod
    def is_string(param, value):
        """ Check if the value is a string.

        Parameters
        ----------
        param : str
            Name of the tested parameter.
        value : Any
            Value of the tested parameter.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if isinstance(value, str):
            return True
        else:
            detail = server.format_detail(param=param, msg=server.detail_must_be_a_string, value=value)
            return abort(status=400, description=detail)

    @staticmethod
    def is_int(param, value):
        """ Check if the value is an integer.

        Parameters
        ----------
        param : str
            Name of the tested parameter.
        value : Any
            Value of the tested parameter.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if isinstance(value, int):
            return True
        else:
            try:
                int(value)
                return True
            except (ValueError, TypeError):
                detail = server.format_detail(param=param, msg=server.detail_must_be_an_integer, value=value)
                return abort(status=400, description=detail)

    @staticmethod
    def is_array(param, value):
        """ Check if the value is an array.

        Parameters
        ----------
        param : str
            Name of the tested parameter.
        value : Any
            Value of the tested parameter.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if isinstance(value, list):
            return True
        else:
            detail = server.format_detail(param=param, msg=server.detail_must_be_an_array, value=value)
            return abort(status=400, description=detail)

    @staticmethod
    def is_object(param, value):
        """ Check if the value is an object.

        Parameters
        ----------
        param : str
            Name of the tested parameter.
        value : Any
            Value of the tested parameter.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if isinstance(value, dict):
            return True
        else:
            detail = server.format_detail(param=param, msg=server.detail_must_be_an_object, value=value)
            return abort(status=400, description=detail)

    @staticmethod
    def has_at_least_one_key(data):
        """ Check if the body have at least one key.

        Parameters
        ----------
        data : dict
            Dict to be tested.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if len(data) != 0:
            return True
        else:
            detail = server.format_detail(param="body", msg=server.detail_must_contain_at_least_one_key, value=data)
            return abort(status=400, description=detail)

    @staticmethod
    def is_boolean(param, value):
        """ Check if the value is a boolean.

        Parameters
        ----------
        param : str
            Name of the tested parameter.
        value : Any
            Value of the tested parameter.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if isinstance(value, bool):
            return True
        else:
            detail = server.format_detail(param=param, msg=server.detail_must_be_a_boolean, value=value)
            return abort(status=400, description=detail)

    @staticmethod
    def is_string_non_empty(param, value):
        """ Check if the value is a non empty string.

        Parameters
        ----------
        param : str
            Name of the tested parameter.
        value : str
            Value of the tested parameter.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if value.strip() == "":
            detail = server.format_detail(param=param, msg=server.detail_must_be_not_empty, value=value)
            return abort(status=400, description=detail)
        else:
            return True

    def is_string_boolean_or_none(self, param, value):
        """ Check if the value is a boolean string or None.

        Parameters
        ----------
        param : str
            Name of the tested parameter.
        value : str
            Value of the tested parameter.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if value is None:
            return True
        else:
            self.is_string(param=param, value=value)
            self.is_in(param=param, value=value, values=["true", "false"])
            return True

    @staticmethod
    def is_mandatory(param, data):
        """ Check if the param is present in body.

        Parameters
        ----------
        param : str
            Name of the tested parameter.
        data : dict
            Dict to be tested.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if param in data:
            return True
        else:
            detail = server.format_detail(param=param, msg=server.detail_is_required)
            return abort(status=400, description=detail)

    @staticmethod
    def is_unique_user(param, value):
        """ Check if User already exist.

        Parameters
        ----------
        param : str
            Email to be checked.
        value : str
            Value to be checked.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if not user.check_user_is_unique(email=value):
            detail = server.format_detail(param=param, msg=server.detail_already_exist, value=value)
            return abort(status=400, description=detail)
        return True

    @staticmethod
    def is_unique_ingredient(param, value):
        """ Check if Ingredient already exist.

        Parameters
        ----------
        param : str
            Key to be checked.
        value : str
            Value to be checked.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if not ingredient.check_ingredient_is_unique(key=param, value=value):
            detail = server.format_detail(param=param, msg=server.detail_already_exist, value=value)
            return abort(status=400, description=detail)
        return True

    @staticmethod
    def is_unique_ingredient_recipe(_id_ingredient, _id_recipe):
        """ Check if the key/value is unique.

        Parameters
        ----------
        _id_ingredient : str
            ObjectId of Ingredient.
        _id_recipe : str
            ObjectId of Recipe.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if not ingredient_recipe.check_link_is_unique(_id_ingredient=_id_ingredient, _id_recipe=_id_recipe):
            detail = "link between {} and {} ".format(_id_ingredient, _id_recipe) + server.detail_already_exist.lower()
            return abort(status=400, description=detail)
        return True

    @staticmethod
    def is_unique_recipe(param, value):
        """ Check if the key/value is unique.

        Parameters
        ----------
        param : str
            Key to be checked.
        value : str
            Value to be checked.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if not recipe.check_recipe_is_unique(key=param, value=value):
            detail = server.format_detail(param=param, msg=server.detail_already_exist, value=value)
            return abort(status=400, description=detail)
        return True

    @staticmethod
    def is_mandatory_query(param, value):
        """ Check if the param is present in query.

        Parameters
        ----------
        param : str
            Name of the tested parameter.
        value : str
            Value of the tested parameter.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if value is None:
            detail = server.format_detail(param=param, msg=server.detail_is_required)
            return abort(status=400, description=detail)

    @staticmethod
    def is_between_x_y(param, value, x, y):
        """ Check if the param is between two values.

        Parameters
        ----------
        param : str
            Name of the tested parameter.
        value : int
            Value of the tested parameter.
        x : int
            Lower range.
        y : int
            Higher range.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if x <= value <= y:
            return True
        else:
            detail = server.format_detail(param=param, msg=server.detail_must_be_between + " {0} and {1}".format(x, y),
                                          value=value)
            return abort(status=400, description=detail)

    @staticmethod
    def is_in(param, value, values):
        """ Check if the param is in defined values.

        Parameters
        ----------
        param : str
            Name of the tested parameter.
        value : str
            Value of the tested parameter.
        values : list
            List of accepted values.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if value in values:
            return True
        else:
            detail = server.format_detail(param=param, msg=server.detail_must_be_in + " [" + ', '.join(values) + "]",
                                          value=value)
            return abort(status=400, description=detail)

    @staticmethod
    def is_path_exist(param, value):
        """ Check if the path exist on computer.

        Parameters
        ----------
        param : str
            Name of the tested parameter.
        value : str
            Value of the tested parameter.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if path.exists(value):
            return True
        else:
            detail = server.format_detail(param=param, msg=server.detail_doesnot_exist, value=value)
            return abort(status=400, description=detail)

    @staticmethod
    def is_nutriment(data):
        """ Check if the value validate nutriment schema.

        Parameters
        ----------
        data : dict
            Dict to be tested.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        try:
            jsonschema.validate(instance=data, schema=Schema().nutriment())
            return True
        except jsonschema.exceptions.ValidationError as err:
            detail = Schema().format_detail_from_err(err=err)
            return abort(status=400, description=detail)


class Schema(object):

    def __init__(self):
        """ Schema for validation.
        """
        self.schema = {}

    def nutriment(self):
        """ Set nutriment schema for validation.

        Returns
        -------
        dict
            Nutriment schema.
        """
        schema = {"definitions": {"measurement": {
            "type": "object",
            "properties": {
                "quantity": {"type": "number"},
                "unit": {"type": "string"}},
            "required": ["quantity", "unit"],
            "additionalProperties": False}},

            "type": "object",
            "properties": {
                "calories_per_100g": {"$ref": "#/definitions/measurement"},
                "carbohydrates_per_100g": {"$ref": "#/definitions/measurement"},
                "fats_per_100g": {"$ref": "#/definitions/measurement"},
                "proteins_per_100g": {"$ref": "#/definitions/measurement"}},
            "required": ["calories_per_100g", "carbohydrates_per_100g", "fats_per_100g", "proteins_per_100g"],
            "additionalProperties": False}
        self.__setattr__("schema", schema)

    def format_detail_from_err(self, err):
        """ Format detail from a jsonschema error.

        Parameters
        ----------
        err
            Error raised by jsonschema validation.

        Returns
        -------
        dict
            Detail object.
        """
        param = err.message.split("'")[1]
        msg = self.format_msg(err.message.split("'")[2])
        value = err.instance
        return server.format_detail(param=param, msg=msg, value=value)

    # use in format_detail_from_err
    @staticmethod
    def format_msg(msg):
        """ Format jsonschema message with our own server message.

        Parameters
        ----------
        msg : str
            Message from jsonschema exception.

        Returns
        -------
        str
            Server message.
        """
        if msg == 'is a required property':
            return server.detail_is_required

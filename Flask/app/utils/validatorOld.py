import re

from flask import abort
from pymongo import MongoClient
from bson import ObjectId

from app import utils

mongo = utils.Mongo()


class Validator(object):
    """ All generic validator for the project.
    """

    detail_has_expired = "Has expired"
    detail_was_wrong = "Was wrong"
    detail_is_required = "Is required"
    detail_forbidden = "Forbidden action - Admin only"
    detail_must_be_an_object_id = "Must be an ObjectId"
    detail_must_be_a_string = "Must be a string"
    detail_must_be_a_path = "Must be a path with '/'"
    detail_must_be_an_integer = "Must be an integer"
    detail_must_be_a_float = "Must be a float"
    detail_must_be_an_array = "Must be an array"
    detail_must_be_an_array_of_string = "Must be an array of string"
    detail_must_be_an_array_of_object = "Must be an array of object"
    detail_must_be_an_object = "Must be an object"
    detail_must_be_a_boolean = "Must be a boolean"
    detail_must_be_not_empty = "Must be not empty"
    detail_must_be_between = "Must be between"
    detail_must_be_in = "Must be in"
    detail_must_contain_at_least_one_key = "Must contain at least one key"
    detail_already_exist = "Already exist"
    detail_doesnot_exist = "Doesn't exist"
    detail_must_be_unique = "Must be unique"
    detail_url_not_found = "The requested URL was not found on the server"
    detail_method_not_allowed = "The method is not allowed for the requested URL."

    def __init__(self, **kwargs):
        """ Validator model.

        - param = Api's param not valid (optional)
        - msg = Failure's explication
        - value = Param's value (optional)

        Returns
        -------
        Validator
        """
        self.param = None
        self.msg = None
        self.value = None
        self.set_attributes(kwargs)

    def get_attributes(self):
        """ Get Validator attributes.

        Returns
        -------
        list
            Validator attributes.
        """
        return [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]

    def set_attributes(self, data):
        """ Set Validator attributes.

        Parameters
        ----------
        data : dict
            Json.

        """
        for key, value in data.items():
            if key in self.get_attributes():
                self.__setattr__(key, value)

    def is_token_valid(self, data):
        if isinstance(data, dict):
            validation = Validator(param="token", msg=self.detail_has_expired)
            return validation.__dict__
        elif re.compile("Bad Authorization header", re.IGNORECASE).search(data) is not None:
            validation = Validator(param="token", msg=self.detail_was_wrong)
            return validation.__dict__
        elif re.compile("Missing Authorization Header", re.IGNORECASE).search(data) is not None:
            validation = Validator(param="token", msg=self.detail_is_required)
            return validation.__dict__

    def is_object_id(self, param, value):
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
            validation = Validator(param=param, msg=self.detail_must_be_an_object_id, value=value)
            return abort(status=400, description=validation.__dict__)
        else:
            return True

    def is_object_id_in_collection(self, param, value, collection):
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
        with MongoClient(mongo.ip, mongo.port) as client:
            db = client[mongo.name][collection]
            result = db.count_documents({"_id": ObjectId(value)})
        if result == 0:
            validation = Validator(param=param, msg=self.detail_doesnot_exist, value=value)
            return abort(status=400, description=validation.__dict__)
        else:
            return True

    def is_slug_in_collection(self, param, value, collection):
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
        with MongoClient(mongo.ip, mongo.port) as client:
            db = client[mongo.name][collection]
            result = db.count_documents({"slug": value})
        if result == 0:
            validation = Validator(param=param, msg=self.detail_doesnot_exist, value=value)
            return abort(status=400, description=validation.__dict__)
        else:
            return True

    def is_object_id_in_recipe_steps(self, param, _id_recipe, _id_step):
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
        with MongoClient(mongo.ip, mongo.port) as client:
            db = client[mongo.name][mongo.collection_recipe]
            result = db.count_documents({"$and": [{"_id": ObjectId(_id_recipe)},
                                                  {"steps": {"$elemMatch": {"_id": ObjectId(_id_step)}}}]})
        if result == 0:
            validation = Validator(param=param, msg=self.detail_doesnot_exist, value=_id_step)
            return abort(status=400, description=validation.__dict__)
        else:
            return True

    def is_unique_user(self, param, value):
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
        if not self.check_user_is_unique(email=value):
            validation = Validator(param=param, msg=self.detail_already_exist, value=value)
            return abort(status=400, description=validation.__dict__)
        return True

    # use in is_user_unique
    @staticmethod
    def check_user_is_unique(email):
        """ Check if an email already exist.

        Parameters
        ----------
        email : str
            User's email.

        Returns
        -------
        bool
            True if email doesn't exist in mongo.
        """
        with MongoClient(mongo.ip, mongo.port) as client:
            db = client[mongo.name][mongo.collection_user]
            result = db.count_documents({"email": email})
        if result == 0:
            return True
        else:
            return False

    def is_unique_ingredient(self, param, value):
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
        if not self.check_ingredient_is_unique(key=param, value=value):
            validation = Validator(param=param, msg=self.detail_already_exist, value=value)
            return abort(status=400, description=validation.__dict__)
        return True

    def is_coherent_ingredient(self, param, value, _id):
        """ Check if value and _id are coherent

        Parameters
        ----------
        param : str
            Key to be checked.
        value : str
            Value to be checked.
        _id : str
            Value to be checked.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if not self.check_ingredient_is_unique(key=param, value=value):
            with MongoClient(mongo.ip, mongo.port) as client:
                db = client[mongo.name][mongo.collection_ingredient]
                result = mongo.convert_to_json(db.find_one({"_id": ObjectId(_id)}))
            if result[param] == value:
                return True
            else:
                validation = Validator(param=param, msg=self.detail_already_exist, value=value)
                return abort(status=400, description=validation.__dict__)
        else:
            return True

    # use in is_unique_ingredient
    # use in is_coherent_ingredient
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
        with MongoClient(mongo.ip, mongo.port) as client:
            db = client[mongo.name][mongo.collection_ingredient]
            result = db.count_documents({key: value})
        if result == 0:
            return True
        else:
            return False

    def is_unique_recipe(self, param, value):
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
        if not self.check_recipe_is_unique(key=param, value=value):
            validation = Validator(param=param, msg=self.detail_already_exist, value=value)
            return abort(status=400, description=validation.__dict__)
        return True

    def is_coherent_recipe(self,  param, value, _id):
        """ Check if value and _id are coherent

        Parameters
        ----------
        param : str
            Key to be checked.
        value : str
            Value to be checked.
        _id : str
            Value to be checked.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if not self.check_recipe_is_unique(key=param, value=value):
            with MongoClient(mongo.ip, mongo.port) as client:
                db = client[mongo.name][mongo.collection_recipe]
                result = mongo.convert_to_json(db.find_one({"_id": ObjectId(_id)}))
            if result[param] == value:
                return True
            else:
                validation = Validator(param=param, msg=self.detail_already_exist, value=value)
                return abort(status=400, description=validation.__dict__)
        else:
            return True

    # use in is_unique_recipe
    # use in is_coherent_recipe
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
        with MongoClient(mongo.ip, mongo.port) as client:
            db = client[mongo.name][mongo.collection_recipe]
            result = db.count_documents({key: value})
        if result == 0:
            return True
        else:
            return False

    @staticmethod
    def is_unique_ingredient_associated(param, data):
        """ Check if ingredients are unique.

        Parameters
        ----------
        param : str
            Parameter's name.
        data : dict
            PostLinks's body.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        """
        len_default = len(data["ingredients"])
        len_unique = len(set([ingr["_id"] for ingr in data["ingredients"]]))
        if len_default != len_unique:
            detail = response.format_detail(param=param, msg=response.detail_must_be_unique,
                                            value=[ingr["_id"] for ingr in data["ingredients"]])
            return abort(status=400, description=detail)
        else:
            return True
        """
        assert True == False
        pass

    def is_string(self, param, value):
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
            validation = Validator(param=param, msg=self.detail_must_be_a_string, value=value)
            return abort(status=400, description=validation.__dict__)

    def is_string_non_empty(self, param, value):
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
            validation = Validator(param=param, msg=self.detail_must_be_not_empty, value=value)
            return abort(status=400, description=validation.__dict__)
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

    def is_string_path(self, param, value):
        """ Check if the value is a path string.

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
        if len(value.split("/")) < 2:
            validation = Validator(param=param, msg=self.detail_must_be_a_path, value=value)
            return abort(status=400, description=validation.__dict__)
        else:
            return True

    def is_int(self, param, value):
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
                validation = Validator(param=param, msg=self.detail_must_be_an_integer, value=value)
                return abort(status=400, description=validation.__dict__)

    def is_float(self, param, value):
        """ Check if the value is an float.

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
        if isinstance(value, float):
            return True
        else:
            try:
                float(value)
                return True
            except (ValueError, TypeError):
                validation = Validator(param=param, msg=self.detail_must_be_a_float, value=value)
                return abort(status=400, description=validation.__dict__)

    def is_array(self, param, value):
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
            validation = Validator(param=param, msg=self.detail_must_be_an_array, value=value)
            return abort(status=400, description=validation.__dict__)

    def is_array_non_empty(self, param, value):
        """ Check if the value is an array non empty.

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
        if len(value) == 0:
            validation = Validator(param=param, msg=self.detail_must_be_not_empty, value=value)
            return abort(status=400, description=validation.__dict__)
        else:
            return True

    def is_array_of_object(self, param, value):
        """ Check if the value is an array of object.

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
        for element in value:
            if not isinstance(element, dict):
                validation = Validator(param=param, msg=self.detail_must_be_an_array_of_object, value=value)
                return abort(status=400, description=validation.__dict__)
        return True

    def is_object(self, param, value):
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
            print("@@@@@@@@@@@@@@@@@@ OK ")
            return True
        else:
            print("@@@@@@@@@@@@@@@@@@ NOK ")
            validation = Validator(param=param, msg=self.detail_must_be_an_object, value=value)
            return abort(status=400, description=validation.__dict__)

    def is_between_x_y(self, param, value, x, y):
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
            validation = Validator(param=param, msg=self.detail_must_be_between + " {0} and {1}".format(x, y),
                                   value=value)
            return abort(status=400, description=validation.__dict__)

    def is_in(self, param, value, values):
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
            validation = Validator(param=param, msg=self.detail_must_be_in + " ['" + "', '".join(values) + "']",
                                   value=value)
            return abort(status=400, description=validation.__dict__)

    def has_at_least_one_key(self, param, data):
        """ Check if the body have at least one key.

        Parameters
        ----------
        param : str
            Param to be tested.
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
            validation = Validator(param=param, msg=self.detail_must_contain_at_least_one_key, value=data)
            return abort(status=400, description=validation.__dict__)

    def is_mandatoryOld(self, name, param, data):
        """ Check if the param is present in body.

        Parameters
        ----------
        name : str
            Name of the tested parameter.
        param : str
            Value of the tested parameter.
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
            validation = Validator(param=name, msg=self.detail_is_required)
            return abort(status=400, description=validation.__dict__)

    def is_mandatory(self, param, value):
        """ Check if the param is present in body.

        Parameters
        ----------
        param : str
            Value of the tested parameter.
        value : Any
            Value of the tested parameter.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        if value is None:
            validation = Validator(param=param, msg=self.detail_is_required)
            return abort(status=400, description=validation.__dict__)
        else:
            return True

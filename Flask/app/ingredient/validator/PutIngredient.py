import utils
import app.ingredient.factory.PutIngredient as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate PutIngredient.
    """

    @staticmethod
    def is_object_id_valid(value):
        """ Check if _id is correct.

        Parameters
        ----------
        value : str
            ObjectId of Ingredient.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_object_id(param=api.param_id, value=value)
        validator.is_object_id_in_collection(param=api.param_id, value=value, collection=mongo.collection_ingredient)
        return True

    def is_body_valid(self, data):
        """ Check if body is correct.

        Parameters
        ----------
        data : dict
            Body of PutIngredient.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.has_at_least_one_key(data=data)
        self.is_name_valid(data=data)
        self.is_slug_valid(data=data)
        self.is_categories_valid(data=data)
        return True

    # use in is_body_valid
    @staticmethod
    def is_name_valid(data):
        """ Check if name is correct if specified.

        Parameters
        ----------
        data : dict
            Body of PostIngredient.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_name in data:
            validator.is_string(param=api.param_name, value=data[api.param_name])
            validator.is_string_non_empty(param=api.param_name, value=data[api.param_name])
            validator.is_unique(kind="ingredient", param=api.param_name, value=data[api.param_name])
            return True

    # use in is_body_valid
    @staticmethod
    def is_slug_valid(data):
        """ Check if slug is correct if specified.

        Parameters
        ----------
        data : dict
            Body of PostIngredient.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_slug in data:
            validator.is_string(param=api.param_slug, value=data[api.param_slug])
            validator.is_string_non_empty(param=api.param_slug, value=data[api.param_slug])
            validator.is_unique(kind="ingredient", param=api.param_slug, value=data[api.param_slug])
        return True

    # use in is_body_valid
    @staticmethod
    def is_categories_valid(data):
        """ Check if categories is correct if specified.

        Parameters
        ----------
        data : dict
            Body of PostIngredient.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_categories in data:
            validator.is_array(param=api.param_categories, value=data[api.param_categories])
            return True
        return True
    
    @staticmethod
    def is_with_files_valid(value):
        """ Check if with_files is correct if specified.

        Parameters
        ----------
        value : str
            Value of parameter with_files.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_string_boolean(param=api.param_with_files, value=value)
        return True

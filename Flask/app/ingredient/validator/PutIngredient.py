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
            Ingredient's ObjectId.

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
            PutIngredient's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.has_at_least_one_key(param="body", data=data)
        self.is_name_valid(data=data)
        self.is_slug_valid(data=data)
        self.is_categories_valid(data=data)
        self.is_nutriments_valid(data=data)
        return True

    # use in is_body_valid
    @staticmethod
    def is_name_valid(data):
        """ Check if name is correct if specified.

        Parameters
        ----------
        data : dict
            PutIngredient's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_name in data:
            validator.is_string(param=api.param_name, value=data[api.param_name])
            validator.is_string_non_empty(param=api.param_name, value=data[api.param_name])
            validator.is_unique_ingredient(param=api.param_name, value=data[api.param_name])
            return True

    # use in is_body_valid
    @staticmethod
    def is_slug_valid(data):
        """ Check if slug is correct if specified.

        Parameters
        ----------
        data : dict
            PutIngredient's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_slug in data:
            validator.is_string(param=api.param_slug, value=data[api.param_slug])
            validator.is_string_non_empty(param=api.param_slug, value=data[api.param_slug])
            validator.is_unique_ingredient(param=api.param_slug, value=data[api.param_slug])
        return True

    # use in is_body_valid
    @staticmethod
    def is_categories_valid(data):
        """ Check if categories is correct if specified.

        Parameters
        ----------
        data : dict
            PutIngredient's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_categories in data:
            validator.is_array(param=api.param_categories, value=data[api.param_categories])
            return True
        return True

    # use in is_body_valid
    @staticmethod
    def is_nutriments_valid(data):
        """ Check if nutriments is correct if specified.

        Parameters
        ----------
        data : dict
            PutIngredient's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_nutriments in data:
            validator.is_object(param=api.param_nutriments, value=data[api.param_nutriments])
            validator.has_at_least_one_key(param=api.param_nutriments, data=data[api.param_nutriments])
            nutriments = data[api.param_nutriments]
            """ calories """
            if api.param_calories in nutriments:
                validator.is_string(param=api.param_calories, value=nutriments[api.param_calories])
                validator.is_string_non_empty(param=api.param_calories, value=nutriments[api.param_calories])
            """ carbohydrates """
            if api.param_carbohydrates in nutriments:
                validator.is_string(param=api.param_carbohydrates, value=nutriments[api.param_carbohydrates])
                validator.is_string_non_empty(param=api.param_carbohydrates, value=nutriments[api.param_carbohydrates])
            """ fats """
            if api.param_fats in nutriments:
                validator.is_string(param=api.param_fats, value=nutriments[api.param_fats])
                validator.is_string_non_empty(param=api.param_fats, value=nutriments[api.param_fats])
            """ proteins """
            if api.param_proteins in nutriments:
                validator.is_string(param=api.param_proteins, value=nutriments[api.param_proteins])
                validator.is_string_non_empty(param=api.param_proteins, value=nutriments[api.param_proteins])
            """ info """
            if api.param_info in nutriments:
                validator.is_string(param=api.param_info, value=nutriments[api.param_info])
                validator.is_string_non_empty(param=api.param_info, value=nutriments[api.param_info])
            return True
        return True
    
    @staticmethod
    def is_with_files_valid(value):
        """ Check if with_files is correct if specified.

        Parameters
        ----------
        value : str
            With_files value.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_string_boolean_or_none(param=api.param_with_files, value=value)
        return True

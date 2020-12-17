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
        self.is_categories_valid(data=data)
        self.is_name_valid(data=data)
        self.is_nutriments_valid(data=data)
        self.is_slug_valid(data=data)
        self.is_unit_valid(data=data)
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
    def is_nutriments_valid(self, data):
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
            self.is_nutriments_calories_valid(data=nutriments)
            self.is_nutriments_carbohydrates_valid(data=nutriments)
            self.is_nutriments_fats_valid(data=nutriments)
            self.is_nutriments_proteins_valid(data=nutriments)
            self.is_nutriments_portion_valid(data=nutriments)
            return True
        return True

    # use in is_nutriments_valid
    @staticmethod
    def is_nutriments_calories_valid(data):
        """ Check if nutriments.calories is correct.

        Parameters
        ----------
        data : dict
            PostIngredient's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        param_name = api.param_nutriments + "." + api.param_nutriments_calories
        if api.param_nutriments_calories in data:
            validator.is_float(param=param_name, value=data[api.param_nutriments_calories])
            return True
        return True

    # use in is_nutriments_valid
    @staticmethod
    def is_nutriments_carbohydrates_valid(data):
        """ Check if nutriments.carbohydrates is correct.

        Parameters
        ----------
        data : dict
            PostIngredient's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        param_name = api.param_nutriments + "." + api.param_nutriments_carbohydrates
        if api.param_nutriments_carbohydrates in data:
            validator.is_float(param=param_name, value=data[api.param_nutriments_carbohydrates])
            return True
        return True

    # use in is_nutriments_valid
    @staticmethod
    def is_nutriments_fats_valid(data):
        """ Check if nutriments.fats is correct.

        Parameters
        ----------
        data : dict
            PostIngredient's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        param_name = api.param_nutriments + "." + api.param_nutriments_fats
        if api.param_nutriments_fats in data:
            validator.is_float(param=param_name, value=data[api.param_nutriments_fats])
            return True
        return True

    # use in is_nutriments_valid
    @staticmethod
    def is_nutriments_portion_valid(data):
        """ Check if nutriments.info is correct.

        Parameters
        ----------
        data : dict
            PostIngredient's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        param_name = api.param_nutriments + "." + api.param_nutriments_portion
        if api.param_nutriments_portion in data:
            validator.is_float(param=param_name, value=data[api.param_nutriments_portion])
            return True
        return True

    # use in is_nutriments_valid
    @staticmethod
    def is_nutriments_proteins_valid(data):
        """ Check if nutriments.proteins is correct.

        Parameters
        ----------
        data : dict
            PostIngredient's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        param_name = api.param_nutriments + "." + api.param_nutriments_proteins
        if api.param_nutriments_proteins in data:
            validator.is_float(param=param_name, value=data[api.param_nutriments_proteins])
            return True
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
    def is_unit_valid(data):
        """ Check if unit is correct if specified.

        Parameters
        ----------
        data : dict
            PutIngredient's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_unit in data:
            validator.is_string(param=api.param_unit, value=data[api.param_unit])
            validator.is_in(param=api.param_unit, value=data[api.param_unit], values=["g", "ml"])
        return True

from app import utils
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

    def is_ingredient_valid(self, ingredient):
        """ Check if body is correct.

        Parameters
        ----------
        ingredient : Ingredient

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        self.is_categories_valid(value=ingredient.categories)
        self.is_name_valid(value=ingredient.name)
        self.is_nutriments_valid(nutriments=ingredient.nutriments)
        self.is_slug_valid(value=ingredient.slug)
        self.is_unit_valid(value=ingredient.unit)
        return True

    # use in is_ingredient_valid
    @staticmethod
    def is_categories_valid(value):
        """ Check if categories is correct if specified.

        Parameters
        ----------
        value : list
            Ingredient's category.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_array(param=api.param_categories, value=value)
        return True

    # use in is_ingredient_valid
    @staticmethod
    def is_name_valid(value):
        """ Check if name is correct.

        Parameters
        ----------
        value : str
            Ingredient's name.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_string(param=api.param_name, value=value)
        validator.is_string_non_empty(param=api.param_name, value=value)
        #validator.is_coherent_ingredient(param=api.param_name, value=data[api.param_name], _id=_id)

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
    def is_slug_valid(data, _id):
        """ Check if slug is correct if specified.

        Parameters
        ----------
        data : dict
            PutIngredient's body.
        _id : str
            Ingredient's ObjectId.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_slug in data:
            validator.is_string(param=api.param_slug, value=data[api.param_slug])
            validator.is_string_non_empty(param=api.param_slug, value=data[api.param_slug])
            validator.is_coherent_ingredient(param=api.param_slug, value=data[api.param_slug], _id=_id)
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

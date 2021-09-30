from app import utils
import app.ingredient.factory.PostIngredient as Factory

validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate PostIngredient.
    """

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
        validator.is_mandatory(param=api.param_name, value=value)
        validator.is_string(param=api.param_name, value=value)
        validator.is_string_non_empty(param=api.param_name, value=value)
        validator.is_unique_ingredient(param=api.param_name, value=value)
        return True

    # use in is_ingredient_valid
    def is_nutriments_valid(self, nutriments):
        """ Check if nutriments is correct if specified.

        Parameters
        ----------
        nutriments : Nutriments
            Ingredient's Nutriments.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        self.is_nutriments_calories_valid(value=nutriments.calories)
        self.is_nutriments_carbohydrates_valid(value=nutriments.carbohydrates)
        self.is_nutriments_fats_valid(value=nutriments.fats)
        self.is_nutriments_proteins_valid(value=nutriments.proteins)
        self.is_nutriments_portion_valid(value=nutriments.portion)
        return True

    # use in is_nutriments_valid
    @staticmethod
    def is_nutriments_calories_valid(value):
        """ Check if nutriments.calories is correct.

        Parameters
        ----------
        value : float
            Nutriments' calories.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        param_name = api.param_nutriments+"."+api.param_nutriments_calories
        validator.is_mandatory(param=param_name, value=value)
        validator.is_float(param=param_name, value=value)
        return True

    # use in is_nutriments_valid
    @staticmethod
    def is_nutriments_carbohydrates_valid(value):
        """ Check if nutriments.carbohydrates is correct.

        Parameters
        ----------
        value : float
            Nutriments' carbohydrates.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        param_name = api.param_nutriments + "." + api.param_nutriments_carbohydrates
        validator.is_mandatory(param=param_name, value=value)
        validator.is_float(param=param_name, value=value)
        return True

    # use in is_nutriments_valid
    @staticmethod
    def is_nutriments_fats_valid(value):
        """ Check if nutriments.fats is correct.

        Parameters
        ----------
        value : float
            Nutriments' fats.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        param_name = api.param_nutriments + "." + api.param_nutriments_fats
        validator.is_mandatory(param=param_name, value=value)
        validator.is_float(param=param_name, value=value)
        return True

    # use in is_nutriments_valid
    @staticmethod
    def is_nutriments_portion_valid(value):
        """ Check if nutriments.portion is correct.

        Parameters
        ----------
        value : float
            Nutriments' portion.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        param_name = api.param_nutriments + "." + api.param_nutriments_portion
        validator.is_mandatory(param=param_name, value=value)
        validator.is_float(param=param_name, value=value)
        return True

    # use in is_nutriments_valid
    @staticmethod
    def is_nutriments_proteins_valid(value):
        """ Check if nutriments.proteins is correct.

        Parameters
        ----------
        value : float
            Nutriments' proteins.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        param_name = api.param_nutriments + "." + api.param_nutriments_proteins
        validator.is_mandatory(param=param_name, value=value)
        validator.is_float(param=param_name, value=value)
        return True

    # use in is_ingredient_valid
    @staticmethod
    def is_slug_valid(value):
        """ Check if slug is correct.

        Parameters
        ----------
        value : str
            Ingredient's slug.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(param=api.param_slug, value=value)
        validator.is_string(param=api.param_slug, value=value)
        validator.is_string_non_empty(param=api.param_slug, value=value)
        validator.is_unique_ingredient(param=api.param_slug, value=value)
        return True

    # use in is_body_valid
    @staticmethod
    def is_unit_valid(value):
        """ Check if unit is correct.

        Parameters
        ----------
        value : str
            Ingredient's unit.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_string(param=api.param_unit, value=value)
        validator.is_in(param=api.param_unit, value=value, values=["g", "ml"])
        return True

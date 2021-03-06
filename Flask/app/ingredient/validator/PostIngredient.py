from app import utils
import app.ingredient.factory.PostIngredient as Factory

validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate PostIngredient.
    """

    def is_body_valid(self, data):
        """ Check if body is correct.

        Parameters
        ----------
        data : dict
            PostIngredient's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
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
            PostIngredient's body.

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
        """ Check if name is correct.

        Parameters
        ----------
        data : dict
            PostIngredient's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(name=api.param_name, param=api.param_name, data=data)
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
            PostIngredient's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_nutriments in data:
            validator.is_object(param=api.param_nutriments, value=data[api.param_nutriments])
            nutriments = data[api.param_nutriments]
            """ calories """
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
        param_name = api.param_nutriments+"."+api.param_nutriments_calories
        validator.is_mandatory(name=param_name, param=api.param_nutriments_calories, data=data)
        validator.is_float(param=param_name, value=data[api.param_nutriments_calories])
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
        validator.is_mandatory(name=param_name, param=api.param_nutriments_carbohydrates, data=data)
        validator.is_float(param=param_name, value=data[api.param_nutriments_carbohydrates])
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
        validator.is_mandatory(name=param_name, param=api.param_nutriments_fats, data=data)
        validator.is_float(param=param_name, value=data[api.param_nutriments_fats])
        return True

    # use in is_nutriments_valid
    @staticmethod
    def is_nutriments_portion_valid(data):
        """ Check if nutriments.portion is correct.

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
        validator.is_mandatory(name=param_name, param=api.param_nutriments_portion, data=data)
        validator.is_float(param=param_name, value=data[api.param_nutriments_portion])
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
        validator.is_mandatory(name=param_name, param=api.param_nutriments_proteins, data=data)
        validator.is_float(param=param_name, value=data[api.param_nutriments_proteins])
        return True

    # use in is_body_valid
    @staticmethod
    def is_slug_valid(data):
        """ Check if slug is correct.

        Parameters
        ----------
        data : dict
            PostIngredient's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(name=api.param_slug, param=api.param_slug, data=data)
        validator.is_string(param=api.param_slug, value=data[api.param_slug])
        validator.is_string_non_empty(param=api.param_slug, value=data[api.param_slug])
        validator.is_unique_ingredient(param=api.param_slug, value=data[api.param_slug])
        return True

    # use in is_body_valid
    @staticmethod
    def is_unit_valid(data):
        """ Check if unit is correct.

        Parameters
        ----------
        data : dict
            PostIngredient's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_unit in data:
            validator.is_string(param=api.param_unit, value=data[api.param_unit])
            validator.is_in(param=api.param_unit, value=data[api.param_unit], values=["g", "ml"])
            return True
        return True

import utils
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
        self.is_name_valid(data=data)
        self.is_slug_valid(data=data)
        self.is_categories_valid(data=data)
        self.is_nutriments_valid(data=data)
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
        validator.is_mandatory(param=api.param_name, data=data)
        validator.is_string(param=api.param_name, value=data[api.param_name])
        validator.is_string_non_empty(param=api.param_name, value=data[api.param_name])
        validator.is_unique_ingredient(param=api.param_name, value=data[api.param_name])
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
        validator.is_mandatory(param=api.param_slug, data=data)
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
    def is_nutriments_valid(data):
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
            validator.is_mandatory(param=api.param_calories, data=nutriments)
            validator.is_string(param=api.param_calories, value=nutriments[api.param_calories])
            validator.is_string_non_empty(param=api.param_calories, value=nutriments[api.param_calories])
            """ carbohydrates """
            validator.is_mandatory(param=api.param_carbohydrates, data=nutriments)
            validator.is_string(param=api.param_carbohydrates, value=nutriments[api.param_carbohydrates])
            validator.is_string_non_empty(param=api.param_carbohydrates, value=nutriments[api.param_carbohydrates])
            """ fats """
            validator.is_mandatory(param=api.param_fats, data=nutriments)
            validator.is_string(param=api.param_fats, value=nutriments[api.param_fats])
            validator.is_string_non_empty(param=api.param_fats, value=nutriments[api.param_fats])
            """ proteins """
            validator.is_mandatory(param=api.param_proteins, data=nutriments)
            validator.is_string(param=api.param_proteins, value=nutriments[api.param_proteins])
            validator.is_string_non_empty(param=api.param_proteins, value=nutriments[api.param_proteins])
            """ info """
            if api.param_info in nutriments:
                validator.is_string(param=api.param_info, value=nutriments[api.param_info])
                validator.is_string_non_empty(param=api.param_info, value=nutriments[api.param_info])
            return True
        return True

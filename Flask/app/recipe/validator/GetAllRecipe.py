from app import utils
import app.recipe.factory.GetAllRecipe as Factory

validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate GetAllRecipe.
    """

    @staticmethod
    def is_with_calories_valid(value):
        """ Check if with_calories is correct if specified.
        Parameters
        ----------
        value : str
            With_calories's value.
        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_string_boolean_or_none(param=api.param_with_calories, value=value)
        return True

    @staticmethod
    def is_search_valid(data):
        """ Check if search params are correct if specified.

        Parameters
        ----------
        data : dict
            Search dict.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        for i, j in data.items():
            if i in [api.param_title, api.param_slug, api.param_categories, api.param_status]:
                validator.is_string_non_empty(param=i, value=j)
            elif i in [api.param_level, api.param_cooking_time, api.param_preparation_time, api.param_nb_people]:
                validator.is_int(param=i, value=j)
            elif i == "order":
                validator.is_string_non_empty(param=i, value=j)
                validator.is_in(param=api.param_order, value=j,
                                values=["asc", "desc"])
            elif i == "orderBy":
                validator.is_string_non_empty(param=i, value=j)
                validator.is_in(param=api.param_order_by, value=j,
                                values=[api.param_title, api.param_slug, api.param_level, api.param_cooking_time,
                                        api.param_preparation_time, api.param_nb_people])
        return True

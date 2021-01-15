from app import utils
import app.recipe.factory.SearchRecipe as Factory

validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate SearchRecipe.
        """

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
        return True

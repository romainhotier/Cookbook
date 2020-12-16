import utils
import app.recipe.factory.GetRecipe as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate GetRecipe.
    """

    @staticmethod
    def is_slug_valid(value):
        """ Check if slug is correct.

        Parameters
        ----------
        value : str
            Recipe's slug.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_string_non_empty(param=api.param_slug, value=value)
        validator.is_slug_in_collection(param=api.param_slug, value=value, collection=mongo.collection_recipe)
        return True

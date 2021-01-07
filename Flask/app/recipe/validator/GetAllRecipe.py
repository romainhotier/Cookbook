import utils
import app.recipe.factory.GetAllRecipe as Factory

validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate GetAllRecipe.
    """

    @staticmethod
    def is_with_files_mongo_valid(value):
        """ Check if with_files_mongo is correct if specified.
        Parameters
        ----------
        value : str
            With_files_mongo's value.
        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_string_boolean_or_none(param=api.param_with_files_mongo, value=value)
        return True

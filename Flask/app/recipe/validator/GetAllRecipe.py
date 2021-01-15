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

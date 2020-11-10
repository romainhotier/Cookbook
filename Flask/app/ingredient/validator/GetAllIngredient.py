import utils
import app.ingredient.factory.GetAllIngredient as Factory

validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate GetAllIngredient.
    """

    @staticmethod
    def is_with_files_valid(value):
        """ Check if with_files is correct if specified.

        Parameters
        ----------
        value : str
            Value of parameter with_files.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        return validator.is_string_boolean(param=api.param_query_with_files, value=value)

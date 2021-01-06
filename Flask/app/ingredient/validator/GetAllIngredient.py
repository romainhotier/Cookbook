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
            With_files's value.
        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_string_boolean_or_none(param=api.param_with_files, value=value)
        return True

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

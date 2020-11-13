import utils
import app.ingredient.factory.SearchIngredient as Factory

validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate SearchIngredient.
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
            if i in api.get_search_param():
                validator.is_string_non_empty(param=i, value=j)
        return True

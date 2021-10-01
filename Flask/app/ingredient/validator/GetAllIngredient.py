from app import utils
import app.ingredient.factory.GetAllIngredient as Factory

validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate GetAllIngredient.
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
            if i in api.get_search_param():
                validator.is_string_non_empty(param=i, value=j)
                if i == "order":
                    validator.is_in(param=api.param_order, value=j,
                                    values=["asc", "desc"])
                elif i == "orderBy":
                    validator.is_in(param=api.param_order_by, value=j,
                                    values=[api.param_name, api.param_slug])
        return True

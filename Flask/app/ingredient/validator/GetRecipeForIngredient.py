import utils
import app.ingredient.factory.GetRecipeForIngredient as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate GetRecipeForIngredient.
    """

    @staticmethod
    def is_object_id_valid(value):
        """ Check if _id is correct.

        Parameters
        ----------
        value : str
            ObjectId of Ingredient.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_object_id(param=api.param_query_id, value=value)
        validator.is_object_id_in_collection(param=api.param_query_id, value=value,
                                             collection=mongo.collection_ingredient)
        return True

    @staticmethod
    def is_with_titles_valid(value):
        """ Check if with_titles is correct if specified.

        Parameters
        ----------
        value : str
            Value of parameter with_titles.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_string_boolean(param=api.param_query_with_titles, value=value)
        return True

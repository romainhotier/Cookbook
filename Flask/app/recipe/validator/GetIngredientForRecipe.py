import utils
import app.recipe.factory.GetIngredientForRecipe as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate GetIngredientForRecipe.
    """

    @staticmethod
    def is_object_id_valid(value):
        validator.is_object_id(param=api.param_id, value=value)
        validator.is_object_id_in_collection(param=api.param_id, value=value, collection=mongo.collection_recipe)
        return True

    @staticmethod
    def is_with_names_valid(value):
        """ Check if with_names is correct if specified.

        Parameters
        ----------
        value : str
            With_names's value.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_string_boolean_or_none(param=api.param_with_names, value=value)
        return True

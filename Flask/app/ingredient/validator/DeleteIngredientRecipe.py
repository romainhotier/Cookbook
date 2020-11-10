import utils
import app.ingredient.factory.DeleteIngredientRecipe as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate DeleteIngredientRecipe.
    """

    @staticmethod
    def is_object_id_valid(value):
        """ Check if _id is correct.

        Parameters
        ----------
        value : str
            ObjectId of IngredientRecipe.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_object_id(param=api.param_query_id, value=value)
        validator.is_object_id_in_collection(param=api.param_query_id, value=value,
                                             collection=mongo.collection_ingredient_recipe)
        return True

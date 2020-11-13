import utils
import app.recipe.factory.DeleteRecipe as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate DeleteRecipe.
    """

    @staticmethod
    def is_object_id_valid(value):
        """ Check if _id is correct.

        Parameters
        ----------
        value : str
            Recipe's ObjectId.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_object_id(param=api.param_id, value=value)
        validator.is_object_id_in_collection(param=api.param_id, value=value, collection=mongo.collection_recipe)
        return True

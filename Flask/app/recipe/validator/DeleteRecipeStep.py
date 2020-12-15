import utils
import app.recipe.factory.DeleteRecipeStep as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate DeleteRecipeStep.
    """

    @staticmethod
    def is_object_id_valid_recipe(value):
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
        validator.is_object_id(param=api.param_id_recipe, value=value)
        validator.is_object_id_in_collection(param=api.param_id_recipe, value=value, collection=mongo.collection_recipe)
        return True

    @staticmethod
    def is_object_id_valid_steps(_id_recipe, _id_step):
        """ Check if _id is correct.

        Parameters
        ----------
        _id_recipe : str
            Recipe's ObjectId.
        _id_step : str
            Step's ObjectId.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_object_id(param=api.param_id_step, value=_id_step)
        validator.is_object_id_in_recipe_steps(param=api.param_id_step, _id_recipe=_id_recipe, _id_step=_id_step)
        return True

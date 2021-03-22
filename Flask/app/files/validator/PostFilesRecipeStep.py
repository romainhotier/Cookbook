from app import utils
import app.files.factory.PostFilesRecipeStep as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate PostFilesRecipeStep.
    """

    @staticmethod
    def is_object_id_valid_recipe(value):
        """ Check if _id is correct.

        Parameters
        ----------
        value : str
            ObjectId of the element.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_object_id(param=api.param_id_recipe, value=value)
        validator.is_object_id_in_collection(param=api.param_id_recipe, value=value, collection="recipe")
        return True

    @staticmethod
    def is_object_id_valid_step(_id_recipe, _id_step):
        """ Check if _id is correct.

        Parameters
        ----------
        _id_recipe : str
            ObjectId of the element.
        _id_step : str
            ObjectId of the element.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_object_id(param=api.param_id_step, value=_id_step)
        validator.is_object_id_in_recipe_steps(param=api.param_id_step, _id_recipe=_id_recipe, _id_step=_id_step)
        return True

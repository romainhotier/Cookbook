import utils
import app.ingredient.factory.GetIngredient as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate GetIngredient.
    """

    @staticmethod
    def is_object_id_valid(value):
        """ Check if _id is correct.

        Parameters
        ----------
        value : str
            Ingredient's ObjectId.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_object_id(param=api.param_id, value=value)
        validator.is_object_id_in_collection(param=api.param_id, value=value, collection=mongo.collection_ingredient)
        return True

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

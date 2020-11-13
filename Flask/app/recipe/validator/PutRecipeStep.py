import utils
import app.recipe.factory.PutRecipeStep as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate PutRecipeStep.
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
            Step's ObjectId

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_object_id(param=api.param_id_step, value=_id_step)
        validator.is_object_id_in_recipe_steps(param=api.param_id_step, _id_recipe=_id_recipe, _id_step=_id_step)
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

    def is_body_valid(self, data):
        """ Check if body is correct.

        Parameters
        ----------
        data : dict
            PutRecipeStep's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        self.is_description_valid(data)

    # use in is_body_valid
    @staticmethod
    def is_description_valid(data):
        """ Check if description is correct.

        Parameters
        ----------
        data : dict
            PutRecipeStep's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(param=api.param_description, data=data)
        validator.is_string(param=api.param_description, value=data[api.param_description])
        validator.is_string_non_empty(param=api.param_description, value=data[api.param_description])
        return True

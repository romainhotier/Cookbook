import utils
import app.recipe.model as recipe_model
import app.recipe.factory.PutRecipeSteps as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()
step = recipe_model.Step()


class Validator(object):
    """ Class to validate PutRecipeSteps.
    """

    @staticmethod
    def is_object_id_valid(value):
        validator.is_object_id(param=api.param_id_recipe, value=value)
        validator.is_object_id_in_collection(param=api.param_id_recipe, value=value, collection=mongo.collection_recipe)
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
            PutRecipeSteps's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        self.is_steps_valid(data=data)

    # use in is_body_valid
    def is_steps_valid(self, data):
        """ Check if steps is correct.

        Parameters
        ----------
        data : dict
            PutRecipeSteps's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(param=api.param_steps, data=data)
        validator.is_array(param=api.param_steps, value=data[api.param_steps])
        validator.is_array_non_empty(param=api.param_steps, value=data[api.param_steps])
        validator.is_array_of_object(param=api.param_steps, value=data[api.param_steps])
        for stp in data[api.param_steps]:
            self.is_description_valid(data=stp)
        return True

    # use in is_steps_valid
    @staticmethod
    def is_description_valid(data):
        """ Check if description is correct.

        Parameters
        ----------
        data : dict
            Body of PostRecipe.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(param=api.param_description, data=data)
        validator.is_string(param=api.param_description, value=data[api.param_description])
        validator.is_string_non_empty(param=api.param_description, value=data[api.param_description])
        return True

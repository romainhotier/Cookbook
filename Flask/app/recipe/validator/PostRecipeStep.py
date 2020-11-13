import utils
import app.recipe.model as recipe_model
import app.recipe.factory.PostRecipeStep as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()
step = recipe_model.Step()


class Validator(object):
    """ Class to validate PostRecipeStep.
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

    def is_body_valid(self, _id_recipe, data):
        """ Check if body is correct.

        Parameters
        ----------
        _id_recipe : str
            Recipe's ObjectId.
        data : dict
            PostRecipeStep's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        self.is_description_valid(data=data)
        self.is_position_valid(_id_recipe=_id_recipe, data=data)

    # use in is_body_valid
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

    # use in is_body_valid
    @staticmethod
    def is_position_valid(_id_recipe, data):
        """ Check if slug is correct if specified.

        Parameters
        ----------
        _id_recipe : str
            Recipe's ObjectId.
        data : dict
            PostRecipeStep's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_position in data:
            validator.is_int(api.param_position, data[api.param_position])
            validator.is_between_x_y(param=api.param_position, value=data[api.param_position], x=0,
                                     y=step.get_steps_length(_id_recipe=_id_recipe))
            return True
        return True

import utils
import app.ingredient.factory.PutIngredientRecipe as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate PutIngredientRecipe.
    """

    @staticmethod
    def is_object_id_valid(value):
        """ Check if _id is correct.

        Parameters
        ----------
        value : str
            IngredientRecipe's ObjectId.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        utils.Validator.is_object_id(param=api.param_id, value=value)
        utils.Validator.is_object_id_in_collection(param=api.param_id, value=value,
                                                   collection=mongo.collection_ingredient_recipe)
        return True

    def is_body_valid(self, data):
        """ Check if body is correct.

        Parameters
        ----------
        data : dict
            PutIngredientRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        utils.Validator.has_at_least_one_key(data=data)
        self.is_quantity_valid(data=data)
        self.is_unit_valid(data=data)
        return True

    # use in is_body_valid
    @staticmethod
    def is_quantity_valid(data):
        """ Check if quantity is correct if specified.

        Parameters
        ----------
        data : dict
            PutIngredientRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_quantity in data:
            utils.Validator.is_int(param=api.param_quantity, value=data[api.param_quantity])
            return True

    # use in is_body_valid
    @staticmethod
    def is_unit_valid(data):
        """ Check if unit is correct if specified.

        Parameters
        ----------
        data : dict
            PutIngredientRecipe's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        if api.param_unit in data:
            utils.Validator.is_string(param=api.param_unit, value=data[api.param_unit])
            return True

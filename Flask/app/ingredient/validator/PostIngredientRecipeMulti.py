import utils
import app.ingredient.factory.PostIngredientRecipeMulti as Factory

mongo = utils.Mongo()
validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate PostIngredientRecipeMulti.
    """

    def is_body_valid(self, data):
        """ Check if body is correct.

        Parameters
        ----------
        data : dict
            PostIngredientRecipeMulti's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        self.is_id_recipe_valid(data=data)
        self.is_ingredients_valid(data=data)

    # use in is_body_valid
    @staticmethod
    def is_id_recipe_valid(data):
        """ Check if _di_recipe is correct.

        Parameters
        ----------
        data : dict
            PostIngredientRecipeMulti's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(param=api.param_id_recipe, data=data)
        validator.is_object_id(param=api.param_id_recipe, value=data[api.param_id_recipe])
        validator.is_object_id_in_collection(param=api.param_id_recipe, value=data[api.param_id_recipe],
                                             collection=mongo.collection_recipe)
        return True

    # use in is_body_valid
    def is_ingredients_valid(self, data):
        """ Check if ingredients is correct.

        Parameters
        ----------
        data : dict
            PostIngredientRecipeMulti's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(param=api.param_ingredients, data=data)
        validator.is_array(param=api.param_ingredients, value=data[api.param_ingredients])
        validator.is_array_non_empty(param=api.param_ingredients, value=data[api.param_ingredients])
        validator.is_array_of_object(param=api.param_ingredients, value=data[api.param_ingredients])
        for ingredient in data[api.param_ingredients]:
            validator.is_object(param=api.param_ingredients, value=ingredient)
            self.is_id_ingredient_valid(data=ingredient)
            self.is_quantity_valid(data=ingredient)
            self.is_unit_valid(data=ingredient)
            validator.is_unique_ingredient_recipe(_id_ingredient=ingredient[api.param_id_ingredient],
                                                  _id_recipe=data[api.param_id_recipe])
        validator.is_unique_ingredient_recipe_multi(param=api.param_id_ingredient, data=data)
        return True

    # use in is_ingredients_valid
    @staticmethod
    def is_id_ingredient_valid(data):
        """ Check if _id_ingredient is correct.

        Parameters
        ----------
        data : dict
            PostIngredientRecipeMulti's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(param=api.param_id_ingredient, data=data)
        validator.is_object_id(param=api.param_id_ingredient, value=data[api.param_id_ingredient])
        validator.is_object_id_in_collection(param=api.param_id_ingredient, value=data[api.param_id_ingredient],
                                             collection=mongo.collection_ingredient)
        return True

    # use in is_ingredients_valid
    @staticmethod
    def is_quantity_valid(data):
        """ Check if quantity is correct.

        Parameters
        ----------
        data : dict
            PostIngredientRecipeMulti's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(param=api.param_quantity, data=data)
        validator.is_int(param=api.param_quantity, value=data[api.param_quantity])
        return True

    # use in is_ingredients_valid
    @staticmethod
    def is_unit_valid(data):
        """ Check if unit is correct.

        Parameters
        ----------
        data : dict
            PostIngredientRecipeMulti's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(param=api.param_unit, data=data)
        validator.is_string(param=api.param_unit, value=data[api.param_unit])
        return True

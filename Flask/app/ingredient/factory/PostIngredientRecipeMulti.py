class Factory(object):

    def __init__(self):
        """ Class to work around PostIngredientRecipeMulti.
        """
        self.param_id_recipe = "_id_recipe"
        self.param_ingredients = "ingredients"
        self.param_id_ingredient = "_id_ingredient"
        self.param_quantity = "quantity"
        self.param_unit = "unit"
        self.body = {}

    def get_body_param(self):
        """ Get PostIngredientRecipeMulti's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_id_recipe, self.param_ingredients]

    def get_ingredients_body_param(self):
        """ Get PostIngredientRecipeMulti's ingredients body parameters.

        Returns
        -------
        list
            Ingredients body parameters.
        """
        return [self.param_id_ingredient, self.param_unit, self.param_quantity]

    def clean_body(self, data):
        """ Remove keys that are not in PostIngredientRecipeMulti's parameters.

        Parameters
        ----------
        data : dict
            To be cleaned.

        Returns
        -------
        dict
            Correct body.
        """
        self.__setattr__("body", data)
        self.remove_foreign_key()
        self.remove_foreign_key_ingredients()
        return self.body

    # use in clean_body
    def remove_foreign_key(self):
        """ Remove keys that are not in PostIngredientRecipeMulti's parameters.
        """
        for i in list(self.body):
            if i not in self.get_body_param():
                del self.body[i]

    # use in clean_body
    def remove_foreign_key_ingredients(self):
        """ Remove keys that are not in PostIngredientRecipeMulti's parameters for ingredients param.
        """
        try:
            ingredients = self.body[self.param_ingredients]
            try:
                for index, ingredient in enumerate(ingredients):
                    for i in list(ingredient):
                        if i not in self.get_ingredients_body_param():
                            del self.body[self.param_ingredients][index][i]
            except TypeError:
                pass
        except KeyError:
            pass

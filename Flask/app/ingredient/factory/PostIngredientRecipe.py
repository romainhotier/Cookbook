class Factory(object):

    def __init__(self):
        """ Class to work around PostIngredientRecipe.
        """
        self.param_id_ingredient = "_id_ingredient"
        self.param_id_recipe = "_id_recipe"
        self.param_quantity = "quantity"
        self.param_unit = "unit"
        self.body = {}

    def get_body_param(self):
        """ Get PostIngredientRecipe's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_id_recipe, self.param_id_ingredient, self.param_quantity, self.param_unit]

    def clean_body(self, data):
        """ Remove keys that are not in PostIngredientRecipe's parameters.

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
        return self.body

    # use in clean_body
    def remove_foreign_key(self):
        """ Remove keys that are not in PostIngredientRecipe's parameters.
        """
        for i in list(self.body):
            if i not in self.get_body_param():
                del self.body[i]

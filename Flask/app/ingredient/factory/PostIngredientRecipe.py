class Factory(object):

    def __init__(self):
        """ Class to work around PostIngredientRecipe.
        """
        self.param_body_id_ingredient = "_id_ingredient"
        self.param_body_id_recipe = "_id_recipe"
        self.param_body_quantity = "quantity"
        self.param_body_unit = "unit"

    def get_body_param(self):
        """ Get PostIngredientRecipe's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [getattr(self, param) for param in dir(self) if not callable(getattr(self, param)) and
                not param.startswith("__")]

    def format_body(self, data):
        """ Format body for PostIngredientRecipe.

        Parameters
        ----------
        data : dict
            To be cleaned.

        Returns
        -------
        dict
            Correct body.
        """
        cleaned = self.remove_foreign_key(data)
        return cleaned

    # use in format_body
    def remove_foreign_key(self, data):
        """ Remove keys that are not in PostIngredientRecipe's parameters.

        Parameters
        ----------
        data : dict
            To be cleaned

        Returns
        -------
        dict
            Cleaned dict.
        """
        for i in list(data):
            if i not in self.get_body_param():
                del data[i]
        return data

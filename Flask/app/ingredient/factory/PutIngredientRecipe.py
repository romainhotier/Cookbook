class Factory(object):

    def __init__(self):
        """ Class to work around PutIngredientRecipe.
        """
        self.param_id = "_id"
        self.param_quantity = "quantity"
        self.param_unit = "unit"

    def get_body_param(self):
        """ Get PutIngredientRecipe's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_quantity, self.param_unit]

    def format_body(self, data):
        """ Format body for PutIngredientRecipe.

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
        """ Remove keys that are not in PutIngredientRecipe's parameters.

        Parameters
        ----------
        data : dict
            To be cleaned.

        Returns
        -------
        dict
            Cleaned dict.
        """
        for i in list(data):
            if i not in self.get_body_param():
                del data[i]
        return data

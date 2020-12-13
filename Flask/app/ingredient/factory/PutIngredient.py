class Factory(object):

    def __init__(self):
        """ Class to work around PutIngredient.
        """
        self.param_id = "_id"
        self.param_categories = "categories"
        self.param_name = "name"
        self.param_nutriments = "nutriments"
        self.param_nutriments_calories = "calories"
        self.param_nutriments_carbohydrates = "carbohydrates"
        self.param_nutriments_fats = "fats"
        self.param_nutriments_info = "info"
        self.param_nutriments_proteins = "proteins"
        self.param_slug = "slug"
        self.body = {}

    def get_body_param(self):
        """ Get PutIngredient's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_categories, self.param_name, self.param_nutriments, self.param_slug]

    def get_nutriments_param(self):
        """ Get PutIngredient's nutriments parameters.

        Returns
        -------
        list
            Nutriments parameters.
        """
        return [self.param_nutriments_calories, self.param_nutriments_carbohydrates, self.param_nutriments_fats,
                self.param_nutriments_info, self.param_nutriments_proteins]

    def clean_body(self, data):
        """ Remove keys that are not in PutIngredient's parameters.

        Parameters
        ----------
        data : dict
            To be cleaned.

        Returns
        -------
        dict
            Cleaned dict.
        """
        """ body keys """
        self.__setattr__("body", data)
        self.remove_foreign_key()
        self.remove_foreign_key_nutriments()
        return self.body

    # use in clean_body
    def remove_foreign_key(self):
        """ Remove keys that are not in PostIngredient's body parameters.
        """
        for i in list(self.body):
            if i not in self.get_body_param():
                del self.body[i]

    # use in clean_body
    def remove_foreign_key_nutriments(self):
        """ Remove keys that are not in PostIngredient's nutriments parameters.
        """
        try:
            for i in list(self.body[self.param_nutriments]):
                if i not in self.get_nutriments_param():
                    del self.body[self.param_nutriments][i]
        except (KeyError, TypeError):
            pass

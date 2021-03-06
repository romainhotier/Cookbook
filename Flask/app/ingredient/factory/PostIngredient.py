class Factory(object):

    def __init__(self):
        """ Class to work around PostIngredient.
        """
        self.param_categories = "categories"
        self.param_name = "name"
        self.param_nutriments = "nutriments"
        self.param_nutriments_calories = "calories"
        self.param_nutriments_carbohydrates = "carbohydrates"
        self.param_nutriments_fats = "fats"
        self.param_nutriments_proteins = "proteins"
        self.param_nutriments_portion = "portion"
        self.param_slug = "slug"
        self.param_unit = "unit"
        self.body = {}

    def get_body_param(self):
        """ Get PostIngredient's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_categories, self.param_name, self.param_nutriments, self.param_slug, self.param_unit]

    def get_nutriments_param(self):
        """ Get PostIngredient's nutriments parameters.

        Returns
        -------
        list
            Nutriments parameters.
        """
        return [self.param_nutriments_calories, self.param_nutriments_carbohydrates, self.param_nutriments_fats,
                self.param_nutriments_proteins, self.param_nutriments_portion]

    def clean_body(self, data):
        """ Remove keys that are not in PostIngredient's parameters.

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

    def fill_body(self, data):
        """ Fill body for PostIngredient.

        Parameters
        ----------
        data : dict
            To be filled.

        Returns
        -------
        dict
            Correct body.
        """
        self.__setattr__("body", data)
        self.fill_body_missing_key()
        return self.body

    # use in fill_body
    def fill_body_missing_key(self):
        """ Fill keys that are not mandatory with default value for PostIngredient.
            - categories -> []
            - nutriments -> {"calories": "0", "carbohydrates": "0","fats": "0","proteins": "0","portion": ""}
            - unit -> "g"
        """
        for key in self.get_body_param():
            if key not in self.body:
                if key == self.param_categories:
                    self.body[key] = []
                if key == self.param_nutriments:
                    self.body[key] = {self.param_nutriments_calories: 0,
                                      self.param_nutriments_carbohydrates: 0,
                                      self.param_nutriments_fats: 0,
                                      self.param_nutriments_proteins: 0,
                                      self.param_nutriments_portion: 1}
                if key == self.param_unit:
                    self.body[key] = "g"

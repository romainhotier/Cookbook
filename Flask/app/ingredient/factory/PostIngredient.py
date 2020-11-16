class Factory(object):

    def __init__(self):
        """ Class to work around PostIngredient.
        """
        self.param_name = "name"
        self.param_slug = "slug"
        self.param_categories = "categories"
        self.param_nutriments = "nutriments"
        self.param_calories = "calories"
        self.param_carbohydrates = "carbohydrates"
        self.param_fats = "fats"
        self.param_proteins = "proteins"
        self.param_info = "info"

    def get_body_param(self):
        """ Get PostIngredient's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_name, self.param_slug, self.param_categories, self.param_nutriments]

    def format_body(self, data):
        """ Format body for PostIngredient.

        Parameters
        ----------
        data : dict
            To be cleaned.

        Returns
        -------
        dict
            Correct body.
        """
        cleaned = self.remove_foreign_key(data=data)
        filled = self.fill_body_with_missing_key(data=cleaned)
        return filled

    # use in format_body
    def remove_foreign_key(self, data):
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
        for i in list(data):
            if i not in self.get_body_param():
                del data[i]
        return data

    # use in format_body
    def fill_body_with_missing_key(self, data):
        """ Fill keys that are not mandatory with default value for PostIngredient.
         - categories -> []
         - nutriments -> {"calories": "0", "carbohydrates": "0","fats": "0","proteins": "0","info": "per 100g"}

        Parameters
        ----------
        data : dict
            Dict to be filled with default value.

        Returns
        -------
        dict
            Filled dict.
        """
        for key in self.get_body_param():
            if key not in data:
                if key == self.param_categories:
                    data[key] = []
                if key == self.param_nutriments:
                    data[key] = {self.param_calories: "0",
                                 self.param_carbohydrates: "0",
                                 self.param_fats: "0",
                                 self.param_proteins: "0",
                                 self.param_info: "per 100g"}
        return data

class Factory(object):

    def __init__(self):
        """ Class to work around PutIngredient.
        """
        self.param_id = "_id"
        self.param_with_files = "with_files"
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
        """ Get PutIngredient's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_name, self.param_slug, self.param_categories, self.param_nutriments]

    def format_body(self, data):
        """ Format body for PutIngredient.

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
        for i in list(data):
            if i not in self.get_body_param():
                del data[i]
        return data

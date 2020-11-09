class Factory(object):

    def __init__(self):
        """ Class to work around PostIngredient's Body.
        """
        self.name = "name"
        self.slug = "slug"
        self.categories = "categories"
        self.nutriments = "nutriments"

    def get_param(self):
        """ Get PostIngredient's parameters.
        """
        return [param for param in dir(self) if not callable(getattr(self, param)) and not param.startswith("__")]

    def clean_body(self, data):
        """ Cleaned and filled dict for PostIngredient.

        Parameters
        ----------
        data : dict
            Dict to be cleaned and filled with default value.
        """
        cleaned = self.remove_foreign_key(data=data)
        filled = self.fill_body_with_missing_key(data=cleaned)
        return filled

    # use in clean body
    def remove_foreign_key(self, data):
        """ Remove keys that are not in PostIngredient's parameters.

        Parameters
        ----------
        data : dict
            Dict to be cleaned
        """
        for i, j in data.items():
            if i not in self.get_param():
                del data[i]
        return data

    # use in clean body
    def fill_body_with_missing_key(self, data):
        """ Fill keys that are not mandatory with default value for PostIngredient. \n
        categories -> []\n
        nutriments -> {}

        Parameters
        ----------
        data : dict
            Dict to be filled with default value
        """
        for key in self.get_param():
            if key not in data.keys():
                if key == self.categories:
                    data[key] = []
                if key == self.nutriments:
                    data[key] = {}
        return data

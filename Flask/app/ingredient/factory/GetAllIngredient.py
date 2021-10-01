class Factory(object):

    def __init__(self):
        """ Class to work around GetAllIngredient.
        """
        self.param_categories = "categories"
        self.param_name = "name"
        self.param_order = "order"
        self.param_order_by = "orderBy"
        self.param_slug = "slug"

    def get_search_param(self):
        """ Get SearchIngredient's parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_categories, self.param_name, self.param_order, self.param_order_by, self.param_slug]

    def format_body(self, data):
        """ Format body for SearchIngredient.

        Parameters
        ----------
        data : dict
            To be cleaned.

        Returns
        -------
        dict
            Correct body.
        """
        converted = self.convert_immutable_dict(data)
        cleaned = self.remove_foreign_key(converted)
        return cleaned

    # use in format_body
    @staticmethod
    def convert_immutable_dict(data):
        """ Convert ImmutableMultiDict to classic dict.

        Parameters
        ----------
        data : dict
            To be converted

        Returns
        -------
        dict
            Converted dict.
        """
        converted = {}
        for i, j in data.items():
            converted[i] = j
        return converted

    # use in format_body
    def remove_foreign_key(self, data):
        """ Remove keys that are not in SearchIngredient's parameters.

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
            if i not in self.get_search_param():
                del data[i]
        return data

class Factory(object):

    def __init__(self):
        """ Class to work around SearchIngredient.
        """
        self.param_query_name = "name"
        self.param_query_slug = "slug"
        self.param_query_categories = "categories"
        self.param_query_with_files = "with_files"

    def get_search_param(self):
        """ Get SearchIngredient's parameters.

        Returns
        -------
        list
            Body parameters.
        """
        params = [getattr(self, param) for param in dir(self) if not callable(getattr(self, param)) and
                      not param.startswith("__")]
        params.remove(self.param_query_with_files)
        return params

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
        cleaned = self.remove_foreign_key(data)
        return cleaned

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

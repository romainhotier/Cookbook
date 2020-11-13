class Factory(object):

    def __init__(self):
        """ Class to work around PostRecipeStep.
        """
        self.param_id_recipe = "_id_recipe"
        self.param_with_files = "with_files"
        self.param_description = "description"
        self.param_position = "position"

    def get_body_param(self):
        """ Get PostRecipeStep's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_description, self.param_position]

    def format_body(self, data):
        """ Format body for PostRecipeStep.

        Parameters
        ----------
        data : dict
            To be cleaned.

        Returns
        -------
        dict
            Correct body.
        """
        filled = self.remove_foreign_key(data)
        return filled

    # use in format_body
    def remove_foreign_key(self, data):
        """ Remove keys that are not in PostRecipeStep's parameters.

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

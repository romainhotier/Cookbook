class Factory(object):

    def __init__(self):
        """ Class to work around PutRecipeStep.
        """
        self.param_id_recipe = "_id_recipe"
        self.param_id_step = "_id_step"
        self.param_with_files = "with_files"
        self.param_description = "description"

    def get_body_param(self):
        """ Get PutRecipeStep's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_description]

    def format_body(self, data):
        """ Format body for PutRecipeStep.

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
        """ Remove keys that are not in PutRecipeStep's parameters.

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

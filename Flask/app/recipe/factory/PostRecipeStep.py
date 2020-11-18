class Factory(object):

    def __init__(self):
        """ Class to work around PostRecipeStep.
        """
        self.param_id_recipe = "_id_recipe"
        self.param_with_files = "with_files"
        self.param_description = "description"
        self.param_position = "position"
        self.body = {}

    def get_body_param(self):
        """ Get PostRecipeStep's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_description, self.param_position]

    def clean_body(self, data):
        """ Remove keys that are not in PostRecipeStep's parameters.

        Parameters
        ----------
        data : dict
            To be cleaned.

        Returns
        -------
        dict
            Correct body.
        """
        self.__setattr__("body", data)
        self.remove_foreign_key()
        return self.body

    # use in clean_body
    def remove_foreign_key(self):
        """ Remove keys that are not in PostRecipeStep's parameters.
        """
        for i in list(self.body):
            if i not in self.get_body_param():
                del self.body[i]

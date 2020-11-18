class Factory(object):

    def __init__(self):
        """ Class to work around PutRecipeStep.
        """
        self.param_id_recipe = "_id_recipe"
        self.param_id_step = "_id_step"
        self.param_with_files = "with_files"
        self.param_description = "description"
        self.body = {}

    def get_body_param(self):
        """ Get PutRecipeStep's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_description]

    def clean_body(self, data):
        """ Remove keys that are not in PutRecipeStep's parameters.

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

    # use in format_body
    def remove_foreign_key(self):
        """ Remove keys that are not in PutRecipeStep's parameters.
        """
        for i in list(self.body):
            if i not in self.get_body_param():
                del self.body[i]

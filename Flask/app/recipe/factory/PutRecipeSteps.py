class Factory(object):

    def __init__(self):
        """ Class to work around PutRecipeSteps.
        """
        self.param_id_recipe = "_id_recipe"
        self.param_with_files = "with_files"
        self.param_steps = "steps"
        self.param_description = "description"
        self.body = {}

    def get_body_param(self):
        """ Get PutRecipeSteps's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_steps]

    def get_steps_body_param(self):
        """ Get PutRecipeSteps's step body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_description]

    def clean_body(self, data):
        """ Remove keys that are not in PutRecipeSteps's parameters.

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
        self.remove_foreign_key_steps()
        return self.body

    # use in clean_body
    def remove_foreign_key(self):
        """ Remove keys that are not in PutRecipeSteps's parameters.
        """
        for i in list(self.body):
            if i not in self.get_body_param():
                del self.body[i]

    # use in clean_body
    def remove_foreign_key_steps(self):
        """ Remove keys that are not in PutRecipeSteps's parameters for steps param.
        """
        try:
            steps = self.body[self.param_steps]
            try:
                for index, stp in enumerate(steps):
                    for i in list(stp):
                        if i not in self.get_steps_body_param():
                            del self.body[self.param_steps][index][i]
            except TypeError:
                pass
        except KeyError:
            pass

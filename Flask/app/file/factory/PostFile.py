class Factory(object):

    def __init__(self):
        """ Class to work around PostFile.
        """
        self.param_id = "_id"
        self.param_id_recipe = "_id_recipe"
        self.param_id_step = "_id_step"
        self.param_is_main = "is_main"
        self.param_filename = "filename"
        self.param_path = "path"
        self.body = {}

    def get_body_param(self):
        """ Get PostFile's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_is_main, self.param_filename, self.param_path]

    def clean_body(self, data):
        """ Remove keys that are not in PostFile's parameters.

        Parameters
        ----------
        data : dict
            To be cleaned.

        Returns
        -------
        dict
            Cleaned dict.
        """
        """ body keys """
        self.__setattr__("body", data)
        self.remove_foreign_key()
        return self.body

    # use in clean_body
    def remove_foreign_key(self):
        """ Remove keys that are not in PostFile's parameters.
        """
        for i in list(self.body):
            if i not in self.get_body_param():
                del self.body[i]

    def fill_body(self, data):
        """ Fill body for PostIngredient.

        Parameters
        ----------
        data : dict
            To be filled.

        Returns
        -------
        dict
            Correct body.
        """
        self.__setattr__("body", data)
        self.fill_body_missing_key()
        return self.body

    # use in fill_body
    def fill_body_missing_key(self):
        """ Fill keys that are not mandatory with default value for PostFile.
            - is_main -> False
        """
        for key in self.get_body_param():
            if key not in self.body:
                if key == self.param_is_main:
                    self.body[key] = False

    @staticmethod
    def detail_information(_id_file):
        """ Get new File's ObjectId.

        Parameters
        ----------
        _id_file : str
            Added file's ObjectId.

        Returns
        -------
        str
            Information.
        """
        return "added file ObjectId: {0}".format(_id_file)

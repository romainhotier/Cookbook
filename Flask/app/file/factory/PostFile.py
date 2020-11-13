class Factory(object):

    def __init__(self):
        """ Class to work around PostFile.
        """
        self.param_id = "_id"
        self.param_id_recipe = "_id_recipe"
        self.param_id_step = "_id_step"
        self.param_path = "path"
        self.param_filename = "filename"
        self.param_is_main = "is_main"

    def get_body_param(self):
        """ Get PostFile's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_path, self.param_filename, self.param_is_main]

    def format_body(self, data):
        """ Format body for PostFile.

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
        filled = self.fill_body_with_missing_key(cleaned)
        return filled

    # use in format_body
    def remove_foreign_key(self, data):
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
        for i in list(data):
            if i not in self.get_body_param():
                del data[i]
        return data

    # use in format_body
    def fill_body_with_missing_key(self, data):
        """ Fill keys that are not mandatory with default value for PostFile.
         - is_main -> False

        Parameters
        ----------
        data : dict
            Dict to be filled with default value.

        Returns
        -------
        dict
            Filled dict.
        """
        for key in self.get_body_param():
            if key not in data:
                if key == self.param_is_main:
                    data[key] = False
        return data

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

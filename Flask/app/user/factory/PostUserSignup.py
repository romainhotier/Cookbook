class Factory(object):

    def __init__(self):
        """ Class to work around PostUserSignup.
        """
        self.param_body_display_name = "display_name"
        self.param_body_email = "email"
        self.param_body_password = "password"

    def get_body_param(self):
        """ Get PostUserSignup's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [getattr(self, param) for param in dir(self) if not callable(getattr(self, param)) and
                not param.startswith("__")]

    def format_body(self, data):
        """ Format body for PostUserSignup.

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
        """ Remove keys that are not in PostUserSignup's parameters.

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
            if i not in self.get_body_param():
                del data[i]
        return data

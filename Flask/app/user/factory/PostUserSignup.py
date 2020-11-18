class Factory(object):

    def __init__(self):
        """ Class to work around PostUserSignup.
        """
        self.param_display_name = "display_name"
        self.param_email = "email"
        self.param_password = "password"
        self.body = {}

    def get_body_param(self):
        """ Get PostUserSignup's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [self.param_display_name, self.param_email, self.param_password]

    def clean_body(self, data):
        """ Remove keys that are not in PostUserSignup's parameters.

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
        """ Remove keys that are not in PostUserSignup's parameters.
        """
        for i in list(self.body):
            if i not in self.get_body_param():
                del self.body[i]

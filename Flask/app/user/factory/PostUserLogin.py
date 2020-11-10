import app.user.model as user_model


class Factory(object):

    def __init__(self):
        """ Class to work around PostUserLogin.
        """
        self.param_body_email = "email"
        self.param_body_password = "password"

    def get_body_param(self):
        """ Get PostUserLogin's body parameters.

        Returns
        -------
        list
            Body parameters.
        """
        return [getattr(self, param) for param in dir(self) if not callable(getattr(self, param)) and
                not param.startswith("__")]

    def format_body(self, data):
        """ Format body for PostUserLogin.

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
        """ Remove keys that are not in PostUserLogin's parameters.

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

    def check_password(self, data):
        """ Check access for the user.

        Parameters
        ----------
        data : dict
            PostUserLogin's body.

        Returns
        -------
        bool
            True if the password is correct.
        """
        user = user_model.User().select_one_by_email(email=data[self.param_body_email]).result
        return user_model.User().check_password(password=user["password"],
                                                password_attempt=data[self.param_body_password])

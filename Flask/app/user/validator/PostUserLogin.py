import utils

import app.user.factory.PostUserLogin as Factory

api = Factory.Factory()


class Validator(object):
    """ Class to validate PostUserLogin's body.
    """

    def is_body_valid(self, data):
        """ Check if body is correct.

        Parameters
        ----------
        data : dict
            Body of PostUserLogin.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        self.is_email_valid(data)
        self.is_password_valid(data)
        return True

    # use in is_body_valid
    @staticmethod
    def is_email_valid(data):
        """ Check if email is correct.

        Parameters
        ----------
        data : dict
            Body of PostUserLogin.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        utils.Validator.is_mandatory(param=api.param_email, data=data)
        utils.Validator.is_string(param=api.param_email, value=data[api.param_email])
        utils.Validator.is_string_non_empty(param=api.param_email, value=data[api.param_email])
        return True

    # use in is_body_valid
    @staticmethod
    def is_password_valid(data):
        """ Check if password is correct.

        Parameters
        ----------
        data : dict
            Body of PostUserLogin.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        utils.Validator.is_mandatory(param=api.param_password, data=data)
        utils.Validator.is_string(param=api.param_password, value=data[api.param_password])
        utils.Validator.is_string_non_empty(param=api.param_password, value=data[api.param_password])
        return True

import utils
import app.user.factory.PostUserLogin as Factory

validator = utils.Validator()
api = Factory.Factory()


class Validator(object):
    """ Class to validate PostUserLogin.
    """

    def is_body_valid(self, data):
        """ Check if body is correct.

        Parameters
        ----------
        data : dict
            PostUserLogin's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        self.is_email_valid(data=data)
        self.is_password_valid(data=data)
        return True

    # use in is_body_valid
    @staticmethod
    def is_email_valid(data):
        """ Check if email is correct.

        Parameters
        ----------
        data : dict
            PostUserLogin's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(name=api.param_email, param=api.param_email, data=data)
        validator.is_string(param=api.param_email, value=data[api.param_email])
        validator.is_string_non_empty(param=api.param_email, value=data[api.param_email])
        return True

    # use in is_body_valid
    @staticmethod
    def is_password_valid(data):
        """ Check if password is correct.

        Parameters
        ----------
        data : dict
            PostUserLogin's body.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(name=api.param_password, param=api.param_password, data=data)
        validator.is_string(param=api.param_password, value=data[api.param_password])
        validator.is_string_non_empty(param=api.param_password, value=data[api.param_password])
        return True

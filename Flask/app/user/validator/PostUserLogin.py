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
            Body of PostUserLogin.

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
            Body of PostUserLogin.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        validator.is_mandatory(param=api.param_body_email, data=data)
        validator.is_string(param=api.param_body_email, value=data[api.param_body_email])
        validator.is_string_non_empty(param=api.param_body_email, value=data[api.param_body_email])
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
        validator.is_mandatory(param=api.param_body_password, data=data)
        validator.is_string(param=api.param_body_password, value=data[api.param_body_password])
        validator.is_string_non_empty(param=api.param_body_password, value=data[api.param_body_password])
        return True

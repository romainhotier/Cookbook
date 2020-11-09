from flask import abort

import utils

import app.user.factory.PostUserSignup as Factory
import app.user.model as user_model


api = Factory.Factory()


class Validator(object):
    """ Class to validate PostUserSignup's body.
    """

    def is_body_valid(self, data):
        """ Check if body is correct.

        Parameters
        ----------
        data : dict
            Body of PostUserSignup.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        self.is_display_name_valid(data)
        self.is_email_valid(data)
        self.is_password_valid(data)
        return True

    # use in is_body_valid
    @staticmethod
    def is_display_name_valid(data):
        """ Check if display_name is correct.

        Parameters
        ----------
        data : dict
            Body of PostUserSignup.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        utils.Validator.is_mandatory(param=api.param_display_name, data=data)
        utils.Validator.is_string(param=api.param_display_name, value=data[api.param_display_name])
        utils.Validator.is_string_non_empty(param=api.param_display_name, value=data[api.param_display_name])
        return True

    # use in is_body_valid
    def is_email_valid(self, data):
        """ Check if email is correct.

        Parameters
        ----------
        data : dict
            Body of PostUserSignup.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        utils.Validator.is_mandatory(param=api.param_email, data=data)
        utils.Validator.is_string(param=api.param_email, value=data[api.param_email])
        utils.Validator.is_string_non_empty(param=api.param_email, value=data[api.param_email])
        self.is_email_already_exist(data)
        return True

    # use in is_email_valid
    @staticmethod
    def is_email_already_exist(data):
        """ Check if email already exist.

        Parameters
        ----------
        data : dict
            Body of PostUserSignup.

        Returns
        -------
        Any
            Raise an "abort 400" if validation failed.
        """
        email = data[api.param_email]
        if user_model.User().check_user_is_unique(email=email):
            return False
        else:
            detail = utils.Server().format_detail(param=api.param_email, msg=utils.Server().detail_already_exist,
                                                  value=email)
            return abort(status=400, detail=detail)

    # use in is_body_valid
    @staticmethod
    def is_password_valid(data):
        """ Check if password is correct.

        Parameters
        ----------
        data : dict
            Body of PostUserSignup.

        Returns
        -------
        Any
            Response server if validation failed, True otherwise.
        """
        utils.Validator.is_mandatory(param=api.param_password, data=data)
        utils.Validator.is_string(param=api.param_password, value=data[api.param_password])
        utils.Validator.is_string_non_empty(param=api.param_password, value=data[api.param_password])
        return True

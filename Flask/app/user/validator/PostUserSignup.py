from flask import abort

import utils
import app.user as user_model


class Validator(object):

    def is_body_valid(self, data):
        self.is_display_name_valid(data)
        self.is_email_valid(data)
        self.is_password_valid(data)

    @staticmethod
    def is_display_name_valid(data):
        utils.Validator.is_mandatory(param="display_name", data=data)
        utils.Validator.is_string(param="display_name", value=data["display_name"])
        utils.Validator.is_string_non_empty(param="display_name", value=data["display_name"])
        return True

    def is_email_valid(self, data):
        utils.Validator.is_mandatory(param="email", data=data)
        utils.Validator.is_string(param="email", value=data["email"])
        utils.Validator.is_string_non_empty(param="email", value=data["email"])
        self.is_email_already_exist(data)
        return True

    @staticmethod
    def is_password_valid(data):
        utils.Validator.is_mandatory(param="password", data=data)
        utils.Validator.is_string(param="password", value=data["password"])
        utils.Validator.is_string_non_empty(param="password", value=data["password"])
        return True

    @staticmethod
    def is_email_already_exist(data):
        """ check name already exist """
        email = data["email"]
        result = user_model.UserModel.check_user_is_unique(email=email)
        if result == 0:
            return False
        else:
            detail = {"param": "email", "msg": utils.Server.detail_already_exist, "value": email}
            return abort(400, description=detail)

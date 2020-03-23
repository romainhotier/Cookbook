from flask import abort

from server import server as server, validator as validator
import app.user.user.model as user

server = server.Server()
validator = validator.Validator()
user = user.User()


class Validator(object):

    def is_body_valid(self, data):
        self.is_display_name_valid(data)
        self.is_email_valid(data)
        self.is_password_valid(data)

    @staticmethod
    def is_display_name_valid(data):
        validator.is_mandatory(param="display_name", data=data)
        validator.is_string(param="display_name", value=data["display_name"])
        validator.is_string_non_empty(param="display_name", value=data["display_name"])
        return True

    def is_email_valid(self, data):
        validator.is_mandatory(param="email", data=data)
        validator.is_string(param="email", value=data["email"])
        validator.is_string_non_empty(param="email", value=data["email"])
        self.is_email_already_exist(data)
        return True

    @staticmethod
    def is_password_valid(data):
        validator.is_mandatory(param="password", data=data)
        validator.is_string(param="password", value=data["password"])
        validator.is_string_non_empty(param="password", value=data["password"])
        return True

    @staticmethod
    def is_email_already_exist(data):
        """ check name already exist """
        email = data["email"]
        result_mongo = user.select_one_by_email(email=email)
        if result_mongo is None:
            return False
        else:
            detail = {"param": "email", "msg": server.detail_already_exist, "value": email}
            return abort(400, description=detail)

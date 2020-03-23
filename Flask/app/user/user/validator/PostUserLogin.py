from server import server as server, validator as validator
import app.user.user.model as user

server = server.Server()
validator = validator.Validator()
user = user.User()


class Validator(object):

    def is_body_valid(self, data):
        self.is_email_valid(data)
        self.is_password_valid(data)

    @staticmethod
    def is_email_valid(data):
        validator.is_mandatory(param="email", data=data)
        validator.is_string(param="email", value=data["email"])
        validator.is_string_non_empty(param="email", value=data["email"])
        return True

    @staticmethod
    def is_password_valid(data):
        validator.is_mandatory(param="password", data=data)
        validator.is_string(param="password", value=data["password"])
        validator.is_string_non_empty(param="password", value=data["password"])
        return True

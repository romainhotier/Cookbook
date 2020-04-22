import utils


class Validator(object):

    def is_body_valid(self, data):
        self.is_email_valid(data)
        self.is_password_valid(data)

    @staticmethod
    def is_email_valid(data):
        utils.Validator.is_mandatory(param="email", data=data)
        utils.Validator.is_string(param="email", value=data["email"])
        utils.Validator.is_string_non_empty(param="email", value=data["email"])
        return True

    @staticmethod
    def is_password_valid(data):
        utils.Validator.is_mandatory(param="password", data=data)
        utils.Validator.is_string(param="password", value=data["password"])
        utils.Validator.is_string_non_empty(param="password", value=data["password"])
        return True

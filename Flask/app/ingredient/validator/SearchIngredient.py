import utils


class Validator(object):

    @staticmethod
    def is_name_valid(name):
        utils.Validator.is_string(param="name", value=name)
        utils.Validator.is_string_non_empty(param="name", value=name)
        return True

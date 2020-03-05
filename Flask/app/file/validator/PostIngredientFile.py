from server import factory as factory, validator as validator

server = factory.Server()
validator = validator.Validator()


class Validator(object):

    def is_body_valid(self, data):
        self.is_path_valid(data)
        self.is_filename_valid(data)
        self.is_is_main_valid(data)

    @staticmethod
    def is_path_valid(data):
        validator.is_path_exist(param="path", value=data["path"])
        return True

    @staticmethod
    def is_filename_valid(data):
        validator.is_mandatory(param="filename", data=data)
        validator.is_string(param="filename", value=data["filename"])
        validator.is_string_non_empty(param="filename", value=data["filename"])
        return True

    @staticmethod
    def is_is_main_valid(data):
        if "is_main" in data.keys():
            validator.is_boolean(param="is_main", value=data["is_main"])
            return True

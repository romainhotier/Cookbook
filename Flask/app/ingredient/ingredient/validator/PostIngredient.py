from flask import abort

from server import factory as factory, validator as validator
import app.ingredient.ingredient.model as ingredient

server = factory.Server()
validator = validator.Validator()
ingredient = ingredient.Ingredient()


class Validator(object):

    @staticmethod
    def is_string_boolean(with_files):
        if with_files is None:
            return True, False
        else:
            validator.is_string(param="with_files", value=with_files)
            validator.is_in(param="with_files", value=with_files, values=["true", "false"])
            if with_files == "true":
                return True, True
            elif with_files == "false":
                return True, False

    def is_body_valid(self, data):
        self.is_name_valid(data)

    @staticmethod
    def is_name_valid(data):
        validator.is_mandatory(param="name", data=data)
        validator.is_string(param="name", value=data["name"])
        validator.is_string_non_empty(param="name", value=data["name"])
        return True

    @staticmethod
    def is_name_already_exist(data):
        """ check name already exist """
        name = data["name"]
        result_mongo = ingredient.select_one_by_name(name=name)
        if result_mongo.count() == 0:
            return False
        else:
            detail = {"param": "name", "msg": server.detail_already_exist, "value": name}
            return abort(400, description=detail)

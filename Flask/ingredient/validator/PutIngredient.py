from flask import abort

import factory as factory
import validator as validator
import ingredient.model as ingredient

server = factory.Server()
validator = validator.Validator()
ingredient = ingredient.Ingredient()


class Validator(object):

    @staticmethod
    def is_object_id(_id):
        validator.is_object_id(_id)
        return True

    def is_body_valid(self, data):
        self.is_name_valid(data)

    @staticmethod
    def is_name_valid(data):
        validator.is_mandatory("name", data)
        validator.is_string("name", data["name"])
        validator.is_string_non_empty("name", data["name"])
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

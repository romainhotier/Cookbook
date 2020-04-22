from flask import abort

import utils
import app.ingredient as ingredient_model


class Validator(object):

    @staticmethod
    def is_string_boolean(with_files):
        if with_files is None:
            return True, False
        else:
            utils.Validator.is_string(param="with_files", value=with_files)
            utils.Validator.is_in(param="with_files", value=with_files, values=["true", "false"])
            if with_files == "true":
                return True, True
            elif with_files == "false":
                return True, False

    def is_body_valid(self, data):
        self.is_name_valid(data)

    def is_name_valid(self, data):
        utils.Validator.is_mandatory(param="name", data=data)
        utils.Validator.is_string(param="name", value=data["name"])
        utils.Validator.is_string_non_empty(param="name", value=data["name"])
        self.is_name_already_exist(data)
        return True

    @staticmethod
    def is_name_already_exist(data):
        """ check name already exist """
        name = data["name"]
        result = ingredient_model.IngredientModel.check_ingredient_is_unique(name=name)
        if result == 0:
            return False
        else:
            detail = {"param": "name", "msg": utils.Server.detail_already_exist, "value": name}
            return abort(400, description=detail)

import jsonschema
import copy

import utils


class PostIngredient(object):

    def __init__(self):
        self.url = 'ingredient'
        self.param_name = "name"
        self.param_slug = "slug"
        self.param_categories = "categories"
        self.rep_code_msg_created = utils.Server.rep_code_msg_created.replace("xxx", "ingredient")
        self.rep_code_msg_error_400 = utils.Server.rep_code_msg_error_400.replace("xxx", "ingredient")
        self.rep_code_msg_error_404_url = utils.Server.rep_code_msg_error_404.replace("xxx", "cookbook")

    @staticmethod
    def create_detail(param, msg, **kwargs):
        detail = {"param": param, "msg": msg}
        if "value" in kwargs:
            detail["value"] = kwargs["value"]
        return detail

    def custom_body(self, body):
        data = copy.deepcopy(body)
        if self.param_categories not in body.keys():
            data["categories"] = []
        return data

    @staticmethod
    def create_schema(ingredient):
        return {"type": "object",
                "properties": {
                    "_id": {"type": "string"},
                    "name": {"enum": [ingredient.name]},
                    "slug": {"enum": [ingredient.slug]},
                    "categories": {"enum": [ingredient.categories]}},
                "required": ["_id", "name", "slug", "categories"],
                "additionalProperties": False}

    def json_check(self, data, data_expected):
        try:
            jsonschema.validate(instance=data, schema=self.create_schema(ingredient=data_expected))
            return {"result": True, "error": None}
        except jsonschema.exceptions.ValidationError as err:
            return {"result": False, "error": err}

    @staticmethod
    def check_not_present(value, rep):
        if value in rep.keys():
            return False
        else:
            return True


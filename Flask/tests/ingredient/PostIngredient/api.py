import jsonschema
import copy

import utils

server = utils.Server()


class PostIngredient(object):

    def __init__(self):
        self.url = 'ingredient'
        self.param_name = "name"
        self.param_slug = "slug"
        self.param_categories = "categories"
        self.param_nutriments = "nutriments"
        self.param_calories = "calories"
        self.param_carbohydrates = "carbohydrates"
        self.param_fats = "fats"
        self.param_proteins = "proteins"
        self.param_info = "info"
        self.rep_code_msg_created = server.rep_code_msg_created.replace("xxx", "ingredient")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "ingredient")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")

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
        if self.param_nutriments not in body.keys():
            data["nutriments"] = {self.param_calories: "0",
                                  self.param_carbohydrates: "0",
                                  self.param_fats: "0",
                                  self.param_proteins: "0",
                                  self.param_info: "per 100g"}
        return data

    @staticmethod
    def create_schema(ingredient):
        return {"type": "object",
                "properties": {
                    "_id": {"type": "string"},
                    "name": {"enum": [ingredient.name]},
                    "slug": {"enum": [ingredient.slug]},
                    "categories": {"enum": [ingredient.categories]},
                    "nutriments": {"enum": [ingredient.nutriments]}},
                "required": ["_id", "name", "slug", "categories", "nutriments"],
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


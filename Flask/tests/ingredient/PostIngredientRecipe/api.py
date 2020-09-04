import jsonschema

import utils


class PostIngredientRecipe(object):

    def __init__(self):
        self.url = 'ingredient/recipe'
        self.param_id_recipe = "_id_recipe"
        self.param_id_ingredient = "_id_ingredient"
        self.param_quantity = "quantity"
        self.param_unit = "unit"
        self.rep_code_msg_created = utils.Server.rep_code_msg_created.replace("xxx", "ingredient")
        self.rep_code_msg_error_400 = utils.Server.rep_code_msg_error_400.replace("xxx", "ingredient")
        self.rep_code_msg_error_404_url = utils.Server.rep_code_msg_error_404.replace("xxx", "cookbook")

    @staticmethod
    def create_detail(param, msg, **kwargs):
        detail = {"param": param, "msg": msg}
        if "value" in kwargs:
            detail["value"] = kwargs["value"]
        return detail

    @staticmethod
    def create_schema(link):
        return {"type": "object",
                "properties": {
                    "_id": {"type": "string"},
                    "quantity": {"enum": [link.quantity]},
                    "unit": {"enum": [link.unit]},
                    "_id_ingredient": {"enum": [link.get_id_ingredient()]},
                    "_id_recipe": {"enum": [link.get_id_recipe()]}},
                "required": ["_id", "quantity", "unit", "_id_ingredient", "_id_recipe"],
                "additionalProperties": False}

    def json_check(self, data, data_expected):
        try:
            jsonschema.validate(instance=data, schema=self.create_schema(link=data_expected))
            return {"result": True, "error": None}
        except jsonschema.exceptions.ValidationError as err:
            return {"result": False, "error": err}

    @staticmethod
    def check_not_present(value, rep):
        if value in rep.keys():
            return False
        else:
            return True

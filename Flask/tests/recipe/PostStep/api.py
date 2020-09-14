import jsonschema
import utils


class PostStep(object):

    def __init__(self):
        self.url = 'recipe/step'
        self.param_step = "step"
        self.rep_code_msg_created = utils.Server.rep_code_msg_created.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = utils.Server.rep_code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_405 = utils.Server.rep_code_msg_error_405.replace("xxx", "cookbook")

    @staticmethod
    def create_detail(param, msg, **kwargs):
        detail = {"param": param, "msg": msg}
        if "value" in kwargs:
            detail["value"] = kwargs["value"]
        return detail

    @staticmethod
    def check_not_present(value, rep):
        if value in rep.keys():
            return False
        else:
            return True

    def create_schema(self, body):
        return {"type": "object",
                "properties": {
                    "_id": {"type": "string"},
                    "step": {"enum": [body[self.param_step]]}},
                "required": ["_id", "step"],
                "additionalProperties": False}

    def json_check(self, data, data_expected):
        try:
            jsonschema.validate(instance=data, schema=self.create_schema(body=data_expected))
            return {"result": True, "error": None}
        except jsonschema.exceptions.ValidationError as err:
            return {"result": False, "error": err}

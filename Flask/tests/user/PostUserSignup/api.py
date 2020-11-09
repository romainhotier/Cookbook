import jsonschema

import utils


class PostUserSignup(object):

    def __init__(self):
        self.url = 'user/signup'
        self.param_display_name = "display_name"
        self.param_email = "email"
        self.param_password = "password"
        self.rep_code_msg_created = utils.Server().rep_code_msg_created.replace("xxx", "user")
        self.rep_code_msg_error_400 = utils.Server().rep_code_msg_error_400.replace("xxx", "user")
        self.rep_code_msg_error_404_url = utils.Server().rep_code_msg_error_404.replace("xxx", "cookbook")

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

    @staticmethod
    def create_schema(user):
        return {"type": "object",
                "properties": {
                    "_id": {"type": "string"},
                    "display_name": {"enum": [user.display_name]},
                    "email": {"enum": [user.email]}},
                "required": ["_id", "display_name", "email"],
                "additionalProperties": False}

    def json_check(self, data, data_expected):
        try:
            jsonschema.validate(instance=data, schema=self.create_schema(user=data_expected))
            return {"result": True, "error": None}
        except jsonschema.exceptions.ValidationError as err:
            return {"result": False, "error": err}

import jsonschema
import copy
from bson import ObjectId

import utils


class PostRecipeStep(object):

    def __init__(self):
        self.url = 'recipe/step'
        self.param_id = "_id"
        self.param_with_files = "with_files"
        self.param_step = "step"
        self.param_position = "position"
        self.rep_code_msg_created = utils.Server.rep_code_msg_created.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = utils.Server.rep_code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_404_url = utils.Server.rep_code_msg_error_404.replace("xxx", "cookbook")

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

    def custom_steps(self, recipe, body, rep):
        steps = copy.deepcopy(recipe.steps)
        if self.param_position in body.keys():
            new_id = self.get_new_id(data=rep["data"], position=body[self.param_position])
            steps.insert(body[self.param_position], {"_id": ObjectId(new_id), "step": body[self.param_step]})
        else:
            new_id = rep["data"]["steps"][-1]["_id"]
            steps.append({"_id": ObjectId(new_id), "step": body[self.param_step]})
        return {"steps": steps}

    @staticmethod
    def create_schema(recipe):
        return {"type": "object",
                "properties": {
                    "_id": {"type": "string"},
                    "categories": {"enum": [recipe.categories]},
                    "cooking_time": {"enum": [recipe.cooking_time]},
                    "level": {"enum": [recipe.level]},
                    "nb_people": {"enum": [recipe.nb_people]},
                    "note": {"enum": [recipe.note]},
                    "preparation_time": {"enum": [recipe.preparation_time]},
                    "resume": {"enum": [recipe.resume]},
                    "slug": {"enum": [recipe.slug]},
                    "steps": {"enum": [recipe.get_steps_stringify()]},
                    "title": {"enum": [recipe.title]}},
                "required": ["_id", "categories", "cooking_time", "level", "nb_people", "note", "preparation_time",
                             "resume", "slug", "steps", "title"],
                "additionalProperties": False}

    def json_check(self, data, data_expected):
        try:
            jsonschema.validate(instance=data, schema=self.create_schema(recipe=data_expected))
            return {"result": True, "error": None}
        except jsonschema.exceptions.ValidationError as err:
            return {"result": False, "error": err}

    @staticmethod
    def get_new_id(data, position):
        return data["steps"][position]["_id"]

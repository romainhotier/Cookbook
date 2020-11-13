import copy
from bson import ObjectId

import utils

server = utils.Server()


class PostRecipeStep(object):

    def __init__(self):
        self.url = 'recipe/step'
        self.param_id_recipe = "_id_recipe"
        self.param_with_files = "with_files"
        self.param_description = "description"
        self.param_position = "position"
        self.rep_code_msg_created = server.rep_code_msg_created.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")

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
            steps.insert(body[self.param_position], {"_id": ObjectId(new_id), "description": body[self.param_description]})
        else:
            new_id = rep["data"]["steps"][-1]["_id"]
            steps.append({"_id": ObjectId(new_id), "description": body[self.param_description]})
        return {"steps": steps}

    @staticmethod
    def data_expected(recipe):
        data_expected = recipe.get_stringify()
        return data_expected

    @staticmethod
    def get_new_id(data, position):
        return data["steps"][position]["_id"]

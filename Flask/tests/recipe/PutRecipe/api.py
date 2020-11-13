
import utils

server = utils.Server()

class PutRecipe(object):

    def __init__(self):
        self.url = 'recipe'
        self.param_id = "_id"
        self.param_with_files = "with_files"
        self.param_title = "title"
        self.param_slug = "slug"
        self.param_level = "level"
        self.param_resume = "resume"
        self.param_cooking_time = "cooking_time"
        self.param_preparation_time = "preparation_time"
        self.param_nb_people = "nb_people"
        self.param_note = "note"
        self.param_categories = "categories"
        self.param_steps = "steps"
        self.param_ingredients = "ingredients"
        self.rep_code_msg_ok = server.rep_code_msg_ok.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")
        self.detail_param = "param"
        self.detail_msg = "msg"
        self.detail_value = "value"

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
    def data_expected(recipe, **kwargs):
        if "files" in kwargs.keys():
            data_expected = recipe.get_stringify_with_file(files_recipe=kwargs["files"]["recipe"],
                                                           files_steps=kwargs["files"]["steps"])
        else:
            data_expected = recipe.get_stringify()
        return data_expected

import utils


class GetRecipe(object):

    def __init__(self):
        self.url = 'recipe'
        self.param_slug = "slug"
        self.param_with_files = "with_files"
        self.rep_code_msg_ok = utils.Server.rep_code_msg_ok.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = utils.Server.rep_code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_404_url = utils.Server.rep_code_msg_error_404.replace("xxx", "cookbook")

    @staticmethod
    def create_detail(param, msg, **kwargs):
        detail = {"param": param, "msg": msg}
        if "value" in kwargs:
            detail["value"] = kwargs["value"]
        return detail

    @staticmethod
    def data_expected(recipe, **kwargs):
        if "files" in kwargs.keys():
            data_expected = recipe.get_stringify_with_file(files_recipe=kwargs["files"]["recipe"],
                                                           files_steps=kwargs["files"]["steps"])
        else:
            data_expected = recipe.get_stringify()
        return data_expected

    @staticmethod
    def check_not_present(value, rep):
        if value in rep.keys():
            return False
        else:
            return True

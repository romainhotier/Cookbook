import utils


class GetIngredientForRecipe(object):

    def __init__(self):
        self.url1 = 'recipe'
        self.url2 = 'ingredient'
        self.param_id_recipe = "_id_recipe"
        self.param_with_name = "with_name"
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
    def data_expected(link, **kwargs):
        if "names" in kwargs.keys():
            data_expected = link.add_name().get_stringify()
        else:
            data_expected = link.get_stringify()
        return data_expected

    @staticmethod
    def check_not_present(value, rep):
        if value in rep.keys():
            return False
        else:
            return True

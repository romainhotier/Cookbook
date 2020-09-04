import utils


class GetRecipeForIngredient(object):

    def __init__(self):
        self.url1 = 'ingredient'
        self.url2 = 'recipe'
        self.param_id_ingredient = "_id_ingredient"
        self.param_with_title = "with_title"
        self.rep_code_msg_ok = utils.Server.rep_code_msg_ok.replace("xxx", "ingredient")
        self.rep_code_msg_error_400 = utils.Server.rep_code_msg_error_400.replace("xxx", "ingredient")
        self.rep_code_msg_error_404_url = utils.Server.rep_code_msg_error_404.replace("xxx", "cookbook")

    @staticmethod
    def create_detail(param, msg, **kwargs):
        detail = {"param": param, "msg": msg}
        if "value" in kwargs:
            detail["value"] = kwargs["value"]
        return detail

    @staticmethod
    def data_expected(link, **kwargs):
        if "title" in kwargs.keys():
            data_expected = link.add_title().get_stringify()
        else:
            data_expected = link.get_stringify()
        return data_expected

import utils

server = utils.Server()


class GetRecipeForIngredient(object):

    def __init__(self):
        self.url1 = 'ingredient'
        self.url2 = 'recipe'
        self.param_id_ingredient = "_id_ingredient"
        self.param_with_titles = "with_titles"
        self.rep_code_msg_ok = server.rep_code_msg_ok.replace("xxx", "ingredient")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "ingredient")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")

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

    @staticmethod
    def check_not_present(value, rep):
        if value in rep.keys():
            return False
        else:
            return True

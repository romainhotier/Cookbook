import utils

server = utils.Server()


class PutIngredientRecipe(object):

    def __init__(self):
        self.url = 'ingredient/recipe'
        self.param_id = "_id"
        self.param_quantity = "quantity"
        self.param_unit = "unit"
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
    def data_expected(link):
        return link.get_stringify()

    @staticmethod
    def check_not_present(value, rep):
        if value in rep.keys():
            return False
        else:
            return True

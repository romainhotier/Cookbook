import utils


class DeleteIngredient(object):

    def __init__(self):
        self.url = 'ingredient'
        self.param_id = "_id"
        self.rep_code_msg_error_400 = utils.Server.rep_code_msg_error_400.replace("xxx", "ingredient")
        self.rep_code_msg_error_404_url = utils.Server.rep_code_msg_error_404.replace("xxx", "cookbook")

    @staticmethod
    def create_detail(param, msg, **kwargs):
        detail = {"param": param, "msg": msg}
        if "value" in kwargs:
            detail["value"] = kwargs["value"]
        return detail

    @staticmethod
    def check_no_data(rep):
        if "data" in rep.keys():
            return False
        else:
            return True

import utils


class PostUserLogin(object):

    def __init__(self):
        self.url = 'user/login'
        self.param_email = "email"
        self.param_password = "password"
        self.rep_code_msg_ok = utils.Server().rep_code_msg_ok.replace("xxx", "user")
        self.rep_code_msg_error_400 = utils.Server().rep_code_msg_error_400.replace("xxx", "user")
        self.rep_code_msg_error_404_url = utils.Server().rep_code_msg_error_404.replace("xxx", "cookbook")
        self.data_regex = "[A-Za-z0-9\-\._~\+\/]+=*"

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

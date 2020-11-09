import utils


class GetMe(object):

    def __init__(self):
        self.url = 'user/me'
        self.rep_code_msg_ok = utils.Server().rep_code_msg_ok.replace("xxx", "user")
        self.rep_code_msg_error_401 = utils.Server().rep_code_msg_error_401.replace("xxx", "cookbook")

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
    def data_expected(user):
        return {'_id': user.get_id(),
                'display_name': user.display_name,
                'email': user.email,
                'status': user.status}

import utils


class PostUserLogin(object):

    def __init__(self):
        self.url = 'user/login'
        self.param_email = "email"
        self.param_password = "password"
        self.rep_code_status = 'codeStatus'
        self.rep_code_msg = 'codeMsg'
        self.rep_data = 'data'
        self.rep_detail = 'detail'
        self.rep_code_msg_ok = utils.Server.rep_code_msg_ok.replace("xxx", "user")
        self.rep_code_msg_error_400 = utils.Server.rep_code_msg_error_400.replace("xxx", "user")
        self.rep_code_msg_error_404_url = utils.Server.rep_code_msg_error_404.replace("xxx", "cookbook")
        self.detail_param = "param"
        self.detail_msg = "msg"
        self.detail_value = "value"
        self.data_regex = '[A-Za-z0-9\-\._~\+\/]+=*'

    def create_detail(self, param, msg, value):
        detail = {self.detail_param: param, self.detail_msg: msg}
        if value != "missing":
            detail[self.detail_value] = value
        return detail

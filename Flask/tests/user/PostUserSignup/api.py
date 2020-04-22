import copy

import utils


class PostUserSignup(object):

    def __init__(self):
        self.url = 'user/signup'
        self.param_display_name = "display_name"
        self.param_email = "email"
        self.param_password = "password"
        self.rep_code_status = 'codeStatus'
        self.rep_code_msg = 'codeMsg'
        self.rep_data = 'data'
        self.rep_detail = 'detail'
        self.rep_code_msg_created = utils.Server.rep_code_msg_created.replace("xxx", "user")
        self.rep_code_msg_error_400 = utils.Server.rep_code_msg_error_400.replace("xxx", "user")
        self.rep_code_msg_error_404_url = utils.Server.rep_code_msg_error_404.replace("xxx", "cookbook")
        self.detail_param = "param"
        self.detail_msg = "msg"
        self.detail_value = "value"

    def create_detail(self, param, msg, value):
        detail = {self.detail_param: param, self.detail_msg: msg}
        if value != "missing":
            detail[self.detail_value] = value
        return detail

    @staticmethod
    def format_response(data):
        format_response = copy.deepcopy(data)
        format_response.pop("_id")
        return format_response

    @staticmethod
    def format_data(user):
        format_data = copy.deepcopy(user.get_without_id())
        format_data.pop("password")
        return format_data

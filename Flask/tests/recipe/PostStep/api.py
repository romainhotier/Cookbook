import copy

import utils


class PostStep(object):

    def __init__(self):
        self.url = 'recipe/step'
        self.param_step = "step"
        self.rep_code_status = 'codeStatus'
        self.rep_code_msg = 'codeMsg'
        self.rep_data = 'data'
        self.rep_detail = 'detail'
        self.rep_code_msg_created = utils.Server.rep_code_msg_created.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = utils.Server.rep_code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_405 = utils.Server.rep_code_msg_error_405.replace("xxx", "cookbook")
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
        return {"step": data["step"]}

    @staticmethod
    def format_data(data):
        format_data = copy.deepcopy(data)
        format_data.pop("_id")
        return format_data

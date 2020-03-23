import copy

import server.server as server

server = server.Server()


class PostStep(object):

    def __init__(self):
        self.url = 'step'
        self.param_step = "step"
        self.rep_code_status = 'codeStatus'
        self.rep_code_msg = 'codeMsg'
        self.rep_data = 'data'
        self.rep_detail = 'detail'
        self.rep_code_msg_created = server.rep_code_msg_created.replace("xxx", "step")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "step")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")
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

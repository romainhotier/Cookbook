import copy
from bson import ObjectId

from server import factory as factory

server = factory.Server()


class PostIngredientFile(object):

    def __init__(self):
        self.url = 'file/ingredient'
        self.param_id = "_id"
        self.param_path = "path"
        self.param_filename = "filename"
        self.param_is_main = "is_main"
        self.rep_code_status = 'codeStatus'
        self.rep_code_msg = 'codeMsg'
        self.rep_data = 'data'
        self.rep_detail = 'detail'
        self.rep_code_msg_created = server.rep_code_msg_created.replace("xxx", "file_ingredient")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "file_ingredient")
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
        format_response = copy.deepcopy(data)
        for file in format_response["files"]:
            file["_id"] = ""
        return format_response

    @staticmethod
    def refacto_file_added(data, position):
        data["files"][position]["_id"] = ''
        return data

    @staticmethod
    def return_new_file_id(response):
        return response["detail"].split(": ")[1]

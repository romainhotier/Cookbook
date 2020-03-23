import copy
import os
import platform

import server.server as server

server = server.Server()


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
        self.rep_code_msg_created = server.rep_code_msg_created.replace("xxx", "file")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "file")
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
    def format_response(data, position):
        format_response = copy.deepcopy(data)
        format_response["files"][position]["_id"] = ""
        return format_response

    @staticmethod
    def refacto_file_added(data, position):
        data["files"][position]["_id"] = ''
        return data

    @staticmethod
    def return_new_file_id(response):
        return response["detail"].split(": ")[1]

    @staticmethod
    def get_file_path_for_test():
        current_path = os.getcwd()
        if platform.system() == "Windows":
            if current_path.split('\\')[-1] == "PostIngredientFile":
                default_path = current_path.replace("file\\test\\PostIngredientFile", "_file_exemple\\text.txt")
                return default_path
            elif current_path.split('\\')[-1] == "Flask":
                default_path = current_path + "\\app\\file\\_file_exemple\\text.txt"
                return default_path
        elif platform.system() in ["Linux", "Darwin"]:
            if current_path.split('/')[-1] == "PostIngredientFile":
                default_path = current_path.replace("file/test/PostIngredientFile", "_file_exemple/text.txt")
                return default_path
            elif current_path.split('/')[-1] == "Flask":
                default_path = current_path + "/app/file/_file_exemple/text.txt"
                return default_path

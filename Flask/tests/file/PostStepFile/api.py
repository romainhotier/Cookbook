import os
import platform
from bson import ObjectId

import utils


class PostStepFile(object):

    def __init__(self):
        self.url1 = 'file/recipe'
        self.url2 = 'step'
        self.param_id_recipe = "_id_recipe"
        self.param_id_step = "_id_step"
        self.param_path = "path"
        self.param_filename = "filename"
        self.param_is_main = "is_main"
        self.rep_code_msg_created = utils.Server.rep_code_msg_created.replace("xxx", "file")
        self.rep_code_msg_error_400 = utils.Server.rep_code_msg_error_400.replace("xxx", "file")
        self.rep_code_msg_error_404_url = utils.Server.rep_code_msg_error_404.replace("xxx", "cookbook")

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
    def data_expected(recipe, files, index):
        data_expected = recipe.get_stringify()
        data_expected["files"] = []
        for s in data_expected["steps"]:
            s["files"] = []
        data_expected["steps"][index]["files"] = [{"_id": f.get_id(), "is_main": f.get_is_main()} for f in files]
        return data_expected

    @staticmethod
    def detail_expected(new_id):
        return "added file ObjectId: {0}".format(str(new_id))

    @staticmethod
    def return_new_file_id(response):
        return ObjectId(response["detail"].split(": ")[1])

    @staticmethod
    def get_file_path_for_test():
        current_path = os.getcwd()
        if platform.system() == "Windows":
            if current_path.split('\\')[-1] == "PostStepFile":
                default_path = current_path.replace("PostStepFile", "_file_exemple\\text.txt")
                return default_path
            elif current_path.split('\\')[-1] == "Flask":
                default_path = current_path + "\\tests\\file\\_file_exemple\\text.txt"
                return default_path
        elif platform.system() in ["Linux", "Darwin"]:
            if current_path.split('/')[-1] == "PostStepFile":
                default_path = current_path.replace("PostStepFile", "_file_exemple/text.txt")
                return default_path
            elif current_path.split('/')[-1] == "Flask":
                default_path = current_path + "/tests/file/_file_exemple/text.txt"
                return default_path

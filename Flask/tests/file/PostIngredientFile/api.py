import os
import platform
from bson import ObjectId


import utils

server = utils.Server()


class PostIngredientFile(object):
    """ Class to test PostIngredientFile.
    """

    def __init__(self):
        self.url = 'file/ingredient'
        self.param_id = "_id"
        self.param_is_main = "is_main"
        self.param_filename = "filename"
        self.param_path = "path"
        self.rep_code_msg_created = server.rep_code_msg_created.replace("xxx", "file")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "file")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")

    @staticmethod
    def create_detail(param, msg, **kwargs):
        """ Format Server's detail response.

        Parameters
        ----------
        param : str
            Tested parameter.
        msg : str
            Server's message.
        kwargs : str
            Value if one existed.

        Returns
        -------
        dict
            Server's detail response.
        """
        detail = {"param": param, "msg": msg}
        if "value" in kwargs:
            detail["value"] = kwargs["value"]
        return detail

    @staticmethod
    def check_not_present(value, rep):
        """ Check if data/detail is not present in Server's response.

        Parameters
        ----------
        value : str
            Tested value.
        rep : dict
            Server's response.

        Returns
        -------
        bool
        """
        if value in rep:
            return False
        else:
            return True

    @staticmethod
    def data_expected(new_id):
        """ Format data's response.

        Parameters
        ----------
        new_id : str
            New File's ObjectId.

        Returns
        -------
        str
            Data's response.
        """
        return "added file ObjectId: {0}".format(str(new_id))

    @staticmethod
    def return_new_file_id(response):
        """ Format detail's response.

        Parameters
        ----------
        response : dict
            Server's response.

        Returns
        -------
        str
            File's ObjectId.
        """
        return ObjectId(response["data"].split(": ")[1])

    @staticmethod
    def get_file_path_for_test():
        """ Get file's path.

        Returns
        -------
        str
            Path according to the system.
        """
        current_path = os.getcwd()
        if platform.system() == "Windows":
            if current_path.split('\\')[-1] == "PostIngredientFile":
                default_path = current_path.replace("PostIngredientFile", "_file_exemple\\text.txt")
                return default_path
            elif current_path.split('\\')[-1] == "Flask":
                default_path = current_path + "\\tests\\file\\_file_exemple\\text.txt"
                return default_path
        elif platform.system() in ["Linux", "Darwin"]:
            if current_path.split('/')[-1] == "PostIngredientFile":
                default_path = current_path.replace("PostIngredientFile", "_file_exemple/text.txt")
                return default_path
            elif current_path.split('/')[-1] == "Flask":
                default_path = current_path + "/tests/file/_file_exemple/text.txt"
                return default_path

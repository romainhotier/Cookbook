import os
import platform
from bson import ObjectId

import utils


class PostStepFile(object):
    """ Class to test PostStepFile.
    """

    def __init__(self):
        self.url1 = 'file/recipe'
        self.url2 = 'step'
        self.param_id_recipe = "_id_recipe"
        self.param_id_step = "_id_step"
        self.param_path = "path"
        self.param_filename = "filename"
        self.param_is_main = "is_main"
        self.rep_code_msg_created = utils.Server().rep_code_msg_created.replace("xxx", "file")
        self.rep_code_msg_error_400 = utils.Server().rep_code_msg_error_400.replace("xxx", "file")
        self.rep_code_msg_error_404_url = utils.Server().rep_code_msg_error_404.replace("xxx", "cookbook")

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
        if value in rep.keys():
            return False
        else:
            return True

    @staticmethod
    def data_expected(recipe, files, index):
        """ Format data's response.

        Parameters
        ----------
        recipe : Any
            RecipeTest.
        files : Array
            FileTests.
        index : int
            Step's position.

        Returns
        -------
        str
            Data's response.
        """
        data_expected = recipe.get_stringify()
        data_expected["files"] = []
        for step in data_expected["steps"]:
            step["files"] = []
        data_expected["steps"][index]["files"] = [{"_id": f.get_id(), "is_main": f.get_is_main()} for f in files]
        return data_expected

    @staticmethod
    def detail_expected(new_id):
        """ Format detail's response.

        Parameters
        ----------
        new_id : str
            New File's ObjectId.

        Returns
        -------
        str
            Detail's response.
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
        return ObjectId(response["detail"].split(": ")[1])

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

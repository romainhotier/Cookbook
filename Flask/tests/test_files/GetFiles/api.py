import os
import platform

import utils

server = utils.Server()


class GetFiles(object):
    """ Class to test GetFiles.
    """

    def __init__(self):
        self.url = 'files'
        self.param_path = "path"
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "files")
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
        if value in rep.keys():
            return False
        else:
            return True

    def get_files_path_for_test(self):
        """ Get file's path.

        Returns
        -------
        list
            Path according to the system, len 3.
        """
        current_path = self.convert_to_unix_path(os.getcwd())
        default_path = ""
        for p in current_path.split('/'):
            if p == "Flask":
                default_path += p + "/"
                break
            else:
                default_path += p + "/"
        test_paths = [default_path + "tests/test_files/_file_exemple/text.txt",
                      default_path + "tests/test_files/_file_exemple/image.png",
                      default_path + "tests/test_files/_file_exemple/image2.jpeg"]
        if platform.system() == "Windows":
            return self.convert_to_windows_path(paths=test_paths)
        elif platform.system() in ["Linux", "Darwin"]:
            return test_paths

    @staticmethod
    def convert_to_windows_path(paths):
        """ Get path to windows's paths.

        Parameters
        ----------
        paths : list
            Path to be converted.

        Returns
        -------
        list
            replace / by \\.
        """
        return [path.replace('/', '\\') for path in paths]

    @staticmethod
    def convert_to_unix_path(path):
        """ Get path to windows's path.

        Parameters
        ----------
        path : str
            Path to be converted.

        Returns
        -------
        str
            replace \\ by /.
        """
        return path.replace('\\', '/')

    # @staticmethod
    # def data_expected(new_id):
    #     """ Format data's response.
    #
    #     Parameters
    #     ----------
    #     new_id : str
    #         New File's ObjectId.
    #
    #     Returns
    #     -------
    #     str
    #         Data's response.
    #     """
    #     return "added file ObjectId: {0}".format(str(new_id))
    #
    # @staticmethod
    # def return_new_file_id(response):
    #     """ Format detail's response.
    #
    #     Parameters
    #     ----------
    #     response : dict
    #         Server's response.
    #
    #     Returns
    #     -------
    #     str
    #         File's ObjectId.
    #     """
    #     return ObjectId(response["data"].split(": ")[1])

import os
import platform
import mimetypes

import utils

server = utils.Server()


class PostRecipeFiles(object):
    """ Class to test PostRecipeFiles.
    """

    def __init__(self):
        self.url = 'files/recipe'
        self.param_id = "_id"
        self.rep_code_msg_created = server.rep_code_msg_created.replace("xxx", "files")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "files")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")

    @staticmethod
    def get_file_name(path):
        """ Get filename from path.

        Parameters
        ----------
        path : str
            File path.

        Returns
        -------
        str
            Filename.
        """
        return path.split("/")[-1]

    @staticmethod
    def get_file_mimetype(path):
        """ Get mimetype from path.

        Parameters
        ----------
        path : str
            File path.

        Returns
        -------
        str
            mimetype.
        """
        return mimetypes.guess_type(url=path)[0]

    def format_files_multipart(self, paths):
        """ Return Multipart/form_data and opened files.

        Parameters
        ----------
        paths : list
            File path.

        Returns
        -------
        tuple
            multipart, files_open
        """
        files_open = []
        multipart = []
        for path in paths:
            f = open(path, 'rb')
            files_open.append(f)
            multipart.append(('files', (self.get_file_name(path), f, self.get_file_mimetype(path))))
        return multipart, files_open

    @staticmethod
    def close_files(files_open):
        """ Close open files.

        Parameters
        ----------
        files_open : list
            FilesTest.
        """
        for f in files_open:
            f.close()

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

    def data_expected(self, recipe_id, file_paths):
        """ Format data's response.

        Parameters
        ----------
        recipe_id : str
            Recipe's ObjectId
        file_paths : list
            New File's path.

        Returns
        -------
        str
            Data's response.
        """
        return ["recipe/{}/{}".format(recipe_id, self.get_file_name(path)) for path in file_paths]

    def get_files_path_for_test(self):
        """ Get file's path.

        Returns
        -------
        list
            Path according to the system, len 3 here.
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

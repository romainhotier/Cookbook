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
        self.rep_code_msg_error_405 = server.rep_code_msg_error_405.replace("xxx", "cookbook")

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

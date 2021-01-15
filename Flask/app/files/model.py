import os.path

import utils


class Files(object):

    @staticmethod
    def delete(path):
        """ Insert a File.

        Parameters
        ----------
        path : str
            File's path.

        """
        try:
            os.remove(utils.Server().path_file_storage + path)
        except FileNotFoundError:
            pass

    @staticmethod
    def check_exist(path):
        """ Check if File exist.

        Parameters
        ----------
        path : str
            File's path.

        """
        return os.path.exists(utils.Server().path_file_storage + path)

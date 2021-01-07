import os

import utils


class Files(object):

    @staticmethod
    def delete(path):
        """ Insert a FileMongo.

        Parameters
        ----------
        path : str
            File's path.

        """
        try:
            os.remove(utils.Server().path_file_storage + path)
        except FileNotFoundError:
            pass

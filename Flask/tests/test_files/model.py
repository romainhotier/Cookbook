import os
import shutil

import utils


class FilesTest(object):

    def __init__(self):
        """ FileTest model.

        - origin = origin path (test folder)
        - kind = can be recipe/step/ingredient
        - id = Parent's ObjectId
        - path = path for download
        """
        self.origin = ""
        self.kind = ""
        self.id = ""
        self.path = ""

    def set_short_path(self, kind, _id, path):
        """ Set all informations needed for file exploitation.

        Parameters
        ----------
        kind : str
            can be recipe/step/ingredient.
        _id : str
            ObjectId.
        path : str
            path system of the file.

        Returns
        -------
        FilesTest
            File information.
        """
        self.origin = path
        self.kind = kind
        self.id = _id
        self.path = "{0}/{1}/{2}".format(kind, _id, path.split("/")[-1])
        return self

    def display(self):
        """ Print FileTest model.

        Returns
        -------
        dict
            Display FileTest.
        """
        print(self.__dict__)

    def insert(self):
        """ Copy FileTest to filestorage repo.

        Returns
        -------
        FilesTest
            File copied.
        """
        utils.Server().check_file_storage_folder(kind=self.kind, _id=self.id)
        shutil.copyfile(self.origin, utils.Server().path_file_storage + "/" + self.path)
        return self

    def check_file_exist(self):
        """ Check if file exist.

        Returns
        -------
        bool
            True if exist, False otherwise.
        """
        path = utils.Server().path_file_storage + self.path
        assert os.path.exists(path)

    def check_file_not_exist(self):
        """ Check if file exist.

        Returns
        -------
        bool
            True if exist, False otherwise.
        """
        path = utils.Server().path_file_storage + self.path
        assert os.path.exists(path) is False

    @staticmethod
    def clean():
        """ Clean FilesTest repository.
        """
        shutil.rmtree(path=utils.Server().path_file_storage+"/", ignore_errors=True)
        return

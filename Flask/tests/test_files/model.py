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

    def set_path(self, kind, _id, path):
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
        """ Copy FileTest to filestorage.

        Returns
        -------
        FilesTest
            File copied.
        """
        self.check_save_folder(kind=self.kind, _id=self.id)
        shutil.copyfile(self.origin, utils.Server().path_file_storage + "/" + self.path)
        return self

    # use in insert
    def check_save_folder(self, kind, _id):
        """ Check/Create if folder exist.

        Parameters
        ----------
        kind : str
            can be recipe/step/ingredient.
        _id : str
            ObjectId.
        """
        self.check_file_folder()
        self.check_kind_folder(kind=kind)
        self.check_id_folder(kind=kind, _id=_id)

    # use in check_save_folder
    @staticmethod
    def check_file_folder():
        """ Check/Create if storage folder exist.
        """
        try:
            os.mkdir("{0}".format(utils.Server().path_file_storage))
        except (FileExistsError, OSError):
            pass

    # use in check_save_folder
    @staticmethod
    def check_kind_folder(kind):
        """ Check/Create if type folder exist.

        Parameters
        ----------
        kind : str
            can be recipe/step/ingredient.
        """
        try:
            os.mkdir("{0}/{1}".format(utils.Server().path_file_storage, kind))
        except (FileExistsError, OSError):
            pass

    # use in check_save_folder
    @staticmethod
    def check_id_folder(kind, _id):
        """ Check/Create if id folder exist.

        Parameters
        ----------
        kind : str
            can be recipe/step/ingredient.
        _id : str
            ObjectId.
        """
        try:
            os.mkdir("{0}/{1}/{2}".format(utils.Server().path_file_storage, kind, _id))
        except (FileExistsError, OSError):
            pass

    def check_file_exist(self):
        """ Check if file exist.

        Returns
        -------
        bool
            True if exist, False otherwise.
        """
        path = utils.Server().path_file_storage + self.path
        return os.path.exists(path)

    @staticmethod
    def clean():
        """ Clean FilesTest repository.
        """
        shutil.rmtree(path=utils.Server().path_file_storage+"/", ignore_errors=True)
        return

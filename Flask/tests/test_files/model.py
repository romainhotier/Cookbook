import os
import shutil
import mimetypes

from app import utils, backend


class FileTest(object):

    def __init__(self, **kwargs):
        """ FileTest model.
        - filename = file's name (test folder)
        - origin_test_path = ./Flask/tests/file_exemple/<filename>
        - storage_path = .../Files/recipe/<_id>/<filename>
        - short_path = recipe/<_id>/<filename>
        - data = opened file
        - mimetype = opened file's mimetype

        Parameters
        ----------
        kwargs : Any
            [filename].
        """
        self.filename = "text.txt"
        if "filename" in kwargs:
            self.filename = kwargs["filename"]
        self.origin_test_path = backend.config["FLASK_PATH"] + "tests/file_exemple/" + self.filename
        self.storage_path = ""
        self.short_path = ""
        self.data = open(self.origin_test_path, 'rb')
        self.mimetype = mimetypes.guess_type(url=self.origin_test_path)[0]

    def display(self):
        """ Print FileTest model.

        Returns
        -------
        dict
            Display FileTest.
        """
        print(self.__dict__)

    def set_file_path(self, short_path):
        """ Set complete file storage path and short path.

        Parameters
        ----------
        short_path : str
            file_path.

        Returns
        -------
        FileTest
            File information.
        """
        self.storage_path = backend.config["FILE_STORAGE_PATH"] + short_path + "/" + self.filename
        self.short_path = short_path + "/" + self.filename
        return self

    def insert(self, short_path):
        """ Copy FileTest to filestorage repo.

        Returns
        -------
        FileTest
            File copied.
        """
        self.set_file_path(short_path=short_path)
        utils.PathExplorer().check_files_path_folder(short_path=short_path)
        shutil.copyfile(self.origin_test_path, self.storage_path)
        self.close()
        return self

    def check_file_exist(self):
        """ Check if file exist.

        Returns
        -------
        bool
            True if exist, False otherwise.
        """
        assert os.path.exists(self.storage_path)

    def check_file_not_exist(self):
        """ Check if file exist.

        Returns
        -------
        bool
            True if exist, False otherwise.
        """
        assert os.path.exists(self.storage_path) is False

    def close(self):
        """ Close opened FileTest().
        """
        self.data.close()

    def clean(self):
        """ Clean Files storage repository.
        """
        self.close()
        shutil.rmtree(path=backend.config["FILE_STORAGE_PATH"], ignore_errors=True)
        return

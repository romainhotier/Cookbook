import os.path
import shutil
from app import utils, backend


class File(object):

    @staticmethod
    def save_files(short_path, files):
        """ Save Files in specific folder.

        Parameters
        ----------
        short_path : str
            File's path.
        files : list
            FileStorage from request.

        Returns
        -------
        list
            Files's url.
        """
        urls = []
        utils.PathExplorer().check_files_path_folder(short_path=short_path)
        for file in files:
            file.save("{0}/{1}/{2}".format(backend.config["FILE_STORAGE_PATH"], short_path, file.filename))
            urls.append("{0}/{1}".format(short_path, file.filename))
        return urls

    @staticmethod
    def delete(short_path):
        """ Delete a File.

        Parameters
        ----------
        short_path : str
            File's path.

        Returns
        -------
        str
            File short_path.
        """
        try:
            os.remove(backend.config["FILE_STORAGE_PATH"] + short_path)
            return short_path
        except FileNotFoundError:
            return ""

    @staticmethod
    def clean_delete_recipe(_id):
        """ Delete a File.

        Parameters
        ----------
        _id: str
            Recipe ObjectId
        """
        try:
            shutil.rmtree(path=backend.config["FILE_STORAGE_PATH"] + "recipe/{}".format(_id), ignore_errors=True)
        except FileNotFoundError:
            pass

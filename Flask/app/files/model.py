import os.path
import shutil
from app import utils, backend

converter = utils.PathExplorer()


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
            path = "{0}{1}/{2}".format(backend.config["FILE_STORAGE_PATH"], short_path, file.filename)
            url = "{0}/{1}".format(short_path, file.filename)
            if backend.config["SYSTEM"] == "Windows":
                path = converter.convert_path(target="Windows", path=path)
                url = converter.convert_path(target="Windows", path=url)
            file.save(path)
            urls.append(url)
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
        """ Delete a Recipe's File.

        Parameters
        ----------
        _id: str
            Recipe ObjectId
        """
        try:
            path = backend.config["FILE_STORAGE_PATH"] + "recipe/{}".format(_id)
            if backend.config["SYSTEM"] == "Windows":
                converter.convert_path(target="Windows", path=path)
            shutil.rmtree(path=path, ignore_errors=True)
        except FileNotFoundError:
            pass

    @staticmethod
    def clean_delete_step(_id_recipe, _id_step):
        """ Delete a Step's File.

        Parameters
        ----------
        _id_recipe: str
            Recipe's ObjectId
        _id_step: str
            Step's ObjectId
        """
        try:
            path = backend.config["FILE_STORAGE_PATH"] + "recipe/{0}/steps/{1}".format(_id_recipe, _id_step)
            if backend.config["SYSTEM"] == "Windows":
                converter.convert_path(target="Windows", path=path)
            shutil.rmtree(path=path, ignore_errors=True)
        except FileNotFoundError:
            pass

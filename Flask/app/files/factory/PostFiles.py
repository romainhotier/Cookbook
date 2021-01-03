import utils
import os


class Factory(object):

    def __init__(self):
        """ Class to work around PostFile.
        """
        self.param_id = "_id"
        self.param_id_recipe = "_id_recipe"
        self.param_id_step = "_id_step"

    def save_files(self, kind, _id, files):
        """ Save Files in specific folder.

        Parameters
        ----------
        kind : str
            can be recipe/step/ingredient.
        _id : str
            ObjectId.
        files : list
            FileStorage from request.

        Returns
        -------
        list
            Files's url.
        """
        urls = []
        self.check_save_folder(kind=kind, _id=_id)
        for file in files:
            path = "{0}/{1}/{2}/{3}".format(utils.Server().path_file_storage, kind, _id, file.filename)
            file.save(path)
            urls.append(path)
        return urls

    def check_save_folder(self, kind, _id):
        self.check_file_folder()
        self.check_kind_folder(kind=kind)
        self.check_id_folder(kind=kind, _id=_id)

    @staticmethod
    def check_file_folder():
        try:
            os.mkdir("{0}".format(utils.Server().path_file_storage))
        except (FileExistsError, OSError):
            pass

    @staticmethod
    def check_kind_folder(kind):
        try:
            os.mkdir("{0}/{1}".format(utils.Server().path_file_storage, kind))
        except (FileExistsError, OSError):
            pass

    @staticmethod
    def check_id_folder(kind, _id):
        try:
            os.mkdir("{0}/{1}/{2}".format(utils.Server().path_file_storage, kind, _id))
        except (FileExistsError, OSError):
            pass

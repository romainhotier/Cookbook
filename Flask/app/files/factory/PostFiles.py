import utils


class Factory(object):

    def __init__(self):
        """ Class to work around PostFiles.
        """
        self.param_id = "_id"
        self.param_id_recipe = "_id_recipe"
        self.param_id_step = "_id_step"

    @staticmethod
    def save_files(kind, _id, files):
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
        utils.Server().check_file_storage_folder(kind=kind, _id=_id)
        for file in files:
            file.save("{0}/{1}/{2}/{3}".format(utils.Server().path_file_storage, kind, _id, file.filename))
            urls.append("{0}/{1}/{2}".format(kind, _id, file.filename))
        return urls

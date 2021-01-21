import os
import platform


class PathExplorer(object):

    def __init__(self):
        self.flask_path = self.discover_flask_path()
        self.files_storage_path = self.get_files_storage_path()

    """ path """
    @staticmethod
    def discover_flask_path():
        """ Get Flask path to work with.
        Returns
        -------
        str
            Path to Flask/ repository.
        """
        current_path = os.getcwd().replace('\\', '/')  # convert from windows
        flask_path = ""
        for p in current_path.split('/'):
            if p == "Flask":
                flask_path += p + "/"
                break
            else:
                flask_path += p + "/"
        return flask_path

    @staticmethod
    def get_files_storage_path():
        """ Set path for files to be saved locally.

        Returns
        -------
        dict
            Storage path.
        """
        sys = platform.system()
        usr = os.getlogin()
        if usr == "rhr" and sys == "Linux":  # Desktop pc for dev
            return "/home/rhr/Workspace/Python/Cookbook/Flask/_files/"
        elif usr == "ubuntu" and sys == "Linux":  # Raspberry prod
            return "/home/ubuntu/Workspace/Storage/cookbook/"
        # elif usr == "xxx" and sys == "Darwin":  # Mac pc for dev
        #     return "/home/rhr/Workspace/Cookbook/Flask/_files"
        # elif usr == "xxx" and sys == "Windows":  # windows for dev
        #     return "/home/rhr/Workspace/Cookbook/Flask/_files"

    """ mkdir folder"""
    def check_files_path_folder(self, short_path):
        """ Check/Create if folder exist.

        Parameters
        ----------
        short_path : str
            File's path.
        """
        self.check_files_storage_folder()
        self.check_file_path(short_path=short_path)

    # use in check_files_folder
    def check_files_storage_folder(self):
        """ Check/Create if storage folder exist.
        """
        try:
            os.mkdir("{0}".format(self.files_storage_path))
        except (FileExistsError, OSError):
            pass

    # use in check_files_folder
    def check_file_path(self, short_path):
        """ Check/Create File's path exist.

        Parameters
        ----------
        short_path : str
            File's path.
        """
        storage = self.files_storage_path
        for p in short_path.split("/"):
            storage += p
            try:
                os.mkdir("{0}".format(storage))
                storage += "/"
            except (FileExistsError, OSError):
                storage += "/"
                pass

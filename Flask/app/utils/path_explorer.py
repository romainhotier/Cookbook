import os
import platform


class PathExplorer(object):

    def __init__(self):
        self.system = platform.system()
        self.flask_path = self.discover_flask_path()
        self.files_storage_path = self.get_files_storage_path()

    """ convert """
    @staticmethod
    def convert_path(target, path):
        """ Convert path to Unix or Windows system.

        Parameters
        ----------
        target : str
            can be ["Windows", "Unix"].
        path : str
            File's path.

        Returns
        -------
        str
            Converted path.
        """
        if target == "Unix":
            return path.replace('\\', '/')
        elif target == "Windows":
            return path.replace('/', '\\')
        else:
            return path

    """ path """
    def discover_flask_path(self):
        """ Get Flask path to work with.
        Returns
        -------
        str
            Path to Flask/ repository.
        """
        """ get current path into unix """
        current_path = self.convert_path(target="Unix", path=os.getcwd())
        flask_path = ""
        for p in current_path.split('/'):
            if p == "Flask":
                flask_path += p + "/"
                break
            else:
                flask_path += p + "/"
        """ convert for windows """
        if self.system == "Windows":
            return self.convert_path(target="Windows", path=flask_path)
        else:
            return self.convert_path(target="Unix", path=flask_path)

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
        elif sys == "Windows":  # Windows Suneris
            return "C:\\Users\\romain.hotier\\workspace\\perso\\Cookbook\\Flask\\_files\\"
        # elif usr == "xxx" and sys == "Darwin":  # Mac pc for dev
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
        sp = ""
        split_key = ""
        if self.system in "Linux":
            split_key = "/"
            sp = self.convert_path(target="Unix", path=short_path)
        elif self.system == "Windows":
            split_key = "\\"
            sp = self.convert_path(target="Windows", path=short_path)
        for p in sp.split(split_key):
            storage += p
            try:
                os.mkdir("{0}".format(storage))
                storage += split_key
            except (FileExistsError, OSError):
                storage += split_key
                pass

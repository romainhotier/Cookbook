import os
import platform


class PathExplorer(object):

    # use in get_file(s)_path_for_test
    def discover_flask_path(self):
        """ Get Flask path to work with.
        Returns
        -------
        str
            Path to Flask/ repository.
        """
        current_path = self.convert_to_unix_path(os.getcwd())
        default_path = ""
        for p in current_path.split('/'):
            if p == "Flask":
                default_path += p + "/"
                break
            else:
                default_path += p + "/"
        return default_path

    # use in discover path
    @staticmethod
    def convert_to_unix_path(path):
        """ Get path to windows's path.

        Parameters
        ----------
        path : str
            Path to be converted.

        Returns
        -------
        str
            replace \\ by /.
        """
        return path.replace('\\', '/')

    # use in get_file(s)_path_for_test
    @staticmethod
    def convert_to_windows_path(path):
        """ Get path to windows's path.

        Parameters
        ----------
        path : Any
            Path to be converted.

        Returns
        -------
        str
            replace / by \\.
        """
        if isinstance(str, path):
            return path.replace('/', '\\')
        elif isinstance(list, path):
            return [path.replace('/', '\\') for path in path]

    """ for tests """
    def get_file_path_for_test(self):
        """ Get file's path.

        Returns
        -------
        str
            Path according to the system.
        """
        flask_path = self.discover_flask_path()
        test_path = flask_path + "tests/file_exemple/text.txt"
        if platform.system() == "Windows":
            return self.convert_to_windows_path(test_path)
        elif platform.system() in ["Linux", "Darwin"]:
            return test_path

    def get_files_path_for_test(self):
        """ Get files's path.

        Returns
        -------
        list
        Path according to the system, len 3 here.
        """
        flask_path = self.discover_flask_path()
        test_paths = [flask_path + "tests/file_exemple/text.txt",
                      flask_path + "tests/file_exemple/image.png",
                      flask_path + "tests/file_exemple/image2.jpeg"]
        if platform.system() == "Windows":
            return self.convert_to_windows_path(path=test_paths)
        elif platform.system() in ["Linux", "Darwin"]:
            return test_paths

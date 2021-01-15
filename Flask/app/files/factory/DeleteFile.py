class Factory(object):

    def __init__(self):
        """ Class to work around DeleteFile.
        """
        self.param_path = "path"

    @staticmethod
    def len_path(path):
        """ Class to work around DeleteFile.

        Parameters
        ----------
        path : str
            File's short_path.

        Returns
        -------
        int
            short_path length
        """
        return len(path.split("/"))

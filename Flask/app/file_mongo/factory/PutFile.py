class Factory(object):

    def __init__(self):
        """ Class to work around PutFile.
        """
        self.param_id = "_id"

    @staticmethod
    def data_information(_id_file, _id_parent):
        """ Get new main File.

        Parameters
        ----------
        _id_file : str
            Updated File's ObjectId.
        _id_parent : str
            Parent's ObjectId.

        Returns
        -------
        str
            Information.
        """
        return "{0} is now set as main file for {1}".format(_id_file, _id_parent)

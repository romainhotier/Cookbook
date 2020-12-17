class Factory(object):

    def __init__(self):
        """ Class to work around DeleteRecipe.
        """
        self.param_id = "_id"

    @staticmethod
    def data_information(_id):
        """ Get Deleted Recipe's ObjectId.

        Parameters
        ----------
        _id : str
            Deleted Recipe's ObjectId.

        Returns
        -------
        str
            Information.
        """
        return "Deleted Recipe: {0}".format(_id)

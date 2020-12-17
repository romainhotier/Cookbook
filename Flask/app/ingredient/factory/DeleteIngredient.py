class Factory(object):

    def __init__(self):
        """ Class to work around DeleteIngredient.
        """
        self.param_id = "_id"

    @staticmethod
    def data_information(_id):
        """ Get Deleted Ingredient's ObjectId.

        Parameters
        ----------
        _id : str
            Deleted Ingredient's ObjectId.

        Returns
        -------
        str
            Information.
        """
        return "Deleted Ingredient: {0}".format(_id)

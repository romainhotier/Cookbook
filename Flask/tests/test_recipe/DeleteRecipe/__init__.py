from tests import rep


class DeleteRecipe(object):
    """ Class to test DeleteRecipe.
    """

    def __init__(self):
        self.url = 'recipe'
        self.param_id = "_id"
        self.rep_code_msg_ok = rep.code_msg_ok.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = rep.code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_404_url = rep.code_msg_error_404.replace("xxx", "cookbook")

    @staticmethod
    def data_expected(_id):
        """ Format data's response.

        Parameters
        ----------
        _id : str
           RecipeTest's ObjectId.

        Returns
        -------
        str
            Data's response.
        """
        return "Deleted Recipe: {}".format(_id)


api = DeleteRecipe()

from tests import rep


class GetIndex(object):
    """ Class to test GetIndex.
    """

    def __init__(self):
        self.url = ''
        self.rep_code_msg_ok = rep.code_msg_ok.replace("xxx", "recipe")

    # @staticmethod
    # def data_expected(_id):
    #     """ Format data's response.
    #
    #     Parameters
    #     ----------
    #     _id : str
    #        RecipeTest's ObjectId.
    #
    #     Returns
    #     -------
    #     str
    #         Data's response.
    #     """
    #     return "Deleted Recipe: {}".format(_id)


api = GetIndex()

from tests import rep


class GetAllIngredient(object):
    """ Class to test GetAllIngredient.
    """

    def __init__(self):
        self.url = 'ingredient'
        self.rep_code_msg_ok = rep.code_msg_ok.replace("xxx", "ingredient")
        self.rep_code_msg_error_400 = rep.code_msg_error_400.replace("xxx", "ingredient")
        self.rep_code_msg_error_404_url = rep.code_msg_error_404.replace("xxx", "cookbook")

    @staticmethod
    def data_expected(ingredient):
        """ Format data's response.

        Parameters
        ----------
        ingredient : IngredientTest
            IngredientTest.

        Returns
        -------
        str
            Data's response.
        """
        data_expected = ingredient.get_stringify()
        return data_expected


api = GetAllIngredient()

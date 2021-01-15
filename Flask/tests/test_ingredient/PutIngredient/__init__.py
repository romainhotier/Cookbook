from tests import rep


class PutIngredient(object):
    """ Class to test PutIngredient.
    """

    def __init__(self):
        self.url = 'ingredient'
        self.param_id = "_id"
        self.param_categories = "categories"
        self.param_name = "name"
        self.param_nutriments = "nutriments"
        self.param_nutriments_calories = "calories"
        self.param_nutriments_carbohydrates = "carbohydrates"
        self.param_nutriments_fats = "fats"
        self.param_nutriments_proteins = "proteins"
        self.param_nutriments_portion = "portion"
        self.param_slug = "slug"
        self.param_unit = "unit"
        self.rep_code_msg_ok = rep.code_msg_ok.replace("xxx", "ingredient")
        self.rep_code_msg_error_400 = rep.code_msg_error_400.replace("xxx", "ingredient")
        self.rep_code_msg_error_404_url = rep.code_msg_error_404.replace("xxx", "cookbook")
        self.repf_detail_unit = " ['g', 'ml']"

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


api = PutIngredient()

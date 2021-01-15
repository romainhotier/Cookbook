from tests import rep


class GetAllRecipe(object):
    """ Class to test GetAllRecipe.
    """

    def __init__(self):
        self.url = 'recipe'
        self.param_with_calories = "with_calories"
        self.rep_code_msg_ok = rep.code_msg_ok.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = rep.code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_404_url = rep.code_msg_error_404.replace("xxx", "cookbook")
        self.detail_boolean = " ['true', 'false']"

    @staticmethod
    def data_expected(recipe, **kwargs):
        """ Format data's response.

        Parameters
        ----------
        recipe : RecipeTest
            RecipeTest.
        kwargs: Any
            [calories]

        Returns
        -------
        GetAllRecipe
            Data's response.
        """
        if "calories" in kwargs:
            recipe.add_enrichment_calories()
        data_expected = recipe.get_stringify()
        return data_expected


api = GetAllRecipe()

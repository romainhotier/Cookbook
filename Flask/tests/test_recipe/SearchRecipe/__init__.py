from tests import rep


class SearchRecipe(object):
    """ Class to test SearchRecipe.
    """

    def __init__(self):
        self.url = 'recipe/search'
        self.param_categories = "categories"
        self.param_cooking_time = "cooking_time"
        self.param_level = "level"
        self.param_nb_people = "nb_people"
        self.param_preparation_time = "preparation_time"
        self.param_slug = "slug"
        self.param_status = "status"
        self.param_title = "title"
        self.rep_code_msg_ok = rep.code_msg_ok.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = rep.code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_404 = rep.code_msg_error_404.replace("xxx", "cookbook")

    @staticmethod
    def data_expected(recipe):
        """ Format data's response.

        Parameters
        ----------
        recipe : Any
            RecipeTest.

        Returns
        -------
        str
            Data's response.
        """
        data_expected = recipe.get_stringify()
        return data_expected


api = SearchRecipe()

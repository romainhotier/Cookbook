from tests import rep


class GetAllRecipe(object):
    """ Class to test GetAllRecipe.
    """

    def __init__(self):
        self.url = 'recipe'
        self.param_with_calories = "with_calories"
        self.param_categories = "categories"
        self.param_cooking_time = "cooking_time"
        self.param_level = "level"
        self.param_nb_people = "nb_people"
        self.param_preparation_time = "preparation_time"
        self.param_slug = "slug"
        self.param_status = "status"
        self.param_title = "title"
        self.param_order_by = "orderBy"
        self.param_order = "order"
        self.rep_code_msg_ok = rep.code_msg_ok.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = rep.code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_404_url = rep.code_msg_error_404.replace("xxx", "cookbook")
        self.detail_boolean = " ['true', 'false']"
        self.detail_order = " ['asc', 'desc']"
        self.detail_order_by = " ['title', 'slug', 'level', 'cooking_time', 'preparation_time', 'nb_people']"

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

    @staticmethod
    def check_order(key, data):
        """ Check data's order.

        Parameters
        ----------
        key : str
            Key to be ordered.
        data : dict
            Api response

        Returns
        -------
        list
            Data's order.
        """
        order = []
        for ingredient in data:
            order.append(ingredient[key])
        return order


api = GetAllRecipe()

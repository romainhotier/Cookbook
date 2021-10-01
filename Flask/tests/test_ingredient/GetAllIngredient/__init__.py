from tests import rep


class GetAllIngredient(object):
    """ Class to test GetAllIngredient.
    """

    def __init__(self):
        self.url = 'ingredient'
        self.param_categories = "categories"
        self.param_name = "name"
        self.param_order = "order"
        self.param_order_by = "orderBy"
        self.param_slug = "slug"
        self.rep_code_msg_ok = rep.code_msg_ok.replace("xxx", "ingredient")
        self.rep_code_msg_error_400 = rep.code_msg_error_400.replace("xxx", "ingredient")
        self.rep_code_msg_error_404_url = rep.code_msg_error_404.replace("xxx", "cookbook")
        self.detail_order = " ['asc', 'desc']"
        self.detail_order_by = " ['name', 'slug']"

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


api = GetAllIngredient()

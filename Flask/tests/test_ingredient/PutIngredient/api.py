import utils

server = utils.Server()


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
        self.rep_code_msg_ok = server.rep_code_msg_ok.replace("xxx", "ingredient")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "ingredient")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")
        self.repf_detail_unit = " ['g', 'ml']"

    @staticmethod
    def create_detail(param, msg, **kwargs):
        """ Format Server's detail response.

        Parameters
        ----------
        param : str
            Tested parameter.
        msg : str
            Server's message.
        kwargs : Any
            Value if one existed.

        Returns
        -------
        dict
            Server's detail response.
        """
        detail = {"param": param, "msg": msg}
        if "value" in kwargs:
            detail["value"] = kwargs["value"]
        return detail

    @staticmethod
    def data_expected(ingredient):
        """ Format data's response.

        Parameters
        ----------
        ingredient : Any
            IngredientTest.

        Returns
        -------
        str
            Data's response.
        """
        data_expected = ingredient.get_stringify()
        return data_expected

    @staticmethod
    def check_not_present(value, rep):
        """ Check if data/detail is not present in Server's response.

        Parameters
        ----------
        value : str
            Tested value.
        rep : dict
            Server's response.

        Returns
        -------
        bool
        """
        if value in rep.keys():
            return False
        else:
            return True
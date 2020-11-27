import utils

server = utils.Server()


class GetIngredientForRecipe(object):
    """ Class to test GetIngredientForRecipe.
    """

    def __init__(self):
        self.url1 = 'recipe'
        self.url2 = 'ingredient'
        self.param_id = "_id"
        self.param_with_names = "with_names"
        self.rep_code_msg_ok = server.rep_code_msg_ok.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")
        self.detail_true_false = " ['true', 'false']"

    @staticmethod
    def create_detail(param, msg, **kwargs):
        """ Format Server's detail response.

        Parameters
        ----------
        param : str
            Tested parameter.
        msg : str
            Server's message.
        kwargs : str
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
    def data_expected(link, **kwargs):
        """ Format data's response.

        Parameters
        ----------
        link : Any
            IngredientRecipeTest.
        kwargs : Any
            names: bool.

        Returns
        -------
        str
            Data's response.
        """
        if "names" in kwargs.keys():
            data_expected = link.add_name().get_stringify()
        else:
            data_expected = link.get_stringify()
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

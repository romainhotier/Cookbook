import utils

server = utils.Server()


class GetRecipeForIngredient(object):
    """ Class to test GetRecipeForIngredient.
    """

    def __init__(self):
        self.url1 = 'ingredient'
        self.url2 = 'recipe'
        self.param_id_ingredient = "_id_ingredient"
        self.param_with_titles = "with_titles"
        self.rep_code_msg_ok = server.rep_code_msg_ok.replace("xxx", "ingredient")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "ingredient")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")
        self.rep_detail_true_false = " ['true', 'false']"

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
            titles: bool.

        Returns
        -------
        str
            Data's response.
        """
        if "title" in kwargs.keys():
            data_expected = link.add_title().get_stringify()
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

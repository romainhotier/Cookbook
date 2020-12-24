import utils

server = utils.Server()


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
        self.rep_code_msg_ok = server.rep_code_msg_ok.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "recipe")

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

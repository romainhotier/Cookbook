import utils

server = utils.Server()


class PutRecipeStep(object):
    """ Class to test PutRecipeStep.
    """

    def __init__(self):
        self.url1 = 'recipe'
        self.url2 = 'step'
        self.param_id_recipe = "_id_recipe"
        self.param_id_step = "_id_step"
        self.param_with_files = "with_files"
        self.param_description = "description"
        self.param_position = "position"
        self.rep_code_msg_ok = server.rep_code_msg_ok.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")
        self.rep_code_msg_error_405 = server.rep_code_msg_error_405.replace("xxx", "cookbook")
        self.detail_with_files = " ['true', 'false']"

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

    @staticmethod
    def data_expected(recipe, **kwargs):
        """ Format data's response.

        Parameters
        ----------
        recipe : Any
            RecipeTest.
        kwargs : Any
            files: [FileTests].

        Returns
        -------
        str
            Data's response.
        """
        if "files" in kwargs.keys():
            data_expected = recipe.get_stringify_with_file(files_recipe=kwargs["files"]["recipe"],
                                                           files_steps=kwargs["files"]["steps"])
        else:
            data_expected = recipe.get_stringify()
        return data_expected

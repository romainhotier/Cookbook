import utils

server = utils.Server()


class GetIngredient(object):
    """ Class to test GetIngredient.
    """

    def __init__(self):
        self.url = 'ingredient'
        self.param_id = "_id"
        self.param_with_files_mongo = "with_files_mongo"
        self.rep_code_msg_ok = server.rep_code_msg_ok.replace("xxx", "ingredient")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "ingredient")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")
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
    def data_expected(ingredient, **kwargs):
        """ Format data's response.

        Parameters
        ----------
        ingredient : Any
            IngredientTest.
        kwargs : Any
            files: [FileTests].
            files_mongo: [FileMongoTests].

        Returns
        -------
        str
            Data's response.
        """
        data_expected = ingredient.get_stringify()
        if "files" in kwargs:
            data_expected["files"] = [file.get_enrichment() for file in kwargs["files"]]
        if "files_mongo" in kwargs:
            data_expected["files_mongo"] = [file.get_enrichment() for file in kwargs["files_mongo"]]
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

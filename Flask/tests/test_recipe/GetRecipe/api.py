import utils

server = utils.Server()


class GetRecipe(object):
    """ Class to test GetRecipe.
    """

    def __init__(self):
        self.url = 'recipe'
        self.param_slug = "slug"
        self.param_with_files = "with_files"
        self.param_with_files_mongo = "with_files_mongo"
        self.rep_code_msg_ok = server.rep_code_msg_ok.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")
        self.detail_with_files = " ['true', 'false']"
        self.formated_data = {}

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

    def data_expected(self, recipe, **kwargs):
        """ Format data's response.

        Parameters
        ----------
        recipe : Any
            RecipeTest.
        kwargs : Any
            files: [FileTests].

        Returns
        -------
        GetRecipe
            Data's response.
        """
        data_expected = recipe.get_stringify()
        # if "files" in kwargs:
        #     data_expected["files"] = [file.get_enrichment() for file in kwargs["files"]]
        if "files_mongo" in kwargs:
            data_expected["files_mongo"] = [file.get_enrichment() for file in kwargs["files_mongo"]]
        self.formated_data = data_expected
        return self

    def get_data_expected(self):
        """ Format data's response.

        Returns
        -------
        dict
            Data's expected.
        """
        return self.formated_data

    def add_ingredient_files_mongo(self, ingredient, files_mongo):
        """ Format data's response.

        Parameters
        ----------
        ingredient : Any
            IngredientTest.
        files_mongo : list
            files_mongo: [FileMongoTests].

        Returns
        -------
        GetRecipe
            Data's response.
        """
        try:
            for ingr in self.formated_data["ingredients"]:
                if ingr["_id"] == ingredient.get_id():
                    ingr["files_mongo"] = [file.get_enrichment() for file in files_mongo]
                    break
        except KeyError:
            pass
        return self.formated_data

    def add_steps_files_mongo(self, _id, files_mongo):
        """ Format data's response.

        Parameters
        ----------
        _id : str
            Step's ObjectId.
        files_mongo : list
            files_mongo: [FileMongoTests].

        Returns
        -------
        GetRecipe
            Data's response.
        """
        try:
            for step in self.formated_data["steps"]:
                if step["_id"] == _id:
                    step["files_mongo"] = [file.get_enrichment() for file in files_mongo]
                    break
        except KeyError:
            pass
        return self.formated_data

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

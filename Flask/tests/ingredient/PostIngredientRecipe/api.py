import jsonschema

import utils

server = utils.Server()


class PostIngredientRecipe(object):
    """ Class to test PostIngredientRecipe.
    """

    def __init__(self):
        self.url = 'ingredient/recipe'
        self.param_id_recipe = "_id_recipe"
        self.param_id_ingredient = "_id_ingredient"
        self.param_quantity = "quantity"
        self.param_unit = "unit"
        self.rep_code_msg_created = server.rep_code_msg_created.replace("xxx", "ingredient")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "ingredient")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")

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
    def create_schema(link):
        """ Format schema's response.

        Parameters
        ----------
        link : Any
            IngredientRecipeTest.

        Returns
        -------
        dict
            Schema.
        """
        return {"type": "object",
                "properties": {
                    "_id": {"type": "string"},
                    "quantity": {"enum": [link.quantity]},
                    "unit": {"enum": [link.unit]},
                    "_id_ingredient": {"enum": [link.get_id_ingredient()]},
                    "_id_recipe": {"enum": [link.get_id_recipe()]}},
                "required": ["_id", "quantity", "unit", "_id_ingredient", "_id_recipe"],
                "additionalProperties": False}

    def json_check(self, data, data_expected):
        """ Format schema's response.

        Parameters
        ----------
        data : dict
            Server's response.
        data_expected : Any
            Schema from IngredientRecipeTest.

        Returns
        -------
        dict
            Result and err if exist.
        """
        try:
            jsonschema.validate(instance=data, schema=self.create_schema(link=data_expected))
            return {"result": True, "error": None}
        except jsonschema.exceptions.ValidationError as err:
            return {"result": False, "error": err}

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

import jsonschema
import copy

import utils

server = utils.Server()


class PostIngredient(object):
    """ Class to test PostIngredient.
    """

    def __init__(self):
        self.url = 'ingredient'
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
        self.rep_code_msg_created = server.rep_code_msg_created.replace("xxx", "ingredient")
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

    def custom_body(self, body):
        """ Format body to custom the Ingredient.

        Parameters
        ----------
        body : dict
            Body's value.

        Returns
        -------
        dict
        """
        data = copy.deepcopy(body)
        if self.param_categories not in body.keys():
            data["categories"] = []
        if self.param_nutriments not in body.keys():
            data["nutriments"] = {self.param_nutriments_calories: 0,
                                  self.param_nutriments_carbohydrates: 0,
                                  self.param_nutriments_fats: 0,
                                  self.param_nutriments_proteins: 0,
                                  self.param_nutriments_portion: 1}
        if self.param_unit not in body.keys():
            data["unit"] = "g"
        return data

    @staticmethod
    def create_schema(ingredient):
        """ Format schema's response.

        Parameters
        ----------
        ingredient : Any
            IngredientTest.

        Returns
        -------
        dict
            Schema.
        """
        return {"type": "object",
                "properties": {
                    "_id": {"type": "string"},
                    "categories": {"enum": [ingredient.categories]},
                    "name": {"enum": [ingredient.name]},
                    "nutriments": {"enum": [ingredient.nutriments]},
                    "slug": {"enum": [ingredient.slug]},
                    "unit": {"enum": [ingredient.unit]}},
                "required": ["_id", "categories", "name", "nutriments", "slug", "unit"],
                "additionalProperties": False}

    def json_check(self, data, data_expected):
        """ Format schema's response.

        Parameters
        ----------
        data : dict
            Server's response.
        data_expected : Any
            Schema from IngredientTest.

        Returns
        -------
        dict
            Result and err if exist.
        """
        try:
            jsonschema.validate(instance=data, schema=self.create_schema(ingredient=data_expected))
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

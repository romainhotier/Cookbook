import jsonschema
import copy

import utils

server = utils.Server()


class PostRecipe(object):
    """ Class to test PostRecipe.
    """

    def __init__(self):
        self.url = 'recipe'
        self.param_title = "title"
        self.param_slug = "slug"
        self.param_level = "level"
        self.param_resume = "resume"
        self.param_cooking_time = "cooking_time"
        self.param_preparation_time = "preparation_time"
        self.param_nb_people = "nb_people"
        self.param_note = "note"
        self.param_categories = "categories"
        self.param_status = "status"
        self.rep_detail_status = " ['in_progress', 'finished']"
        self.rep_code_msg_created = server.rep_code_msg_created.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_404 = server.rep_code_msg_error_404.replace("xxx", "recipe")
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

    def default_value(self, body):
        """ Add default value if not present.

        Parameters
        ----------
        body : dict
            Body's request.

        Returns
        -------
        dict
            Body filled with default value.
        """
        default_value = copy.deepcopy(body)
        if self.param_categories not in default_value.keys():
            default_value["categories"] = []
        if self.param_cooking_time not in default_value.keys():
            default_value["cooking_time"] = 0
        if self.param_level not in default_value.keys():
            default_value["level"] = 0
        if self.param_nb_people not in default_value.keys():
            default_value["nb_people"] = 0
        if self.param_note not in default_value.keys():
            default_value["note"] = ""
        if self.param_preparation_time not in default_value.keys():
            default_value["preparation_time"] = 0
        if self.param_resume not in default_value.keys():
            default_value["resume"] = ""
        if self.param_status not in default_value.keys():
            default_value["status"] = "in_progress"
        default_value["steps"] = []
        return default_value

    @staticmethod
    def create_schema(recipe):
        """ Format schema's response.

        Parameters
        ----------
        recipe : Any
            RecipeTest.

        Returns
        -------
        dict
            Schema.
        """
        return {"type": "object",
                "properties": {
                    "_id": {"type": "string"},
                    "categories": {"enum": [recipe.categories]},
                    "cooking_time": {"enum": [recipe.cooking_time]},
                    "level": {"enum": [recipe.level]},
                    "nb_people": {"enum": [recipe.nb_people]},
                    "note": {"enum": [recipe.note]},
                    "preparation_time": {"enum": [recipe.preparation_time]},
                    "resume": {"enum": [recipe.resume]},
                    "slug": {"enum": [recipe.slug]},
                    "steps": {"enum": [[]]},
                    "title": {"enum": [recipe.title]},
                    "status": {"enum": [recipe.status]}},
                "required": ["_id", "categories", "cooking_time", "level", "nb_people", "note", "preparation_time",
                             "resume", "slug", "steps", "title", "status"],
                "additionalProperties": False}

    def json_check(self, data, data_expected):
        """ Format schema's response.

        Parameters
        ----------
        data : dict
            Server's response.
        data_expected : Any
            Schema from RecipeTest.

        Returns
        -------
        dict
            Result and err if exist.
        """
        try:
            jsonschema.validate(instance=data, schema=self.create_schema(recipe=data_expected))
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

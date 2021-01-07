import jsonschema
import copy

import utils

server = utils.Server()


class PostRecipe(object):
    """ Class to test PostRecipe.
    """

    def __init__(self):
        self.url = 'recipe'
        self.param_categories = "categories"
        self.param_cooking_time = "cooking_time"
        self.param_ingredients = "ingredients"
        self.param_ingredient = "ingredient"
        self.param_ingredient_id = "_id"
        self.param_ingredient_quantity = "quantity"
        self.param_ingredient_unit = "unit"
        self.param_level = "level"
        self.param_nb_people = "nb_people"
        self.param_note = "note"
        self.param_preparation_time = "preparation_time"
        self.param_resume = "resume"
        self.param_slug = "slug"
        self.param_status = "status"
        self.param_steps = "steps"
        self.param_step_description = "description"
        self.param_title = "title"
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

    def add_default_value(self, body):
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
        """ fill body """
        filled_body = copy.deepcopy(body)
        if self.param_categories not in filled_body:
            filled_body["categories"] = []
        if self.param_cooking_time not in filled_body:
            filled_body["cooking_time"] = 0
        if self.param_ingredients not in filled_body:
            filled_body["ingredients"] = []
        if self.param_level not in filled_body:
            filled_body["level"] = 0
        if self.param_nb_people not in filled_body:
            filled_body["nb_people"] = 0
        if self.param_note not in filled_body:
            filled_body["note"] = ""
        if self.param_preparation_time not in filled_body:
            filled_body["preparation_time"] = 0
        if self.param_resume not in filled_body:
            filled_body["resume"] = ""
        if self.param_status not in filled_body:
            filled_body["status"] = "in_progress"
        if self.param_steps not in filled_body:
            filled_body["steps"] = []
        """ clean value for ingredients and steps param """
        cleaned_ingredient = self.clean_value_ingredients(filled_body)
        cleaned_step = self.clean_value_steps(cleaned_ingredient)
        return cleaned_step

    @staticmethod
    def clean_value_ingredients(data):
        """ Clean ingredients values.

        Parameters
        ----------
        data : dict
            Body's request.

        Returns
        -------
        dict
            Cleaned ingredients parameter.
        """
        try:
            for ingr in data["ingredients"]:
                for key in list(ingr):
                    if key not in ["_id", "quantity", "unit"]:
                        ingr.pop(key)
            return data
        except (TypeError, AttributeError):
            return data

    @staticmethod
    def clean_value_steps(data):
        """ Clean steps values.

        Parameters
        ----------
        data : dict
            Body's request.

        Returns
        -------
        dict
            Cleaned step parameter.
        """
        try:
            for step in data["steps"]:
                for key in list(step):
                    if key not in ["_id", "description"]:
                        step.pop(key)
            return data
        except (TypeError, AttributeError):
            return data

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
        schema = {"definitions": {"steps": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "_id": {"type": "string"},
                    "description": {"type": "string",
                                    "enum": [step["description"] for step in recipe.steps]}},
                "required": ["_id", "description"],
                "additionalProperties": False}}},

            "type": "object",
            "properties": {
                "_id": {"type": "string"},
                "categories": {"enum": [recipe.categories]},
                "cooking_time": {"enum": [recipe.cooking_time]},
                "ingredients": {"enum": [recipe.ingredients]},
                "level": {"enum": [recipe.level]},
                "nb_people": {"enum": [recipe.nb_people]},
                "note": {"enum": [recipe.note]},
                "preparation_time": {"enum": [recipe.preparation_time]},
                "resume": {"enum": [recipe.resume]},
                "slug": {"enum": [recipe.slug]},
                "steps": {"$ref": "#/definitions/steps"},
                "status": {"enum": [recipe.status]},
                "title": {"enum": [recipe.title]}},
            "required": ["_id", "categories", "cooking_time",  "ingredients", "level", "nb_people", "note",
                         "preparation_time", "resume", "slug", "steps", "status", "title"],
            "additionalProperties": False}
        return schema

    def nutriment(self):
        """ Set nutriment schema for validation.
        Returns
        -------
        dict
            Nutriment schema.
        """
        schema = {"definitions": {"measurement": {
            "type": "object",
            "properties": {
                "quantity": {"type": "number"},
                "unit": {"type": "string"}},
            "required": ["quantity", "unit"],
            "additionalProperties": False}},

            "type": "object",
            "properties": {
                "calories_per_100g": {"$ref": "#/definitions/measurement"},
                "carbohydrates_per_100g": {"$ref": "#/definitions/measurement"},
                "fats_per_100g": {"$ref": "#/definitions/measurement"},
                "proteins_per_100g": {"$ref": "#/definitions/measurement"}},
            "required": ["calories_per_100g", "carbohydrates_per_100g", "fats_per_100g", "proteins_per_100g"],
            "additionalProperties": False}
        self.__setattr__("schema", schema)

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
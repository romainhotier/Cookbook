from tests import rep


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
        self.rep_code_msg_created = rep.code_msg_created.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = rep.code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_404 = rep.code_msg_error_404.replace("xxx", "recipe")
        self.rep_code_msg_error_404_url = rep.code_msg_error_404.replace("xxx", "cookbook")

    @staticmethod
    def create_schema(recipe):
        """ Format schema's response.

        Parameters
        ----------
        recipe : RecipeTest
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
                                    "enum": [step["description"] for step in recipe.steps]},
                    "files": {"enum": [[]]}},
                "required": ["_id", "description", "files"],
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


api = PostRecipe()

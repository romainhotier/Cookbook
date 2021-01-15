from tests import rep


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
        self.rep_code_msg_created = rep.code_msg_created.replace("xxx", "ingredient")
        self.rep_code_msg_error_400 = rep.code_msg_error_400.replace("xxx", "ingredient")
        self.rep_code_msg_error_404_url = rep.code_msg_error_404.replace("xxx", "cookbook")
        self.repf_detail_unit = " ['g', 'ml']"

    @staticmethod
    def create_schema(ingredient):
        """ Format schema's response.

        Parameters
        ----------
        ingredient : IngredientTest
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


api = PostIngredient()

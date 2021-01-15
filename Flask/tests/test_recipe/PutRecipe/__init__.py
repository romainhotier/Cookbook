import copy
import re

from tests import rep


class PutRecipe(object):
    """ Class to test PutRecipe.
    """

    def __init__(self):
        self.url = 'recipe'
        self.param_id = "_id"
        self.param_categories = "categories"
        self.param_cooking_time = "cooking_time"
        self.param_ingredients = "ingredients"
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
        self.param_step = "step"
        self.param_step_id = "_id"
        self.param_step_description = "description"
        self.param_title = "title"
        self.rep_code_msg_ok = rep.code_msg_ok.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = rep.code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_404_url = rep.code_msg_error_404.replace("xxx", "cookbook")
        self.detail_status = " ['in_progress', 'finished']"

    @staticmethod
    def response_without_steps(data):
        """ Get response without steps.

        Parameters
        ----------
        data : dict
            Server's response.

        Returns
        -------
        dict
            Server's response without steps.
        """
        response = copy.deepcopy(data)
        response.pop("steps")
        return response

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
    def data_expected_without_steps(recipe):
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
        data_expected.pop("steps")
        return data_expected

    @staticmethod
    def check_steps(recipe, response_data):
        """ Check steps information.

        Parameters
        ----------
        recipe : Any
            RecipeTest.
        response_data : dict
            Server's response.
        """
        recipe_steps = (copy.deepcopy(recipe.get_stringify())).pop("steps")
        response_steps = (copy.deepcopy(response_data)).pop("steps")
        regx_1 = re.compile('.*aaaaaa.*', re.IGNORECASE)
        regx_2 = re.compile('.*bbbbbb.*', re.IGNORECASE)
        regx_3 = re.compile('.*cccccc.*', re.IGNORECASE)
        for i, step in enumerate(recipe_steps):
            try:
                if re.search(regx_1, step["_id"]) or re.search(regx_2, step["_id"]) or re.search(regx_3, step["_id"]):
                    assert step["description"] == response_steps[i]["description"]
                    assert step["_id"] == response_steps[i]["_id"]
                else:
                    assert step["description"] == response_steps[i]["description"]
            except KeyError:
                assert step["description"] == response_steps[i]["description"]


api = PutRecipe()

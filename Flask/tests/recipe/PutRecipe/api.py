import utils
import copy

server = utils.Server()


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
        self.rep_code_msg_ok = server.rep_code_msg_ok.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")
        self.detail_status = " ['in_progress', 'finished']"

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
        recipe_steps = (copy.deepcopy(recipe.get_stringify())).pop("steps")
        response_steps = (copy.deepcopy(response_data)).pop("steps")
        for i, step in enumerate(recipe_steps):
            if isinstance(step, dict):
                assert step == response_steps[i]
            elif isinstance(step, str):
                assert step == response_steps[i]["description"]

    def clean_body(self, data):
        """ Clean body.

        Parameters
        ----------
        data : dict
            Body's request.

        Returns
        -------
        dict
            Cleaned body.
        """
        cp = copy.deepcopy(data)
        data_i = self.clean_value_ingredients(data=cp)
        data_s = self.clean_value_steps(data=data_i)
        return data_s

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
            Cleaned steps parameter.
        """
        try:
            for step in data["steps"]:
                if isinstance(step, dict):
                    for key in list(step):
                        if key not in ["_id", "description"]:
                            step.pop(key)
            return data
        except (TypeError, AttributeError):
            return data

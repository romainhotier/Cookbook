import copy
from bson import ObjectId

import utils

server = utils.Server()


class PutRecipeSteps(object):
    """ Class to test PutRecipeSteps.
    """

    def __init__(self):
        self.url = 'recipe/steps'
        self.param_id_recipe = "_id_recipe"
        self.param_with_files = "with_files"
        self.param_steps = "steps"
        self.param_description = "description"
        self.rep_code_msg_created = server.rep_code_msg_created.replace("xxx", "recipe")
        self.rep_code_msg_error_400 = server.rep_code_msg_error_400.replace("xxx", "recipe")
        self.rep_code_msg_error_404_url = server.rep_code_msg_error_404.replace("xxx", "cookbook")
        self.detail_true_false = " ['true', 'false']"

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

    def custom_steps(self, recipe, body, rep):
        """ Get Step's ObjectId.

        Parameters
        ----------
        recipe : Any
            RecipeTest.
        body : dict
            Body's request.
        rep : dict
            Server's response.

        Returns
        -------
        dict
            Recipe's Step information.
        """
        steps = copy.deepcopy(recipe.steps)
        if self.param_position in body.keys():
            new_id = self.get_new_id(data=rep["data"], position=body[self.param_position])
            steps.insert(body[self.param_position], {"_id": ObjectId(new_id),
                                                     "description": body[self.param_description]})
        else:
            new_id = rep["data"]["steps"][-1]["_id"]
            steps.append({"_id": ObjectId(new_id), "description": body[self.param_description]})
        return {"steps": steps}

    @staticmethod
    def data_expected(recipe):
        """ Get Step's ObjectId.

        Parameters
        ----------
        recipe : Any
            RecipeTest.

        Returns
        -------
        dict
            Data's response.
        """
        data_expected = recipe.get_stringify()
        return data_expected

    @staticmethod
    def get_new_id(data, position):
        """ Get Step's ObjectId.

        Parameters
        ----------
        data : dict
            Server's response.
        position : int
            Step's position.

        Returns
        -------
        int
            Step's ObjectId
        """
        return data["steps"][position]["_id"]

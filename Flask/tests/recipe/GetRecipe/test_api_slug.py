import unittest
import requests

import utils
import tests.recipe.GetRecipe.api as api
import tests.recipe.model as recipe_model

server = utils.Server()
api = api.GetRecipe()
recipe = recipe_model.RecipeTest()


class GetRecipe(unittest.TestCase):
    
    def setUp(self):
        """ Clean RecipeTest."""
        recipe.clean()

    def test_slug_without(self):
        """ QueryParameter slug is missing.

        Return

            200 - Go to GetAllRecipe.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_recipe2 = recipe_model.RecipeTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(recipe=tc_recipe1).get_data_expected(), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe2).get_data_expected(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_slug_string(self):
        """ QueryParameter slug is a string.

        Return

            400 - Bad request.
        """
        """ env """
        recipe_model.RecipeTest().insert()
        """ param """
        tc_slug = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_doesnot_exist, value=tc_slug)
        self.assertEqual(response_body["detail"], detail)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetRecipe())


if __name__ == '__main__':
    unittest.main()

import unittest
import requests

import utils
import tests.test_recipe.GetAllRecipe.api as api
import tests.test_recipe.model as recipe_model

server = utils.Server()
api = api.GetAllRecipe()
recipe = recipe_model.RecipeTest()


class GetAllRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest."""
        recipe.clean()

    def test_api_ok(self):
        """ Default case.

        Return
            200 - All Recipes.
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

    def test_api_ok_more_param(self):
        """ Default case with more parameters.

        Return
            200 - All Recipes.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_recipe2 = recipe_model.RecipeTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "?invalid=invalid"
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

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        recipe_model.RecipeTest().insert()
        recipe_model.RecipeTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetAllRecipe())


if __name__ == '__main__':
    unittest.main()

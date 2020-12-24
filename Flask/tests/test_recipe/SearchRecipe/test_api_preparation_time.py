import unittest
import requests

import utils
import tests.test_recipe.SearchRecipe.api as api
import tests.test_recipe.model as recipe_model

server = utils.Server()
api = api.SearchRecipe()
recipe = recipe_model.RecipeTest()


class SearchRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest."""
        recipe.clean()

    def test_preparation_time_empty(self):
        """ QueryParameter preparation_time is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        recipe_model.RecipeTest().insert()
        """ param """
        tc_preparation_time = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_preparation_time + "=" + tc_preparation_time
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = api.create_detail(param=api.param_preparation_time, msg=server.detail_must_be_an_integer,
                                   value=tc_preparation_time)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))

    def test_preparation_time_invalid(self):
        """ QueryParameter preparation_time is a string.

        Return
            400 - Bad request.
        """
        """ env """
        recipe_model.RecipeTest().insert()
        """ param """
        tc_preparation_time = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_preparation_time + "=" + tc_preparation_time
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = api.create_detail(param=api.param_preparation_time, msg=server.detail_must_be_an_integer,
                                   value=tc_preparation_time)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))

    def test_preparation_time_ok(self):
        """ QueryParameter preparation_time is a number.

        Return
            200 - Matched Recipe.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().custom({"preparation_time": 5}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"preparation_time": 6}).insert()
        """ param """
        tc_preparation_time = "5"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_preparation_time + "=" + tc_preparation_time
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertNotIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(SearchRecipe())


if __name__ == '__main__':
    unittest.main()

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

    def test_api_ok(self):
        """ Default case.

        Return
            200 - Matched Recipes.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        """ param """
        tc_title = "qa_rhr"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_title + "=" + tc_title
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(recipe=tc_recipe1), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe2), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_api_ok_more_param(self):
        """ Default case with more parameters.

        Return
            200 - Matched Recipes.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b"}).insert()
        """ param """
        tc_title = "qa_rhr"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_title + "=" + tc_title + "&invalid=invalid"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_api_no_param(self):
        """ Default case with no parameter.

        Return
            200 - Go to GetAll.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_recipe2 = recipe_model.RecipeTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "?"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_api_multi_param(self):
        """ Default case with several parameters.

        Return
            200 - Matched Recipes.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a", "level": 5}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b", "level": 5}).insert()
        tc_recipe3 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a", "level": 6}).insert()
        """ param """
        tc_title = "qa_rhr_a"
        tc_level = "5"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_title + "=" + tc_title + "&" + \
            api.param_level + "=" + tc_level
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_stringify(), response_body["data"])
        self.assertNotIn(tc_recipe2.get_stringify(), response_body["data"])
        self.assertNotIn(tc_recipe3.get_stringify(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            200 - Go to GetRecipe.
        """
        """ env """
        recipe_model.RecipeTest().insert()
        """ param """
        tc_title = "qa_rhr"
        """ call api """
        url = server.main_url + "/" + api.url + "x" + "?" + api.param_title + "=" + tc_title
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = api.create_detail(param="slug", msg=server.detail_doesnot_exist, value="searchx")
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(SearchRecipe())


if __name__ == '__main__':
    unittest.main()

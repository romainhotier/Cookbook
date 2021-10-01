import unittest
import requests

from tests import server, rep
from tests.test_recipe import RecipeTest
from tests.test_recipe.GetAllRecipe import api


class TestGetAllRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest."""
        RecipeTest().clean()

    def test_categories_empty(self):
        """ QueryParameter categories is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        RecipeTest().insert()
        """ param """
        tc_categories = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_categories + "=" + tc_categories
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = rep.format_detail(param=api.param_categories, msg=rep.detail_must_be_not_empty, value=tc_categories)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))

    def test_categories_invalid(self):
        """ QueryParameter categories is a string.

        Return
            200 - Matched Recipe.
        """
        """ env """
        tc_recipe1 = RecipeTest().custom({"categories": ["qa_rhr_", "qa_rhr_b", "qa_rhr_c"]}).insert()
        tc_recipe2 = RecipeTest().custom({"categories": ["qa_rhr_a", "qa_rhr_c"]}).insert()
        """ param """
        tc_categories = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_categories + "=" + tc_categories
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertNotIn(api.data_expected(recipe=tc_recipe1), response_body["data"])
        self.assertNotIn(api.data_expected(recipe=tc_recipe2), response_body["data"])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_categories_ok(self):
        """ QueryParameter categories is a ok string.

        Return
            200 - Matched Recipe.
        """
        """ env """
        tc_recipe1 = RecipeTest().custom({"categories": ["qa_rhr_", "qa_rhr_b", "qa_rhr_c"]}).insert()
        tc_recipe2 = RecipeTest().custom({"categories": ["qa_rhr_a", "qa_rhr_c"]}).insert()
        """ param """
        tc_categories = "qa_rhr_b"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_categories + "=" + tc_categories
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(recipe=tc_recipe1), response_body["data"])
        self.assertNotIn(api.data_expected(recipe=tc_recipe2), response_body["data"])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestGetAllRecipe())


if __name__ == '__main__':
    unittest.main()

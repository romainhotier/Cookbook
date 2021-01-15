import unittest
import requests

from tests import server, rep
from tests.test_recipe import RecipeTest
from tests.test_recipe.GetRecipe import api


class TestGetRecipe(unittest.TestCase):
    
    def setUp(self):
        """ Clean RecipeTest."""
        RecipeTest().clean()

    def test_slug_without(self):
        """ QueryParameter slug is missing.

        Return

            200 - Go to GetAllRecipe.
        """
        """ env """
        tc_recipe1 = RecipeTest().insert()
        tc_recipe2 = RecipeTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(recipe=tc_recipe1), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe2), response_body["data"])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_slug_string(self):
        """ QueryParameter slug is a string.

        Return

            400 - Bad request.
        """
        """ env """
        RecipeTest().insert()
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
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_slug, msg=rep.detail_doesnot_exist, value=tc_slug)
        self.assertEqual(response_body["detail"], detail)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestGetRecipe())


if __name__ == '__main__':
    unittest.main()

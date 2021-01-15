import unittest
import requests

from tests import server, rep
from tests.test_recipe import RecipeTest
from tests.test_recipe.GetRecipe import api


class TestGetRecipe(unittest.TestCase):
    
    def setUp(self):
        """ Clean RecipeTest."""
        RecipeTest().clean()

    def test_api_ok(self):
        """ Default case.

        Return
            200 - One Recipe.
        """
        """ env """
        tc_recipe1 = RecipeTest().insert()
        RecipeTest().insert()
        """ param """
        tc_slug = tc_recipe1.slug
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe1))
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_api_ok_more_param(self):
        """ Default case with more parameters.

        Return
            200 - One Recipe.
        """
        """ env """
        tc_recipe1 = RecipeTest().insert()
        RecipeTest().insert()
        """ param """
        tc_slug = tc_recipe1.slug
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug + "?invalid=invalid"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe1))
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - Bad request.
        """
        """ env """
        tc_recipe1 = RecipeTest().insert()
        RecipeTest().insert()
        """ param """
        tc_slug = tc_recipe1.slug
        """ call api """
        url = server.main_url + "/" + api.url + "x/" + tc_slug
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        self.assertEqual(response_body["detail"], rep.detail_url_not_found)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestGetRecipe())


if __name__ == '__main__':
    unittest.main()

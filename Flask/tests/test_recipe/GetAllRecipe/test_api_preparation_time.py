import unittest
import requests

from tests import server, rep
from tests.test_recipe import RecipeTest
from tests.test_recipe.GetAllRecipe import api


class TestGetAllRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest."""
        RecipeTest().clean()

    def test_preparation_time_empty(self):
        """ QueryParameter preparation_time is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        RecipeTest().insert()
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
        detail = rep.format_detail(param=api.param_preparation_time, msg=rep.detail_must_be_an_integer,
                                   value=tc_preparation_time)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))

    def test_preparation_time_invalid(self):
        """ QueryParameter preparation_time is a string.

        Return
            400 - Bad request.
        """
        """ env """
        RecipeTest().insert()
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
        detail = rep.format_detail(param=api.param_preparation_time, msg=rep.detail_must_be_an_integer,
                                   value=tc_preparation_time)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))

    def test_preparation_time_ok(self):
        """ QueryParameter preparation_time is a number.

        Return
            200 - Matched Recipe.
        """
        """ env """
        tc_recipe1 = RecipeTest().custom({"preparation_time": 5}).insert()
        tc_recipe2 = RecipeTest().custom({"preparation_time": 6}).insert()
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
        self.assertIn(api.data_expected(recipe=tc_recipe1), response_body["data"])
        self.assertNotIn(api.data_expected(recipe=tc_recipe2), response_body["data"])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestGetAllRecipe())


if __name__ == '__main__':
    unittest.main()

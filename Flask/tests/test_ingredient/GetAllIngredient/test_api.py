import unittest
import requests

from tests import server, rep
from tests.test_ingredient import IngredientTest
from tests.test_ingredient.GetAllIngredient import api


class TestGetAllIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest."""
        IngredientTest().clean()

    def test_api_ok(self):
        """ Default case.

        Return
            200 - All Ingredient.
        """
        """ env """
        tc_ingredient1 = IngredientTest().insert()
        tc_ingredient2 = IngredientTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_api_ok_more_param(self):
        """ Default case with more parameter.

        Return
            200 - All Ingredient.
        """
        """ env """
        tc_ingredient1 = IngredientTest().insert()
        tc_ingredient2 = IngredientTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "?invalid=invalid"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        IngredientTest().insert()
        IngredientTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        self.assertEqual(response_body["detail"], rep.detail_url_not_found)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestGetAllIngredient())


if __name__ == '__main__':
    unittest.main()

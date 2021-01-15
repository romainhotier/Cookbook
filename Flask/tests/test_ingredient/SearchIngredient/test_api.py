import unittest
import requests

from tests import server, rep
from tests.test_ingredient import IngredientTest
from tests.test_ingredient.SearchIngredient import api


class TestSearchIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest."""
        IngredientTest().clean()

    def test_api_no_param(self):
        """ Default case.

        Return
            200 - Go to GetIngredient.
        """
        """ env """
        tc_ingredient1 = IngredientTest().insert()
        tc_ingredient2 = IngredientTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "?"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_api_more_param(self):
        """ Default case with more parameters.

        Return
            200 - Go to GetIngredient.
        """
        """ env """
        tc_ingredient1 = IngredientTest().custom({"invalid": "invalid"}).insert()
        tc_ingredient2 = IngredientTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "?" + "invalid=invalid"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            400 - Go to GetIngredient.
        """
        """ env """
        IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        """ param """
        tc_name = "qa"
        """ call api """
        url = server.main_url + "/" + api.url + "x" + "?" + api.param_name + "=" + tc_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param="_id", msg=rep.detail_must_be_an_object_id, value="searchx")
        self.assertEqual(response_body["detail"], detail)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestSearchIngredient())


if __name__ == '__main__':
    unittest.main()

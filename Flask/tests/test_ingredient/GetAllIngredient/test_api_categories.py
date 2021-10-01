import unittest
import requests

from tests import server, rep
from tests.test_ingredient import IngredientTest
from tests.test_ingredient.GetAllIngredient import api


class TestGetAllIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest."""
        IngredientTest().clean()

    def test_categories_empty(self):
        """ QueryParameter categories is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        IngredientTest().custom({"categories": ["qa_rhr_a"]}).insert()
        """ param """
        tc_categories = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_categories + "=" + tc_categories
        response = requests.get(url, verify=False)
        response_body = response.json()
        print(url)
        print(response_body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_categories, msg=rep.detail_must_be_not_empty, value=tc_categories)
        self.assertEqual(response_body["detail"], detail)

    def test_categories_invalid(self):
        """ QueryParameter categories is a string.

        Return
            200 - Get Ingredient.
        """
        """ env """
        IngredientTest().custom({"categories": ["qa_rhr_a"]}).insert()
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
        self.assertCountEqual(response_body["data"], [])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_categories_exact(self):
        """ QueryParameter categories is exact.

        Return
            200 - Get Ingredient.
        """
        """ env """
        tc_ingredient1 = IngredientTest().custom({"categories": ["qa_rhr_a"]}).insert()
        IngredientTest().custom({"categories": ["qa_rhr_b"]}).insert()
        """ param """
        tc_categories = tc_ingredient1.categories[0]
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_categories + "=" + tc_categories
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(ingredient=tc_ingredient1)])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_categories_partial(self):
        """ QueryParameter categories is partial.

        Return
            200 - Get Ingredient.
        """
        """ env """
        tc_ingredient1 = IngredientTest().custom({"categories": ["qa_rhr_a"]}).insert()
        tc_ingredient2 = IngredientTest().custom({"categories": ["qa_rhr_b"]}).insert()
        """ param """
        tc_categories = "qa_rhr"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_categories + "=" + tc_categories
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(ingredient=tc_ingredient1),
                                                      api.data_expected(ingredient=tc_ingredient2)])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestGetAllIngredient())


if __name__ == '__main__':
    unittest.main()

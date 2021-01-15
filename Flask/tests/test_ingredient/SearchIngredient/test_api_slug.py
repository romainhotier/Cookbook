import unittest
import requests

from tests import server, rep
from tests.test_ingredient import IngredientTest
from tests.test_ingredient.SearchIngredient import api


class TestSearchIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest."""
        IngredientTest().clean()
        
    def test_slug_empty(self):
        """ QueryParameter slug is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        IngredientTest().custom({"slug": "qa_rhr_a"}).insert()
        """ param """
        tc_slug = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_slug + "=" + tc_slug
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_slug, msg=rep.detail_must_be_not_empty, value=tc_slug)
        self.assertEqual(response_body["detail"], detail)

    def test_slug_invalid(self):
        """ QueryParameter slug is a string.

        Return
            200 - Get Ingredient.
        """
        """ env """
        IngredientTest().custom({"slug": "qa_rhr_a"}).insert()
        """ param """
        tc_slug = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_slug + "=" + tc_slug
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_slug_exact(self):
        """ QueryParameter slug is exact.

        Return
            200 - Get Ingredient.
        """
        """ env """
        tc_ingredient1 = IngredientTest().custom({"slug": "qa_rhr_a"}).insert()
        IngredientTest().custom({"slug": "qa_rhr_b"}).insert()
        """ param """
        tc_slug = tc_ingredient1.slug
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_slug + "=" + tc_slug
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(ingredient=tc_ingredient1)])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_slug_partial(self):
        """ QueryParameter slug is partial.

        Return
            200 - Get Ingredient.
        """
        """ env """
        tc_ingredient1 = IngredientTest().custom({"slug": "qa_rhr_a"}).insert()
        tc_ingredient2 = IngredientTest().custom({"slug": "qa_rhr_b"}).insert()
        """ param """
        tc_slug = "qa_rhr"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_slug + "=" + tc_slug
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
        cls.setUp(TestSearchIngredient())


if __name__ == '__main__':
    unittest.main()

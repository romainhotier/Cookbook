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

    def test_api_ok_complex_search_asc(self):
        """ Default case with complex search.

        Return
            200 - Matching Ingredient.
        """
        """ env """
        tc_ingredient1 = IngredientTest().custom({"name": "aaa_qa_rhr_tata", "slug": "aaa1"}).insert()
        tc_ingredient2 = IngredientTest().custom({"name": "zzz_qa_rhr_tata", "slug": "aaa2"}).insert()
        tc_ingredient3 = IngredientTest().custom({"name": "bbb_qa_rhr_tata", "slug": "aaa3"}).insert()
        tc_ingredient4 = IngredientTest().custom({"name": "aaa_qa_rhr_tutu", "slug": "bbb1"}).insert()
        tc_ingredient5 = IngredientTest().custom({"name": "zzz_qa_rhr_tutu", "slug": "bbb2"}).insert()
        tc_ingredient6 = IngredientTest().custom({"name": "bbb_qa_rhr_tutu", "slug": "bbb3"}).insert()
        tc_ingredient7 = IngredientTest().custom({"name": "eee_qa_rhr_tata", "slug": "ccc1"}).insert()
        tc_ingredient8 = IngredientTest().custom({"name": "eee_qa_rhr_tutu", "slug": "ccc2"}).insert()
        """ param """
        tc_name = "tutu"
        tc_slug = "bb"
        tc_order_by = "name"
        tc_order = "asc"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + \
            api.param_name + "=" + tc_name + "&" + \
            api.param_order_by + "=" + tc_order_by + "&" +\
            api.param_slug + "=" + tc_slug + "&" +\
            api.param_order + "=" + tc_order + "&" + \
            "&invalid=invalid"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertNotIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertNotIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertNotIn(api.data_expected(ingredient=tc_ingredient3), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient4), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient5), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient6), response_body["data"])
        self.assertNotIn(api.data_expected(ingredient=tc_ingredient7), response_body["data"])
        self.assertNotIn(api.data_expected(ingredient=tc_ingredient8), response_body["data"])
        self.assertEqual(api.check_order("name", response_body["data"]),
                         [tc_ingredient4.name, tc_ingredient6.name, tc_ingredient5.name])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_api_ok_complex_search_desc(self):
        """ Default case with complex search.

        Return
            200 - Matching Ingredient.
        """
        """ env """
        tc_ingredient1 = IngredientTest().custom({"name": "aaa_qa_rhr_tata", "slug": "aaa1"}).insert()
        tc_ingredient2 = IngredientTest().custom({"name": "zzz_qa_rhr_tata", "slug": "aaa2"}).insert()
        tc_ingredient3 = IngredientTest().custom({"name": "bbb_qa_rhr_tata", "slug": "aaa3"}).insert()
        tc_ingredient4 = IngredientTest().custom({"name": "aaa_qa_rhr_tutu", "slug": "bbb1"}).insert()
        tc_ingredient5 = IngredientTest().custom({"name": "zzz_qa_rhr_tutu", "slug": "bbb2"}).insert()
        tc_ingredient6 = IngredientTest().custom({"name": "bbb_qa_rhr_tutu", "slug": "bbb3"}).insert()
        tc_ingredient7 = IngredientTest().custom({"name": "eee_qa_rhr_tata", "slug": "ccc1"}).insert()
        tc_ingredient8 = IngredientTest().custom({"name": "eee_qa_rhr_tutu", "slug": "ccc2"}).insert()
        """ param """
        tc_name = "tutu"
        tc_slug = "bb"
        tc_order_by = "name"
        tc_order = "desc"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + \
            api.param_name + "=" + tc_name + "&" + \
            api.param_order_by + "=" + tc_order_by + "&" +\
            api.param_slug + "=" + tc_slug + "&" +\
            api.param_order + "=" + tc_order + "&" + \
            "&invalid=invalid"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertNotIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertNotIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertNotIn(api.data_expected(ingredient=tc_ingredient3), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient4), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient5), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient6), response_body["data"])
        self.assertNotIn(api.data_expected(ingredient=tc_ingredient7), response_body["data"])
        self.assertNotIn(api.data_expected(ingredient=tc_ingredient8), response_body["data"])
        self.assertEqual(api.check_order("name", response_body["data"]),
                         [tc_ingredient5.name, tc_ingredient6.name, tc_ingredient4.name])
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

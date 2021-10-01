import unittest
import requests

from tests import server, rep
from tests.test_ingredient import IngredientTest
from tests.test_ingredient.GetAllIngredient import api


class TestGetAllIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest."""
        IngredientTest().clean()

    def test_order_empty(self):
        """ QueryParameter order is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        IngredientTest().custom({"name": "aaa_qa_rhr"}).insert()
        """ param """
        tc_order = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_order + "=" + tc_order
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_order, msg=rep.detail_must_be_not_empty, value=tc_order)
        self.assertEqual(response_body["detail"], detail)

    def test_order_invalid(self):
        """ QueryParameter order is an string.

        Return
            400 - Bad request.
        """
        """ env """
        IngredientTest().custom({"name": "aaa_qa_rhr"}).insert()
        """ param """
        tc_order = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_order + "=" + tc_order
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_order, msg=rep.detail_must_be_in+api.detail_order,
                                   value=tc_order)
        self.assertEqual(response_body["detail"], detail)

    def test_order_asc(self):
        """ Order Ingredient ascending.

        Return
            200 - All Ingredient ordered.
        """
        """ env """
        tc_ingredient1 = IngredientTest().custom({"name": "aaa_qa_rhr"}).insert()
        tc_ingredient2 = IngredientTest().custom({"name": "zzz_qa_rhr"}).insert()
        tc_ingredient3 = IngredientTest().custom({"name": "bbb_qa_rhr"}).insert()
        """ param """
        tc_order_by = "name"
        tc_order = "asc"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_order_by + "=" + tc_order_by + "&" + \
            api.param_order + "=" + tc_order
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient3), response_body["data"])
        self.assertEqual(api.check_order("name", response_body["data"]),
                         [tc_ingredient1.name, tc_ingredient3.name, tc_ingredient2.name])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_order_desc(self):
        """ Order Ingredient descending.

        Return
            200 - All Ingredient ordered.
        """
        """ env """
        tc_ingredient1 = IngredientTest().custom({"name": "aaa_qa_rhr"}).insert()
        tc_ingredient2 = IngredientTest().custom({"name": "zzz_qa_rhr"}).insert()
        tc_ingredient3 = IngredientTest().custom({"name": "bbb_qa_rhr"}).insert()
        """ param """
        tc_order_by = "name"
        tc_order = "desc"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_order_by + "=" + tc_order_by + "&" + \
            api.param_order + "=" + tc_order
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient3), response_body["data"])
        self.assertEqual(api.check_order("name", response_body["data"]),
                         [tc_ingredient2.name, tc_ingredient3.name, tc_ingredient1.name])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestGetAllIngredient())


if __name__ == '__main__':
    unittest.main()

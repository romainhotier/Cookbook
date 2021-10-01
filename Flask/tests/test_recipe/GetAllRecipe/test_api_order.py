import unittest
import requests

from tests import server, rep
from tests.test_recipe import RecipeTest
from tests.test_recipe.GetAllRecipe import api


class TestGetAllRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest."""
        RecipeTest().clean()

    def test_order_empty(self):
        """ QueryParameter order is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        RecipeTest().insert()
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
        detail = rep.format_detail(param=api.param_order, msg=rep.detail_must_be_not_empty, value=tc_order)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))

    def test_order_invalid(self):
        """ QueryParameter order is a string.

        Return
            400 - Bad request.
        """
        """ env """
        RecipeTest().insert()
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
        detail = rep.format_detail(param=api.param_order, msg=rep.detail_must_be_in+api.detail_order, value=tc_order)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))

    def test_order_asc(self):
        """ Order Recipe by title asc.

        Return
            200 - All Recipe ordered by title.
        """
        """ env """
        tc_recipe1 = RecipeTest().custom({"title": "aaa_qa_rhr"}).insert()
        tc_recipe2 = RecipeTest().custom({"title": "zzz_qa_rhr"}).insert()
        tc_recipe3 = RecipeTest().custom({"title": "bbb_qa_rhr"}).insert()
        """ param """
        tc_order = "asc"
        tc_order_by = "title"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_order_by + "=" + tc_order_by + "&" + \
            api.param_order + "=" + tc_order
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(recipe=tc_recipe1), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe2), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe3), response_body["data"])
        self.assertEqual(api.check_order("title", response_body["data"]),
                         [tc_recipe1.title, tc_recipe3.title, tc_recipe2.title])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_order_desc(self):
        """ Order Recipe by title desc.

        Return
            200 - All Recipe ordered by title.
        """
        """ env """
        tc_recipe1 = RecipeTest().custom({"title": "aaa_qa_rhr"}).insert()
        tc_recipe2 = RecipeTest().custom({"title": "zzz_qa_rhr"}).insert()
        tc_recipe3 = RecipeTest().custom({"title": "bbb_qa_rhr"}).insert()
        """ param """
        tc_order = "desc"
        tc_order_by = "title"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_order_by + "=" + tc_order_by + "&" + \
            api.param_order + "=" + tc_order
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(recipe=tc_recipe1), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe2), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe3), response_body["data"])
        self.assertEqual(api.check_order("title", response_body["data"]),
                         [tc_recipe2.title, tc_recipe3.title, tc_recipe1.title])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestGetAllRecipe())


if __name__ == '__main__':
    unittest.main()

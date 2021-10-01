import unittest
import requests

from tests import server, rep
from tests.test_recipe import RecipeTest
from tests.test_recipe.GetAllRecipe import api


class TestGetAllRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest."""
        RecipeTest().clean()

    def test_api_ok(self):
        """ Default case.

        Return
            200 - All Recipes.
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

    def test_api_ok_more_param(self):
        """ Default case with more parameters.

        Return
            200 - All Recipes.
        """
        """ env """
        tc_recipe1 = RecipeTest().insert()
        tc_recipe2 = RecipeTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "?invalid=invalid"
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

    def test_api_ok_complex_search_asc(self):
        """ Default case with complex search.

        Return
            200 - Matching Recipes.
        """
        """ env """
        tc_recipe1 = RecipeTest().custom({"title": "aaa_qa_rhr_tata", "slug": "aaa1"}).insert()
        tc_recipe2 = RecipeTest().custom({"title": "zzz_qa_rhr_tata", "slug": "aaa2"}).insert()
        tc_recipe3 = RecipeTest().custom({"title": "bbb_qa_rhr_tata", "slug": "aaa3"}).insert()
        tc_recipe4 = RecipeTest().custom({"title": "aaa_qa_rhr_tutu", "slug": "bbb1"}).insert()
        tc_recipe5 = RecipeTest().custom({"title": "zzz_qa_rhr_tutu", "slug": "bbb1"}).insert()
        tc_recipe6 = RecipeTest().custom({"title": "bbb_qa_rhr_tutu", "slug": "bbb1"}).insert()
        tc_recipe7 = RecipeTest().custom({"title": "eee_qa_rhr_tata", "slug": "ccc1"}).insert()
        tc_recipe8 = RecipeTest().custom({"title": "eee_qa_rhr_tutu", "slug": "ccc2"}).insert()
        """ param """
        tc_title = "tutu"
        tc_slug = "bb"
        tc_order_by = "title"
        tc_order = "asc"
        tc_with_calories = "true"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + \
            api.param_title + "=" + tc_title + "&" + \
            api.param_order_by + "=" + tc_order_by + "&" +\
            api.param_slug + "=" + tc_slug + "&" +\
            api.param_order + "=" + tc_order + "&" + \
            api.param_with_calories + "=" + tc_with_calories + "&" + \
            "&invalid=invalid"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertNotIn(api.data_expected(recipe=tc_recipe1, calories=True), response_body["data"])
        self.assertNotIn(api.data_expected(recipe=tc_recipe2, calories=True), response_body["data"])
        self.assertNotIn(api.data_expected(recipe=tc_recipe3, calories=True), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe4, calories=True), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe5, calories=True), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe6, calories=True), response_body["data"])
        self.assertNotIn(api.data_expected(recipe=tc_recipe7, calories=True), response_body["data"])
        self.assertNotIn(api.data_expected(recipe=tc_recipe8, calories=True), response_body["data"])
        self.assertEqual(api.check_order("title", response_body["data"]),
                         [tc_recipe4.title, tc_recipe6.title, tc_recipe5.title])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_api_ok_complex_search_desc(self):
        """ Default case with complex search.

        Return
            200 - Matching Recipes.
        """
        """ env """
        tc_recipe1 = RecipeTest().custom({"title": "aaa_qa_rhr_tata", "slug": "aaa1"}).insert()
        tc_recipe2 = RecipeTest().custom({"title": "zzz_qa_rhr_tata", "slug": "aaa2"}).insert()
        tc_recipe3 = RecipeTest().custom({"title": "bbb_qa_rhr_tata", "slug": "aaa3"}).insert()
        tc_recipe4 = RecipeTest().custom({"title": "aaa_qa_rhr_tutu", "slug": "bbb1"}).insert()
        tc_recipe5 = RecipeTest().custom({"title": "zzz_qa_rhr_tutu", "slug": "bbb1"}).insert()
        tc_recipe6 = RecipeTest().custom({"title": "bbb_qa_rhr_tutu", "slug": "bbb1"}).insert()
        tc_recipe7 = RecipeTest().custom({"title": "eee_qa_rhr_tata", "slug": "ccc1"}).insert()
        tc_recipe8 = RecipeTest().custom({"title": "eee_qa_rhr_tutu", "slug": "ccc2"}).insert()
        """ param """
        tc_title = "tutu"
        tc_slug = "bb"
        tc_order_by = "title"
        tc_order = "desc"
        tc_with_calories = "true"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + \
            api.param_title + "=" + tc_title + "&" + \
            api.param_order_by + "=" + tc_order_by + "&" +\
            api.param_slug + "=" + tc_slug + "&" +\
            api.param_order + "=" + tc_order + "&" + \
            api.param_with_calories + "=" + tc_with_calories + "&" + \
            "&invalid=invalid"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertNotIn(api.data_expected(recipe=tc_recipe1, calories=True), response_body["data"])
        self.assertNotIn(api.data_expected(recipe=tc_recipe2, calories=True), response_body["data"])
        self.assertNotIn(api.data_expected(recipe=tc_recipe3, calories=True), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe4, calories=True), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe5, calories=True), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe6, calories=True), response_body["data"])
        self.assertNotIn(api.data_expected(recipe=tc_recipe7, calories=True), response_body["data"])
        self.assertNotIn(api.data_expected(recipe=tc_recipe8, calories=True), response_body["data"])
        self.assertEqual(api.check_order("title", response_body["data"]),
                         [tc_recipe5.title, tc_recipe6.title, tc_recipe4.title])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        RecipeTest().insert()
        RecipeTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body["detail"], rep.detail_url_not_found)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestGetAllRecipe())


if __name__ == '__main__':
    unittest.main()

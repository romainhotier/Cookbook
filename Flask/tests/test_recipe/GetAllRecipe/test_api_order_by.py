import unittest
import requests

from tests import server, rep
from tests.test_recipe import RecipeTest
from tests.test_recipe.GetAllRecipe import api


class TestGetAllRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest."""
        RecipeTest().clean()

    def test_order_by_empty(self):
        """ QueryParameter orderBy is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        RecipeTest().insert()
        """ param """
        tc_order_by = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_order_by + "=" + tc_order_by
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = rep.format_detail(param=api.param_order_by, msg=rep.detail_must_be_not_empty, value=tc_order_by)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))

    def test_order_by_invalid(self):
        """ QueryParameter orderBy is a string.

        Return
            400 - Bad request.
        """
        """ env """
        RecipeTest().insert()
        """ param """
        tc_order_by = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_order_by + "=" + tc_order_by
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = rep.format_detail(param=api.param_order_by, msg=rep.detail_must_be_in+api.detail_order_by,
                                   value=tc_order_by)
        self.assertEqual(response_body["detail"], detail)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))

    def test_order_by_title(self):
        """ Order Recipe by title.

        Return
            200 - All Recipe ordered by title.
        """
        """ env """
        tc_recipe1 = RecipeTest().custom({"title": "aaa_qa_rhr"}).insert()
        tc_recipe2 = RecipeTest().custom({"title": "zzz_qa_rhr"}).insert()
        tc_recipe3 = RecipeTest().custom({"title": "bbb_qa_rhr"}).insert()
        """ param """
        tc_order_by = "title"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_order_by + "=" + tc_order_by
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

    def test_order_by_slug(self):
        """ Order Recipe by slug.

        Return
            200 - All Recipe ordered by slug.
        """
        """ env """
        tc_recipe1 = RecipeTest().custom({"slug": "aaa_qa_rhr"}).insert()
        tc_recipe2 = RecipeTest().custom({"slug": "zzz_qa_rhr"}).insert()
        tc_recipe3 = RecipeTest().custom({"slug": "bbb_qa_rhr"}).insert()
        """ param """
        tc_order_by = "slug"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_order_by + "=" + tc_order_by
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
        self.assertEqual(api.check_order("slug", response_body["data"]),
                         [tc_recipe1.slug, tc_recipe3.slug, tc_recipe2.slug])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_order_by_level(self):
        """ Order Recipe by level.

        Return
            200 - All Recipe ordered by level.
        """
        """ env """
        tc_recipe1 = RecipeTest().custom({"level": 1}).insert()
        tc_recipe2 = RecipeTest().custom({"level": 5}).insert()
        tc_recipe3 = RecipeTest().custom({"level": 3}).insert()
        """ param """
        tc_order_by = "level"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_order_by + "=" + tc_order_by
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
        self.assertEqual(api.check_order("level", response_body["data"]),
                         [tc_recipe1.level, tc_recipe3.level, tc_recipe2.level])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_order_by_cooking_time(self):
        """ Order Recipe by cooking_time.

        Return
            200 - All Recipe ordered by cooking_time.
        """
        """ env """
        tc_recipe1 = RecipeTest().custom({"cooking_time": 1}).insert()
        tc_recipe2 = RecipeTest().custom({"cooking_time": 5}).insert()
        tc_recipe3 = RecipeTest().custom({"cooking_time": 3}).insert()
        """ param """
        tc_order_by = "cooking_time"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_order_by + "=" + tc_order_by
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
        self.assertEqual(api.check_order("cooking_time", response_body["data"]),
                         [tc_recipe1.cooking_time, tc_recipe3.cooking_time, tc_recipe2.cooking_time])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_order_by_preparation_time(self):
        """ Order Recipe by preparation_time.

        Return
            200 - All Recipe ordered by preparation_time.
        """
        """ env """
        tc_recipe1 = RecipeTest().custom({"preparation_time": 1}).insert()
        tc_recipe2 = RecipeTest().custom({"preparation_time": 5}).insert()
        tc_recipe3 = RecipeTest().custom({"preparation_time": 3}).insert()
        """ param """
        tc_order_by = "preparation_time"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_order_by + "=" + tc_order_by
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
        self.assertEqual(api.check_order("preparation_time", response_body["data"]),
                         [tc_recipe1.preparation_time, tc_recipe3.preparation_time, tc_recipe2.preparation_time])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_order_by_nb_people(self):
        """ Order Recipe by nb_people.

        Return
            200 - All Recipe ordered by nb_people.
        """
        """ env """
        tc_recipe1 = RecipeTest().custom({"nb_people": 1}).insert()
        tc_recipe2 = RecipeTest().custom({"nb_people": 5}).insert()
        tc_recipe3 = RecipeTest().custom({"nb_people": 3}).insert()
        """ param """
        tc_order_by = "nb_people"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_order_by + "=" + tc_order_by
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
        self.assertEqual(api.check_order("nb_people", response_body["data"]),
                         [tc_recipe1.nb_people, tc_recipe3.nb_people, tc_recipe2.nb_people])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestGetAllRecipe())


if __name__ == '__main__':
    unittest.main()

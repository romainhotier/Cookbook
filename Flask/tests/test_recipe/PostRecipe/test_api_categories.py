import unittest
import requests

from tests import server, rep
from tests.test_recipe import RecipeTest
from tests.test_recipe.PostRecipe import api


class TestPostRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest and FileTest."""
        RecipeTest().clean()

    def test_categories_without(self):
        """ BodyParameter categories is missing.

        Return
            201 - Inserted Recipe.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = RecipeTest().custom_from_body(data=body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = rep.json_schema_check(data=response_body["data"], schema=api.create_schema(recipe=tc_recipe))
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_recipe.custom_id_from_body(data=response_body).check_bdd_data()

    def test_categories_none(self):
        """ BodyParameter categories is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_categories: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = RecipeTest().custom_from_body(data=body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_categories, msg=rep.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_categories_empty(self):
        """ BodyParameter categories is an empty string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_categories: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = RecipeTest().custom_from_body(data=body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_categories, msg=rep.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_categories_string(self):
        """ BodyParameter categories is a string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_categories: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = RecipeTest().custom_from_body(data=body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_categories, msg=rep.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_categories_tab(self):
        """ BodyParameter categories is an empty tab.

        Return
            201 - Inserted Recipe.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_categories: []}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = RecipeTest().custom_from_body(data=body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = rep.json_schema_check(data=response_body["data"], schema=api.create_schema(recipe=tc_recipe))
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_recipe.custom_id_from_body(data=response_body).check_bdd_data()

    def test_categories_object(self):
        """ BodyParameter categories is an empty object.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_categories: {}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = RecipeTest().custom_from_body(data=body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_categories, msg=rep.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestPostRecipe())


if __name__ == '__main__':
    unittest.main()

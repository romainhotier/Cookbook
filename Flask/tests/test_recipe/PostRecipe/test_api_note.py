import unittest
import requests

from tests import server, rep
from tests.test_recipe import RecipeTest
from tests.test_recipe.PostRecipe import api


class TestPostRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest and FileTest."""
        RecipeTest().clean()

    def test_note_without(self):
        """ BodyParameter note is missing.

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

    def test_note_none(self):
        """ BodyParameter note is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_note: None}
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
        detail = rep.format_detail(param=api.param_note, msg=rep.detail_must_be_a_string, value=body[api.param_note])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_note_empty(self):
        """ BodyParameter note is an empty string.

        Return
            201 - Inserted Recipe.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_note: ""}
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

    def test_note_string(self):
        """ BodyParameter note is a string.

        Return
            201 - Inserted Recipe.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_note: "invalid"}
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

    def test_note_tab(self):
        """ BodyParameter note is an empty tab.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_note: []}
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
        detail = rep.format_detail(param=api.param_note, msg=rep.detail_must_be_a_string, value=body[api.param_note])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_note_object(self):
        """ BodyParameter note is an empty object.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_note: {}}
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
        detail = rep.format_detail(param=api.param_note, msg=rep.detail_must_be_a_string, value=body[api.param_note])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestPostRecipe())


if __name__ == '__main__':
    unittest.main()

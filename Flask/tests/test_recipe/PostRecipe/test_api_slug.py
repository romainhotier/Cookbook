import unittest
import requests

import utils
import tests.test_recipe.PostRecipe.api as api
import tests.test_recipe.model as recipe_model

server = utils.Server()
api = api.PostRecipe()
recipe = recipe_model.RecipeTest()


class PostRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest and FileTest."""
        recipe.clean()

    def test_slug_without(self):
        """ BodyParameter slug is missing.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_slug_none(self):
        """ BodyParameter slug is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_must_be_a_string, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_slug_empty(self):
        """ BodyParameter slug is an empty string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_slug_string(self):
        """ BodyParameter slug is a string.

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
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.custom_id_from_body(data=response_body).check_bdd_data()

    def test_slug_tab(self):
        """ BodyParameter slug is an empty tab.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: []}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_must_be_a_string, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_slug_object(self):
        """ BodyParameter slug is an empty object.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: {}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_must_be_a_string, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_slug_already_exist(self):
        """ BodyParameter slug already exist.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title_2",
                api.param_slug: tc_recipe.slug}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_already_exist, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostRecipe())


if __name__ == '__main__':
    unittest.main()

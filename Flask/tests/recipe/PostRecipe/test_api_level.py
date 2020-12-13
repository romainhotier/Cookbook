import unittest
import requests

import utils
import tests.recipe.PostRecipe.api as api
import tests.recipe.model as recipe_model

server = utils.Server()
api = api.PostRecipe()
recipe = recipe_model.RecipeTest()


class PostRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest and FileTest."""
        recipe.clean()

    def test_level_without(self):
        """ BodyParameter level is missing.

        Return
            400 - Bad request.
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

    def test_level_none(self):
        """ BodyParameter level is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: None}
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
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer, 
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_level_empty(self):
        """ BodyParameter level is an empty string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: ""}
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
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_level_string(self):
        """ BodyParameter level is a string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: "invalid"}
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
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_level_integer_min_over(self):
        """ BodyParameter level is min-1.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: 5}
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
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_between + " 0 and 3",
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_level_integer_min(self):
        """ BodyParameter level is min.

        Return
            201 - Inserted Recipe.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: 0}
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

    def test_level_integer_max(self):
        """ BodyParameter level is max.

        Return
            201 - Inserted Recipe.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: 3}
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

    def test_level_integer_max_over(self):
        """ BodyParameter level is max+1.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: 4}
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
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_between + " 0 and 3",
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_level_tab(self):
        """ BodyParameter level is an empty tab.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: []}
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
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_level_object(self):
        """ BodyParameter level is an empty object.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_level: {}}
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
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostRecipe())


if __name__ == '__main__':
    unittest.main()

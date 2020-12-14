import unittest
import requests

import utils
import tests.ingredient.PostIngredient.api as api
import tests.ingredient.model as ingredient_model

server = utils.Server()
api = api.PostIngredient()
ingredient = ingredient_model.IngredientTest()


class PostIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest."""
        ingredient.clean()

    def test_name_without(self):
        """ BodyParameter name is missing.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_slug: "qa_rhr_slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_name, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_name_none(self):
        """ BodyParameter name is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: None,
                api.param_slug: "qa_rhr_slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_name, msg=server.detail_must_be_a_string, value=body[api.param_name])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_name_empty(self):
        """ BodyParameter name is an empty string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_name: "",
                api.param_slug: "qa_rhr_slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_name, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_name])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_doesnt_exist_by_name()

    def test_name_string(self):
        """ BodyParameter name is a string.

        Return
            201 - Inserted Ingredient.
        """
        """ param """
        body = {api.param_name: "qa_rhr_name",
                api.param_slug: "qa_rhr_slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient = ingredient_model.IngredientTest().custom(api.custom_body(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient.custom_id_from_body(data=response_body).check_bdd_data()

    def test_name_already_exist(self):
        """ BodyParameter name already exist.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_name: tc_ingredient.name,
                api.param_slug: "qa_rhr_slug_2nd"}
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
        detail = api.create_detail(param=api.param_name, msg=server.detail_already_exist, value=body[api.param_name])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostIngredient())


if __name__ == '__main__':
    unittest.main()

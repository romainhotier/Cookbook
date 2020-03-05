import unittest
import requests

from server import factory as factory
import app.ingredient.ingredient.model as ingredient_model
import app.ingredient.ingredient.test.PostIngredient.api as api

server = factory.Server()
api = api.PostIngredient()
ingredient = ingredient_model.IngredientTest()


class PostIngredient(unittest.TestCase):

    def setUp(self):
        ingredient.clean()

    def test_0_api_ok(self):
        body = {api.param_name: "qa_rhr_name"}
        tc_ingredient = ingredient_model.IngredientTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_ingredient.get_data_without_id())
        """ refacto """
        tc_ingredient.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_0_api_ok_more_param(self):
        body = {api.param_name: "qa_rhr_name",
                "invalid": "invalid"}
        tc_ingredient = ingredient_model.IngredientTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_ingredient.get_data_without_id())
        """ refacto """
        tc_ingredient.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_1_url_not_found(self):
        body = {api.param_name: "qa_rhr_name"}
        tc_ingredient = ingredient_model.IngredientTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_ingredient.select_nok_by_name()

    def test_2_name_without(self):
        body = {}
        tc_ingredient = ingredient_model.IngredientTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_name, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_ingredient.select_nok_by_name()

    def test_2_name_none(self):
        body = {api.param_name: None}
        tc_ingredient = ingredient_model.IngredientTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_name, server.detail_must_be_a_string, body[api.param_name])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_ingredient.select_nok_by_name()

    def test_2_name_empty(self):
        body = {api.param_name: ""}
        tc_ingredient = ingredient_model.IngredientTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_name, server.detail_must_be_not_empty, body[api.param_name])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_ingredient.select_nok_by_name()

    def test_2_name_string(self):
        body = {api.param_name: "qa_rhr_name"}
        tc_ingredient = ingredient_model.IngredientTest().custom(body)
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_ingredient.get_data_without_id())
        """ refacto """
        tc_ingredient.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_3_name_already_exist(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        body = {api.param_name: tc_ingredient.get_data_value("name")}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_name, server.detail_already_exist, body[api.param_name])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_ingredient.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostIngredient())


if __name__ == '__main__':
    unittest.main()

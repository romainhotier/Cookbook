import unittest
import requests

import factory as factory
import ingredient.model as ingredient_model
import ingredient.test.PutIngredient.api as api

server = factory.Server()
api = api.PutIngredient()
ingredient = ingredient_model.IngredientTest()


class PutIngredient(unittest.TestCase):

    def setUp(self):
        ingredient.clean()

    def test_0_api_ok(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom_test({"name": "b"}).insert()
        tc_id = tc_ingredient1.get_id()
        body = {api.param_name: "qa_rhr_name_update"}
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient1.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_ingredient1.get_data_stringify_object_id())
        """ refacto """
        tc_ingredient1.select_ok()
        tc_ingredient2.select_ok()

    def test_0_api_ok_more_param(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_name: "qa_rhr_name_update",
                "invalid": "invalid"}
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_ingredient.get_data_stringify_object_id())
        """ refacto """
        tc_ingredient.select_ok()

    def test_1_url_not_found(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_name: "qa_rhr_name_update"}
        """ cal api """
        url = server.main_url + "/" + api.url + "x/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_ingredient.select_ok()

    def test_2_id_without(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        body = {api.param_name: "qa_rhr_name_update"}
        """ cal api """
        url = server.main_url + "/" + api.url + "/"
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_ingredient.select_ok()

    def test_2_id_string(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = "invalid"
        body = {api.param_name: "qa_rhr_name_update"}
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id, server.detail_must_be_an_object_id, tc_id)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_ingredient.select_ok()

    def test_2_id_object_id_invalid(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        body = {api.param_name: "qa_rhr_name_update"}
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], [])
        tc_ingredient.select_ok()

    def test_3_name_without(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = tc_ingredient.get_id()
        body = {}
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_name, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_ingredient.select_ok()

    def test_3_name_none(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_name: None}
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_name, server.detail_must_be_a_string, body[api.param_name])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_ingredient.select_ok()

    def test_3_name_empty(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_name: ""}
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_name, server.detail_must_be_not_empty, body[api.param_name])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_ingredient.select_ok()

    def test_3_name_string(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_name: "qa_rhr_name_update"}
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_ingredient.get_data_stringify_object_id())
        """ refacto """
        tc_ingredient.select_ok()

    def test_4_name_already_exist(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom_test({"name": "b"}).insert()
        tc_id = tc_ingredient1.get_id()
        body = {api.param_name: tc_ingredient2.get_data_value("name")}
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_name, server.detail_already_exist, body[api.param_name])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_ingredient1.select_ok()
        tc_ingredient2.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PutIngredient())


if __name__ == '__main__':
    unittest.main()

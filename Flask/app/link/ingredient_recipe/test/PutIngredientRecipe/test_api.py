import unittest
import requests

import server.server as server
import app.link.ingredient_recipe.model as link_model
import app.link.ingredient_recipe.test.PutIngredientRecipe.api as api

server = server.Server()
api = api.PutIngredientRecipe()
link = link_model.LinkIngredientRecipeTest()


class PutIngredientRecipe(unittest.TestCase):

    def setUp(self):
        link.clean()

    def test_0_api_ok(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = tc_link.get_id()
        body = {api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit_up"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_link.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_link.get_data_stringify_object_id())
        tc_link.select_ok()

    def test_0_api_ok_more_param(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = tc_link.get_id()
        body = {api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit_up",
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_link.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_link.get_data_stringify_object_id())
        tc_link.select_ok()

    def test_1_url_not_found(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = tc_link.get_id()
        body = {api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit_up"}
        """ call api """
        url = server.main_url + "/x" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_link.select_ok()

    def test_2_id_without(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        body = {api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit_up"}
        """ call api """
        url = server.main_url + "/" + api.url + "/"
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_link.select_ok()

    def test_2_id_string(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = "invalid"
        body = {api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit_up"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id, server.detail_must_be_an_object_id, tc_id)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_ok()

    def test_2_id_object_id_invalid(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        body = {api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit_up"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id, server.detail_doesnot_exist, tc_id)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_ok()

    def test_3_quantity_without(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = tc_link.get_id()
        body = {api.param_unit: "qa_rhr_unit_up"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_link.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_link.get_data_stringify_object_id())
        tc_link.select_ok()

    def test_3_quantity_null(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = tc_link.get_id()
        body = {api.param_quantity: None,
                api.param_unit: "qa_rhr_unit_up"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_quantity, server.detail_must_be_an_integer, body[api.param_quantity])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_ok()

    def test_3_quantity_empty(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = tc_link.get_id()
        body = {api.param_quantity: "",
                api.param_unit: "qa_rhr_unit_up"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_quantity, server.detail_must_be_an_integer, body[api.param_quantity])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_ok()

    def test_3_quantity_string(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = tc_link.get_id()
        body = {api.param_quantity: "invalid",
                api.param_unit: "qa_rhr_unit_up"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_quantity, server.detail_must_be_an_integer, body[api.param_quantity])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_ok()

    def test_4_unit_without(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = tc_link.get_id()
        body = {api.param_quantity: 5}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_link.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_link.get_data_stringify_object_id())
        tc_link.select_ok()

    def test_4_unit_null(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = tc_link.get_id()
        body = {api.param_quantity: 5,
                api.param_unit: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_unit, server.detail_must_be_a_string, body[api.param_unit])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_ok()

    def test_4_unit_empty(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = tc_link.get_id()
        body = {api.param_quantity: 5,
                api.param_unit: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_link.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_link.get_data_stringify_object_id())
        tc_link.select_ok()

    def test_4_unit_string(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = tc_link.get_id()
        body = {api.param_quantity: 5,
                api.param_unit: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_link.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_link.get_data_stringify_object_id())
        tc_link.select_ok()

    def test_5_without_nothing(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = tc_link.get_id()
        body = {}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_link.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail("body", server.detail_must_contain_at_least_one_key, body)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PutIngredientRecipe())


if __name__ == '__main__':
    unittest.main()

import unittest
import requests

from server import factory as factory
import app.ingredient.ingredient.model as ingredient_model
import app.file.file.model as file_model
import app.ingredient.ingredient.test.PutIngredient.api as api

server = factory.Server()
api = api.PutIngredient()
ingredient = ingredient_model.IngredientTest()
file = file_model.FileTest()


class PutIngredient(unittest.TestCase):

    def setUp(self):
        ingredient.clean()
        file.clean()

    def test_0_api_ok(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom_test({"name": "b"}).insert()
        tc_id = tc_ingredient1.get_id()
        body = {api.param_name: "qa_rhr_name_update"}
        """ call api """
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
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?invalid=invalid"
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
        """ call api """
        url = server.main_url + "/" + api.url + "x/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_ingredient.select_ok()

    def test_2_id_without(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        body = {api.param_name: "qa_rhr_name_update"}
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
        tc_ingredient.select_ok()

    def test_2_id_string(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = "invalid"
        body = {api.param_name: "qa_rhr_name_update"}
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
        tc_ingredient.select_ok()

    def test_2_id_object_id_invalid(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        body = {api.param_name: "qa_rhr_name_update"}
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
        tc_ingredient.select_ok()

    def test_3_name_without(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = tc_ingredient.get_id()
        body = {}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_name, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_ingredient.select_ok()

    def test_3_name_none(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_name: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_name, server.detail_must_be_a_string, body[api.param_name])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_ingredient.select_ok()

    def test_3_name_empty(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_name: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_name, server.detail_must_be_not_empty, body[api.param_name])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_ingredient.select_ok()

    def test_3_name_string(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_name: "qa_rhr_name_update"}
        """ call api """
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

    def test_4_with_file_without(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_name: "qa_rhr_name_update"}
        """ call api """
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

    def test_4_with_file_empty(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = tc_ingredient.get_id()
        tc_with_files = ""
        body = {api.param_name: "qa_rhr_name_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_with_files, server.detail_must_be_in + " [true, false]", tc_with_files)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_ingredient.select_ok()

    def test_4_with_file_string(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = tc_ingredient.get_id()
        tc_with_files = "invalid"
        body = {api.param_name: "qa_rhr_name_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_with_files, server.detail_must_be_in + " [true, false]", tc_with_files)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_ingredient.select_ok()

    def test_4_with_file_string_false(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = tc_ingredient1.get_id()
        tc_with_files = "false"
        body = {api.param_name: "qa_rhr_name_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?" + api.param_with_files + "=" + tc_with_files
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

    def test_4_with_file_string_true(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = tc_ingredient1.get_id()
        tc_file1 = tc_ingredient1.add_file(is_main=True)
        tc_file2 = tc_ingredient1.add_file(is_main=False)
        tc_with_files = "true"
        body = {api.param_name: "qa_rhr_name_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient1.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_ingredient1.get_data_with_file(files=[tc_file1, tc_file2]))
        """ refacto """
        tc_ingredient1.select_ok()

    def test_5_name_already_exist(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom_test({"name": "b"}).insert()
        tc_id = tc_ingredient1.get_id()
        body = {api.param_name: tc_ingredient2.get_data_value("name")}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
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

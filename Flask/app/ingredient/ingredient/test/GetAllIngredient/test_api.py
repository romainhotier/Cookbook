import unittest
import requests

import server.server as server
import app.ingredient.ingredient.model as ingredient_model
import app.file.file.model as file_model
import app.ingredient.ingredient.test.GetAllIngredient.api as api

server = server.Server()
api = api.GetAllIngredient()
ingredient = ingredient_model.IngredientTest()
file = file_model.FileTest()


class GetAllIngredient(unittest.TestCase):

    def setUp(self):
        ingredient.clean()
        file.clean()

    def test_0_api_ok(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom_test({"name": "b"}).insert()
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertIn(tc_ingredient1.get_data_stringify_object_id(), response_body[api.rep_data])
        self.assertIn(tc_ingredient2.get_data_stringify_object_id(), response_body[api.rep_data])

    def test_0_api_ok_more_param(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom_test({"name": "b"}).insert()
        """ call api """
        url = server.main_url + "/" + api.url + "?invalid=invalid"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertIn(tc_ingredient1.get_data_stringify_object_id(), response_body[api.rep_data])
        self.assertIn(tc_ingredient2.get_data_stringify_object_id(), response_body[api.rep_data])

    def test_1_url_not_found(self):
        ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        ingredient_model.IngredientTest().custom_test({"name": "b"}).insert()
        """ call api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)

    def test_2_with_files_without(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom_test({"name": "b"}).insert()
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertIn(tc_ingredient1.get_data_stringify_object_id(), response_body[api.rep_data])
        self.assertIn(tc_ingredient2.get_data_stringify_object_id(), response_body[api.rep_data])

    def test_2_with_files_empty(self):
        ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        ingredient_model.IngredientTest().custom_test({"name": "b"}).insert()
        tc_with_files = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_with_files, server.detail_must_be_in + " [true, false]", tc_with_files)
        self.assertEqual(response_body[api.rep_detail], detail)

    def test_2_with_files_string(self):
        ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        ingredient_model.IngredientTest().custom_test({"name": "b"}).insert()
        tc_with_files = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_with_files, server.detail_must_be_in + " [true, false]", tc_with_files)
        self.assertEqual(response_body[api.rep_detail], detail)

    def test_2_with_files_string_false(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom_test({"name": "b"}).insert()
        tc_ingredient1.add_file(filename="qa_rhr_1", is_main=False)
        tc_ingredient1.add_file(filename="qa_rhr_2", is_main=True)
        tc_ingredient2.add_file(filename="qa_rhr_3", is_main=False)
        tc_with_files = "false"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertIn(tc_ingredient1.get_data_stringify_object_id(), response_body[api.rep_data])
        self.assertIn(tc_ingredient2.get_data_stringify_object_id(), response_body[api.rep_data])

    def test_2_with_files_string_true(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom_test({"name": "b"}).insert()
        tc_file1 = tc_ingredient1.add_file(filename="qa_rhr_1", is_main=False)
        tc_file2 = tc_ingredient1.add_file(filename="qa_rhr_2", is_main=True)
        tc_file3 = tc_ingredient2.add_file(filename="qa_rhr_3", is_main=False)
        tc_with_files = "true"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertIn(tc_ingredient1.get_data_with_file(files=[tc_file1, tc_file2]), response_body[api.rep_data])
        self.assertIn(tc_ingredient2.get_data_with_file(files=[tc_file3]), response_body[api.rep_data])

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetAllIngredient())


if __name__ == '__main__':
    unittest.main()

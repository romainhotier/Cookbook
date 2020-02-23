import unittest
import requests

import factory as factory
import ingredient.model as ingredient_model
import ingredient.test.GetIngredient.api as api

server = factory.Server()
api = api.GetIngredient()
ingredient = ingredient_model.IngredientTest()


class GetIngredient(unittest.TestCase):

    def setUp(self):
        ingredient.clean()

    def test_0_api_ok(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        ingredient_model.IngredientTest().custom_test({"name": "b"}).insert()
        tc_id = tc_ingredient1.get_id()
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_ingredient1.get_data_stringify_object_id())

    def test_1_url_not_found(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        ingredient_model.IngredientTest().custom_test({"name": "b"}).insert()
        tc_id = tc_ingredient1.get_id()
        """ cal api """
        url = server.main_url + "/" + api.url + "x/" + tc_id
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)

    def test_2_id_without(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom_test({"name": "b"}).insert()
        """ cal api """
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

    def test_2_id_string(self):
        ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = "invalid"
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id, server.detail_must_be_an_object_id, tc_id)
        self.assertEqual(response_body[api.rep_detail], detail)

    def test_2_id_object_id_invalid(self):
        ingredient_model.IngredientTest().custom_test({"name": "a"}).insert()
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404)
        self.assertEqual(response_body[api.rep_detail], "")

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetIngredient())


if __name__ == '__main__':
    unittest.main()

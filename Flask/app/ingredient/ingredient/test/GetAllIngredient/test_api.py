import unittest
import requests

from server import factory as factory
import app.ingredient.ingredient.model as ingredient_model
import app.ingredient.ingredient.test.GetAllIngredient.api as api

server = factory.Server()
api = api.GetAllIngredient()
ingredient = ingredient_model.IngredientTest()


class GetAllIngredient(unittest.TestCase):

    def setUp(self):
        ingredient.clean()

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

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetAllIngredient())


if __name__ == '__main__':
    unittest.main()

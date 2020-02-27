import unittest
import requests

from server import factory as factory
import app.recipe.recipe.model as recipe_model
import app.recipe.recipe.test.GetAllRecipe.api as api

server = factory.Server()
api = api.GetAllRecipe()
recipe = recipe_model.RecipeTest()


class GetAllRecipe(unittest.TestCase):

    def setUp(self):
        recipe.clean()

    def test_0_api_ok(self):
        tc_recipe1 = recipe_model.RecipeTest().custom_test({"title": "a"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom_test({"title": "b"}).insert()
        """ cal api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertIn(tc_recipe1.get_data_stringify_object_id(), response_body[api.rep_data])
        self.assertIn(tc_recipe2.get_data_stringify_object_id(), response_body[api.rep_data])

    def test_1_url_not_found(self):
        recipe_model.RecipeTest().custom_test({"title": "a"}).insert()
        recipe_model.RecipeTest().custom_test({"title": "b"}).insert()
        """ cal api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetAllRecipe())


if __name__ == '__main__':
    unittest.main()

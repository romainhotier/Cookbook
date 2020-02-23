import unittest
import requests

import factory as factory
import recipe.recipe.model as recipe_model
import recipe.recipe.test.GetRecipe.api as api

server = factory.Server()
api = api.GetRecipe()
recipe = recipe_model.RecipeTest()


class GetRecipe(unittest.TestCase):

    def setUp(self):
        recipe.clean()

    def test_0_api_ok(self):
        tc_recipe1 = recipe_model.RecipeTest().custom_test({"title": "a"}).insert()
        recipe_model.RecipeTest().custom_test({"title": "b"}).insert()
        tc_id = tc_recipe1.get_id()
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_recipe1.get_data_stringify_object_id())

    def test_1_url_not_found(self):
        tc_recipe1 = recipe_model.RecipeTest().custom_test({"title": "a"}).insert()
        recipe_model.RecipeTest().custom_test({"title": "b"}).insert()
        tc_id = tc_recipe1.get_id()
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

    def test_2_id_string(self):
        recipe_model.RecipeTest().custom_test({"title": "a"}).insert()
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
        recipe_model.RecipeTest().custom_test({"title": "a"}).insert()
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
        cls.setUp(GetRecipe())


if __name__ == '__main__':
    unittest.main()

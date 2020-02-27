import unittest
import requests

from server import factory as factory
import app.recipe.recipe.model as recipe_model
import app.recipe.recipe.test.DeleteRecipe.api as api

server = factory.Server()
api = api.DeleteRecipe()
recipe = recipe_model.RecipeTest()


class DeleteRecipe(unittest.TestCase):

    def setUp(self):
        recipe.clean()

    def test_0_api_ok(self):
        tc_recipe1 = recipe_model.RecipeTest().custom_test({}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe1.get_id()
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        tc_recipe1.select_nok()
        tc_recipe2.select_ok()

    def test_1_url_not_found(self):
        tc_recipe1 = recipe_model.RecipeTest().custom_test({}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe1.get_id()
        """ cal api """
        url = server.main_url + "/" + api.url + "x/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_recipe1.select_ok()
        tc_recipe2.select_ok()

    def test_2_id_without(self):
        tc_recipe1 = recipe_model.RecipeTest().custom_test({}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom_test({}).insert()
        """ cal api """
        url = server.main_url + "/" + api.url + "/"
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 404)
        tc_recipe1.select_ok()
        tc_recipe2.select_ok()

    def test_2_id_string(self):
        tc_recipe1 = recipe_model.RecipeTest().custom_test({}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = "invalid"
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id, server.detail_must_be_an_object_id, tc_id)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe1.select_ok()
        tc_recipe2.select_ok()

    def test_2_id_object_id_invalid(self):
        tc_recipe1 = recipe_model.RecipeTest().custom_test({}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        """ cal api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id, server.detail_doesnot_exist, tc_id)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe1.select_ok()
        tc_recipe2.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(DeleteRecipe())


if __name__ == '__main__':
    unittest.main()

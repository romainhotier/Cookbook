import unittest
import requests

from server import factory as factory
import app.recipe.recipe.model as recipe_model
import app.recipe.steps.test.DeleteRecipeStep.api as api

server = factory.Server()
api = api.DeleteRecipeStep()
recipe = recipe_model.RecipeTest()


class DeleteRecipeStep(unittest.TestCase):

    def setUp(self):
        recipe.clean()

    def test_0_api_ok(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        tc_position = "1"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2 + "/" + tc_position
        response = requests.delete(url, verify=False)
        response_body = response.json()
        tc_recipe.custom({"steps": ["a"]})
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_recipe.get_data_stringify_object_id())
        tc_recipe.select_ok()

    def test_1_url_not_found_1(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        tc_position = "1"
        """ call api """
        url = server.main_url + "/" + api.url1 + "x/" + tc_id + "/" + api.url2 + "/" + tc_position
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_recipe.select_ok()

    def test_1_url_not_found_2(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        tc_position = "1"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/x" + api.url2 + "/" + tc_position
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_recipe.select_ok()

    def test_2_id_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"steps": ["a", "b"]}).insert()
        tc_id = ""
        tc_position = "1"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2 + "/" + tc_position
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_recipe.select_ok()

    def test_2_id_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"steps": ["a", "b"]}).insert()
        tc_id = "invalid"
        tc_position = "1"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2 + "/" + tc_position
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id, server.detail_must_be_an_object_id, tc_id)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_2_id_object_id_invalid(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"steps": ["a", "b"]}).insert()
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        tc_position = "1"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2 + "/" + tc_position
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id, server.detail_doesnot_exist, tc_id)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_3_position_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        tc_position = ""
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2 + "/" + tc_position
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_recipe.select_ok()

    def test_3_position_without_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        tc_position = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2 + "/" + tc_position
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_position, server.detail_must_be_an_integer, tc_position)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_3_position_without_min_over(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        tc_position = "-1"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2 + "/" + tc_position
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_position, server.detail_must_be_between + " 0 and 1", int(tc_position))
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_3_position_without_min(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        tc_position = "0"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2 + "/" + tc_position
        response = requests.delete(url, verify=False)
        response_body = response.json()
        tc_recipe.custom({"steps": ["b"]})
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_recipe.get_data_stringify_object_id())
        tc_recipe.select_ok()

    def test_3_position_without_max(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        tc_position = "1"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2 + "/" + tc_position
        response = requests.delete(url, verify=False)
        response_body = response.json()
        tc_recipe.custom({"steps": ["a"]})
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_recipe.get_data_stringify_object_id())
        tc_recipe.select_ok()

    def test_3_position_without_max_over(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        tc_position = "2"
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2 + "/" + tc_position
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_position, server.detail_must_be_between + " 0 and 1", int(tc_position))
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(DeleteRecipeStep())


if __name__ == '__main__':
    unittest.main()

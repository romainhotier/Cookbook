import unittest
import requests

import server.server as server
import app.link.ingredient_recipe.model as link_model
import app.link.ingredient_recipe.test.DeleteIngredientRecipe.api as api

server = server.Server()
api = api.DeleteIngredientRecipe()
link = link_model.LinkIngredientRecipeTest()


class DeleteIngredientRecipe(unittest.TestCase):

    def setUp(self):
        link.clean()

    def test_0_api_ok(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = tc_link.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        tc_link.select_nok()

    def test_1_url_not_found(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = tc_link.get_id()
        """ call api """
        url = server.main_url + "/x" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
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
        """ call api """
        url = server.main_url + "/" + api.url + "/"
        response = requests.delete(url, verify=False)
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
        """ call api """
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
        tc_link.select_ok()

    def test_2_id_object_id_invalid(self):
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({}).insert()
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        """ call api """
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
        tc_link.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(DeleteIngredientRecipe())


if __name__ == '__main__':
    unittest.main()

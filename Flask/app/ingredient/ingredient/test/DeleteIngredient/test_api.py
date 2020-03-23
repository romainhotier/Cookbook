import unittest
import requests

import server.server as server
import app.ingredient.ingredient.model as ingredient_model
import app.recipe.recipe.model as recipe_model
import app.link.ingredient_recipe.model as link_model
import app.file.file.model as file_model
import app.ingredient.ingredient.test.DeleteIngredient.api as api

server = server.Server()
api = api.DeleteIngredient()
ingredient = ingredient_model.IngredientTest()
recipe = recipe_model.RecipeTest()
link = link_model.LinkIngredientRecipeTest()
file = file_model.FileTest()


class DeleteIngredient(unittest.TestCase):

    def setUp(self):
        ingredient.clean()
        recipe.clean()
        link.clean()
        file.clean()

    def test_0_api_ok(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_id = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        tc_ingredient1.select_nok()
        tc_ingredient2.select_ok()

    def test_1_url_not_found(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_id = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "x/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_ingredient1.select_ok()
        tc_ingredient2.select_ok()

    def test_2_id_without(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom_test({}).insert()
        """ call api """
        url = server.main_url + "/" + api.url + "/"
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 404)
        tc_ingredient1.select_ok()
        tc_ingredient2.select_ok()

    def test_2_id_string(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom_test({}).insert()
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
        tc_ingredient1.select_ok()
        tc_ingredient2.select_ok()

    def test_2_id_object_id_invalid(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom_test({}).insert()
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
        tc_ingredient1.select_ok()
        tc_ingredient2.select_ok()

    def test_3_file_clean(self):
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_file1 = tc_ingredient1.add_file(filename="qa_rhr_1", is_main=False)
        tc_file2 = tc_ingredient1.add_file(filename="qa_rhr_2", is_main=False)
        tc_id = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        tc_ingredient1.select_nok()
        tc_file1.select_nok()
        tc_file2.select_nok()

    def test_4_link_clean(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({"_id_ingredient": tc_ingredient.get_id_objectId(),
                                                                     "_id_recipe": tc_recipe.get_id_objectId()}).\
            insert()
        tc_id = tc_ingredient.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        tc_ingredient.select_nok()
        tc_recipe.select_ok()
        tc_link.select_nok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(DeleteIngredient())


if __name__ == '__main__':
    unittest.main()

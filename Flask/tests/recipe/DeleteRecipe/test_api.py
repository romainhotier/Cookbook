import unittest
import requests

import utils
import tests.recipe.DeleteRecipe.api as api
import tests.ingredient.model as ingredient_model
import tests.recipe.model as recipe_model
import tests.file.model as file_model

server = utils.Server
api = api.DeleteRecipe()
ingredient = ingredient_model.IngredientTest()
recipe = recipe_model.RecipeTest()
link = ingredient_model.IngredientRecipeTest
file = file_model.FileTest()


class DeleteRecipe(unittest.TestCase):

    def setUp(self):
        recipe.clean()
        ingredient.clean()
        file.clean()
        link.clean()

    def test_0_api_ok(self):
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_recipe2 = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        tc_recipe1.select_nok()
        tc_recipe2.select_ok()

    def test_1_url_not_found(self):
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_recipe2 = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe1.get_id()
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
        tc_recipe1.select_ok()
        tc_recipe2.select_ok()

    def test_2_id_without(self):
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_recipe2 = recipe_model.RecipeTest().insert()
        """ call api """
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
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_recipe2 = recipe_model.RecipeTest().insert()
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
        tc_recipe1.select_ok()
        tc_recipe2.select_ok()

    def test_2_id_object_id_invalid(self):
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_recipe2 = recipe_model.RecipeTest().insert()
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
        tc_recipe1.select_ok()
        tc_recipe2.select_ok()

    def test_3_clean_file(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"})
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b"})
        tc_recipe1.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe1.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe2.add_step(_id_step="333333333333333333333333", step="step recipe 2 - 1st")
        tc_recipe1.insert()
        tc_recipe2.insert()
        tc_file_recipe11 = tc_recipe1.add_file_recipe(filename="qa_rhr_1", is_main=True)
        tc_file_recipe12 = tc_recipe1.add_file_recipe(filename="qa_rhr_2", is_main=False)
        tc_file_recipe2 = tc_recipe2.add_file_recipe(filename="qa_rhr_3", is_main=False)
        tc_file_step111 = tc_recipe1.add_file_step(_id_step="111111111111111111111111", filename="qa_rhr_11",
                                                   is_main=False)
        tc_file_step121 = tc_recipe1.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_21",
                                                   is_main=False)
        tc_file_step122 = tc_recipe1.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_22",
                                                   is_main=True)
        tc_file_step211 = tc_recipe2.add_file_step(_id_step="333333333333333333333333", filename="qa_rhr_31",
                                                   is_main=True)
        tc_file_step212 = tc_recipe2.add_file_step(_id_step="333333333333333333333333", filename="qa_rhr_32",
                                                   is_main=False)
        tc_id = tc_recipe1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        tc_recipe1.select_nok()
        tc_file_recipe11.select_nok()
        tc_file_recipe12.select_nok()
        tc_file_step111.select_nok()
        tc_file_step121.select_nok()
        tc_file_step122.select_nok()
        tc_recipe2.select_ok()
        tc_file_recipe2.select_ok()
        tc_file_step211.select_ok()
        tc_file_step212.select_ok()

    def test_4_link_clean(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_lk = ingredient_model.IngredientRecipeTest().custom({"_id_ingredient": tc_ingredient._id,
                                                                "_id_recipe": tc_recipe._id}).insert()
        tc_id = tc_recipe.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        tc_ingredient.select_ok()
        tc_recipe.select_nok()
        tc_lk.select_nok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(DeleteRecipe())


if __name__ == '__main__':
    unittest.main()
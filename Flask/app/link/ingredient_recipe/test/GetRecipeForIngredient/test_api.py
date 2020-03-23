import unittest
import requests

import server.server as server
import app.ingredient.ingredient.model as ingredient_model
import app.recipe.recipe.model as recipe_model
import app.link.ingredient_recipe.model as link_model
import app.link.ingredient_recipe.test.GetRecipeForIngredient.api as api

server = server.Server()
api = api.GetRecipeForIngredient()
ingredient = ingredient_model.IngredientTest()
recipe = recipe_model.RecipeTest()
link = link_model.LinkIngredientRecipeTest()


class GetRecipeForIngredient(unittest.TestCase):

    def setUp(self):
        ingredient.clean()
        recipe.clean()
        link.clean()

    def test_0_api_ok(self):
        tc_recipe1 = recipe_model.RecipeTest().custom_test({}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom_test({}).insert()
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_ingredient3 = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_link11 = link_model.LinkIngredientRecipeTest().\
            custom_test({"_id_recipe": tc_recipe1.get_id_objectId(),
                         "_id_ingredient": tc_ingredient1.get_id_objectId()}).insert()
        tc_link12 = link_model.LinkIngredientRecipeTest().\
            custom_test({"_id_recipe": tc_recipe1.get_id_objectId(),
                         "_id_ingredient": tc_ingredient2.get_id_objectId()}).insert()
        tc_link21 = link_model.LinkIngredientRecipeTest(). \
            custom_test({"_id_recipe": tc_recipe2.get_id_objectId(),
                         "_id_ingredient": tc_ingredient1.get_id_objectId()}).insert()
        tc_link23 = link_model.LinkIngredientRecipeTest(). \
            custom_test({"_id_recipe": tc_recipe2.get_id_objectId(),
                         "_id_ingredient": tc_ingredient3.get_id_objectId()}).insert()
        tc_id_ingredient = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id_ingredient
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertIn(tc_link11.get_data_stringify_object_id(), response_body[api.rep_data])
        self.assertNotIn(tc_link12.get_data_stringify_object_id(), response_body[api.rep_data])
        self.assertIn(tc_link21.get_data_stringify_object_id(), response_body[api.rep_data])
        self.assertNotIn(tc_link23.get_data_stringify_object_id(), response_body[api.rep_data])

    def test_1_url_not_found(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        link_model.LinkIngredientRecipeTest().custom_test({"_id_recipe": tc_recipe.get_id_objectId(),
                                                           "_id_ingredient": tc_ingredient.get_id_objectId()}).insert()
        tc_id_ingredient = tc_recipe.get_id()
        """ call api """
        url = server.main_url + "/x" + api.url + "/" + tc_id_ingredient
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)

    def test_2_id_ingredient_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        link_model.LinkIngredientRecipeTest().custom_test({"_id_recipe": tc_recipe.get_id_objectId(),
                                                           "_id_ingredient": tc_ingredient.get_id_objectId()}).insert()
        """ call api """
        url = server.main_url + "/" + api.url + "/"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)

    def test_2_id_ingredient_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        link_model.LinkIngredientRecipeTest().custom_test({"_id_recipe": tc_recipe.get_id_objectId(),
                                                           "_id_ingredient": tc_ingredient.get_id_objectId()}).insert()
        tc_id_ingredient = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id_ingredient
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_ingredient, server.detail_must_be_an_object_id, tc_id_ingredient)
        self.assertEqual(response_body[api.rep_detail], detail)

    def test_2_id_ingredient_object_id_invalid(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        link_model.LinkIngredientRecipeTest().custom_test({"_id_recipe": tc_recipe.get_id_objectId(),
                                                           "_id_ingredient": tc_ingredient.get_id_objectId()}).insert()
        tc_id_ingredient = "aaaaaaaaaaaaaaaaaaaaaaaa"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id_ingredient
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_ingredient, server.detail_doesnot_exist, tc_id_ingredient)
        self.assertEqual(response_body[api.rep_detail], detail)

    def test_3_with_title_without(self):
        tc_recipe1 = recipe_model.RecipeTest().custom_test({"title": "r1"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom_test({"title": "r2"}).insert()
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_link1 = link_model.LinkIngredientRecipeTest().\
            custom_test({"_id_recipe": tc_recipe1.get_id_objectId(),
                         "_id_ingredient": tc_ingredient1.get_id_objectId()}).insert()
        tc_link2 = link_model.LinkIngredientRecipeTest().\
            custom_test({"_id_recipe": tc_recipe2.get_id_objectId(),
                         "_id_ingredient": tc_ingredient1.get_id_objectId()}).insert()
        tc_id_ingredient = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id_ingredient
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertIn(tc_link1.get_data_stringify_object_id(), response_body[api.rep_data])
        self.assertIn(tc_link2.get_data_stringify_object_id(), response_body[api.rep_data])

    def test_3_with_title_empty(self):
        tc_recipe1 = recipe_model.RecipeTest().custom_test({"title": "r1"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom_test({"title": "r2"}).insert()
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({}).insert()
        link_model.LinkIngredientRecipeTest().custom_test({"_id_recipe": tc_recipe1.get_id_objectId(),
                                                           "_id_ingredient": tc_ingredient1.get_id_objectId()}).insert()
        link_model.LinkIngredientRecipeTest().custom_test({"_id_recipe": tc_recipe2.get_id_objectId(),
                                                           "_id_ingredient": tc_ingredient1.get_id_objectId()}).insert()
        tc_id_ingredient = tc_ingredient1.get_id()
        tc_with_name = ""
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id_ingredient + "?" + api.param_with_title + "=" + tc_with_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_with_title, server.detail_must_be_in + " [true, false]", tc_with_name)
        self.assertEqual(response_body[api.rep_detail], detail)

    def test_3_with_title_string(self):
        tc_recipe1 = recipe_model.RecipeTest().custom_test({"title": "r1"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom_test({"title": "r2"}).insert()
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({}).insert()
        link_model.LinkIngredientRecipeTest().custom_test({"_id_recipe": tc_recipe1.get_id_objectId(),
                                                           "_id_ingredient": tc_ingredient1.get_id_objectId()}).insert()
        link_model.LinkIngredientRecipeTest().custom_test({"_id_recipe": tc_recipe2.get_id_objectId(),
                                                           "_id_ingredient": tc_ingredient1.get_id_objectId()}).insert()
        tc_id_ingredient = tc_ingredient1.get_id()
        tc_with_name = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id_ingredient + "?" + api.param_with_title + "=" + tc_with_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_with_title, server.detail_must_be_in + " [true, false]", tc_with_name)
        self.assertEqual(response_body[api.rep_detail], detail)

    def test_3_with_title_string_false(self):
        tc_recipe1 = recipe_model.RecipeTest().custom_test({"title": "r1"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom_test({"title": "r2"}).insert()
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_link1 = link_model.LinkIngredientRecipeTest().\
            custom_test({"_id_recipe": tc_recipe1.get_id_objectId(),
                         "_id_ingredient": tc_ingredient1.get_id_objectId()}).insert()
        tc_link2 = link_model.LinkIngredientRecipeTest().\
            custom_test({"_id_recipe": tc_recipe2.get_id_objectId(),
                         "_id_ingredient": tc_ingredient1.get_id_objectId()}).insert()
        tc_id_ingredient = tc_ingredient1.get_id()
        tc_with_name = "false"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id_ingredient + "?" + api.param_with_title + "=" + tc_with_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertIn(tc_link1.get_data_stringify_object_id(), response_body[api.rep_data])
        self.assertIn(tc_link2.get_data_stringify_object_id(), response_body[api.rep_data])

    def test_3_with_title_string_true(self):
        tc_recipe1 = recipe_model.RecipeTest().custom_test({"title": "r1"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom_test({"title": "r2"}).insert()
        tc_ingredient1 = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_link1 = link_model.LinkIngredientRecipeTest().\
            custom_test({"_id_recipe": tc_recipe1.get_id_objectId(),
                         "_id_ingredient": tc_ingredient1.get_id_objectId()}).insert()
        tc_link2 = link_model.LinkIngredientRecipeTest().\
            custom_test({"_id_recipe": tc_recipe2.get_id_objectId(),
                         "_id_ingredient": tc_ingredient1.get_id_objectId()}).insert()
        tc_id_ingredient = tc_ingredient1.get_id()
        tc_with_name = "true"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id_ingredient + "?" + api.param_with_title + "=" + tc_with_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertIn(tc_link1.add_title().get_data_stringify_object_id(), response_body[api.rep_data])
        self.assertIn(tc_link2.add_title().get_data_stringify_object_id(), response_body[api.rep_data])

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetRecipeForIngredient())


if __name__ == '__main__':
    unittest.main()

import unittest
import requests
from bson import ObjectId

import server.server as server
import app.ingredient.ingredient.model as ingredient_model
import app.recipe.recipe.model as recipe_model
import app.link.ingredient_recipe.model as link_model
import app.link.ingredient_recipe.test.PostIngredientRecipe.api as api

server = server.Server()
api = api.PostIngredientRecipe()
recipe = recipe_model.RecipeTest()
link = link_model.LinkIngredientRecipeTest()
ingredient = ingredient_model.IngredientTest()


class PostIngredientRecipe(unittest.TestCase):

    def setUp(self):
        ingredient.clean()
        recipe.clean()
        link.clean()

    def test_0_api_ok(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_link.get_data_without_id())
        """ refacto """
        tc_link.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_0_api_ok_more_param(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit",
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_link.get_data_without_id())
        """ refacto """
        tc_link.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_1_url_not_found(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/x" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_link.select_nok_by_unit()

    def test_2_id_ingredient_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom({"unit": body[api.param_unit]})
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_ingredient, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_nok_by_unit()

    def test_2_id_ingredient_null(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        body = {api.param_id_ingredient: None,
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom({"unit": body[api.param_unit]})
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_ingredient, server.detail_must_be_an_object_id,
                                   body[api.param_id_ingredient])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_nok_by_unit()

    def test_2_id_ingredient_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        body = {api.param_id_ingredient: "",
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom({"unit": body[api.param_unit]})
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_ingredient, server.detail_must_be_an_object_id,
                                   body[api.param_id_ingredient])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_nok_by_unit()

    def test_2_id_ingredient_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        body = {api.param_id_ingredient: "invalid",
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom({"unit": body[api.param_unit]})
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_ingredient, server.detail_must_be_an_object_id,
                                   body[api.param_id_ingredient])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_nok_by_unit()

    def test_2_id_ingredient_object_id_invalid(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        body = {api.param_id_ingredient: "aaaaaaaaaaaaaaaaaaaaaaaa",
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom({"unit": body[api.param_unit]})
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_ingredient, server.detail_doesnot_exist, body[api.param_id_ingredient])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_nok_by_unit()

    def test_3_id_recipe_without(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom({"unit": body[api.param_unit]})
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_recipe, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_nok_by_unit()

    def test_3_id_recipe_null(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: None,
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom({"unit": body[api.param_unit]})
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_recipe, server.detail_must_be_an_object_id, body[api.param_id_recipe])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_nok_by_unit()

    def test_3_id_recipe_empty(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: "",
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom({"unit": body[api.param_unit]})
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_recipe, server.detail_must_be_an_object_id, body[api.param_id_recipe])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_nok_by_unit()

    def test_3_id_recipe_string(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: "invalid",
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom({"unit": body[api.param_unit]})
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_recipe, server.detail_must_be_an_object_id, body[api.param_id_recipe])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_nok_by_unit()

    def test_3_id_recipe_object_id_invalid(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: "aaaaaaaaaaaaaaaaaaaaaaaa",
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom({"unit": body[api.param_unit]})
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_recipe, server.detail_doesnot_exist, body[api.param_id_recipe])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_nok_by_unit()

    def test_4_quantity_without(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_quantity, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_nok_by_linked()

    def test_4_quantity_null(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: None,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_quantity, server.detail_must_be_an_integer, body[api.param_quantity])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_nok_by_linked()

    def test_4_quantity_empty(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: "",
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_quantity, server.detail_must_be_an_integer, body[api.param_quantity])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_nok_by_linked()
        
    def test_4_quantity_string(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: "string",
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_quantity, server.detail_must_be_an_integer, body[api.param_quantity])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_nok_by_linked()

    def test_4_quantity_integer(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_link.get_data_without_id())
        """ refacto """
        tc_link.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_5_unit_without(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_unit, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_nok_by_linked()

    def test_5_unit_null(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_unit, server.detail_must_be_a_string, body[api.param_unit])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_nok_by_linked()

    def test_5_unit_empty(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_link.get_data_without_id())
        """ refacto """
        tc_link.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_5_unit_string(self):
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = link_model.LinkIngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_link.get_data_without_id())
        """ refacto """
        tc_link.custom({"_id": response_body[api.rep_data]["_id"]}).select_ok()

    def test_6_already_exist(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_ingredient = ingredient_model.IngredientTest().custom_test({}).insert()
        """ param """
        tc_id_ingredient = tc_ingredient.get_id()
        tc_id_recipe = tc_recipe.get_id()
        tc_link = link_model.LinkIngredientRecipeTest().custom_test({"_id_ingredient": ObjectId(tc_id_ingredient),
                                                                     "_id_recipe": ObjectId(tc_id_recipe)}).insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit2"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link2 = link_model.LinkIngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = "link between {} and {} ".format(tc_id_ingredient, tc_id_recipe) + server.detail_already_exist.lower()
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_link.select_ok()
        tc_link2.select_nok_by_unit()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostIngredientRecipe())


if __name__ == '__main__':
    unittest.main()

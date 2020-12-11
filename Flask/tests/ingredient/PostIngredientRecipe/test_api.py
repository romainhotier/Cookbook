import unittest
import requests
from bson import ObjectId

import utils
import tests.ingredient.PostIngredientRecipe.api as api
import tests.ingredient.model as ingredient_model
import tests.recipe.model as recipe_model

server = utils.Server()
api = api.PostIngredientRecipe()
recipe = recipe_model.RecipeTest()
link = ingredient_model.IngredientRecipeTest()
ingredient = ingredient_model.IngredientTest()


class PostIngredientRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest, RecipeTest and IngredientRecipeTest."""
        ingredient.clean()
        recipe.clean()
        link.clean()

    def test_0_api_ok(self):
        """ Default case.

        Return
            201 - Inserted IngredientRecipe.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_link)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_link.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_0_api_ok_more_param(self):
        """ Default case with more parameters.

        Return
            201 - Inserted IngredientRecipe.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit",
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_link)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_link.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_1_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/x" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check """
        tc_link.select_nok_by_unit()

    def test_2_id_ingredient_without(self):
        """ BodyParameter _id_ingredient is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_ingredient, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_unit()

    def test_2_id_ingredient_null(self):
        """ BodyParameter _id_ingredient is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_ingredient: None,
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_ingredient, msg=server.detail_must_be_an_object_id,
                                   value=body[api.param_id_ingredient])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_unit()

    def test_2_id_ingredient_empty(self):
        """ BodyParameter _id_ingredient is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_ingredient: "",
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_ingredient, msg=server.detail_must_be_an_object_id,
                                   value=body[api.param_id_ingredient])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_unit()

    def test_2_id_ingredient_string(self):
        """ BodyParameter _id_ingredient is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_ingredient: "invalid",
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_ingredient, msg=server.detail_must_be_an_object_id,
                                   value=body[api.param_id_ingredient])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_unit()

    def test_2_id_ingredient_object_id_invalid(self):
        """ BodyParameter _id_ingredient is a nok ObjectId.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_ingredient: "aaaaaaaaaaaaaaaaaaaaaaaa",
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_ingredient, msg=server.detail_doesnot_exist,
                                   value=body[api.param_id_ingredient])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_unit()

    def test_3_id_recipe_without(self):
        """ BodyParameter _id_recipe is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_recipe, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_unit()

    def test_3_id_recipe_null(self):
        """ BodyParameter _id_recipe is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: None,
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_recipe, msg=server.detail_must_be_an_object_id,
                                   value=body[api.param_id_recipe])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_unit()

    def test_3_id_recipe_empty(self):
        """ BodyParameter _id_recipe is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: "",
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_recipe, msg=server.detail_must_be_an_object_id,
                                   value=body[api.param_id_recipe])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_unit()

    def test_3_id_recipe_string(self):
        """ BodyParameter _id_recipe is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: "invalid",
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_recipe, msg=server.detail_must_be_an_object_id,
                                   value=body[api.param_id_recipe])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_unit()

    def test_3_id_recipe_object_id_invalid(self):
        """ BodyParameter _id_recipe is an nok ObjectId.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: "aaaaaaaaaaaaaaaaaaaaaaaa",
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_recipe, msg=server.detail_doesnot_exist,
                                   value=body[api.param_id_recipe])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_unit()

    def test_4_quantity_without(self):
        """ BodyParameter quantity is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_quantity, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_linked()

    def test_4_quantity_null(self):
        """ BodyParameter quantity is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: None,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_quantity, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_quantity])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_linked()

    def test_4_quantity_empty(self):
        """ BodyParameter quantity is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: "",
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_quantity, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_quantity])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_linked()
        
    def test_4_quantity_string(self):
        """ BodyParameter quantity is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: "string",
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_quantity, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_quantity])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_linked()

    def test_4_quantity_integer(self):
        """ BodyParameter quantity is a number.

        Return
            201 - Inserted IngredientRecipe.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_recipe = recipe_model.RecipeTest().insert()
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_link)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_link.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_5_unit_without(self):
        """ BodyParameter unit is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_unit, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_linked()

    def test_5_unit_null(self):
        """ BodyParameter unit is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_unit, msg=server.detail_must_be_a_string, value=body[api.param_unit])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_linked()

    def test_5_unit_empty(self):
        """ BodyParameter unit is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_link)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_link.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_5_unit_string(self):
        """ BodyParameter unit is a string.

        Return
            201 - Inserted IngredientRecipe.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_link)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_link.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_6_already_exist(self):
        """ IngredientRecipe already exist.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_link = ingredient_model.IngredientRecipeTest().custom({"_id_ingredient": ObjectId(tc_ingredient.get_id()),
                                                                  "_id_recipe": ObjectId(tc_recipe.get_id())}).insert()
        """ param """
        tc_id_ingredient = tc_ingredient.get_id()
        tc_id_recipe = tc_recipe.get_id()
        """ param """
        body = {api.param_id_ingredient: tc_ingredient.get_id(),
                api.param_id_recipe: tc_recipe.get_id(),
                api.param_quantity: 5,
                api.param_unit: "qa_rhr_unit2"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link2 = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = "link between {} and {} ".format(tc_id_ingredient, tc_id_recipe) + server.detail_already_exist.lower()
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_ok()
        tc_link2.select_nok_by_unit()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostIngredientRecipe())
        link.clean_complete()


if __name__ == '__main__':
    unittest.main()

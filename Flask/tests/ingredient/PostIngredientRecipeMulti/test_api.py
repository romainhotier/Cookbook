import unittest
import requests

import utils
import tests.ingredient.PostIngredientRecipeMulti.api as api
import tests.ingredient.model as ingredient_model
import tests.recipe.model as recipe_model

server = utils.Server()
api = api.PostIngredientRecipeMulti()
recipe = recipe_model.RecipeTest()
link = ingredient_model.IngredientRecipeTest()
ingredient = ingredient_model.IngredientTest()


class PostIngredientRecipeMulti(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest, RecipeTest and IngredientRecipeTest."""
        ingredient.clean()
        recipe.clean()
        link.clean()

    def test_0_api_ok(self):
        """ Default case.

        Return
            201 - Inserted IngredientRecipes.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(api.custom_body(body=body, index=0))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check1 = api.json_check(data=response_body["data"], data_expected=tc_link)
        self.assertTrue(data_check1["result"], data_check1["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        api.edit_id(data=response_body["data"], link=tc_link).select_ok()

    def test_0_api_ok_multi(self):
        """ Default case multi.

        Return
            201 - Inserted IngredientRecipes.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient1.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"},
                                        {api.param_id_ingredient: tc_ingredient2.get_id(),
                                         api.param_quantity: 6,
                                         api.param_unit: "qa_rhr_unit2"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link1 = ingredient_model.IngredientRecipeTest().custom(api.custom_body(body=body, index=0))
        tc_link2 = ingredient_model.IngredientRecipeTest().custom(api.custom_body(body=body, index=1))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check1 = api.json_check(data=response_body["data"], data_expected=tc_link1)
        self.assertTrue(data_check1["result"], data_check1["error"])
        data_check2 = api.json_check(data=response_body["data"], data_expected=tc_link2)
        self.assertTrue(data_check2["result"], data_check2["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        api.edit_id(data=response_body["data"], link=tc_link1).select_ok()
        api.edit_id(data=response_body["data"], link=tc_link2).select_ok()

    def test_0_api_ok_more_param(self):
        """ Default case with more parameters.

        Return
            201 - Inserted IngredientRecipe.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                "invalid": "invalid",
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient1.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit",
                                         "invalid": "invalid"},
                                        {api.param_id_ingredient: tc_ingredient2.get_id(),
                                         api.param_quantity: 6,
                                         api.param_unit: "qa_rhr_unit2"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link1 = ingredient_model.IngredientRecipeTest().custom(api.custom_body(body=body, index=0))
        tc_link2 = ingredient_model.IngredientRecipeTest().custom(api.custom_body(body=body, index=1))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check1 = api.json_check(data=response_body["data"], data_expected=tc_link1)
        self.assertTrue(data_check1["result"], data_check1["error"])
        data_check2 = api.json_check(data=response_body["data"], data_expected=tc_link2)
        self.assertTrue(data_check2["result"], data_check2["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        api.edit_id(data=response_body["data"], link=tc_link1).select_ok()
        api.edit_id(data=response_body["data"], link=tc_link2).select_ok()

    def test_1_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/x" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(api.custom_body(body=body, index=0))
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check """
        tc_link.select_nok_by_unit()

    def test_2_id_recipe_without(self):
        """ BodyParameter _id_recipe is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(api.custom_body(body=body, index=0))
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

    def test_2_id_recipe_null(self):
        """ BodyParameter _id_recipe is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: None,
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(api.custom_body(body=body, index=0))
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

    def test_2_id_recipe_empty(self):
        """ BodyParameter _id_recipe is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: "",
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(api.custom_body(body=body, index=0))
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

    def test_2_id_recipe_string(self):
        """ BodyParameter _id_recipe is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: "invalid",
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(api.custom_body(body=body, index=0))
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

    def test_2_id_recipe_object_id_invalid(self):
        """ BodyParameter _id_recipe is an nok ObjectId.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: "aaaaaaaaaaaaaaaaaaaaaaaa",
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(api.custom_body(body=body, index=0))
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

    def test_3_ingredients_without(self):
        """ BodyParameter ingredients is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id()}
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
        detail = api.create_detail(param=api.param_ingredients, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_3_ingredients_null(self):
        """ BodyParameter ingredients is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: None}
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
        detail = api.create_detail(param=api.param_ingredients, msg=server.detail_must_be_an_array,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_3_ingredients_empty(self):
        """ BodyParameter ingredients is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: ""}
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
        detail = api.create_detail(param=api.param_ingredients, msg=server.detail_must_be_an_array,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_3_ingredients_invalid(self):
        """ BodyParameter ingredients is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: "invalid"}
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
        detail = api.create_detail(param=api.param_ingredients, msg=server.detail_must_be_an_array,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_3_ingredients_object(self):
        """ BodyParameter ingredients is an object.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: {}}
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
        detail = api.create_detail(param=api.param_ingredients, msg=server.detail_must_be_an_array,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_3_ingredients_tab(self):
        """ BodyParameter ingredients is a empty tab.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: []}
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
        detail = api.create_detail(param=api.param_ingredients, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_3_ingredients_tab_null(self):
        """ BodyParameter ingredients is a tab with null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [None,
                                        {api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
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
        detail = api.create_detail(param=api.param_ingredients, msg=server.detail_must_be_an_array_of_object,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_3_ingredients_tab_empty(self):
        """ BodyParameter ingredients is a tab with empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: ["",
                                        {api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
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
        detail = api.create_detail(param=api.param_ingredients, msg=server.detail_must_be_an_array_of_object,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_3_ingredients_tab_invalid(self):
        """ BodyParameter ingredients is a tab with string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: ["invalid",
                                        {api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
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
        detail = api.create_detail(param=api.param_ingredients, msg=server.detail_must_be_an_array_of_object,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_3_ingredients_tab_tab(self):
        """ BodyParameter ingredients is a tab with tab.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [[],
                                        {api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
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
        detail = api.create_detail(param=api.param_ingredients, msg=server.detail_must_be_an_array_of_object,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_3_ingredients_tab_object(self):
        """ BodyParameter ingredients is a tab with tab.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{},
                                        {api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
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
        tc_link.select_nok_by_id_recipe()

    def test_4_id_ingredient_without(self):
        """ BodyParameter ingredients._id_ingredient is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
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
        tc_link.select_nok_by_id_recipe()

    def test_4_id_ingredient_is_null(self):
        """ BodyParameter ingredients._id_ingredient is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: None,
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
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
                                   value=body[api.param_ingredients][0][api.param_id_ingredient])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_4_id_ingredient_is_empty(self):
        """ BodyParameter ingredients._id_ingredient is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: "",
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
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
                                   value=body[api.param_ingredients][0][api.param_id_ingredient])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_4_id_ingredient_is_invalid(self):
        """ BodyParameter ingredients._id_ingredient is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: "invalid",
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
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
                                   value=body[api.param_ingredients][0][api.param_id_ingredient])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_4_id_ingredient_is_invalid_object_id(self):
        """ BodyParameter ingredients._id_ingredient is an nok ObjectId.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: "aaaaaaaaaaaaaaaaaaaaaaaa",
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
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
                                   value=body[api.param_ingredients][0][api.param_id_ingredient])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_5_quantity_without(self):
        """ BodyParameter ingredients.quantity is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_unit: "qa_rhr_unit"}]}
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
        tc_link.select_nok_by_id_recipe()

    def test_5_quantity_null(self):
        """ BodyParameter ingredients.quantity is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: None,
                                         api.param_unit: "qa_rhr_unit"}]}
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
                                   value=body[api.param_ingredients][0][api.param_quantity])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_5_quantity_empty(self):
        """ BodyParameter ingredients.quantity is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: "",
                                         api.param_unit: "qa_rhr_unit"}]}
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
                                   value=body[api.param_ingredients][0][api.param_quantity])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_5_quantity_invalid(self):
        """ BodyParameter ingredients.quantity is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: "invalid",
                                         api.param_unit: "qa_rhr_unit"}]}
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
                                   value=body[api.param_ingredients][0][api.param_quantity])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_5_quantity_number_string(self):
        """ BodyParameter ingredients.quantity is a string number.

        Return
            201 - Inserted IngredientRecipes.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: "5",
                                         api.param_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(api.custom_body(body=body, index=0))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check1 = api.json_check(data=response_body["data"], data_expected=tc_link)
        self.assertTrue(data_check1["result"], data_check1["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        api.edit_id(data=response_body["data"], link=tc_link).select_ok()

    def test_5_quantity_number(self):
        """ BodyParameter ingredients.quantity is a number.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(api.custom_body(body=body, index=0))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check1 = api.json_check(data=response_body["data"], data_expected=tc_link)
        self.assertTrue(data_check1["result"], data_check1["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        api.edit_id(data=response_body["data"], link=tc_link).select_ok()

    def test_6_unit_without(self):
        """ BodyParameter ingredients.unit is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5}]}
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
        tc_link.select_nok_by_id_recipe()

    def test_6_unit_null(self):
        """ BodyParameter ingredients.unit is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: None}]}
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
        detail = api.create_detail(param=api.param_unit, msg=server.detail_must_be_a_string,
                                   value=body[api.param_ingredients][0][api.param_unit])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    def test_6_unit_empty(self):
        """ BodyParameter ingredients.unit is an empty string.

        Return
            201 - Inserted IngredientRecipes.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: ""}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(api.custom_body(body=body, index=0))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check1 = api.json_check(data=response_body["data"], data_expected=tc_link)
        self.assertTrue(data_check1["result"], data_check1["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        api.edit_id(data=response_body["data"], link=tc_link).select_ok()

    def test_6_unit_invalid(self):
        """ BodyParameter ingredients.unit is a string.

        Return
            201 - Inserted IngredientRecipes.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "invalid"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_link = ingredient_model.IngredientRecipeTest().custom(api.custom_body(body=body, index=0))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check1 = api.json_check(data=response_body["data"], data_expected=tc_link)
        self.assertTrue(data_check1["result"], data_check1["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        api.edit_id(data=response_body["data"], link=tc_link).select_ok()

    def test_7_already_exist(self):
        """ Special case: already exist.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_link = ingredient_model.IngredientRecipeTest().custom({"_id_recipe": tc_recipe._id,
                                                                  "_id_ingredient": tc_ingredient._id}).insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = "link between {} and {} ".format(tc_ingredient._id, tc_recipe._id) + \
                 server.detail_already_exist.lower()
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_ok()

    def test_7_identical(self):
        """ Special case: identical.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_id_recipe: tc_recipe.get_id(),
                api.param_ingredients: [{api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 5,
                                         api.param_unit: "qa_rhr_unit"},
                                        {api.param_id_ingredient: tc_ingredient.get_id(),
                                         api.param_quantity: 6,
                                         api.param_unit: "qa_rhr_unit2"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_link = ingredient_model.IngredientRecipeTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id_ingredient, msg=server.detail_must_be_unique,
                                   value=[ingr[api.param_id_ingredient] for ingr in body[api.param_ingredients]])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_link.select_nok_by_id_recipe()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostIngredientRecipeMulti())
        link.clean_complete()


if __name__ == '__main__':
    unittest.main()

import unittest
import requests

import utils
import tests.recipe.PostRecipe.api as api
import tests.recipe.model as recipe_model
import tests.ingredient.model as ingredient_model

server = utils.Server()
api = api.PostRecipe()
ingredient = ingredient_model.IngredientTest()
recipe = recipe_model.RecipeTest()


class PostRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest, RecipeTest."""
        ingredient.clean()
        recipe.clean()

    def test_ingredients_without(self):
        """ Default case.

        Return
            201 - Inserted Recipe.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.custom_id_from_body(data=response_body).check_bdd_data()

    def test_ingredients_null(self):
        """ BodyParameter ingredients is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
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
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_empty(self):
        """ BodyParameter ingredients is an empty string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
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
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_invalid(self):
        """ BodyParameter ingredients is a string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
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
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_object(self):
        """ BodyParameter ingredients is an object.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: {}}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
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
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_tab(self):
        """ BodyParameter ingredients is a empty tab.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: []}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
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
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_tab_null(self):
        """ BodyParameter ingredients is a tab with null.

        Return
            400 - Bad request.
        """

        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [None,
                                        {api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
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
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_tab_empty(self):
        """ BodyParameter ingredients is a tab with empty string.

        Return
            400 - Bad request.
        """

        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: ["",
                                        {api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
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
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_tab_invalid(self):
        """ BodyParameter ingredients is a tab with string.

        Return
            400 - Bad request.
        """

        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: ["invalid",
                                        {api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
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
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_tab_tab(self):
        """ BodyParameter ingredients is a tab with tab.

        Return
            400 - Bad request.
        """

        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [[],
                                        {api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
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
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_tab_object(self):
        """ BodyParameter ingredients is a tab with tab.

        Return
            400 - Bad request.
        """

        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{},
                                        {api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_ingredient+"."+api.param_ingredient_id,
                                   msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_id_without(self):
        """ BodyParameter ingredients._id_ingredient is missing.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_ingredient+"."+api.param_ingredient_id,
                                   msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_id_is_null(self):
        """ BodyParameter ingredients._id_ingredient is null.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{api.param_ingredient_id: None,
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_ingredient+"."+api.param_ingredient_id,
                                   msg=server.detail_must_be_an_object_id,
                                   value=body[api.param_ingredients][0][api.param_ingredient_id])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_id_is_empty(self):
        """ BodyParameter ingredients._id_ingredient is an empty string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{api.param_ingredient_id: "",
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_ingredient+"."+api.param_ingredient_id,
                                   msg=server.detail_must_be_an_object_id,
                                   value=body[api.param_ingredients][0][api.param_ingredient_id])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_id_is_invalid(self):
        """ BodyParameter ingredients._id_ingredient is a string.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{api.param_ingredient_id: "invalid",
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_ingredient+"."+api.param_ingredient_id,
                                   msg=server.detail_must_be_an_object_id,
                                   value=body[api.param_ingredients][0][api.param_ingredient_id])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_id_is_invalid_object_id(self):
        """ BodyParameter ingredients._id_ingredient is an nok ObjectId.

        Return
            400 - Bad request.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{api.param_ingredient_id: "aaaaaaaaaaaaaaaaaaaaaaaa",
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_ingredient+"."+api.param_ingredient_id,
                                   msg=server.detail_doesnot_exist,
                                   value=body[api.param_ingredients][0][api.param_ingredient_id])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_quantity_without(self):
        """ BodyParameter ingredients.quantity is missing.

        Return
            400 - Bad request.
        """

        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_ingredient+"."+api.param_ingredient_quantity,
                                   msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_quantity_null(self):
        """ BodyParameter ingredients.quantity is null.

        Return
            400 - Bad request.
        """

        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: None,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_ingredient+"."+api.param_ingredient_quantity,
                                   msg=server.detail_must_be_an_integer,
                                   value=body[api.param_ingredients][0][api.param_ingredient_quantity])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_quantity_empty(self):
        """ BodyParameter ingredients.quantity is an empty string.

        Return
            400 - Bad request.
        """

        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: "",
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_ingredient+"."+api.param_ingredient_quantity,
                                   msg=server.detail_must_be_an_integer,
                                   value=body[api.param_ingredients][0][api.param_ingredient_quantity])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_quantity_invalid(self):
        """ BodyParameter ingredients.quantity is a string.

        Return
            400 - Bad request.
        """

        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: "invalid",
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_ingredient+"."+api.param_ingredient_quantity,
                                   msg=server.detail_must_be_an_integer,
                                   value=body[api.param_ingredients][0][api.param_ingredient_quantity])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_quantity_number_string(self):
        """ BodyParameter ingredients.quantity is a string number.

        Return
            201 - Inserted Recipe.
        """

        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: "5",
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.custom_id_from_body(data=response_body).check_bdd_data()

    def test_ingredients_quantity_number(self):
        """ BodyParameter ingredients.quantity is a number.

        Return
            400 - Bad request.
        """

        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.custom_id_from_body(data=response_body).check_bdd_data()

    def test_ingredients_unit_without(self):
        """ BodyParameter ingredients.unit is missing.

        Return
            400 - Bad request.
        """

        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_ingredient+"."+api.param_ingredient_unit,
                                   msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_unit_null(self):
        """ BodyParameter ingredients.unit is null.

        Return
            400 - Bad request.
        """

        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: None}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_ingredient+"."+api.param_ingredient_unit,
                                   msg=server.detail_must_be_a_string,
                                   value=body[api.param_ingredients][0][api.param_ingredient_unit])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    def test_ingredients_unit_empty(self):
        """ BodyParameter ingredients.unit is an empty string.

        Return
            201 - Inserted Recipe.
        """

        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: ""}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.custom_id_from_body(data=response_body).check_bdd_data()

    def test_ingredients_unit_invalid(self):
        """ BodyParameter ingredients.unit is a string.

        Return
            201 - Inserted Recipe.
        """

        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "invalid"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.custom_id_from_body(data=response_body).check_bdd_data()

    def test_ingredients_same(self):
        """ Special case: identical.

        Return
            400 - Bad request.
        """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug",
                api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"},
                                        {api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 6,
                                         api.param_ingredient_unit: "qa_rhr_unit2"}]}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_ingredient+"."+api.param_ingredient_id,
                                   msg=server.detail_must_be_unique,
                                   value=[ingr[api.param_ingredient_id] for ingr in body[api.param_ingredients]])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostRecipe())


if __name__ == '__main__':
    unittest.main()

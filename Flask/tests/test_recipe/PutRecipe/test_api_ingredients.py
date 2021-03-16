import unittest
import requests

from tests import server, rep
from tests.test_ingredient import IngredientTest
from tests.test_recipe import RecipeTest
from tests.test_recipe.PutRecipe import api


class TestPutRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest and IngredientTest."""
        RecipeTest().clean()
        IngredientTest().clean()

    def test_ingredients_without(self):
        """ BodyParameter ingredients is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param="body", msg=rep.detail_must_contain_at_least_one_key, value=body)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_null(self):
        """ BodyParameter ingredients is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients, msg=rep.detail_must_be_an_array,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_empty(self):
        """ BodyParameter ingredients is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients, msg=rep.detail_must_be_an_array,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_invalid(self):
        """ BodyParameter ingredients is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients, msg=rep.detail_must_be_an_array,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_object(self):
        """ BodyParameter ingredients is an object.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: {}}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients, msg=rep.detail_must_be_an_array,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_tab(self):
        """ BodyParameter ingredients is a empty tab.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: []}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients, msg=rep.detail_must_be_not_empty,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_tab_null(self):
        """ BodyParameter ingredients is a tab with null.

        Return
            400 - Bad request.
        """

        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [None,
                                        {api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients, msg=rep.detail_must_be_an_array_of_object,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_tab_empty(self):
        """ BodyParameter ingredients is a tab with empty string.

        Return
            400 - Bad request.
        """

        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: ["",
                                        {api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients, msg=rep.detail_must_be_an_array_of_object,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_tab_invalid(self):
        """ BodyParameter ingredients is a tab with string.

        Return
            400 - Bad request.
        """

        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: ["invalid",
                                        {api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients, msg=rep.detail_must_be_an_array_of_object,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_tab_tab(self):
        """ BodyParameter ingredients is a tab with tab.

        Return
            400 - Bad request.
        """

        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [[],
                                        {api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients, msg=rep.detail_must_be_an_array_of_object,
                                   value=body[api.param_ingredients])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_tab_object(self):
        """ BodyParameter ingredients is a tab with tab.

        Return
            400 - Bad request.
        """

        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{},
                                        {api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients+"."+api.param_ingredient_id, msg=rep.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_id_without(self):
        """ BodyParameter ingredients._id_ingredient is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients+"."+api.param_ingredient_id,
                                   msg=rep.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_id_is_null(self):
        """ BodyParameter ingredients._id_ingredient is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: None,
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients+"."+api.param_ingredient_id,
                                   msg=rep.detail_must_be_an_object_id,
                                   value=body[api.param_ingredients][0][api.param_ingredient_id])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_id_is_empty(self):
        """ BodyParameter ingredients._id_ingredient is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: "",
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients+"."+api.param_ingredient_id,
                                   msg=rep.detail_must_be_an_object_id,
                                   value=body[api.param_ingredients][0][api.param_ingredient_id])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_id_is_invalid(self):
        """ BodyParameter ingredients._id_ingredient is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: "invalid",
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients+"."+api.param_ingredient_id,
                                   msg=rep.detail_must_be_an_object_id,
                                   value=body[api.param_ingredients][0][api.param_ingredient_id])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_id_is_invalid_object_id(self):
        """ BodyParameter ingredients._id_ingredient is an nok ObjectId.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: "aaaaaaaaaaaaaaaaaaaaaaaa",
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients+"."+api.param_ingredient_id,
                                   msg=rep.detail_doesnot_exist,
                                   value=body[api.param_ingredients][0][api.param_ingredient_id])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_quantity_without(self):
        """ BodyParameter ingredients.quantity is missing.

        Return
            400 - Bad request.
        """

        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients+"."+api.param_ingredient_quantity,
                                   msg=rep.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_quantity_null(self):
        """ BodyParameter ingredients.quantity is null.

        Return
            400 - Bad request.
        """

        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: None,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients+"."+api.param_ingredient_quantity,
                                   msg=rep.detail_must_be_a_float,
                                   value=body[api.param_ingredients][0][api.param_ingredient_quantity])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_quantity_empty(self):
        """ BodyParameter ingredients.quantity is an empty string.

        Return
            400 - Bad request.
        """

        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: "",
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients+"."+api.param_ingredient_quantity,
                                   msg=rep.detail_must_be_a_float,
                                   value=body[api.param_ingredients][0][api.param_ingredient_quantity])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_quantity_invalid(self):
        """ BodyParameter ingredients.quantity is a string.

        Return
            400 - Bad request.
        """

        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: "invalid",
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients+"."+api.param_ingredient_quantity,
                                   msg=rep.detail_must_be_a_float,
                                   value=body[api.param_ingredients][0][api.param_ingredient_quantity])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_quantity_number_string(self):
        """ BodyParameter ingredients.quantity is a string number.

        Return
            200 - Updated Recipe.
        """

        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: "5",
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_quantity_number(self):
        """ BodyParameter ingredients.quantity is a number.

        Return
            200 - Updated Recipe.
        """

        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_quantity_float(self):
        """ BodyParameter ingredients.quantity is a number float.

        Return
            200 - Updated Recipe.
        """

        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5.1,
                                         api.param_ingredient_unit: "qa_rhr_unit"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_unit_without(self):
        """ BodyParameter ingredients.unit is missing.

        Return
            400 - Bad request.
        """

        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients+"."+api.param_ingredient_unit,
                                   msg=rep.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_unit_null(self):
        """ BodyParameter ingredients.unit is null.

        Return
            400 - Bad request.
        """

        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: None}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients+"."+api.param_ingredient_unit,
                                   msg=rep.detail_must_be_a_string,
                                   value=body[api.param_ingredients][0][api.param_ingredient_unit])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_unit_empty(self):
        """ BodyParameter ingredients.unit is an empty string.

        Return
            200 - Updated Recipe.
        """

        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: ""}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_unit_invalid(self):
        """ BodyParameter ingredients.unit is a string.

        Return
            200 - Updated Recipe.
        """

        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "invalid"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_same(self):
        """ Special case: identical.

        Return
            400 - Bad request.
        """
        tc_ingredient = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"},
                                        {api.param_ingredient_id: tc_ingredient.get_id(),
                                         api.param_ingredient_quantity: 6,
                                         api.param_ingredient_unit: "qa_rhr_unit2"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_ingredients+"."+api.param_ingredient_id,
                                   msg=rep.detail_must_be_unique,
                                   value=[ingr[api.param_ingredient_id] for ingr in body[api.param_ingredients]])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe.check_bdd_data()

    def test_ingredients_already_exist(self):
        """ Special case: already_exist.

        Return
            400 - Bad request.
        """
        tc_ingredient1 = IngredientTest().insert()
        tc_ingredient2 = IngredientTest().insert()
        tc_ingredient3 = IngredientTest().insert()
        """ env """
        tc_recipe = RecipeTest().insert()
        tc_recipe.add_ingredient(ingredient=tc_ingredient1, quantity=1, unit="unit1")
        tc_recipe.add_ingredient(ingredient=tc_ingredient2, quantity=2, unit="unit2")
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_ingredients: [{api.param_ingredient_id: tc_ingredient1.get_id(),
                                         api.param_ingredient_quantity: 5,
                                         api.param_ingredient_unit: "qa_rhr_unit"},
                                        {api.param_ingredient_id: tc_ingredient3.get_id(),
                                         api.param_ingredient_quantity: 3,
                                         api.param_ingredient_unit: "qa_rhr_unit3"},
                                        {api.param_ingredient_id: tc_ingredient2.get_id(),
                                         api.param_ingredient_quantity: 6,
                                         api.param_ingredient_unit: "qa_rhr_unit2"}]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestPutRecipe())


if __name__ == '__main__':
    unittest.main()

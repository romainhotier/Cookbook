import unittest
import requests

import utils
import tests.ingredient.DeleteIngredient.api as api
import tests.ingredient.model as ingredient_model
import tests.file.model as file_model
import tests.recipe.model as recipe_model

server = utils.Server()
api = api.DeleteIngredient()
ingredient = ingredient_model.IngredientTest()
ingredient_recipe = ingredient_model.IngredientRecipeTest()
recipe = recipe_model.RecipeTest()
file = file_model.FileTest()


class DeleteIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean all IngredientTest, RecipeTest, IngredientRecipeTest and FileTest. """
        ingredient.clean()
        recipe.clean()
        ingredient_recipe.clean()
        file.clean()

    def test_0_api_ok(self):
        """ Default case.

        Return
            204 - Ingredient Deleted.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.text, '')
        """ check """
        tc_ingredient1.select_nok()
        tc_ingredient2.select_ok()

    def test_1_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "x/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check """
        tc_ingredient1.select_ok()
        tc_ingredient2.select_ok()

    def test_2_id_without(self):
        """ QueryParameter _id missing.

        Return
            404 - Url not found.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "/"
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check """
        tc_ingredient1.select_ok()
        tc_ingredient2.select_ok()

    def test_2_id_string(self):
        """ QueryParameter _id is string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id, msg=server.detail_must_be_an_object_id, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient1.select_ok()
        tc_ingredient2.select_ok()

    def test_2_id_object_id_invalid(self):
        """ QueryParameter _id is nok ObjectId.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id, msg=server.detail_doesnot_exist, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient1.select_ok()
        tc_ingredient2.select_ok()

    def test_3_file_clean(self):
        """ File associated cleaned.

        Return
            204 - Ingredient Deleted.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_file1 = tc_ingredient1.add_file(filename="qa_rhr_1", is_main=False)
        tc_file2 = tc_ingredient1.add_file(filename="qa_rhr_2", is_main=False)
        """ param """
        tc_id = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.text, '')
        """ check """
        tc_ingredient1.select_nok()
        tc_file1.select_nok()
        tc_file2.select_nok()

    def test_4_link_clean(self):
        """ IngredientRecipe associated cleaned.

        Return
            204 - Ingredient Deleted.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_lk = ingredient_model.IngredientRecipeTest().custom({"_id_ingredient": tc_ingredient._id,
                                                                "_id_recipe": tc_recipe._id}).insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.text, '')
        """ check """
        tc_ingredient.select_nok()
        tc_recipe.select_ok()
        tc_lk.select_nok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(DeleteIngredient())


if __name__ == '__main__':
    unittest.main()

import unittest
import requests

import utils
import tests.test_recipe.DeleteRecipe.api as api
import tests.test_ingredient.model as ingredient_model
import tests.test_recipe.model as recipe_model

server = utils.Server()
api = api.DeleteRecipe()
ingredient = ingredient_model.IngredientTest()
recipe = recipe_model.RecipeTest()


class DeleteRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest, RecipeTest."""
        recipe.clean()
        ingredient.clean()

    def test_id_without(self):
        """ QueryParameter _id is missing.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_recipe2 = recipe_model.RecipeTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "/"
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
        tc_recipe1.check_bdd_data()
        tc_recipe2.check_bdd_data()

    def test_id_string(self):
        """ QueryParameter _id is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_recipe2 = recipe_model.RecipeTest().insert()
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
        detail = api.create_detail(param=api.param_id, msg=server.detail_must_be_an_object_id, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe1.check_bdd_data()
        tc_recipe2.check_bdd_data()

    def test_id_object_id_invalid(self):
        """ QueryParameter _id is a nok ObjectId.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_recipe2 = recipe_model.RecipeTest().insert()
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
        detail = api.create_detail(param=api.param_id, msg=server.detail_doesnot_exist, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_recipe1.check_bdd_data()
        tc_recipe2.check_bdd_data()
        
    @classmethod
    def tearDownClass(cls):
        cls.setUp(DeleteRecipe())


if __name__ == '__main__':
    unittest.main()

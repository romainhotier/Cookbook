import unittest
import requests

import utils
import tests.recipe.DeleteRecipe.api as api
import tests.ingredient.model as ingredient_model
import tests.recipe.model as recipe_model
import tests.file.model as file_model

server = utils.Server()
api = api.DeleteRecipe()
ingredient = ingredient_model.IngredientTest()
recipe = recipe_model.RecipeTest()
file = file_model.FileTest()


class DeleteRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest, RecipeTest and FileTest."""
        recipe.clean()
        ingredient.clean()
        file.clean()

    def test_api_ok(self):
        """ Default case.

        Return
            204 - Recipe Deleted.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_recipe2 = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(_id=tc_id))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe1.check_doesnt_exist_by_id()
        tc_recipe2.check_bdd_data()

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().insert()
        tc_recipe2 = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe1.get_id()
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
        tc_recipe1.check_bdd_data()
        tc_recipe2.check_bdd_data()

    def test_api_clean_file(self):
        """ File associated cleaned.

        Return
            204 - Recipe Deleted.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "qa_rhr_a"})
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "qa_rhr_b"})
        tc_recipe1.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe1.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        tc_recipe2.add_step(_id_step="333333333333333333333333", description="step recipe 2 - 1st")
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
        """ param """
        tc_id = tc_recipe1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.text, '')
        """ check """
        tc_recipe1.check_doesnt_exist_by_id()
        tc_file_recipe11.check_doesnt_exist_by_id()
        tc_file_recipe12.check_doesnt_exist_by_id()
        tc_file_step111.check_doesnt_exist_by_id()
        tc_file_step121.check_doesnt_exist_by_id()
        tc_file_step122.check_doesnt_exist_by_id()
        tc_recipe2.check_bdd_data()
        tc_file_recipe2.check_exist_by_id()
        tc_file_step211.check_exist_by_id()
        tc_file_step212.check_exist_by_id()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(DeleteRecipe())


if __name__ == '__main__':
    unittest.main()

import unittest
import requests

import utils
import tests.recipe.GetAllRecipe.api as api
import tests.recipe.model as recipe_model
import tests.ingredient.model as ingredient_model
import tests.file.model as file_model

server = utils.Server()
api = api.GetAllRecipe()
recipe = recipe_model.RecipeTest()
ingredient = ingredient_model.IngredientTest()
file = file_model.FileTest()


class GetAllRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest, IngredientTest and FileTest."""
        recipe.clean()
        ingredient.clean()
        file.clean()

    def test_with_files_without(self):
        """ QueryParameter with_files is missing.

        Return
            200 - All Recipes.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest()
        tc_recipe2 = recipe_model.RecipeTest()
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
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(recipe=tc_recipe1), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe2), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_with_files_empty(self):
        """ QueryParameter with_files is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        recipe_model.RecipeTest().insert()
        recipe_model.RecipeTest().insert()
        """ param """
        tc_with_files = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + api.detail_with_files,
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)

    def test_with_files_invalid(self):
        """ QueryParameter with_files is a string.

        Return
            400 - Bad request.
        """
        """ env """
        recipe_model.RecipeTest().insert()
        recipe_model.RecipeTest().insert()
        """ param """
        tc_with_files = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + api.detail_with_files,
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)

    def test_with_files_false(self):
        """ QueryParameter with_files is false.

        Return
            200 - All Recipes.
        """
        """ env """
        tc_recipe1 = recipe_model.RecipeTest()
        tc_recipe2 = recipe_model.RecipeTest()
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
        tc_with_files = "false"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(recipe=tc_recipe1), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe2), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_with_files_true(self):
        """ QueryParameter with_files is true.

        Return
            200 - All Recipes.
        """
        """"""" env """""""
        """ ingredients """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ recipe1 """
        tc_recipe1 = recipe_model.RecipeTest()
        tc_recipe1.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe1.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        """ recipe1 ingredients """
        tc_recipe1.add_ingredient(_id=tc_ingredient1.get_id(), quantity=1, unit="qa_rhr1")
        tc_recipe1.add_ingredient(_id=tc_ingredient2.get_id(), quantity=2, unit="qa_rhr2")
        """ recipe2 """
        tc_recipe2 = recipe_model.RecipeTest()
        tc_recipe2.add_step(_id_step="333333333333333333333333", description="step recipe 2 - 1st")
        """ recipe2 ingredients """
        tc_recipe2.add_ingredient(_id=tc_ingredient2.get_id(), quantity=22, unit="qa_rhr22")
        """" recipes """
        tc_recipe1.insert()
        tc_recipe2.insert()
        """ files ingredients """
        tc_file_ingredient1 = tc_ingredient1.add_file(filename="qa_rhr_ing_11", is_main=True)
        tc_file_ingredient1_bis = tc_ingredient1.add_file(filename="qa_rhr_ing_11", is_main=False)
        tc_file_ingredient2 = tc_ingredient2.add_file(filename="qa_rhr_ing_2", is_main=False)
        """ files recipes """
        tc_file_recipe1 = tc_recipe1.add_file_recipe(filename="qa_rhr_1", is_main=True)
        tc_file_recipe1_bis = tc_recipe1.add_file_recipe(filename="qa_rhr_2", is_main=False)
        tc_file_recipe2 = tc_recipe2.add_file_recipe(filename="qa_rhr_3", is_main=False)
        """ files steps """
        tc_file_step1 = tc_recipe1.add_file_step(_id_step="111111111111111111111111", filename="qa_rhr_11",
                                                 is_main=False)
        tc_file_step2 = tc_recipe1.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_21",
                                                 is_main=False)
        tc_file_step2_bis = tc_recipe1.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_22",
                                                     is_main=True)
        tc_file_step3 = tc_recipe2.add_file_step(_id_step="333333333333333333333333", filename="qa_rhr_31",
                                                 is_main=True)
        tc_file_step3_bis = tc_recipe2.add_file_step(_id_step="333333333333333333333333", filename="qa_rhr_32",
                                                     is_main=False)

        """ param """
        tc_with_files = "true"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.get(url, verify=False)
        response_body = response.json()
        print(response_body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(recipe=tc_recipe1), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe2), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetAllRecipe())


if __name__ == '__main__':
    unittest.main()

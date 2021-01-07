import unittest
import requests

import utils
import tests.test_recipe.GetAllRecipe.api as api
import tests.test_recipe.model as recipe_model
import tests.test_ingredient.model as ingredient_model

server = utils.Server()
api = api.GetAllRecipe()
recipe = recipe_model.RecipeTest()
ingredient = ingredient_model.IngredientTest()


class GetAllRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest, IngredientTest."""
        recipe.clean()
        ingredient.clean()

    def test_with_calories_without(self):
        """ QueryParameter with_calories is missing.

        Return
            200 - All Recipes.
        """
        """"""" env """""""
        """ ingredients """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        tc_ingredient3 = ingredient_model.IngredientTest().insert()
        """ recipe1 """
        tc_recipe1 = recipe_model.RecipeTest()
        tc_recipe1.add_ingredient(_id=tc_ingredient1.get_id(), quantity=1, unit="gr")
        tc_recipe1.add_ingredient(_id=tc_ingredient2.get_id(), quantity=2, unit="gr")
        tc_recipe1.insert()
        """ recipe2 """
        tc_recipe2 = recipe_model.RecipeTest()
        tc_recipe2.add_ingredient(_id=tc_ingredient2.get_id(), quantity=2, unit="gr")
        tc_recipe2.add_ingredient(_id=tc_ingredient3.get_id(), quantity=3, unit="portion")
        tc_recipe2.insert()
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(recipe=tc_recipe1).get_data_expected(), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe2).get_data_expected(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_with_calories_empty(self):
        """ QueryParameter with_calories is an empty string.

        Return
            400 - Bad request.
        """
        """"""" env """""""
        """ ingredients """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        tc_ingredient3 = ingredient_model.IngredientTest().insert()
        """ recipe1 """
        tc_recipe1 = recipe_model.RecipeTest()
        tc_recipe1.add_ingredient(_id=tc_ingredient1.get_id(), quantity=1, unit="gr")
        tc_recipe1.add_ingredient(_id=tc_ingredient2.get_id(), quantity=2, unit="gr")
        tc_recipe1.insert()
        """ recipe2 """
        tc_recipe2 = recipe_model.RecipeTest()
        tc_recipe2.add_ingredient(_id=tc_ingredient2.get_id(), quantity=2, unit="gr")
        tc_recipe2.add_ingredient(_id=tc_ingredient3.get_id(), quantity=3, unit="portion")
        tc_recipe2.insert()
        """ param """
        tc_with_calories = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_calories + "=" + tc_with_calories
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_calories,
                                   msg=server.detail_must_be_in + api.detail_with_files,
                                   value=tc_with_calories)
        self.assertEqual(response_body["detail"], detail)

    def test_with_calories_invalid(self):
        """ QueryParameter with_calories is a string.

        Return
            400 - Bad request.
        """
        """"""" env """""""
        """ ingredients """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        tc_ingredient3 = ingredient_model.IngredientTest().insert()
        """ recipe1 """
        tc_recipe1 = recipe_model.RecipeTest()
        tc_recipe1.add_ingredient(_id=tc_ingredient1.get_id(), quantity=1, unit="gr")
        tc_recipe1.add_ingredient(_id=tc_ingredient2.get_id(), quantity=2, unit="gr")
        tc_recipe1.insert()
        """ recipe2 """
        tc_recipe2 = recipe_model.RecipeTest()
        tc_recipe2.add_ingredient(_id=tc_ingredient2.get_id(), quantity=2, unit="gr")
        tc_recipe2.add_ingredient(_id=tc_ingredient3.get_id(), quantity=3, unit="portion")
        tc_recipe2.insert()
        """ param """
        tc_with_calories = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_calories + "=" + tc_with_calories
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_calories,
                                   msg=server.detail_must_be_in + api.detail_with_files,
                                   value=tc_with_calories)
        self.assertEqual(response_body["detail"], detail)

    def test_with_calories_false(self):
        """ QueryParameter with_calories is false.

        Return
            200 - All Recipes.
        """
        """"""" env """""""
        """ ingredients """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        tc_ingredient3 = ingredient_model.IngredientTest().insert()
        """ recipe1 """
        tc_recipe1 = recipe_model.RecipeTest()
        tc_recipe1.add_ingredient(_id=tc_ingredient1.get_id(), quantity=1, unit="gr")
        tc_recipe1.add_ingredient(_id=tc_ingredient2.get_id(), quantity=2, unit="gr")
        tc_recipe1.insert()
        """ recipe2 """
        tc_recipe2 = recipe_model.RecipeTest()
        tc_recipe2.add_ingredient(_id=tc_ingredient2.get_id(), quantity=2, unit="gr")
        tc_recipe2.add_ingredient(_id=tc_ingredient3.get_id(), quantity=3, unit="portion")
        tc_recipe2.insert()
        """ param """
        tc_with_calories = "false"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_calories + "=" + tc_with_calories
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(recipe=tc_recipe1).get_data_expected(), response_body["data"])
        self.assertIn(api.data_expected(recipe=tc_recipe2).get_data_expected(), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_with_calories_true(self):
        """ QueryParameter with_calories is true.

        Return
            200 - All Recipes.
        """
        """"""" env """""""
        """ ingredients """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        tc_ingredient3 = ingredient_model.IngredientTest().insert()
        """ recipe1 """
        tc_recipe1 = recipe_model.RecipeTest()
        tc_recipe1.add_ingredient(_id=tc_ingredient1.get_id(), quantity=1, unit="gr")
        tc_recipe1.add_ingredient(_id=tc_ingredient2.get_id(), quantity=2, unit="gr")
        tc_recipe1.insert()
        """ recipe2 """
        tc_recipe2 = recipe_model.RecipeTest()
        tc_recipe2.add_ingredient(_id=tc_ingredient2.get_id(), quantity=2, unit="gr")
        tc_recipe2.add_ingredient(_id=tc_ingredient3.get_id(), quantity=3, unit="portion")
        tc_recipe2.insert()
        """ param """
        tc_with_calories = "true"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_with_calories + "=" + tc_with_calories
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        print(response_body)
        # """ data recipe 1 """
        # formated_data1 = api.data_expected(recipe=tc_recipe1, files_mongo=[tc_file_recipe1, tc_file_recipe1_bis])
        # formated_data1.add_ingredient_files_mongo(ingredient=tc_ingredient1, files_mongo=[tc_file_ingredient1,
        #                                                                                   tc_file_ingredient1_bis])
        # formated_data1.add_ingredient_files_mongo(ingredient=tc_ingredient2, files_mongo=[tc_file_ingredient2])
        # formated_data1.add_steps_files_mongo(_id="111111111111111111111111", files_mongo=[tc_file_step1])
        # formated_data1.add_steps_files_mongo(_id="222222222222222222222222",
        #                                      files_mongo=[tc_file_step2, tc_file_step2_bis])
        # """ data recipe 2 """
        # formated_data2 = api.data_expected(recipe=tc_recipe2, files_mongo=[tc_file_recipe2])
        # formated_data2.add_ingredient_files_mongo(ingredient=tc_ingredient2, files_mongo=[tc_file_ingredient2])
        # formated_data2.add_steps_files_mongo(_id="333333333333333333333333",
        #                                      files_mongo=[tc_file_step3, tc_file_step3_bis])
        # """ assert data """
        # self.assertIn(formated_data1.get_data_expected(), response_body["data"])
        # self.assertIn(formated_data2.get_data_expected(), response_body["data"])
        # self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetAllRecipe())


if __name__ == '__main__':
    unittest.main()

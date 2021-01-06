import unittest
import requests

import utils
import tests.test_recipe.GetRecipe.api as api
import tests.test_recipe.model as recipe_model
import tests.test_ingredient.model as ingredient_model
import tests.test_file_mongo.model as file_mongo_model

server = utils.Server()
api = api.GetRecipe()
recipe = recipe_model.RecipeTest()
ingredient = ingredient_model.IngredientTest()
file_mongo = file_mongo_model.FileMongoTest()


class GetRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest, IngredientTest and FileMongoTest."""
        recipe.clean()
        ingredient.clean()
        file_mongo.clean()

    def test_with_files_without(self):
        """ QueryParameter with_files is missing.

        Return
            200 - All Recipes.
        """
        """"""" env """""""
        """ ingredients """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ recipe1 """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        """ recipe1 ingredients """
        tc_recipe.add_ingredient(_id=tc_ingredient1.get_id(), quantity=1, unit="qa_rhr1")
        tc_recipe.add_ingredient(_id=tc_ingredient2.get_id(), quantity=2, unit="qa_rhr2")
        """" recipes """
        tc_recipe.insert()
        """ files ingredients """
        tc_ingredient1.add_file_mongo(filename="qa_rhr_ing_11", is_main=True)
        tc_ingredient1.add_file_mongo(filename="qa_rhr_ing_11", is_main=False)
        tc_ingredient2.add_file_mongo(filename="qa_rhr_ing_2", is_main=False)
        """ files recipes """
        tc_recipe.add_file_mongo_recipe(filename="qa_rhr_1", is_main=True)
        tc_recipe.add_file_mongo_recipe(filename="qa_rhr_2", is_main=False)
        """ files steps """
        tc_recipe.add_file_mongo_step(_id_step="111111111111111111111111", filename="qa_rhr_11", is_main=False)
        tc_recipe.add_file_mongo_step(_id_step="222222222222222222222222", filename="qa_rhr_21", is_main=False)
        tc_recipe.add_file_mongo_step(_id_step="222222222222222222222222", filename="qa_rhr_22", is_main=True)
        """ param """
        tc_slug = tc_recipe.slug
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe).get_data_expected())
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_with_files_empty(self):
        """ QueryParameter with_files is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_slug = tc_recipe.slug
        tc_with_files_mongo = ""
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug + "?" + api.param_with_files_mongo + "=" + \
            tc_with_files_mongo
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files_mongo,
                                   msg=server.detail_must_be_in + api.detail_with_files,
                                   value=tc_with_files_mongo)
        self.assertEqual(response_body["detail"], detail)

    def test_with_files_invalid(self):
        """ QueryParameter with_files is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_slug = tc_recipe.slug
        tc_with_files_mongo = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug + "?" + api.param_with_files_mongo + "=" + \
            tc_with_files_mongo
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files_mongo,
                                   msg=server.detail_must_be_in + api.detail_with_files,
                                   value=tc_with_files_mongo)
        self.assertEqual(response_body["detail"], detail)

    def test_with_files_false(self):
        """ QueryParameter with_files is false.

        Return
            200 - All Recipes.
        """
        """"""" env """""""
        """ ingredients """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ recipe1 """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        """ recipe1 ingredients """
        tc_recipe.add_ingredient(_id=tc_ingredient1.get_id(), quantity=1, unit="qa_rhr1")
        tc_recipe.add_ingredient(_id=tc_ingredient2.get_id(), quantity=2, unit="qa_rhr2")
        """" recipes """
        tc_recipe.insert()
        """ files ingredients """
        tc_ingredient1.add_file_mongo(filename="qa_rhr_ing_11", is_main=True)
        tc_ingredient1.add_file_mongo(filename="qa_rhr_ing_11", is_main=False)
        tc_ingredient2.add_file_mongo(filename="qa_rhr_ing_2", is_main=False)
        """ files recipes """
        tc_recipe.add_file_mongo_recipe(filename="qa_rhr_1", is_main=True)
        tc_recipe.add_file_mongo_recipe(filename="qa_rhr_2", is_main=False)
        """ files steps """
        tc_recipe.add_file_mongo_step(_id_step="111111111111111111111111", filename="qa_rhr_11", is_main=False)
        tc_recipe.add_file_mongo_step(_id_step="222222222222222222222222", filename="qa_rhr_21", is_main=False)
        tc_recipe.add_file_mongo_step(_id_step="222222222222222222222222", filename="qa_rhr_22", is_main=True)
        """ param """
        tc_slug = tc_recipe.slug
        tc_with_files_mongo = "false"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug + "?" + api.param_with_files_mongo + "=" + \
            tc_with_files_mongo
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe).get_data_expected())
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
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_step(_id_step="111111111111111111111111", description="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", description="step recipe 1 - 2nd")
        """ recipe1 ingredients """
        tc_recipe.add_ingredient(_id=tc_ingredient1.get_id(), quantity=1, unit="qa_rhr1")
        tc_recipe.add_ingredient(_id=tc_ingredient2.get_id(), quantity=2, unit="qa_rhr2")
        """" recipes """
        tc_recipe.insert()
        """ files ingredients """
        tc_file_ingredient1 = tc_ingredient1.add_file_mongo(filename="qa_rhr_ing_11", is_main=True)
        tc_file_ingredient1_bis = tc_ingredient1.add_file_mongo(filename="qa_rhr_ing_11", is_main=False)
        tc_file_ingredient2 = tc_ingredient2.add_file_mongo(filename="qa_rhr_ing_2", is_main=False)
        """ files recipes """
        tc_file_recipe1 = tc_recipe.add_file_mongo_recipe(filename="qa_rhr_1", is_main=True)
        tc_file_recipe1_bis = tc_recipe.add_file_mongo_recipe(filename="qa_rhr_2", is_main=False)
        """ files steps """
        tc_file_step1 = tc_recipe.add_file_mongo_step(_id_step="111111111111111111111111", filename="qa_rhr_11",
                                                      is_main=False)
        tc_file_step2 = tc_recipe.add_file_mongo_step(_id_step="222222222222222222222222", filename="qa_rhr_21",
                                                      is_main=False)
        tc_file_step2_bis = tc_recipe.add_file_mongo_step(_id_step="222222222222222222222222", filename="qa_rhr_22",
                                                          is_main=True)
        """ param """
        tc_slug = tc_recipe.slug
        tc_with_files_mongo = "true"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug + "?" + api.param_with_files_mongo + "=" + \
            tc_with_files_mongo
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        """ data recipe """
        formated_data = api.data_expected(recipe=tc_recipe, files_mongo=[tc_file_recipe1, tc_file_recipe1_bis])
        formated_data.add_ingredient_files_mongo(ingredient=tc_ingredient1, files_mongo=[tc_file_ingredient1,
                                                                                         tc_file_ingredient1_bis])
        formated_data.add_ingredient_files_mongo(ingredient=tc_ingredient2, files_mongo=[tc_file_ingredient2])
        formated_data.add_steps_files_mongo(_id="111111111111111111111111", files_mongo=[tc_file_step1])
        formated_data.add_steps_files_mongo(_id="222222222222222222222222",
                                            files_mongo=[tc_file_step2, tc_file_step2_bis])
        """ assert data """
        self.assertEqual(response_body["data"], formated_data.get_data_expected())
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetRecipe())


if __name__ == '__main__':
    unittest.main()

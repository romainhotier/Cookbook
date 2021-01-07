import unittest
import requests

import utils
import tests.test_recipe.GetRecipe.api as api
import tests.test_recipe.model as recipe_model
import tests.test_ingredient.model as ingredient_model

server = utils.Server()
api = api.GetRecipe()
recipe = recipe_model.RecipeTest()
ingredient = ingredient_model.IngredientTest()


class GetRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest, IngredientTest."""
        recipe.clean()
        ingredient.clean()

    def test_calories_without(self):
        """ QueryParameter with_calories is missing.

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

    def test_calories_empty(self):
        """ QueryParameter with_calories is an empty string.

        Return
            400 - Bad request.
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
        """ param """
        tc_slug = tc_recipe.slug
        tc_with_calories = ""
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug + "?" + api.param_with_calories + "=" + \
            tc_with_calories
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

    def test_calories_invalid(self):
        """ QueryParameter with_calories is a string.

        Return
            400 - Bad request.
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
        """ param """
        tc_slug = tc_recipe.slug
        tc_with_calories = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug + "?" + api.param_with_calories + "=" + \
            tc_with_calories
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

    def test_calories_false(self):
        """ QueryParameter with_calories is false.

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
        """ param """
        tc_slug = tc_recipe.slug
        tc_with_calories = "false"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug + "?" + api.param_with_calories + "=" + \
            tc_with_calories
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe).get_data_expected())
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_calories_true(self):
        """ QueryParameter with_calories is true.

        Return
            200 - All Recipes.
        """
        """"""" env """""""
        """ ingredients """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ recipe """
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_ingredient(_id=tc_ingredient1.get_id(), quantity=2, unit="gr")
        tc_recipe.add_ingredient(_id=tc_ingredient2.get_id(), quantity=3, unit="portion")
        tc_recipe.insert()
        """ param """
        tc_slug = tc_recipe.slug
        tc_with_calories = "true"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_slug + "?" + api.param_with_calories + "=" + \
            tc_with_calories
        response = requests.get(url, verify=False)
        response_body = response.json()
        print(response_body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        """ assert data """
        # self.assertEqual(response_body["data"],
        #                  api.data_expected(recipe=tc_recipe,
        #                                    calories=[tc_ingredient1, tc_ingredient2]).get_data_expected())
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetRecipe())


if __name__ == '__main__':
    unittest.main()

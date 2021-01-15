import unittest
import requests

from tests import server, rep
from tests.test_ingredient import IngredientTest
from tests.test_recipe import RecipeTest
from tests.test_recipe.GetRecipe import api


class TestGetRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest, IngredientTest."""
        RecipeTest().clean()
        IngredientTest.clean()

    def test_calories_without(self):
        """ QueryParameter with_calories is missing.

        Return
            200 - All Recipes.
        """
        """"""" env """""""
        """ ingredients """
        tc_ingredient1 = IngredientTest().insert()
        tc_ingredient2 = IngredientTest().insert()
        """ recipe """
        tc_recipe = RecipeTest().insert()
        """ recipe ingredients """
        tc_recipe.add_ingredient(ingredient=tc_ingredient1, quantity=1, unit="gr")
        tc_recipe.add_ingredient(ingredient=tc_ingredient2, quantity=2, unit="gr")
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
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_calories_empty(self):
        """ QueryParameter with_calories is an empty string.

        Return
            400 - Bad request.
        """
        """"""" env """""""
        """ ingredients """
        tc_ingredient1 = IngredientTest().insert()
        tc_ingredient2 = IngredientTest().insert()
        """ recipe """
        tc_recipe = RecipeTest().insert()
        """ recipe ingredients """
        tc_recipe.add_ingredient(ingredient=tc_ingredient1, quantity=1, unit="gr")
        tc_recipe.add_ingredient(ingredient=tc_ingredient2, quantity=2, unit="gr")
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
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_with_calories, msg=rep.detail_must_be_in + api.detail_boolean,
                                   value=tc_with_calories)
        self.assertEqual(response_body["detail"], detail)

    def test_calories_invalid(self):
        """ QueryParameter with_calories is a string.

        Return
            400 - Bad request.
        """
        """"""" env """""""
        """ ingredients """
        tc_ingredient1 = IngredientTest().insert()
        tc_ingredient2 = IngredientTest().insert()
        """ recipe """
        tc_recipe = RecipeTest().insert()
        """ recipe ingredients """
        tc_recipe.add_ingredient(ingredient=tc_ingredient1, quantity=1, unit="gr")
        tc_recipe.add_ingredient(ingredient=tc_ingredient2, quantity=2, unit="gr")
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
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        detail = rep.format_detail(param=api.param_with_calories, msg=rep.detail_must_be_in + api.detail_boolean,
                                   value=tc_with_calories)
        self.assertEqual(response_body["detail"], detail)

    def test_calories_false(self):
        """ QueryParameter with_calories is false.

        Return
            200 - All Recipes.
        """
        """"""" env """""""
        """ ingredients """
        tc_ingredient1 = IngredientTest().insert()
        tc_ingredient2 = IngredientTest().insert()
        """ recipe """
        tc_recipe = RecipeTest().insert()
        """ recipe ingredients """
        tc_recipe.add_ingredient(ingredient=tc_ingredient1, quantity=1, unit="gr")
        tc_recipe.add_ingredient(ingredient=tc_ingredient2, quantity=2, unit="gr")
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
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    def test_calories_true(self):
        """ QueryParameter with_calories is true.

        Return
            200 - All Recipes.
        """
        """"""" env """""""
        """ ingredients """
        tc_ingredient1 = IngredientTest().insert()
        tc_ingredient2 = IngredientTest().insert()
        """ recipe """
        tc_recipe = RecipeTest().insert()
        """ recipe ingredients """
        tc_recipe.add_ingredient(ingredient=tc_ingredient1, quantity=1, unit="gr")
        tc_recipe.add_ingredient(ingredient=tc_ingredient2, quantity=2, unit="gr")
        """ param """
        tc_slug = tc_recipe.slug
        tc_with_calories = "true"
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
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe, calories=True))
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestGetRecipe())


if __name__ == '__main__':
    unittest.main()

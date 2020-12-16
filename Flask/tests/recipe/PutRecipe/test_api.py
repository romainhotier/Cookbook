import unittest
import requests

import utils
import tests.recipe.PutRecipe.api as api
import tests.recipe.model as recipe_model
import tests.ingredient.model as ingredient_model

server = utils.Server()
api = api.PutRecipe()
recipe = recipe_model.RecipeTest()
ingredient = ingredient_model.IngredientTest()


class PutRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest and IngredientTest."""
        recipe.clean()
        ingredient.clean()

    def test_api_ok(self):
        """ Default case.

        Return
            200 - Updated Recipe.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
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
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_api_ok_more_param(self):
        """ Default case with more parameters.

        Return
            200 - Updated Recipe.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        tc_ingredient3 = ingredient_model.IngredientTest().insert()
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_ingredient(_id=tc_ingredient1.get_id(), quantity=1, unit='unit1')
        tc_recipe.add_ingredient(_id=tc_ingredient2.get_id(), quantity=2, unit='unit2')
        tc_recipe.add_step(_id_step="aaaaaaaaaaaaaaaaaaaaaaaa", description="step1")
        tc_recipe.add_step(_id_step="bbbbbbbbbbbbbbbbbbbbbbbb", description="step2")
        tc_recipe.insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {"categories": ["categori1", "categori2"],
                "cooking_time": 30,
                "ingredients": [{"_id": tc_ingredient1.get_id(), "quantity": 11, "unit": "qa_rhr_unit1_update",
                                 "invalid": "invalid"},
                                {"_id": tc_ingredient3.get_id(), "quantity": 3, "unit": "qa_rhr_unit3"},
                                {"_id": tc_ingredient2.get_id(), "quantity": 2, "unit": "unit2"}],
                "level": 2,
                "nb_people": 4,
                "note": "note_ex",
                "preparation_time": 8,
                "resume": "resume_ex",
                "slug": "slug_update",
                "status": "in_progress",
                "steps": [{api.param_step_id: "aaaaaaaaaaaaaaaaaaaaaaaa", api.param_step_description: "step1_up"},
                          "step_new",
                          {api.param_step_id: "cccccccccccccccccccccccc", api.param_step_description: "step_new_fake"},
                          {api.param_step_id: "bbbbbbbbbbbbbbbbbbbbbbbb", api.param_step_description: "step2_update",
                           "invalid": "invalid"}],
                "title": "qa_rhr_title_update",
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        print(response_body)
        """ change """
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = recipe_model.RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "x" + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check """
        tc_recipe.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        #cls.setUp(PutRecipe())
        pass


if __name__ == '__main__':
    unittest.main()

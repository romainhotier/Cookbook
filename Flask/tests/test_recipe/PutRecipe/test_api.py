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

    def test_api_ok(self):
        """ Default case.

        Return
            200 - Updated Recipe.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(data=body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(api.response_without_steps(data=response_body["data"]),
                         api.data_expected_without_steps(recipe=tc_recipe))
        api.check_steps(recipe=tc_recipe, response_data=response_body["data"])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_api_ok_more_param(self):
        """ Default case with more parameters.

        Return
            200 - Updated Recipe.
        """
        """"""" env """""""
        """ ingredients """
        tc_ingredient1 = IngredientTest().insert()
        tc_ingredient2 = IngredientTest().insert()
        tc_ingredient3 = IngredientTest().insert()
        """ recipe """
        tc_recipe = RecipeTest().insert()
        """ recipe ingredients """
        tc_recipe.add_ingredient(ingredient=tc_ingredient1, quantity=1, unit='unit1')
        tc_recipe.add_ingredient(ingredient=tc_ingredient2, quantity=2, unit='unit2')
        """ recipe steps """
        tc_recipe.add_step(_id_step="aaaaaaaaaaaaaaaaaaaaaaaa", description="step1")
        tc_recipe.add_step(_id_step="bbbbbbbbbbbbbbbbbbbbbbbb", description="step2")
        """ param """
        tc_id = tc_recipe.get_id()
        body = {api.param_categories: ["categori1up", "categori2up"],
                api.param_cooking_time: 30,
                api.param_ingredients: [{api.param_ingredient_id: tc_ingredient1.get_id(),
                                         api.param_ingredient_quantity: 11,
                                         api.param_ingredient_unit: "qa_rhr_unit1_update",
                                         "invalid": "invalid"},
                                        {api.param_ingredient_id: tc_ingredient3.get_id(),
                                         api.param_ingredient_quantity: 3,
                                         api.param_ingredient_unit: "qa_rhr_unit3"},
                                        {api.param_ingredient_id: tc_ingredient2.get_id(),
                                         api.param_ingredient_quantity: 2,
                                         api.param_ingredient_unit: "unit2"}],
                api.param_level: 2,
                api.param_nb_people: 4,
                api.param_note: "note_up",
                api.param_preparation_time: 8,
                api.param_resume: "resume_up",
                api.param_slug: "slug_update",
                api.param_status: "in_progress",
                api.param_steps: [{api.param_step_id: "aaaaaaaaaaaaaaaaaaaaaaaa",
                                   api.param_step_description: "step1_up"},
                                  {api.param_step_description: "step1_up"},
                                  {api.param_step_id: "cccccccccccccccccccccccc",
                                   api.param_step_description: "step_new_fake"},
                                  {api.param_step_id: "bbbbbbbbbbbbbbbbbbbbbbbb",
                                   api.param_step_description: "step2_update",
                                   "invalid": "invalid"}],
                api.param_title: "qa_rhr_title_update",
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?invalid=invalid"
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.custom(data=body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(api.response_without_steps(data=response_body["data"]),
                         api.data_expected_without_steps(recipe=tc_recipe))
        api.check_steps(recipe=tc_recipe, response_data=response_body["data"])
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_recipe.check_bdd_data()

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_recipe = RecipeTest().insert()
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
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        self.assertEqual(response_body["detail"], rep.detail_url_not_found)
        """ check """
        tc_recipe.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestPutRecipe())


if __name__ == '__main__':
    unittest.main()

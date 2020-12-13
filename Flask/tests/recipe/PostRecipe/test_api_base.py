import unittest
import requests

import utils
import tests.recipe.PostRecipe.api as api
import tests.recipe.model as recipe_model
import tests.ingredient.model as ingredient_model

server = utils.Server()
api = api.PostRecipe()
recipe = recipe_model.RecipeTest()
ingredient = ingredient_model.IngredientTest()


class PostRecipe(unittest.TestCase):

    def setUp(self):
        """ Clean RecipeTest and FileTest."""
        recipe.clean()
        ingredient.clean()

    def test_api_ok(self):
        """ Default case.

        Return
            201 - Inserted Recipe.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.custom_id_from_body(data=response_body).check_bdd_data()

    def test_api_ok_more_param(self):
        """ Default case with more parameter.

        Return
            201 - Inserted Recipe.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ param """
        body = {"categories": ["categori1", "categori2"],
                "cooking_time": 30,
                "ingredients": [{"_id": tc_ingredient1.get_id(), "quantity": 1, "unit": "qa_rhr_unit1",
                                 "invalid": "invalid"},
                                {"_id": tc_ingredient2.get_id(), "quantity": 2, "unit": "qa_rhr_unit2"}],
                "level": 2,
                "nb_people": 4,
                "note": "note_ex",
                "preparation_time": 8,
                "resume": "resume_ex",
                "slug": "slug",
                "status": "in_progress",
                "steps": ["description_ex1", "description_ex2"],
                "title": "qa_rhr_title",
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        tc_recipe.display()
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        #data_check = api.json_check(data=response_body["data"], data_expected=tc_recipe)
        #self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(False, "schema tbd")
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_recipe.custom_id_from_body(data=response_body).check_bdd_data()

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ param """
        body = {api.param_title: "qa_rhr_title",
                api.param_slug: "slug"}
        """ call api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe = recipe_model.RecipeTest().custom(api.add_default_value(body=body))
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check """
        tc_recipe.check_doesnt_exist_by_title()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostRecipe())


if __name__ == '__main__':
    unittest.main()

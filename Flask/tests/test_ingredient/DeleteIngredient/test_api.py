import unittest
import requests

import utils
import tests.test_ingredient.DeleteIngredient.api as api
import tests.test_ingredient.model as ingredient_model
import tests.test_file_mongo.model as file_mongo_model
import tests.test_recipe.model as recipe_model

server = utils.Server()
api = api.DeleteIngredient()
ingredient = ingredient_model.IngredientTest()
recipe = recipe_model.RecipeTest()
file_mongo = file_mongo_model.FileMongoTest()


class DeleteIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean all IngredientTest, RecipeTest and FileMongoTest. """
        ingredient.clean()
        recipe.clean()
        file_mongo.clean()

    def test_api_ok(self):
        """ Default case.

        Return
            204 - Ingredient Deleted.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], tc_id)
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient1.check_doesnt_exist_by_id()
        tc_ingredient2.check_bdd_data()

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient1.get_id()
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
        tc_ingredient1.check_bdd_data()
        tc_ingredient2.check_bdd_data()

    def test_api_file_mongo_clean(self):
        """ FileMongo associated cleaned.

        Return
            204 - Ingredient Deleted.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_file1 = tc_ingredient1.add_file_mongo(filename="qa_rhr_1", is_main=False)
        tc_file2 = tc_ingredient1.add_file_mongo(filename="qa_rhr_2", is_main=False)
        """ param """
        tc_id = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], tc_id)
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient1.check_doesnt_exist_by_id()
        tc_file1.check_doesnt_exist_by_id()
        tc_file2.check_doesnt_exist_by_id()

    def test_api_link_clean(self):
        """ IngredientRecipe associated cleaned.

        Return
            204 - Ingredient Deleted.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        tc_recipe = recipe_model.RecipeTest()
        tc_recipe.add_ingredient(_id=tc_ingredient1.get_id(), quantity=1, unit="unit")
        tc_recipe.add_ingredient(_id=tc_ingredient2.get_id(), quantity=2, unit="unit_2")
        tc_recipe.insert()
        """ param """
        tc_id = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.delete_ingredient(_id=tc_ingredient1.get_id())
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], tc_id)
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient1.check_doesnt_exist_by_id()
        tc_ingredient2.check_bdd_data()
        tc_recipe.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(DeleteIngredient())


if __name__ == '__main__':
    unittest.main()

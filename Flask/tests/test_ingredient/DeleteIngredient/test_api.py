import unittest
import requests

from tests import server, rep
from tests.test_recipe import RecipeTest
from tests.test_ingredient import IngredientTest
from tests.test_ingredient.DeleteIngredient import api


class TestDeleteIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean all IngredientTest, RecipeTest. """
        IngredientTest().clean()
        RecipeTest().clean()

    def test_api_ok(self):
        """ Default case.

        Return
            200 - Ingredient Deleted.
        """
        """ env """
        tc_ingredient1 = IngredientTest().insert()
        tc_ingredient2 = IngredientTest().insert()
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
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_ingredient1.check_doesnt_exist_by_id()
        tc_ingredient2.check_bdd_data()

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_ingredient1 = IngredientTest().insert()
        tc_ingredient2 = IngredientTest().insert()
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
        self.assertTrue(rep.check_not_present(value="data", response=response_body))
        self.assertEqual(response_body["detail"], rep.detail_url_not_found)
        """ check """
        tc_ingredient1.check_bdd_data()
        tc_ingredient2.check_bdd_data()

    def test_api_link_clean(self):
        """ Ingredient's Recipe associated cleaned.

        Return
            200 - Ingredient Deleted.
        """
        """ env """
        tc_ingredient1 = IngredientTest().insert()
        tc_ingredient2 = IngredientTest().insert()
        tc_recipe = RecipeTest().insert()
        tc_recipe.add_ingredient(ingredient=tc_ingredient1, quantity=1, unit="unit")
        tc_recipe.add_ingredient(ingredient=tc_ingredient2, quantity=2, unit="unit_2")
        """ param """
        tc_id = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ change """
        tc_recipe.delete_ingredient(ingredient=tc_ingredient1)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], tc_id)
        self.assertTrue(rep.check_not_present(value="detail", response=response_body))
        """ check """
        tc_ingredient1.check_doesnt_exist_by_id()
        tc_ingredient2.check_bdd_data()
        tc_recipe.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(TestDeleteIngredient())


if __name__ == '__main__':
    unittest.main()

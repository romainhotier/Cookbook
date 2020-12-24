import unittest
import requests

import utils
import tests.test_ingredient.GetIngredient.api as api
import tests.test_ingredient.model as ingredient_model

server = utils.Server()
api = api.GetIngredient()
ingredient = ingredient_model.IngredientTest()


class GetIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest. """
        ingredient.clean()

    def test_api_ok(self):
        """ Default case.

        Return
            200 - Get one Ingredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient1))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_api_ok_more_param(self):
        """ Default case with more parameter.

        Return
            200 - Get one Ingredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?invalid=invalid"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient1))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient1.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "x/" + tc_id
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"],  "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(GetIngredient())


if __name__ == '__main__':
    unittest.main()

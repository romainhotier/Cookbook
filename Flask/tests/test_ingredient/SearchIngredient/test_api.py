import unittest
import requests

import utils
import tests.test_ingredient.SearchIngredient.api as api
import tests.test_ingredient.model as ingredient_model

server = utils.Server()
api = api.SearchIngredient()
ingredient = ingredient_model.IngredientTest()


class SearchIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest."""
        ingredient.clean()

    def test_api_no_param(self):
        """ Default case.

        Return
            200 - Go to GetIngredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "?"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_api_more_param(self):
        """ Default case with more parameters.

        Return
            200 - Go to GetIngredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"invalid": "invalid"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "?" + "invalid=invalid"
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertIn(api.data_expected(ingredient=tc_ingredient1), response_body["data"])
        self.assertIn(api.data_expected(ingredient=tc_ingredient2), response_body["data"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_api_url_not_found(self):
        """ Wrong url.

        Return
            400 - Go to GetIngredient.
        """
        """ env """
        ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        """ param """
        tc_name = "qa"
        """ call api """
        url = server.main_url + "/" + api.url + "x" + "?" + api.param_name + "=" + tc_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param="_id", msg=server.detail_must_be_an_object_id, value="searchx")
        self.assertEqual(response_body["detail"], detail)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(SearchIngredient())


if __name__ == '__main__':
    unittest.main()

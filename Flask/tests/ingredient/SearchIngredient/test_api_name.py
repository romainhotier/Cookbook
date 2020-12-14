import unittest
import requests

import utils
import tests.ingredient.SearchIngredient.api as api
import tests.ingredient.model as ingredient_model

server = utils.Server()
api = api.SearchIngredient()
ingredient = ingredient_model.IngredientTest()


class SearchIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest."""
        ingredient.clean()

    def test_name_empty(self):
        """ QueryParameter name is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        """ param """
        tc_name = ""
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_name + "=" + tc_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_name, msg=server.detail_must_be_not_empty, value=tc_name)
        self.assertEqual(response_body["detail"], detail)

    def test_name_invalid(self):
        """ QueryParameter name is a string.

        Return
            200 - Get Ingredient.
        """
        """ env """
        ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        """ param """
        tc_name = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_name + "=" + tc_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_name_exact(self):
        """ QueryParameter name is exact.

        Return
            200 - Get Ingredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        """ param """
        tc_name = tc_ingredient1.name
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_name + "=" + tc_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(ingredient=tc_ingredient1)])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_name_partial(self):
        """ QueryParameter name is partial.

        Return
            200 - Get Ingredient.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_a"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_b"}).insert()
        """ param """
        tc_name = "qa_rhr"
        """ call api """
        url = server.main_url + "/" + api.url + "?" + api.param_name + "=" + tc_name
        response = requests.get(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertCountEqual(response_body["data"], [api.data_expected(ingredient=tc_ingredient1),
                                                      api.data_expected(ingredient=tc_ingredient2)])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    @classmethod
    def tearDownClass(cls):
        cls.setUp(SearchIngredient())


if __name__ == '__main__':
    unittest.main()

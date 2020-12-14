import unittest
import requests

import utils
import tests.ingredient.PutIngredient.api as api
import tests.ingredient.model as ingredient_model

server = utils.Server()
api = api.PutIngredient()
ingredient = ingredient_model.IngredientTest()


class PutIngredient(unittest.TestCase):

    def setUp(self):
        """ Clean IngredientTest."""
        ingredient.clean()

    def test_categories_without(self):
        """ BodyParameter categories is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param="body", msg=server.detail_must_contain_at_least_one_key, value=body)
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_bdd_data()

    def test_categories_none(self):
        """ BodyParameter categories is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_categories: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_categories, msg=server.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_bdd_data()

    def test_categories_empty(self):
        """ BodyParameter categories is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_categories: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_categories, msg=server.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_bdd_data()

    def test_categories_string(self):
        """ BodyParameter categories is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_categories: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_categories, msg=server.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_bdd_data()

    def test_categories_tab(self):
        """ BodyParameter categories is a empty tab.

        Return
            200 - Updated Ingredient.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().custom({"categories": ["qa_rhr_category"]}).insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_categories: []}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient.check_bdd_data()

    def test_categories_tab_2(self):
        """ BodyParameter categories is a tab.

        Return
            200 - Updated Ingredient.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().custom({"categories": ["qa_rhr_category"]}).insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_categories: [None, "", "invalid"]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PutIngredient())


if __name__ == '__main__':
    unittest.main()

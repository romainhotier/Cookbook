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

    def test_name_without(self):
        """ BodyParameter name is missing.

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

    def test_name_none(self):
        """ BodyParameter name is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_name: None}
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
        detail = api.create_detail(param=api.param_name, msg=server.detail_must_be_a_string, value=body[api.param_name])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_bdd_data()

    def test_name_empty(self):
        """ BodyParameter name is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_name: ""}
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
        detail = api.create_detail(param=api.param_name, msg=server.detail_must_be_not_empty, 
                                   value=body[api.param_name])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient.check_bdd_data()

    def test_name_string(self):
        """ BodyParameter name is a string.

        Return
            200 - Updated Ingredient.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_name: "qa_rhr_name_update"}
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
        
    def test_name_already_exist(self):
        """ BodyParameter name already exist.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_name1"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_name2"}).insert()
        """ param """        
        tc_id = tc_ingredient1.get_id()
        body = {api.param_name: tc_ingredient2.name}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        detail = api.create_detail(param=api.param_name, msg=server.detail_already_exist, value=body[api.param_name])
        self.assertEqual(response_body["detail"], detail)
        """ check """
        tc_ingredient1.check_bdd_data()
        tc_ingredient2.check_bdd_data()

    def test_name_already_exist_coherent(self):
        """ BodyParameter name already exist but it's coherent.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient1 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_name1"}).insert()
        tc_ingredient2 = ingredient_model.IngredientTest().custom({"name": "qa_rhr_name2"}).insert()
        """ param """
        tc_id = tc_ingredient1.get_id()
        body = {api.param_name: tc_ingredient1.name}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_ingredient1.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient1))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ check """
        tc_ingredient1.check_bdd_data()
        tc_ingredient2.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PutIngredient())


if __name__ == '__main__':
    unittest.main()

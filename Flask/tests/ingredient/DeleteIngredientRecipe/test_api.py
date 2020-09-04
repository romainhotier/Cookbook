import unittest
import requests

import utils
import tests.ingredient.DeleteIngredientRecipe.api as api
import tests.ingredient.model as ingredient_model

server = utils.Server
api = api.DeleteIngredientRecipe()
link = ingredient_model.IngredientRecipeTest()


class DeleteIngredientRecipe(unittest.TestCase):

    def setUp(self):
        link.clean()

    def test_0_api_ok(self):
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        tc_id = tc_link.get_id()
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        """ assert """
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response.text, '')
        tc_link.select_nok()

    def test_1_url_not_found(self):
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        tc_id = tc_link.get_id()
        """ call api """
        url = server.main_url + "/x" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_no_data(rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        tc_link.select_ok()

    def test_2_id_without(self):
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        """ call api """
        url = server.main_url + "/" + api.url + "/"
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_no_data(rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        tc_link.select_ok()

    def test_2_id_string(self):
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        tc_id = "invalid"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_no_data(rep=response_body))
        detail = api.create_detail(param=api.param_id, msg=server.detail_must_be_an_object_id, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        tc_link.select_ok()

    def test_2_id_object_id_invalid(self):
        tc_link = ingredient_model.IngredientRecipeTest().insert()
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.delete(url, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_no_data(rep=response_body))
        detail = api.create_detail(param=api.param_id, msg=server.detail_doesnot_exist, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        tc_link.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(DeleteIngredientRecipe())


if __name__ == '__main__':
    unittest.main()

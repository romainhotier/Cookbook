import unittest
import requests

import utils
import tests.ingredient.PostIngredient.api as api
import tests.ingredient.model as ingredient_model
import tests.file.model as file_model

server = utils.Server
api = api.PostIngredient()
ingredient = ingredient_model.IngredientTest()
file = file_model.FileTest()


class PostIngredient(unittest.TestCase):

    def setUp(self):
        ingredient.clean()

    def test_0_api_ok(self):
        body = {api.param_name: "qa_rhr_name"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_0_api_ok_more_param(self):
        body = {api.param_name: "qa_rhr_name",
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_1_url_not_found(self):
        body = {api.param_name: "qa_rhr_name"}
        """ call api """
        url = server.main_url + "/" + api.url + "x"
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        tc_ingredient.select_nok_by_name()

    def test_2_name_without(self):
        body = {}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_name, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_2_name_none(self):
        body = {api.param_name: None}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_name, msg=server.detail_must_be_a_string, value=body[api.param_name])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_2_name_empty(self):
        body = {api.param_name: ""}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_name, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_name])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_nok_by_name()

    def test_2_name_string(self):
        body = {api.param_name: "qa_rhr_name"}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_ingredient = ingredient_model.IngredientTest().custom(body)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        data_check = api.json_check(data=response_body["data"], data_expected=tc_ingredient)
        self.assertTrue(data_check["result"], data_check["error"])
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        """ refacto """
        tc_ingredient.custom({"_id": response_body["data"]["_id"]}).select_ok()

    def test_3_name_already_exist(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        body = {api.param_name: tc_ingredient.name}
        """ call api """
        url = server.main_url + "/" + api.url
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_name, msg=server.detail_already_exist, value=body[api.param_name])
        self.assertEqual(response_body["detail"], detail)
        tc_ingredient.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostIngredient())


if __name__ == '__main__':
    unittest.main()

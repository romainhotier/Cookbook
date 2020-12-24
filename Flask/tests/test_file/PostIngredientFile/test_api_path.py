import unittest
import requests

import utils
import tests.test_file.PostIngredientFile.api as api
import tests.test_ingredient.model as ingredient_model
import tests.test_file.model as file_model

server = utils.Server()
api = api.PostIngredientFile()
ingredient = ingredient_model.IngredientTest()
file = file_model.FileTest()

file_path = api.get_file_path_for_test()


class PostIngredientFile(unittest.TestCase):

    def setUp(self):
        """ Clean all FileTest and IngredientTest """
        file.clean()
        ingredient.clean()

    def test_path_without(self):
        """ BodyParameter path is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_path, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_path_null(self):
        """ BodyParameter path is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: None,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_path, msg=server.detail_must_be_a_string, value=body[api.param_path])
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_path_empty(self):
        """ BodyParameter path is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: "",
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_path, msg=server.detail_must_be_not_empty, 
                                   value=body[api.param_path])
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_path_string(self):
        """ BodyParameter path is an nok string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: "invalid",
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_path, msg=server.detail_doesnot_exist, value=body[api.param_path])
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()


if __name__ == '__main__':
    unittest.main()

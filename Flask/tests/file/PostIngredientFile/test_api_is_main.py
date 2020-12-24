import unittest
import requests

import utils
import tests.file.PostIngredientFile.api as api
import tests.ingredient.model as ingredient_model
import tests.file.model as file_model

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

    def test_is_main_without(self):
        """ BodyParameter is_main is missing.

        Return
            201 - IngredientTest and FileTests.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        new_id = api.return_new_file_id(response_body)
        tc_file = tc_ingredient.add_file(filename=body[api.param_filename], is_main=False)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(new_id=new_id))
        """ check file """
        tc_file.check_bdd_data()

    def test_is_main_null(self):
        """ BodyParameter is_main is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: None}
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
        detail = api.create_detail(param=api.param_is_main, msg=server.detail_must_be_a_boolean, 
                                   value=body[api.param_is_main])
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_is_main_empty(self):
        """ BodyParameter is_main is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: ""}
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
        detail = api.create_detail(param=api.param_is_main, msg=server.detail_must_be_a_boolean, 
                                   value=body[api.param_is_main])
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_is_main_string(self):
        """ BodyParameter is_main is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: "invalid"}
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
        detail = api.create_detail(param=api.param_is_main, msg=server.detail_must_be_a_boolean, 
                                   value=body[api.param_is_main])
        self.assertEqual(response_body["detail"], detail)
        """ check file """
        file_model.FileTest().custom_id_from_body(data=body).check_doesnt_exist_by_filename()

    def test_is_main_false(self):
        """ BodyParameter is_main is False.

        Return
            201 - IngredientTest and FileTests.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        new_id = api.return_new_file_id(response_body)
        tc_file = tc_ingredient.add_file(filename=body[api.param_filename], is_main=body[api.param_is_main])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(new_id=new_id))
        """ check file """
        tc_file.check_bdd_data()

    def test_is_main_true(self):
        """ BodyParameter is_main is True.

        Return
            201 - IngredientTest and FileTests.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: True}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        new_id = api.return_new_file_id(response_body)
        tc_file = tc_ingredient.add_file(filename=body[api.param_filename], is_main=body[api.param_is_main])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(new_id=new_id))
        """ check file """
        tc_file.check_bdd_data()

    def test_is_main_true_already_exist(self):
        """ BodyParameter is_main is True and another True exist.

        Return
            201 - IngredientTest and FileTests.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_file1 = tc_ingredient.add_file(filename="qa_rhr_filename", is_main=True)
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename_new",
                api.param_is_main: True}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        tc_file1.custom_is_main(False)
        new_id = api.return_new_file_id(response_body)
        tc_file2 = tc_ingredient.add_file(filename=body[api.param_filename], is_main=body[api.param_is_main])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(new_id=new_id))
        """ check file """
        tc_file2.check_bdd_data()
        tc_file1.check_bdd_data()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostIngredientFile())


if __name__ == '__main__':
    unittest.main()

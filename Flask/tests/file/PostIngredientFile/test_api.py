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

    def test_0_api_ok(self):
        """ Default case

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
        tc_file = tc_ingredient.add_file(filename=body[api.param_filename], is_main=body[api.param_is_main],
                                         identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient, files=[tc_file]))
        self.assertEqual(response_body["detail"], api.detail_expected(new_id=new_id))
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        tc_file.select_ok()

    def test_0_api_ok_more_param(self):
        """ Default case with more parameter.

        Return
            201 - IngredientTest and FileTests.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False,
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ change """
        new_id = api.return_new_file_id(response_body)
        tc_file = tc_ingredient.add_file(filename=body[api.param_filename], is_main=body[api.param_is_main],
                                         identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient, files=[tc_file]))
        self.assertEqual(response_body["detail"], api.detail_expected(new_id=new_id))
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        tc_file.select_ok()

    def test_1_url_not_found(self):
        """ Wrong url.

        Return
            404 - Url not found.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url + "x/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_2_id_without(self):
        """ QueryParameter _id missing.

        Return
            404 - Url not found.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = ""
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_2_id_string(self):
        """ QueryParameter _id is a string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = "invalid"
        body = {api.param_path: file_path,
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
        detail = api.create_detail(param=api.param_id, msg=server.detail_must_be_an_object_id, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_2_id_object_id_invalid(self):
        """ QueryParameter _id is a nok ObjectId.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        body = {api.param_path: file_path,
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
        detail = api.create_detail(param=api.param_id, msg=server.detail_doesnot_exist, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_3_path_without(self):
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
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_3_path_null(self):
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
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_3_path_empty(self):
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
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_3_path_string(self):
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
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_4_filename_without(self):
        """ BodyParameter filename is missing.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
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
        detail = api.create_detail(param=api.param_filename, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        """ check ingredient """
        tc_ingredient.select_ok()

    def test_4_filename_null(self):
        """ BodyParameter filename is null.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: None,
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
        detail = api.create_detail(param=api.param_filename, msg=server.detail_must_be_a_string, 
                                   value=body[api.param_filename])
        self.assertEqual(response_body["detail"], detail)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_4_filename_empty(self):
        """ BodyParameter filename is an empty string.

        Return
            400 - Bad request.
        """
        """ env """
        tc_ingredient = ingredient_model.IngredientTest().insert()
        """ param """
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "",
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
        detail = api.create_detail(param=api.param_filename, msg=server.detail_must_be_not_empty, 
                                   value=body[api.param_filename])
        self.assertEqual(response_body["detail"], detail)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_4_filename_string(self):
        """ BodyParameter filename is a string.

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
        tc_file = tc_ingredient.add_file(filename=body[api.param_filename], is_main=body[api.param_is_main],
                                         identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient, files=[tc_file]))
        self.assertEqual(response_body["detail"], api.detail_expected(new_id=new_id))
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        tc_file.select_ok()

    def test_5_is_main_without(self):
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
        tc_file = tc_ingredient.add_file(filename=body[api.param_filename], is_main=False, identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient, files=[tc_file]))
        self.assertEqual(response_body["detail"], api.detail_expected(new_id=new_id))
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        tc_file.select_ok()

    def test_5_is_main_null(self):
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
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_5_is_main_empty(self):
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
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_5_is_main_string(self):
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
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_5_is_main_false(self):
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
        tc_file = tc_ingredient.add_file(filename=body[api.param_filename], is_main=body[api.param_is_main],
                                         identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient, files=[tc_file]))
        self.assertEqual(response_body["detail"], api.detail_expected(new_id=new_id))
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        tc_file.select_ok()

    def test_5_is_main_true(self):
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
        tc_file = tc_ingredient.add_file(filename=body[api.param_filename], is_main=body[api.param_is_main],
                                         identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient, files=[tc_file]))
        self.assertEqual(response_body["detail"], api.detail_expected(new_id=new_id))
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        tc_file.select_ok()

    def test_5_is_main_true_already_exist(self):
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
        tc_file2 = tc_ingredient.add_file(filename=body[api.param_filename], is_main=body[api.param_is_main],
                                          identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(ingredient=tc_ingredient, files=[tc_file1,
                                                                                                   tc_file2]))
        self.assertEqual(response_body["detail"], api.detail_expected(new_id=new_id))
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        tc_file2.select_ok()
        tc_file1.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostIngredientFile())


if __name__ == '__main__':
    unittest.main()

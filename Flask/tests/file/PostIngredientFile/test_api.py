import unittest
import requests

import utils
import tests.file.PostIngredientFile.api as api
import tests.ingredient.model as ingredient_model
import tests.file.model as file_model

server = utils.Server
api = api.PostIngredientFile()
ingredient = ingredient_model.IngredientTest()
file = file_model.FileTest()

file_path = api.get_file_path_for_test()


class PostIngredientFile(unittest.TestCase):

    def setUp(self):
        ingredient.clean()
        file.clean()

    def test_0_api_ok(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_file = tc_ingredient.add_file(filename=body[api.param_filename], is_main=body[api.param_is_main])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        format_data = api.format_response(data=response_body[api.rep_data], position=0)
        format_response = api.refacto_file_added(data=tc_ingredient.get_stringify_with_file(files=[tc_file]),
                                                 position=0)
        self.assertEqual(format_data, format_response)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        tc_file.custom({"_id": api.return_new_file_id(response_body)})
        tc_file.select_ok()

    def test_0_api_ok_more_param(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False,
                "invalid": "invalid"
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_file = tc_ingredient.add_file(filename=body[api.param_filename], is_main=body[api.param_is_main])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        format_data = api.format_response(data=response_body[api.rep_data], position=0)
        format_response = api.refacto_file_added(data=tc_ingredient.get_stringify_with_file(files=[tc_file]),
                                                 position=0)
        self.assertEqual(format_data, format_response)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        tc_file.custom({"_id": api.return_new_file_id(response_body)})
        tc_file.select_ok()

    def test_1_url_not_found(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "x/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_2_id_without(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = ""
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_2_id_string(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = "invalid"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id, server.detail_must_be_an_object_id, tc_id)
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_2_id_object_id_invalid(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id, server.detail_doesnot_exist, tc_id)
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_3_path_without(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_path, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_3_path_null(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: None,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_path, server.detail_must_be_a_string, body[api.param_path])
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_3_path_empty(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: "",
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_path, server.detail_must_be_not_empty, body[api.param_path])
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_3_path_string(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: "invalid",
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_path, server.detail_doesnot_exist, body[api.param_path])
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_4_filename_without(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_filename, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check ingredient """
        tc_ingredient.select_ok()

    def test_4_filename_null(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: None,
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_filename, server.detail_must_be_a_string, body[api.param_filename])
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_4_filename_empty(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_filename, server.detail_must_be_not_empty, body[api.param_filename])
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_4_filename_string(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_file = tc_ingredient.add_file(filename=body[api.param_filename], is_main=body[api.param_is_main])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        format_data = api.format_response(data=response_body[api.rep_data], position=0)
        format_response = api.refacto_file_added(data=tc_ingredient.get_stringify_with_file(files=[tc_file]),
                                                 position=0)
        self.assertEqual(format_data, format_response)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        tc_file.custom({"_id": api.return_new_file_id(response_body)})
        tc_file.select_ok()

    def test_5_is_main_without(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename"
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_file = tc_ingredient.add_file(filename=body[api.param_filename], is_main=False)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        format_data = api.format_response(data=response_body[api.rep_data], position=0)
        format_response = api.refacto_file_added(data=tc_ingredient.get_stringify_with_file(files=[tc_file]),
                                                 position=0)
        self.assertEqual(format_data, format_response)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        tc_file.custom({"_id": api.return_new_file_id(response_body)})
        tc_file.select_ok()

    def test_5_is_main_null(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: None
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_is_main, server.detail_must_be_a_boolean, body[api.param_is_main])
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_5_is_main_empty(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: ""
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_is_main, server.detail_must_be_a_boolean, body[api.param_is_main])
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_5_is_main_string(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: "invalid"
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_is_main, server.detail_must_be_a_boolean, body[api.param_is_main])
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_5_is_main_false(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_file = tc_ingredient.add_file(filename=body[api.param_filename], is_main=body[api.param_is_main])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        format_data = api.format_response(data=response_body[api.rep_data], position=0)
        format_response = api.refacto_file_added(data=tc_ingredient.get_stringify_with_file(files=[tc_file]),
                                                 position=0)
        self.assertEqual(format_data, format_response)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        tc_file.custom({"_id": api.return_new_file_id(response_body)})
        tc_file.select_ok()

    def test_5_is_main_true(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: True
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_file = tc_ingredient.add_file(filename=body[api.param_filename], is_main=body[api.param_is_main])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        format_data = api.format_response(data=response_body[api.rep_data], position=0)
        format_response = api.refacto_file_added(data=tc_ingredient.get_stringify_with_file(files=[tc_file]),
                                                 position=0)
        self.assertEqual(format_data, format_response)
        """ check ingredient """
        tc_ingredient.select_ok()
        """ check file """
        tc_file.custom({"_id": api.return_new_file_id(response_body)})
        tc_file.select_ok()

    def test_5_is_main_true_already_exist(self):
        tc_ingredient = ingredient_model.IngredientTest().insert()
        tc_file1 = tc_ingredient.add_file(filename="qa_rhr_filename", is_main=True)
        tc_id = tc_ingredient.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename_new",
                api.param_is_main: True
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_file1.custom_is_main(False)
        tc_file2 = tc_ingredient.add_file(filename=body[api.param_filename], is_main=body[api.param_is_main])
        tc_file2.custom({"_id": api.return_new_file_id(response_body)})
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        format_data = api.format_response(data=response_body[api.rep_data], position=1)
        format_response = api.refacto_file_added(data=tc_ingredient.get_stringify_with_file(files=[tc_file1, tc_file2]),
                                                 position=1)
        self.assertEqual(format_data, format_response)
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

import unittest
import requests

import utils
import tests.file.PostStepFile.api as api
import tests.recipe.model as recipe_model
import tests.file.model as file_model

server = utils.Server
api = api.PostStepFile()
recipe = recipe_model.RecipeTest()
file = file_model.FileTest()

file_path = api.get_file_path_for_test()


class PostStepFile(unittest.TestCase):

    def setUp(self):
        recipe.clean()
        file.clean()

    def test_0_api_ok(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_file = tc_recipe.add_file_step(_id_step="111111111111111111111111",
                                          filename=body[api.param_filename],
                                          is_main=body[api.param_is_main])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        format_data = api.format_response(data=response_body[api.rep_data], step_index=0, file_index=0)
        format_response = api.\
            refacto_file_added(data=tc_recipe.
                               get_stringify_with_file(files_recipe=[],
                                                       files_steps={"111111111111111111111111": [tc_file], 
                                                                    "222222222222222222222222": []}),
                               step_index=0, file_index=0)
        self.assertEqual(format_data, format_response)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        tc_file.custom({"_id": api.return_new_file_id(response_body)})
        tc_file.select_ok()

    def test_0_api_ok_more_param(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False,
                "invalid": "invalid"
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_file = tc_recipe.add_file_step(_id_step="111111111111111111111111",
                                          filename=body[api.param_filename],
                                          is_main=body[api.param_is_main])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        format_data = api.format_response(data=response_body[api.rep_data], step_index=0, file_index=0)
        format_response = api.\
            refacto_file_added(data=tc_recipe.
                               get_stringify_with_file(files_recipe=[],
                                                       files_steps={"111111111111111111111111": [tc_file],
                                                                    "222222222222222222222222": []}),
                               step_index=0, file_index=0)
        self.assertEqual(format_data, format_response)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        tc_file.custom({"_id": api.return_new_file_id(response_body)})
        tc_file.select_ok()

    def test_1_url_not_found_1(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "x/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_1_url_not_found_2(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/x" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_2_id_recipe_without(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = ""
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_2_id_recipe_string(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = "invalid"
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_recipe, server.detail_must_be_an_object_id, tc_id_recipe)
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_2_id_recipe_object_id_invalid(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = "aaaaaaaaaaaaaaaaaaaaaaaa"
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_recipe, server.detail_doesnot_exist, tc_id_recipe)
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_3_id_step_without(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = ""
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_3_id_step_string(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "invalid"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_step, server.detail_must_be_an_object_id, tc_id_step)
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_3_id_step_object_id_invalid(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "aaaaaaaaaaaaaaaaaaaaaaaa"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_step, server.detail_doesnot_exist, tc_id_step)
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_4_path_without(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_path, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_4_path_null(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: None,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_path, server.detail_must_be_a_string, body[api.param_path])
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_4_path_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: "",
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_path, server.detail_must_be_not_empty, body[api.param_path])
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_4_path_string(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: "invalid",
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_path, server.detail_doesnot_exist, body[api.param_path])
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_5_filename_without(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_filename, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check recipe """
        tc_recipe.select_ok()

    def test_5_filename_null(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: None,
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_filename, server.detail_must_be_a_string, body[api.param_filename])
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_5_filename_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_filename, server.detail_must_be_not_empty, body[api.param_filename])
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_5_filename_string(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_file = tc_recipe.add_file_step(_id_step="111111111111111111111111",
                                          filename=body[api.param_filename],
                                          is_main=body[api.param_is_main])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        format_data = api.format_response(data=response_body[api.rep_data], step_index=0, file_index=0)
        format_response = api.\
            refacto_file_added(data=tc_recipe.
                               get_stringify_with_file(files_recipe=[],
                                                       files_steps={"111111111111111111111111": [tc_file],
                                                                    "222222222222222222222222": []}),
                               step_index=0, file_index=0)
        self.assertEqual(format_data, format_response)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        tc_file.custom({"_id": api.return_new_file_id(response_body)})
        tc_file.select_ok()

    def test_6_is_main_without(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_file = tc_recipe.add_file_step(_id_step="111111111111111111111111",
                                          filename=body[api.param_filename],
                                          is_main=False)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        format_data = api.format_response(data=response_body[api.rep_data], step_index=0, file_index=0)
        format_response = api.\
            refacto_file_added(data=tc_recipe.
                               get_stringify_with_file(files_recipe=[],
                                                       files_steps={"111111111111111111111111": [tc_file],
                                                                    "222222222222222222222222": []}),
                               step_index=0, file_index=0)
        self.assertEqual(format_data, format_response)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        tc_file.custom({"_id": api.return_new_file_id(response_body)})
        tc_file.select_ok()

    def test_6_is_main_null(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: None
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_is_main, server.detail_must_be_a_boolean, body[api.param_is_main])
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_6_is_main_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: ""
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_is_main, server.detail_must_be_a_boolean, body[api.param_is_main])
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_6_is_main_string(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: "invalid"
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_is_main, server.detail_must_be_a_boolean, body[api.param_is_main])
        self.assertEqual(response_body[api.rep_detail], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_6_is_main_false(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_file = tc_recipe.add_file_step(_id_step="111111111111111111111111",
                                          filename=body[api.param_filename],
                                          is_main=body[api.param_is_main])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        format_data = api.format_response(data=response_body[api.rep_data], step_index=0, file_index=0)
        format_response = api.\
            refacto_file_added(data=tc_recipe.
                               get_stringify_with_file(files_recipe=[],
                                                       files_steps={"111111111111111111111111": [tc_file],
                                                                    "222222222222222222222222": []}),
                               step_index=0, file_index=0)
        self.assertEqual(format_data, format_response)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        tc_file.custom({"_id": api.return_new_file_id(response_body)})
        tc_file.select_ok()

    def test_6_is_main_true(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: True
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_file = tc_recipe.add_file_step(_id_step="111111111111111111111111",
                                          filename=body[api.param_filename],
                                          is_main=body[api.param_is_main])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        format_data = api.format_response(data=response_body[api.rep_data], step_index=0, file_index=0)
        format_response = api.\
            refacto_file_added(data=tc_recipe.
                               get_stringify_with_file(files_recipe=[],
                                                       files_steps={"111111111111111111111111": [tc_file],
                                                                    "222222222222222222222222": []}),
                               step_index=0, file_index=0)
        self.assertEqual(format_data, format_response)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        tc_file.custom({"_id": api.return_new_file_id(response_body)})
        tc_file.select_ok()

    def test_6_is_main_true_already_exist(self):
        tc_recipe = recipe_model.RecipeTest().custom({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step a")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step b")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename_new",
                api.param_is_main: True
                }
        tc_file1 = tc_recipe.add_file_step(_id_step="111111111111111111111111",
                                           filename=body[api.param_filename],
                                           is_main=True)
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_file1.custom_is_main(False)
        tc_file2 = tc_recipe.add_file_step(_id_step="111111111111111111111111",
                                           filename=body[api.param_filename],
                                           is_main=body[api.param_is_main])
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        format_data = api.format_response(data=response_body[api.rep_data], step_index=0, file_index=1)
        format_response = api.\
            refacto_file_added(data=tc_recipe.
                               get_stringify_with_file(files_recipe=[],
                                                       files_steps={"111111111111111111111111": [tc_file1, tc_file2],
                                                                    "222222222222222222222222": []}),
                               step_index=0, file_index=1)
        self.assertEqual(format_data, format_response)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        tc_file2.custom({"_id": api.return_new_file_id(response_body)})
        tc_file2.select_ok()
        tc_file1.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostStepFile())


if __name__ == '__main__':
    unittest.main()

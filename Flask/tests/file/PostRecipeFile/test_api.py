import unittest
import requests

import utils
import tests.file.PostRecipeFile.api as api
import tests.recipe.model as recipe_model
import tests.file.model as file_model

server = utils.Server
api = api.PostRecipeFile()
recipe = recipe_model.RecipeTest()
file = file_model.FileTest()

file_path = api.get_file_path_for_test()


class PostRecipeFile(unittest.TestCase):

    def setUp(self):
        recipe.clean()
        file.clean()

    def test_0_api_ok(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        new_id = api.return_new_file_id(response_body)
        tc_file = tc_recipe.add_file_recipe(filename=body[api.param_filename], is_main=body[api.param_is_main],
                                            identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe, files=[tc_file]))
        self.assertEqual(response_body["detail"], api.detail_expected(new_id=new_id))
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        tc_file.select_ok()

    def test_0_api_ok_more_param(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False,
                "invalid": "invalid"
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        new_id = api.return_new_file_id(response_body)
        tc_file = tc_recipe.add_file_recipe(filename=body[api.param_filename], is_main=body[api.param_is_main],
                                            identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe, files=[tc_file]))
        self.assertEqual(response_body["detail"], api.detail_expected(new_id=new_id))
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        tc_file.select_ok()

    def test_1_url_not_found(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False,
                "invalid": "invalid"
                }
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
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_2_id_without(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_2_id_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id, msg=server.detail_must_be_an_object_id, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_2_id_object_id_invalid(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id, msg=server.detail_doesnot_exist, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_3_path_without(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
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
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_3_path_null(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
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
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_path, msg=server.detail_must_be_a_string, value=body[api.param_path])
        self.assertEqual(response_body["detail"], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_3_path_empty(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
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
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_path, msg=server.detail_must_be_not_empty, 
                                   value=body[api.param_path])
        self.assertEqual(response_body["detail"], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_3_path_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
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
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_path, msg=server.detail_doesnot_exist, value=body[api.param_path])
        self.assertEqual(response_body["detail"], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_4_filename_without(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_is_main: False
                }
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
        """ check recipe """
        tc_recipe.select_ok()

    def test_4_filename_null(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
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
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_filename, msg=server.detail_must_be_a_string, 
                                   value=body[api.param_filename])
        self.assertEqual(response_body["detail"], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_4_filename_empty(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
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
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_filename, msg=server.detail_must_be_not_empty, 
                                   value=body[api.param_filename])
        self.assertEqual(response_body["detail"], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_4_filename_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        new_id = api.return_new_file_id(response_body)
        tc_file = tc_recipe.add_file_recipe(filename=body[api.param_filename], is_main=body[api.param_is_main],
                                            identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe, files=[tc_file]))
        self.assertEqual(response_body["detail"], api.detail_expected(new_id=new_id))
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        tc_file.select_ok()

    def test_5_is_main_without(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename"
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        new_id = api.return_new_file_id(response_body)
        tc_file = tc_recipe.add_file_recipe(filename=body[api.param_filename], is_main=False, identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe, files=[tc_file]))
        self.assertEqual(response_body["detail"], api.detail_expected(new_id=new_id))
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        tc_file.select_ok()

    def test_5_is_main_null(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
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
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_is_main, msg=server.detail_must_be_a_boolean,
                                   value=body[api.param_is_main])
        self.assertEqual(response_body["detail"], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_5_is_main_empty(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
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
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_is_main, msg=server.detail_must_be_a_boolean,
                                   value=body[api.param_is_main])
        self.assertEqual(response_body["detail"], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_5_is_main_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
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
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_is_main, msg=server.detail_must_be_a_boolean,
                                   value=body[api.param_is_main])
        self.assertEqual(response_body["detail"], detail)
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        file_model.FileTest().custom({"filename": body[api.param_filename]}).select_nok_by_filename()

    def test_5_is_main_false(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: False
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        new_id = api.return_new_file_id(response_body)
        tc_file = tc_recipe.add_file_recipe(filename=body[api.param_filename], is_main=body[api.param_is_main],
                                            identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe, files=[tc_file]))
        self.assertEqual(response_body["detail"], api.detail_expected(new_id=new_id))
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        tc_file.select_ok()

    def test_5_is_main_true(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename",
                api.param_is_main: True
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        new_id = api.return_new_file_id(response_body)
        tc_file = tc_recipe.add_file_recipe(filename=body[api.param_filename], is_main=body[api.param_is_main],
                                            identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe, files=[tc_file]))
        self.assertEqual(response_body["detail"], api.detail_expected(new_id=new_id))
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        tc_file.select_ok()

    def test_5_is_main_true_already_exist(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_file1 = tc_recipe.add_file_recipe(filename="qa_rhr_filename", is_main=True)
        tc_id = tc_recipe.get_id()
        body = {api.param_path: file_path,
                api.param_filename: "qa_rhr_filename_new",
                api.param_is_main: True}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_file1.custom_is_main(False)
        new_id = api.return_new_file_id(response_body)
        tc_file2 = tc_recipe.add_file_recipe(filename=body[api.param_filename], is_main=body[api.param_is_main],
                                             identifier=new_id)
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe, files=[tc_file1, tc_file2]))
        self.assertEqual(response_body["detail"], api.detail_expected(new_id=new_id))
        """ check recipe """
        tc_recipe.select_ok()
        """ check file """
        tc_file2.custom({"_id": api.return_new_file_id(response_body)})
        tc_file2.select_ok()
        tc_file1.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostRecipeFile())


if __name__ == '__main__':
    unittest.main()

import unittest
import requests

from server import factory as factory
import app.recipe.recipe.model as recipe_model
import app.file.file.model as file_model
import app.recipe.steps.test.PutRecipeStep.api as api

server = factory.Server()
api = api.PutRecipeStep()
recipe = recipe_model.RecipeTest()
file = file_model.FileTest()


class PutRecipeStep(unittest.TestCase):

    def setUp(self):
        recipe.clean()
        file.clean()

    def test_0_api_ok(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom_step(position=0, data=body[api.param_step])
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_recipe.get_data_stringify_object_id())
        tc_recipe.select_ok()

    def test_0_api_ok_more_param(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_step: "update",
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step \
            + "?invalid=invalid"
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom_step(position=0, data=body[api.param_step])
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_recipe.get_data_stringify_object_id())
        tc_recipe.select_ok()

    def test_1_url_not_found_1(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "x/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_recipe.select_ok()

    def test_1_url_not_found_2(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/x" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_recipe.select_ok()

    def test_2_id_recipe_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = ""
        tc_id_step = "111111111111111111111111"
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_recipe.select_ok()

    def test_2_id_recipe_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = "invalid"
        tc_id_step = "111111111111111111111111"
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_recipe, server.detail_must_be_an_object_id, tc_id_recipe)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_2_id_recipe_object_id_invalid(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = "aaaaaaaaaaaaaaaaaaaaaaaa"
        tc_id_step = "111111111111111111111111"
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_recipe, server.detail_doesnot_exist, tc_id_recipe)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_3_id_step_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = ""
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_recipe.select_ok()

    def test_3_id_step_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "invalid"
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_step, server.detail_must_be_an_object_id, tc_id_step)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_3_id_step_object_id_invalid(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "aaaaaaaaaaaaaaaaaaaaaaaa"
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id_step, server.detail_doesnot_exist, tc_id_step)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_step_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_step, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_step_null(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_step: None}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_step, server.detail_must_be_a_string, body[api.param_step])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_step_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_step: ""}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_step, server.detail_must_be_not_empty, body[api.param_step])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_step_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom_step(position=0, data=body[api.param_step])
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_recipe.get_data_stringify_object_id())
        tc_recipe.select_ok()

    def test_5_with_files_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom_step(position=0, data=body[api.param_step])
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_recipe.get_data_stringify_object_id())
        tc_recipe.select_ok()

    def test_5_with_files_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        tc_with_files = ""
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step + "?"\
            + api.param_with_files + "=" + tc_with_files
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom_step(position=0, data=body[api.param_step])
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_with_files, server.detail_must_be_in + " [true, false]", tc_with_files)
        self.assertEqual(response_body[api.rep_detail], detail)

    def test_5_with_files_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        tc_with_files = "invalid"
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step + "?"\
            + api.param_with_files + "=" + tc_with_files
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom_step(position=0, data=body[api.param_step])
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_with_files, server.detail_must_be_in + " [true, false]", tc_with_files)
        self.assertEqual(response_body[api.rep_detail], detail)

    def test_5_with_files_string_false(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_recipe.add_file_recipe(filename="qa_rhr_1", is_main=True)
        tc_recipe.add_file_recipe(filename="qa_rhr_2", is_main=False)
        tc_recipe.add_file_step(_id_step="111111111111111111111111", filename="qa_rhr_11", is_main=False)
        tc_recipe.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_21", is_main=False)
        tc_recipe.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_22", is_main=True)
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        tc_with_files = "false"
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step + "?" \
            + api.param_with_files + "=" + tc_with_files
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom_step(position=0, data=body[api.param_step])
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_recipe.get_data_stringify_object_id())
        tc_recipe.select_ok()

    def test_5_with_files_string_true(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_file_recipe11 = tc_recipe.add_file_recipe(filename="qa_rhr_1", is_main=True)
        tc_file_recipe12 = tc_recipe.add_file_recipe(filename="qa_rhr_2", is_main=False)
        tc_file_step111 = tc_recipe.add_file_step(_id_step="111111111111111111111111", filename="qa_rhr_11",
                                                  is_main=False)
        tc_file_step121 = tc_recipe.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_21",
                                                  is_main=False)
        tc_file_step122 = tc_recipe.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_22",
                                                  is_main=True)
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        tc_with_files = "true"
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step + "?" \
            + api.param_with_files + "=" + tc_with_files
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom_step(position=0, data=body[api.param_step])
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        r1 = tc_recipe.get_data_with_file(files_recipe=[tc_file_recipe11, tc_file_recipe12],
                                          files_steps={"111111111111111111111111": [tc_file_step111],
                                                       "222222222222222222222222": [tc_file_step121, tc_file_step122]})
        self.assertEqual(response_body[api.rep_data], r1)

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PutRecipeStep())


if __name__ == '__main__':
    unittest.main()

import unittest
import requests

from server import factory as factory
import app.recipe.recipe.model as recipe_model
import app.file.file.model as file_model
import app.recipe.recipe.test.PutRecipe.api as api

server = factory.Server()
api = api.PutRecipe()
recipe = recipe_model.RecipeTest()
file = file_model.FileTest()


class PutRecipe(unittest.TestCase):

    def setUp(self):
        recipe.clean()
        file.clean()

    def test_0_api_ok(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).custom({"resume": "invalid"}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_0_api_ok_more_param(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?invalid=invalid"
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_1_url_not_found(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "x" + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_recipe.select_ok()

    def test_2_id_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/"
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_recipe.select_ok()

    def test_2_id_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = "invalid"
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id, server.detail_must_be_an_object_id, tc_id)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_2_id_object_id_invalid(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id, server.detail_doesnot_exist, tc_id)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_3_title_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail("body", server.detail_must_contain_at_least_one_key, body)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_3_title_none(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_title, server.detail_must_be_a_string, body[api.param_title])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_3_title_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_title, server.detail_must_be_not_empty, body[api.param_title])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_3_title_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_3_title_tab(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: []}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_title, server.detail_must_be_a_string, body[api.param_title])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_3_title_object(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: {}}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_title, server.detail_must_be_a_string, body[api.param_title])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_level_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_4_level_none(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_level: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_level, server.detail_must_be_an_integer, body[api.param_level])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_level_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"level": "invalid"}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_level: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_level, server.detail_must_be_an_integer, body[api.param_level])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_level_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_level: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_level, server.detail_must_be_an_integer, body[api.param_level])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_level_integer_min_over(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_level: -1}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_level, server.detail_must_be_between + " 0 and 3", body[api.param_level])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_level_integer_min(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_level: 0}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_4_level_integer_max(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_level: 3}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_4_level_integer_max_over(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_level: 4}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_level, server.detail_must_be_between + " 0 and 3", body[api.param_level])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_level_tab(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_level: []}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_level, server.detail_must_be_an_integer, body[api.param_level])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_level_object(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_level: {}}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_level, server.detail_must_be_an_integer, body[api.param_level])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_5_resume_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_5_resume_none(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_resume: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_resume, server.detail_must_be_a_string, body[api.param_resume])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_5_resume_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"resume": "invalid"}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_resume: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_5_resume_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_resume: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_5_resume_tab(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_resume: []}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_resume, server.detail_must_be_a_string, body[api.param_resume])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_5_resume_object(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_resume: {}}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_resume, server.detail_must_be_a_string, body[api.param_resume])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_6_cooking_time_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_6_cooking_time_none(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_cooking_time: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_cooking_time, server.detail_must_be_an_integer,
                                   body[api.param_cooking_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_6_cooking_time_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"cooking_time": "invalid"}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_cooking_time: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_cooking_time, server.detail_must_be_an_integer,
                                   body[api.param_cooking_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_6_cooking_time_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"cooking_time": "invalid"}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_cooking_time: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_cooking_time, server.detail_must_be_an_integer,
                                   body[api.param_cooking_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_6_cooking_time_integer(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_cooking_time: 5}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_6_cooking_time_tab(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_cooking_time: []}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_cooking_time, server.detail_must_be_an_integer,
                                   body[api.param_cooking_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_6_cooking_time_object(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_cooking_time: {}}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_cooking_time, server.detail_must_be_an_integer,
                                   body[api.param_cooking_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_7_preparation_time_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_7_preparation_time_none(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_preparation_time: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_preparation_time, server.detail_must_be_an_integer,
                                   body[api.param_preparation_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_7_preparation_time_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"preparation_time": "invalid"}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_preparation_time: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_preparation_time, server.detail_must_be_an_integer,
                                   body[api.param_preparation_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_7_preparation_time_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"preparation_time": "invalid"}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_preparation_time: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_preparation_time, server.detail_must_be_an_integer,
                                   body[api.param_preparation_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_7_preparation_time_integer(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_preparation_time: 5}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_7_preparation_time_tab(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_preparation_time: []}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_preparation_time, server.detail_must_be_an_integer,
                                   body[api.param_preparation_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_7_preparation_time_object(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_preparation_time: {}}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_preparation_time, server.detail_must_be_an_integer,
                                   body[api.param_preparation_time])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_8_nb_people_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_8_nb_people_none(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_nb_people: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_nb_people, server.detail_must_be_an_integer, body[api.param_nb_people])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_8_nb_people_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"nb_people": "invalid"}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_nb_people: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_nb_people, server.detail_must_be_an_integer, body[api.param_nb_people])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_8_nb_people_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"nb_people": "invalid"}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_nb_people: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_nb_people, server.detail_must_be_an_integer, body[api.param_nb_people])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_8_nb_people_integer(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_nb_people: 5}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_8_nb_people_tab(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_nb_people: []}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_nb_people, server.detail_must_be_an_integer, body[api.param_nb_people])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_8_nb_people_object(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_nb_people: {}}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_nb_people, server.detail_must_be_an_integer, body[api.param_nb_people])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_9_note_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_9_note_none(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_note: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_note, server.detail_must_be_a_string, body[api.param_note])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_9_note_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"note": "invalid"}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_note: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_9_note_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_note: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_9_note_tab(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_note: []}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_note, server.detail_must_be_a_string, body[api.param_note])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_9_note_object(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_note: {}}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_note, server.detail_must_be_a_string, body[api.param_note])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_10_steps_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_10_steps_none(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_steps: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({api.param_title: "qa_rhr_title_update"})
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_10_steps_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_steps: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({api.param_title: "qa_rhr_title_update"})
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_10_steps_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_steps: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({api.param_title: "qa_rhr_title_update"})
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_10_steps_tab(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_steps: ["invalid"]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({api.param_title: "qa_rhr_title_update"})
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_10_steps_object(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_steps: {}}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({api.param_title: "qa_rhr_title_update"})
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_11_categorties_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_11_categories_none(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_categories: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_categories, server.detail_must_be_an_array, body[api.param_categories])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_11_categories_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_categories: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_categories, server.detail_must_be_an_array, body[api.param_categories])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_11_categories_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_categories: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_categories, server.detail_must_be_an_array, body[api.param_categories])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_11_categories_tab(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_categories: ["invalid"]}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_11_categories_object(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update",
                api.param_categories: {}}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_categories, server.detail_must_be_an_array, body[api.param_categories])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_12_slug_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_12_slug_none(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_slug: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_slug, server.detail_must_be_a_string, body[api.param_slug])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_12_slug_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_slug: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_slug, server.detail_must_be_not_empty, body[api.param_slug])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_12_slug_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_slug: "slug_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_12_slug_tab(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_slug: []}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_slug, server.detail_must_be_a_string, body[api.param_slug])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_12_slug_object(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_slug: {}}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_slug, server.detail_must_be_a_string, body[api.param_slug])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_13_with_files_without(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(api.format_response(response_body[api.rep_data]), tc_recipe.get_data_without_id())
        tc_recipe.select_ok()

    def test_13_with_files_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        tc_with_files = ""
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_with_files, server.detail_must_be_in + " [true, false]", tc_with_files)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_13_with_files_string(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({}).insert()
        tc_id = tc_recipe.get_id()
        tc_with_files = "invalid"
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_with_files, server.detail_must_be_in + " [true, false]", tc_with_files)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_13_with_files_string_false(self):
        tc_recipe = recipe_model.RecipeTest().custom_test({"title": "a"})
        tc_recipe.add_step(_id_step="111111111111111111111111", step="step recipe 1 - 1st")
        tc_recipe.add_step(_id_step="222222222222222222222222", step="step recipe 1 - 2nd")
        tc_recipe.insert()
        tc_recipe.add_file_recipe(filename="qa_rhr_1", is_main=True)
        tc_recipe.add_file_recipe(filename="qa_rhr_2", is_main=False)
        tc_recipe.add_file_step(_id_step="111111111111111111111111", filename="qa_rhr_11", is_main=False)
        tc_recipe.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_21", is_main=False)
        tc_recipe.add_file_step(_id_step="222222222222222222222222", filename="qa_rhr_22", is_main=True)
        tc_id = tc_recipe.get_id()
        tc_with_files = "false"
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_recipe.get_data_stringify_object_id())
        tc_recipe.select_ok()

    def test_13_with_files_string_true(self):
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
        tc_id = tc_recipe.get_id()
        tc_with_files = "true"
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(body)
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        r1 = tc_recipe.get_data_with_file(files_recipe=[tc_file_recipe11, tc_file_recipe12],
                                          files_steps={"111111111111111111111111": [tc_file_step111],
                                                       "222222222222222222222222": [tc_file_step121, tc_file_step122]})
        self.assertEqual(response_body[api.rep_data], r1)

    def test_14_title_already_exist(self):
        tc_recipe1 = recipe_model.RecipeTest().custom_test({"title": "title_1"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom_test({"title": "title_2"}).insert()
        tc_id = tc_recipe1.get_id()
        body = {api.param_title: tc_recipe2.get_data_value("title")}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_title, server.detail_already_exist, body[api.param_title])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe1.select_ok()
        tc_recipe2.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PutRecipe())


if __name__ == '__main__':
    unittest.main()

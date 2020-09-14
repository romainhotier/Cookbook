import unittest
import requests

import utils
import tests.recipe.PutRecipe.api as api
import tests.recipe.model as recipe_model
import tests.file.model as file_model

server = utils.Server
api = api.PutRecipe()
recipe = recipe_model.RecipeTest()
file = file_model.FileTest()


class PutRecipe(unittest.TestCase):

    def setUp(self):
        recipe.clean()
        file.clean()

    def test_0_api_ok(self):
        tc_recipe = recipe_model.RecipeTest().custom({"resume": "invalid"}).insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_0_api_ok_more_param(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_1_url_not_found(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "x" + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        tc_recipe.select_ok()

    def test_2_id_without(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/"
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 404)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_404_url)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        self.assertEqual(response_body["detail"], server.detail_url_not_found)
        tc_recipe.select_ok()

    def test_2_id_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = "invalid"
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id, msg=server.detail_must_be_an_object_id, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_2_id_object_id_invalid(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        body = {api.param_title: "qa_rhr_title_update"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_id, msg=server.detail_doesnot_exist, value=tc_id)
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_3_title_without(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail("body", msg=server.detail_must_contain_at_least_one_key, value=body)
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_3_title_none(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_title, msg=server.detail_must_be_a_string, 
                                   value=body[api.param_title])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_3_title_empty(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_title, msg=server.detail_must_be_not_empty, 
                                   value=body[api.param_title])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_3_title_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_3_title_tab(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: []}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_title, msg=server.detail_must_be_a_string, 
                                   value=body[api.param_title])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_3_title_object(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_title: {}}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_title, msg=server.detail_must_be_a_string, 
                                   value=body[api.param_title])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_4_level_without(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_4_level_none(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer, 
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_4_level_empty(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer, 
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_4_level_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer, 
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_4_level_integer_min_over(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_between + " 0 and 3", 
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_4_level_integer_min(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_4_level_integer_max(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_4_level_integer_max_over(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_between + " 0 and 3", 
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_4_level_tab(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer, 
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_4_level_object(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_level, msg=server.detail_must_be_an_integer, 
                                   value=body[api.param_level])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_5_resume_without(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_5_resume_none(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_resume, msg=server.detail_must_be_a_string, 
                                   value=body[api.param_resume])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_5_resume_empty(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_5_resume_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_5_resume_tab(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_resume, msg=server.detail_must_be_a_string, 
                                   value=body[api.param_resume])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_5_resume_object(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_resume, msg=server.detail_must_be_a_string, 
                                   value=body[api.param_resume])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_6_cooking_time_without(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_6_cooking_time_none(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_cooking_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_cooking_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_6_cooking_time_empty(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_cooking_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_cooking_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_6_cooking_time_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_cooking_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_cooking_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_6_cooking_time_integer(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_6_cooking_time_tab(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_cooking_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_cooking_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_6_cooking_time_object(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_cooking_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_cooking_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_7_preparation_time_without(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_7_preparation_time_none(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_preparation_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_preparation_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_7_preparation_time_empty(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_preparation_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_preparation_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_7_preparation_time_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_preparation_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_preparation_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_7_preparation_time_integer(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_7_preparation_time_tab(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_preparation_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_preparation_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_7_preparation_time_object(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_preparation_time, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_preparation_time])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_8_nb_people_without(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_8_nb_people_none(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nb_people, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_nb_people])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_8_nb_people_empty(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nb_people, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_nb_people])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_8_nb_people_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nb_people, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_nb_people])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_8_nb_people_integer(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_8_nb_people_tab(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nb_people, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_nb_people])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_8_nb_people_object(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_nb_people, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_nb_people])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_9_note_without(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_9_note_none(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_note, msg=server.detail_must_be_a_string, value=body[api.param_note])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_9_note_empty(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_9_note_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_9_note_tab(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_note, msg=server.detail_must_be_a_string, value=body[api.param_note])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_9_note_object(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_note, msg=server.detail_must_be_a_string, value=body[api.param_note])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_10_steps_without(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_10_steps_none(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_10_steps_empty(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_10_steps_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_10_steps_tab(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_10_steps_object(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_11_categorties_without(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_11_categories_none(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_categories, msg=server.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_11_categories_empty(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_categories, msg=server.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_11_categories_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_categories, msg=server.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_11_categories_tab(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_11_categories_object(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_categories, msg=server.detail_must_be_an_array,
                                   value=body[api.param_categories])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_12_slug_without(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_12_slug_none(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_slug: None}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_must_be_a_string, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_12_slug_empty(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_slug: ""}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_12_slug_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_12_slug_tab(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_slug: []}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_must_be_a_string, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_12_slug_object(self):
        tc_recipe = recipe_model.RecipeTest().insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_slug: {}}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_slug, msg=server.detail_must_be_a_string, value=body[api.param_slug])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_13_with_files_without(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_13_with_files_empty(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + " [true, false]",
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_13_with_files_string(self):
        tc_recipe = recipe_model.RecipeTest().insert()
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
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + " [true, false]",
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_13_with_files_string_false(self):
        tc_recipe = recipe_model.RecipeTest()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_13_with_files_string_true(self):
        tc_recipe = recipe_model.RecipeTest()
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
        self.assertEqual(response_body["codeStatus"], 200)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_ok)
        self.assertEqual(response_body["data"],
                         api.data_expected(recipe=tc_recipe,
                                           files={"recipe": [tc_file_recipe11, tc_file_recipe12],
                                                  "steps": {"111111111111111111111111": [tc_file_step111],
                                                            "222222222222222222222222": [tc_file_step121,
                                                                                         tc_file_step122]}}))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))

    def test_14_title_already_exist(self):
        tc_recipe1 = recipe_model.RecipeTest().custom({"title": "title_1"}).insert()
        tc_recipe2 = recipe_model.RecipeTest().custom({"title": "title_2"}).insert()
        tc_id = tc_recipe1.get_id()
        body = {api.param_title: tc_recipe2.title}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_title, msg=server.detail_already_exist, value=body[api.param_title])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe1.select_ok()
        tc_recipe2.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PutRecipe())


if __name__ == '__main__':
    unittest.main()

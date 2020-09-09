import unittest
import requests
from bson import ObjectId

import utils
import tests.recipe.PostRecipeStep.api as api
import tests.recipe.model as recipe_model
import tests.file.model as file_model

server = utils.Server
api = api.PostRecipeStep()
recipe = recipe_model.RecipeTest()
file = file_model.FileTest()


class PostRecipeStep(unittest.TestCase):

    def setUp(self):
        recipe.clean()
        file.clean()

    def test_0_api_ok_without_position(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id 
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(api.custom_steps(recipe=tc_recipe, body=body, rep=response_body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_0_api_ok_with_position(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: 1}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id 
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(api.custom_steps(recipe=tc_recipe, body=body, rep=response_body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_0_api_ok_more_param(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?invalid=invalid"
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(api.custom_steps(recipe=tc_recipe, body=body, rep=response_body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_1_url_not_found_1(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step"}
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
        tc_recipe.select_ok()

    def test_2_id_without(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = ""
        body = {api.param_step: "new_step"}
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
        tc_recipe.select_ok()

    def test_2_id_string(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = "invalid"
        body = {api.param_step: "new_step"}
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
        tc_recipe.select_ok()

    def test_2_id_object_id_invalid(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        body = {api.param_step: "new_step"
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
        tc_recipe.select_ok()

    def test_3_step_without(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {}
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
        detail = api.create_detail(param=api.param_step, msg=server.detail_is_required)
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_3_step_none(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: None}
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
        detail = api.create_detail(param=api.param_step, msg=server.detail_must_be_a_string, value=body[api.param_step])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_3_step_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: ""}
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
        detail = api.create_detail(param=api.param_step, msg=server.detail_must_be_not_empty,
                                   value=body[api.param_step])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_3_step_string(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step"
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id 
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(api.custom_steps(recipe=tc_recipe, body=body, rep=response_body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_3_step_tab(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: []}
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
        detail = api.create_detail(param=api.param_step, msg=server.detail_must_be_a_string, value=body[api.param_step])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_3_step_object(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: {}}
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
        detail = api.create_detail(param=api.param_step, msg=server.detail_must_be_a_string, value=body[api.param_step])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_4_position_without(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step"
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id 
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(api.custom_steps(recipe=tc_recipe, body=body, rep=response_body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_4_position_none(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: None}
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
        detail = api.create_detail(param=api.param_position, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_position])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_4_position_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: ""}
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
        detail = api.create_detail(param=api.param_position, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_position])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_4_position_string(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: "invalid"}
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
        detail = api.create_detail(param=api.param_position, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_position])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_4_position_tab(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: []}
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
        detail = api.create_detail(param=api.param_position, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_position])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_4_position_object(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: {}}
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
        detail = api.create_detail(param=api.param_position, msg=server.detail_must_be_an_integer,
                                   value=body[api.param_position])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_4_position_int_min_over(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: -1}
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
        detail = api.create_detail(param=api.param_position, msg=server.detail_must_be_between + " 0 and 2",
                                   value=body[api.param_position])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_4_position_int_min(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: 0}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id 
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(api.custom_steps(recipe=tc_recipe, body=body, rep=response_body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_4_position_int_max(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: 2}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id 
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(api.custom_steps(recipe=tc_recipe, body=body, rep=response_body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_4_position_int_max_over(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: 3}
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
        detail = api.create_detail(param=api.param_position, msg=server.detail_must_be_between + " 0 and 2",
                                   value=body[api.param_position])
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_5_with_files_without(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step"
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id 
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(api.custom_steps(recipe=tc_recipe, body=body, rep=response_body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_5_with_files_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        tc_with_files = ""
        body = {api.param_step: "new_step"}
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + " [true, false]",
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_5_with_files_string(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        tc_with_files = "invalid"
        body = {api.param_step: "new_step"
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 400)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_error_400)
        self.assertTrue(api.check_not_present(value="data", rep=response_body))
        detail = api.create_detail(param=api.param_with_files, msg=server.detail_must_be_in + " [true, false]",
                                   value=tc_with_files)
        self.assertEqual(response_body["detail"], detail)
        tc_recipe.select_ok()

    def test_5_with_files_string_false(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        tc_with_files = "false"
        body = {api.param_step: "new_step"
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(api.custom_steps(recipe=tc_recipe, body=body, rep=response_body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    def test_5_with_files_string_true(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": [{"_id": ObjectId("111111111111111111111111"),
                                                                 "step": "step1"},
                                                                {"_id": ObjectId("222222222222222222222222"),
                                                                 "step": "step2"}]}).insert()
        tc_id = tc_recipe.get_id()
        tc_with_files = "false"
        body = {api.param_step: "new_step"
                }
        """ call api """
        url = server.main_url + "/" + api.url + "/" + tc_id + "?" + api.param_with_files + "=" + tc_with_files
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom(api.custom_steps(recipe=tc_recipe, body=body, rep=response_body))
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response_body["codeStatus"], 201)
        self.assertEqual(response_body["codeMsg"], api.rep_code_msg_created)
        self.assertEqual(response_body["data"], api.data_expected(recipe=tc_recipe))
        self.assertTrue(api.check_not_present(value="detail", rep=response_body))
        tc_recipe.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostRecipeStep())


if __name__ == '__main__':
    unittest.main()

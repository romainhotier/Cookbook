import unittest
import requests
from bson import ObjectId

from server import factory as factory
import app.recipe.recipe.model as recipe_model
import app.recipe.steps.test.PutRecipeStep.api as api

server = factory.Server()
api = api.PutRecipeStep()
recipe = recipe_model.RecipeTest()


class PutRecipeStep(unittest.TestCase):

    def setUp(self):
        recipe.clean()

    def test_0_api_ok(self):
        tc_recipe = recipe_model.RecipeTest().\
            custom_test({"steps": [{"_id": ObjectId("111111111111111111111111"), "step": "a"},
                                   {"_id": ObjectId("222222222222222222222222"), "step": "b"}]}).insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom_step(step_index=0,
                              data={"_id": ObjectId("111111111111111111111111"), "step": body[api.param_step]})
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_recipe.get_data_stringify_object_id())
        tc_recipe.select_ok()

    def test_0_api_ok_more_param(self):
        tc_recipe = recipe_model.RecipeTest().\
            custom_test({"steps": [{"_id": ObjectId("111111111111111111111111"), "step": "a"},
                                   {"_id": ObjectId("222222222222222222222222"), "step": "b"}]}).insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_step: "update",
                "invalid": "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom_step(step_index=0,
                              data={"_id": ObjectId("111111111111111111111111"), "step": body[api.param_step]})
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_recipe.get_data_stringify_object_id())
        tc_recipe.select_ok()

    def test_1_url_not_found_1(self):
        tc_recipe = recipe_model.RecipeTest().\
            custom_test({"steps": [{"_id": ObjectId("111111111111111111111111"), "step": "a"},
                                   {"_id": ObjectId("222222222222222222222222"), "step": "b"}]}).insert()
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
        tc_recipe = recipe_model.RecipeTest().\
            custom_test({"steps": [{"_id": ObjectId("111111111111111111111111"), "step": "a"},
                                   {"_id": ObjectId("222222222222222222222222"), "step": "b"}]}).insert()
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
        tc_recipe = recipe_model.RecipeTest().\
            custom_test({"steps": [{"_id": ObjectId("111111111111111111111111"), "step": "a"},
                                   {"_id": ObjectId("222222222222222222222222"), "step": "b"}]}).insert()
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
        tc_recipe = recipe_model.RecipeTest().\
            custom_test({"steps": [{"_id": ObjectId("111111111111111111111111"), "step": "a"},
                                   {"_id": ObjectId("222222222222222222222222"), "step": "b"}]}).insert()
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
        tc_recipe = recipe_model.RecipeTest(). \
            custom_test({"steps": [{"_id": ObjectId("111111111111111111111111"), "step": "a"},
                                   {"_id": ObjectId("222222222222222222222222"), "step": "b"}]}).insert()
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
        tc_recipe = recipe_model.RecipeTest(). \
            custom_test({"steps": [{"_id": ObjectId("111111111111111111111111"), "step": "a"},
                                   {"_id": ObjectId("222222222222222222222222"), "step": "b"}]}).insert()
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
        tc_recipe = recipe_model.RecipeTest(). \
            custom_test({"steps": [{"_id": ObjectId("111111111111111111111111"), "step": "a"},
                                   {"_id": ObjectId("222222222222222222222222"), "step": "b"}]}).insert()
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
        tc_recipe = recipe_model.RecipeTest(). \
            custom_test({"steps": [{"_id": ObjectId("111111111111111111111111"), "step": "a"},
                                   {"_id": ObjectId("222222222222222222222222"), "step": "b"}]}).insert()
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
        tc_recipe = recipe_model.RecipeTest(). \
            custom_test({"steps": [{"_id": ObjectId("111111111111111111111111"), "step": "a"},
                                   {"_id": ObjectId("222222222222222222222222"), "step": "b"}]}).insert()
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
        tc_recipe = recipe_model.RecipeTest(). \
            custom_test({"steps": [{"_id": ObjectId("111111111111111111111111"), "step": "a"},
                                   {"_id": ObjectId("222222222222222222222222"), "step": "b"}]}).insert()
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
        tc_recipe = recipe_model.RecipeTest(). \
            custom_test({"steps": [{"_id": ObjectId("111111111111111111111111"), "step": "a"},
                                   {"_id": ObjectId("222222222222222222222222"), "step": "b"}]}).insert()
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
        tc_recipe = recipe_model.RecipeTest().\
            custom_test({"steps": [{"_id": ObjectId("111111111111111111111111"), "step": "a"},
                                   {"_id": ObjectId("222222222222222222222222"), "step": "b"}]}).insert()
        tc_id_recipe = tc_recipe.get_id()
        tc_id_step = "111111111111111111111111"
        body = {api.param_step: "update"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id_recipe + "/" + api.url2 + "/" + tc_id_step
        response = requests.put(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom_step(step_index=0,
                              data={"_id": ObjectId("111111111111111111111111"), "step": body[api.param_step]})
        """ assert """
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 200)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_ok)
        self.assertEqual(response_body[api.rep_data], tc_recipe.get_data_stringify_object_id())
        tc_recipe.select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PutRecipeStep())


if __name__ == '__main__':
    unittest.main()

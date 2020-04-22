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
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({"steps": ["a", "b", {"_id": "", "step": "new_step"}]})
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_data(data=response_body[api.rep_data], position=2),
                         tc_recipe.get_stringify())
        """ refacto recipe """
        new_id = api.get_new_id(data=response_body[api.rep_data], position=2)
        tc_recipe.custom({"steps": ["a", "b", {"_id": ObjectId(new_id), "step": "new_step"}]}).select_ok()

    def test_0_api_ok_with_position(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: 1
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({"steps": ["a", {"_id": "", "step": "new_step"}, "b"]})
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_data(data=response_body[api.rep_data], position=body[api.param_position]),
                         tc_recipe.get_stringify())
        """ refacto recipe """
        new_id = api.get_new_id(data=response_body[api.rep_data], position=body[api.param_position])
        tc_recipe.custom({"steps": ["a", {"_id": ObjectId(new_id), "step": "new_step"}, "b"]}).select_ok()

    def test_0_api_ok_more_param(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                "invalid": "invalid"
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2 + "?invalid=invalid"
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({"steps": ["a", "b", {"_id": "", "step": "new_step"}]})
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_data(data=response_body[api.rep_data], position=2),
                         tc_recipe.get_stringify())
        """ refacto recipe """
        new_id = api.get_new_id(data=response_body[api.rep_data], position=2)
        tc_recipe.custom({"steps": ["a", "b", {"_id": ObjectId(new_id), "step": "new_step"}]}).select_ok()

    def test_1_url_not_found_1(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                "invalid": "invalid"
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "x/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_recipe.select_ok()

    def test_1_url_not_found_2(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                "invalid": "invalid"
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/x" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 404)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_404_url)
        self.assertEqual(response_body[api.rep_detail], server.detail_url_not_found)
        tc_recipe.select_ok()

    def test_2_id_without(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = ""
        body = {api.param_step: "new_step"
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 405)
        self.assertEqual(response_body[api.rep_detail], server.rep_code_msg_error_405)
        tc_recipe.select_ok()

    def test_2_id_string(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = "invalid"
        body = {api.param_step: "new_step"
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
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
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = "aaaaaaaaaaaaaaaaaaaaaaaa"
        body = {api.param_step: "new_step"
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_id, server.detail_doesnot_exist, tc_id)
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_3_step_without(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_step, server.detail_is_required, "missing")
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_3_step_none(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: None}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_step, server.detail_must_be_a_string, body[api.param_step])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_3_step_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: ""}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_step, server.detail_must_be_not_empty, body[api.param_step])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_3_step_string(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step"
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({"steps": ["a", "b", {"_id": "", "step": "new_step"}]})
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_data(data=response_body[api.rep_data], position=2),
                         tc_recipe.get_stringify())
        """ refacto recipe """
        new_id = api.get_new_id(data=response_body[api.rep_data], position=2)
        tc_recipe.custom({"steps": ["a", "b", {"_id": ObjectId(new_id), "step": "new_step"}]}).select_ok()

    def test_3_step_tab(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: []}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_step, server.detail_must_be_a_string, body[api.param_step])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_3_step_object(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: {}}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_step, server.detail_must_be_a_string, body[api.param_step])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_position_without(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step"
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({"steps": ["a", "b", {"_id": "", "step": "new_step"}]})
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_data(data=response_body[api.rep_data], position=2),
                         tc_recipe.get_stringify())
        """ refacto recipe """
        new_id = api.get_new_id(data=response_body[api.rep_data], position=2)
        tc_recipe.custom({"steps": ["a", "b", {"_id": ObjectId(new_id), "step": "new_step"}]}).select_ok()

    def test_4_position_none(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: None}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_position, server.detail_must_be_an_integer, body[api.param_position])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_position_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: ""}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_position, server.detail_must_be_an_integer, body[api.param_position])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_position_string(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: "invalid"}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_position, server.detail_must_be_an_integer, body[api.param_position])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_position_tab(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: []}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_position, server.detail_must_be_an_integer, body[api.param_position])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_position_object(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: {}}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_position, server.detail_must_be_an_integer, body[api.param_position])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_position_int_min_over(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: -1}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_position, server.detail_must_be_between + " 0 and 2",
                                   body[api.param_position])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_4_position_int_min(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: 0}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({"steps": [{"_id": "", "step": "new_step"}, "a", "b"]})
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_data(data=response_body[api.rep_data], position=0),
                         tc_recipe.get_stringify())
        """ refacto recipe """
        new_id = api.get_new_id(data=response_body[api.rep_data], position=0)
        tc_recipe.custom({"steps": [{"_id": ObjectId(new_id), "step": "new_step"}, "a", "b"]}).select_ok()

    def test_4_position_int_max(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: 2}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({"steps": ["a", "b", {"_id": "", "step": "new_step"}]})
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_data(data=response_body[api.rep_data], position=2),
                         tc_recipe.get_stringify())
        """ refacto recipe """
        new_id = api.get_new_id(data=response_body[api.rep_data], position=2)
        tc_recipe.custom({"steps": ["a", "b", {"_id": ObjectId(new_id), "step": "new_step"}]}).select_ok()

    def test_4_position_int_max_over(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step",
                api.param_position: 3}
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json', )
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_position, server.detail_must_be_between + " 0 and 2",
                                   body[api.param_position])
        self.assertEqual(response_body[api.rep_detail], detail)
        tc_recipe.select_ok()

    def test_5_with_files_without(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        body = {api.param_step: "new_step"
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({"steps": ["a", "b", {"_id": "", "step": "new_step"}]})
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_data(data=response_body[api.rep_data], position=2),
                         tc_recipe.get_stringify())
        """ refacto recipe """
        new_id = api.get_new_id(data=response_body[api.rep_data], position=2)
        tc_recipe.custom({"steps": ["a", "b", {"_id": ObjectId(new_id), "step": "new_step"}]}).select_ok()

    def test_5_with_files_empty(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        tc_with_files = ""
        body = {api.param_step: "new_step"
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2 + "?" \
            + api.param_with_files + "=" + tc_with_files
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({"steps": ["a", "b", {"_id": "", "step": "new_step"}]})
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_with_files, server.detail_must_be_in + " [true, false]", tc_with_files)
        self.assertEqual(response_body[api.rep_detail], detail)

    def test_5_with_files_string(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        tc_with_files = "invalid"
        body = {api.param_step: "new_step"
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2 + "?" \
            + api.param_with_files + "=" + tc_with_files
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({"steps": ["a", "b", {"_id": "", "step": "new_step"}]})
        """ assert """
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 400)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_error_400)
        detail = api.create_detail(api.param_with_files, server.detail_must_be_in + " [true, false]", tc_with_files)
        self.assertEqual(response_body[api.rep_detail], detail)

    def test_5_with_files_string_false(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        tc_with_files = "false"
        body = {api.param_step: "new_step"
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2 + "?" \
            + api.param_with_files + "=" + tc_with_files
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({"steps": ["a", "b", {"_id": "", "step": "new_step"}]})
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_data(data=response_body[api.rep_data], position=2),
                         tc_recipe.get_stringify())
        """ refacto recipe """
        new_id = api.get_new_id(data=response_body[api.rep_data], position=2)
        tc_recipe.custom({"steps": ["a", "b", {"_id": ObjectId(new_id), "step": "new_step"}]}).select_ok()

    def test_5_with_files_string_true(self):
        tc_recipe = recipe_model.RecipeTest().custom({"steps": ["a", "b"]}).insert()
        tc_id = tc_recipe.get_id()
        tc_with_files = "false"
        body = {api.param_step: "new_step"
                }
        """ call api """
        url = server.main_url + "/" + api.url1 + "/" + tc_id + "/" + api.url2 + "?" \
            + api.param_with_files + "=" + tc_with_files
        response = requests.post(url, json=body, verify=False)
        response_body = response.json()
        tc_recipe.custom({"steps": ["a", "b", {"_id": "", "step": "new_step"}]})
        """ assert """
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], 'application/json')
        self.assertEqual(response_body[api.rep_code_status], 201)
        self.assertEqual(response_body[api.rep_code_msg], api.rep_code_msg_created)
        self.assertEqual(api.format_data(data=response_body[api.rep_data], position=2),
                         tc_recipe.get_stringify())
        """ refacto recipe """
        new_id = api.get_new_id(data=response_body[api.rep_data], position=2)
        tc_recipe.custom({"steps": ["a", "b", {"_id": ObjectId(new_id), "step": "new_step"}]}).select_ok()

    @classmethod
    def tearDownClass(cls):
        cls.setUp(PostRecipeStep())


if __name__ == '__main__':
    unittest.main()
